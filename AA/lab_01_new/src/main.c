#include "algorithms.h"
#include <stdio.h>
#include <stdlib.h>
#include "measurement.h"

int main()
{
    int choice = -1;
    char *menu = "\nSelect an option from the menu:\n"
            "  1. Display all algorithms for calculating distances:\n"
            "\t1) Non-recursive Levenshtein distance algorithm\n"
            "\t2) Recursive Levenshtein distance algorithm\n"
            "\t3) Recursive Levenshtein distance algorithm with cash\n"
            "\t4) Recursive Damerau-Levenshtein distance algorithm\n"
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
            printf("1) %d\n", LevNoRec(string_1, string_2));
            printf("2) %d\n", LevRecurse(string_1, string_2));
            printf("3) %d\n", LevRecCash(string_1, string_2));
            printf("4) %d\n", DemLevRec(string_1, string_2));
        }
        if (choice == 2)
        {
            time_measure();
        }
    }

    return 0;
}
