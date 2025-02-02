#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "algorithms.h"
#include "measurement.h"

int main()
{
    int choice = -1;
    char *menu = "\nSelect an option from the menu:\n"
            "  1. Display all algorithms for calculating distances:\n"
            "\t1) Non-recursive Levenshtein distance algorithm\n"
            "\t2) Recursive Levenshtein distance algorithm\n"
            "\t3) Recursive Levenshtein distance algorithm with cash\n"
            "\t4) Non-recursive Damerau-Levenshtein distance algorithm\n"
            "  2. Measurements and performance evaluation of algorithms\n"
            "  0. Exit the program\n";
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
            int n = strlen(string_1);
            int m = strlen(string_2);
            printf("1) %d\n", LevNoRec(string_1, string_2));
            printf("2) %d\n", LevRec(string_1, string_2, n, m));
            printf("3) %d\n", LevRecCash(string_1, string_2, n, m));
            printf("4) %d\n", DemLevNoRec(string_1, string_2));
        }
        if (choice == 2)
        {
            printf("Input iters:\n");
            int iters = 1;
            if (scanf("%d", &iters) == 1)
                time_measure(iters);
        }
    }

    return 0;
}
