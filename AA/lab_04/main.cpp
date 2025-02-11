#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <fstream>
#include <thread>
#include <mutex>
#include <curl/curl.h>

#define _CRT_SECURE_NO_WARNINGS
#define OUTPUT_DIR "./output/"
#define URL_FILE   "./urls.txt"

// Callback для сохранения данных
size_t write_callback(char* data, size_t size, size_t nmemb, std::string* output) {
    if (output) {
        output->append(data, size * nmemb);
    }
    return size * nmemb;
}

// Функция для скачивания контента по URL и сохранения его в файл
void fetch_and_save(const std::string& url, const std::string& filepath) {
    CURL* curl = curl_easy_init();
    std::string content;

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &content);

        CURLcode res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            std::cerr << "Ошибка при загрузке URL: " << curl_easy_strerror(res) << std::endl;
        }

        curl_easy_cleanup(curl);

        // Сохраняем содержимое в файл
        std::ofstream file(filepath);
        if (file.is_open()) {
            file << content;
            file.close();
        } else {
            std::cerr << "Не удалось открыть файл для записи: " << filepath << std::endl;
        }
    }
}

// Функция обработки одного URL в отдельном потоке
void process_url(int index, const std::vector<std::string>& urls) {
    static std::mutex mtx; // Защита общих ресурсов
    std::lock_guard<std::mutex> lock(mtx);

    std::string filename = std::string(OUTPUT_DIR) + "multi_" + std::to_string(index) + ".txt";
    std::string url = urls[index];

    fetch_and_save(url, filename);
}

// Замер времени выполнения многопоточного режима
double measure_multithreaded(const std::vector<std::string>& urls, int num_threads, int iterations) {
    double total_time = 0.0;

    for (int iter = 0; iter < iterations; ++iter) {
        clock_t start = clock();

        std::vector<std::thread> workers;
        for (size_t i = 0; i < urls.size(); i += num_threads) {
            for (int j = 0; j < num_threads && i + j < urls.size(); ++j) {
                workers.emplace_back(process_url, i + j, std::ref(urls));
            }

            for (auto& t : workers) {
                if (t.joinable()) {
                    t.join();
                }
            }
            workers.clear();
        }

        clock_t end = clock();
        total_time += static_cast<double>(end - start) / CLOCKS_PER_SEC;
    }

    return total_time / iterations;
}

// Замер времени выполнения однопоточного режима
double measure_single_threaded(const std::vector<std::string>& urls, int iterations) {
    double total_time = 0.0;

    for (int iter = 0; iter < iterations; ++iter) {
        clock_t start = clock();

        for (size_t i = 0; i < urls.size(); ++i) {
            std::string filename = std::string(OUTPUT_DIR) + "one_" + std::to_string(i) + ".txt";
            fetch_and_save(urls[i], filename);
        }

        clock_t end = clock();
        total_time += static_cast<double>(end - start) / CLOCKS_PER_SEC;
    }

    return total_time / iterations;
}

// Чтение URL из файла
std::vector<std::string> load_urls_from_file(const std::string& filepath, int max_count) {
    std::vector<std::string> urls;
    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Ошибка: не удалось открыть файл " << filepath << std::endl;
        return urls;
    }

    std::string line;
    while (std::getline(file, line) && urls.size() < static_cast<size_t>(max_count)) {
        if (!line.empty()) {
            urls.push_back(line);
        }
    }

    file.close();
    return urls;
}

int main() {
    int url_limit, test_count;

    std::cout << "Введите максимальное количество URL: ";
    std::cin >> url_limit;

    std::cout << "Введите количество тестовых итераций: ";
    std::cin >> test_count;

    if (url_limit <= 0 || test_count <= 0) {
        std::cerr << "Ошибка: неверные параметры" << std::endl;
        return 1;
    }

    std::vector<std::string> urls = load_urls_from_file(URL_FILE, url_limit);

    if (urls.empty()) {
        std::cerr << "Ошибка: список URL пуст" << std::endl;
        return 1;
    }

    // Создаем директорию для вывода
    // mkdir(OUTPUT_DIR, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
    // std::ofstream file("res.txt");

    // Тестирование однопоточного режима
    double single_time = measure_single_threaded(urls, test_count);
    std::cout << "Однопоточный режим: " << single_time << " секунд" << std::endl;
    
    // Тестирование многопоточного режима
    for (int threads = 1; threads <= 64; threads *= 2) {
        double multi_time = measure_multithreaded(urls, threads, test_count);
        std::cout << "Многопоточный режим (" << threads << " потоков): " << multi_time << " секунд" << std::endl;
    }

    return 0;
}
