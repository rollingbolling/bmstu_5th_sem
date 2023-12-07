#include <iostream>
#include <io.h>
#include <fcntl.h>

#include "./inc/algorithms.h"

int main()
{
    setbuf(stdout, NULL);
    _setmode(_fileno(stdout), _O_U8TEXT);
    _setmode(_fileno(stdin), _O_U8TEXT);

    wcout << L"Выберите пункт меню:\n"
            "1.Вывод всех алгоритмов расстояний Леванштейна и Дамерау-Леванштейна:\n"
            "\t1)Нерекурсивный алгоритм поиска расстояния Леванштейна\n"
            "\t2)Нерекурсивный алгоритм поиска расстояния Дамерау-Леванштейна\n"
            "\t3)Рекурсивный алгоритм поиска расстояния Дамерау-Леванштейна без кэша\n"
            "\t4)Рекурсивный алгоритм поиска расстояния Дамерау-Леванштейна с кэшом\n"
            "2. Замеры и вывод времмени и памяти реализованных алгоритмов поиска расстояний Леванштейна и Дамерау-Леванштейна\n"
            "0. Выход из программы\n";

    int choice = -1;
    wstring def_word1 = L"Cat";
    wstring def_word2 = L"Dog";
    int res = 0;
    while (choice != 0)
    {
        wcout << L"Выбирите пункт: ";
        wcin >> choice;

        if (choice == 1)
        {
            wcout << L"Введите первое слово: \n";
            wcin >> def_word1;
            wcout << L"Введите второе слово: \n";
            wcin >> def_word2;


        }

        else if (choice == 2)
        {
            wcout << "Out\n";
        }
    }

    return 0;
}
