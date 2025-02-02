#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "measurement.h"
#include "algorithms.h"

char *generateRandomString(int length) {
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int charsetSize = sizeof(charset) - 1;

    char *randomString = malloc(length + 1);
    if (randomString) {
        for (int i = 0; i < length; i++) {
            int key = rand() % charsetSize;
            randomString[i] = charset[key];
        }
        randomString[length] = '\0';
    }

    return randomString;
}

void time_measure(int iters)
{
    FILE *f_short, *f_long;
    f_short = fopen("measure.csv", "w");
    clock_t start, end;

    srand(time(NULL));

    for (int length = 1; length <= 12; length++) {
        char *string_1 = generateRandomString(length);
        char *string_2 = generateRandomString(length);
        fprintf(f_short, "%d;", length);
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevNoRec(string_1, string_2);
            end = clock();
            fprintf(f_short, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRec(string_1, string_2, length, length);
            end = clock();
            fprintf(f_short, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRecCash(string_1, string_2, length, length);
            end = clock();
            fprintf(f_short, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                DemLevNoRec(string_1, string_2);
            end = clock();
            fprintf(f_short, "%lf", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        free(string_1);
        free(string_2);
        fprintf(f_short, "\n");
    }
    fclose(f_short);

    f_long = fopen("measure_long.csv", "w");
    for (int length = 25; length <= 1000; length+=25)
    {
        char *string_1 = generateRandomString(length);
        char *string_2 = generateRandomString(length);
        fprintf(f_long, "%d;", length);
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevNoRec(string_1, string_2);
            end = clock();
            fprintf(f_long, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        {
            fprintf(f_long, "%lf;", ((double)0));
        }
        {
            start = clock();
            for (int i = 0; i < iters; i ++)
                LevRecCash(string_1, string_2, length, length);
            end = clock();
            fprintf(f_long, "%lf;", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        {
            start = clock();
            for (int i = 0; i < iters; i++)
                DemLevNoRec(string_1, string_2);
            end = clock();
            fprintf(f_long, "%lf", ((double)((end - start) / iters) / CLOCKS_PER_SEC));
        }
        free(string_1);
        free(string_2);
        fprintf(f_long, "\n");
    }
    fclose(f_short);
}