#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "measurement.h"
#include "algorithms.h"

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

void time_measure(int iters)
{
    FILE *f;
    f = fopen("measure.csv", "w");
    clock_t start, end;
    // int dist = 0;
    // int length = 1;
    srand(time(NULL));
    for (int length = 1; length <= 12; length++) {
        char *string_1 = generateRandomString(length);
        char *string_2 = generateRandomString(length);
        fprintf(f, "%d;", length);
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevNoRec(string_1, string_2);
            end = clock();
            fprintf(f, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("1) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRecurse(string_1, string_2);
            end = clock();
            fprintf(f, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("2) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRecCash(string_1, string_2);
            end = clock();
            fprintf(f, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("3) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                DemLevNoRec(string_1, string_2);
            end = clock();
            fprintf(f, "%lf", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("4) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        free(string_1);
        free(string_2);
        fprintf(f, "\n");
    }
    // printf("%d", dist);
    fclose(f);

    FILE *f2;
    f2 = fopen("measure_long.csv", "w");
    for (int length = 25; length <= 1000; length+=25)
    {
        char *string_1 = generateRandomString(length);
        char *string_2 = generateRandomString(length);
        fprintf(f2, "%d;", length);
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevNoRec(string_1, string_2);
            end = clock();
            fprintf(f2, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("1) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            fprintf(f2, "%lf;", ((double)0));
            // printf("2) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRecCash(string_1, string_2);
            end = clock();
            fprintf(f2, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("3) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        {
            start = clock();
            for (int i = 0; i < iters; i++)
                DemLevNoRec(string_1, string_2);
            end = clock();
            fprintf(f2, "%lf", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
            // printf("4) %d, Time: %lf\n", dist, ((double)(end - start)) / CLOCKS_PER_SEC);
        }
        free(string_1);
        free(string_2);
        fprintf(f2, "\n");
    }
    fclose(f);
}