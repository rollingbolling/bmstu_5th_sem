#include "algorithms.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char *generateRandomString(int length) {
    // Массив возможных символов (заглавные и строчные буквы)
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int charsetSize = sizeof(charset) - 1; // исключаем нулевой символ

    // Выделяем память для строки (+1 для завершающего нулевого символа)
    char *randomString = malloc(length + 1);
    if (randomString) {
        for (int i = 0; i < length; i++) {
            int key = rand() % charsetSize; // выбираем случайный индекс
            randomString[i] = charset[key];
        }
        randomString[length] = '\0'; // завершающий нулевой символ
    }

    return randomString;
}

int main()
{
    int choice = -1;
    char *menu = "\nSelect an option from the menu:\n"
            "1. Display all algorithms for calculating distances:\n"
            "\t1) Non-recursive Levenshtein distance algorithm\n"
            "\t2) Recursive Levenshtein distance algorithm\n"
            "\t3) Recursive Levenshtein distance algorithm with cash\n"
            "\t4) Non-recursive Damerau-Levenshtein distance algorithm\n"
            "2. Measurements and performance evaluation of algorithms\n"
            "0. Exit the program\n\n";
    char string_1[10000], string_2[10000];
    
    while (choice != 0)
    {
        printf("%s", menu);
        scanf("%d", &choice);
        if (choice == 1)
        {
            printf("Input two words:\n");
            scanf("%s", string_1);
            scanf("%s", string_2);
            printf("1) %d\n", LevNoRec(string_1, string_2));
            printf("2) %d\n", LevRecurse(string_1, string_2));
            printf("3) %d\n", LevRecCash(string_1, string_2));
            printf("4) %d\n", DemLevNoRec(string_1, string_2));
        }
        if (choice == 2)
        {
            clock_t start, end;
            int dist = 0;
            printf("Input two words:\n");
            int length = 800;
            srand(time(NULL));
            char *string_1 = generateRandomString(length);
            char *string_2 = generateRandomString(length);
            {
                start = clock();
                dist = LevNoRec(string_1, string_2);
                end = clock();
                printf("1) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
            }
            // {
            //     start = clock();
            //     dist = LevRecurse(string_1, string_2);
            //     end = clock();
            //     printf("2) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
            // }
            {
                start = clock();
                dist = LevRecCash(string_1, string_2);
                end = clock();
                printf("3) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
            }
            {
                start = clock();
                dist = DemLevNoRec(string_1, string_2);
                end = clock();
                printf("4) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
            }
            free(string_1);
            free(string_2);
        }
    }

    return 0;
}
