#include "algorithms.h"
#include <stdio.h>
#include <stdlib.h>



int main()
{
    // int rc = EXIT_FAILURE;
    int choice = -1;
    printf("Select an option from the menu:\n"
            "1. Display all algorithms for calculating distances:\n"
            "\t1) Non-recursive Levenshtein distance algorithm\n"
            "\t2) Recursive Levenshtein distance algorithm\n"
            "\t3) Recursive Levenshtein distance algorithm with cash\n"
            "\t4) Non-recursive Damerau-Levenshtein distance algorithm\n"
            "2. Measurements and performance evaluation of algorithms\n"
            "0. Exit the program\n");
    char string_1[10000], string_2[10000];
    
    while (choice != 0)
    {
        printf("Select an option from the menu:\n");
        scanf("%d", &choice);
        if (choice == 1)
        {
            printf("Input two words:\n");
            scanf("%s", string_1);
            scanf("%s", string_2);
            // printf("1) %d\n", );
            printf("2) %d\n", Lev(string_1, string_2));
        }
        if (choice == 2)
        {
            printf("n/a");   
        }
    }

    return 0;
}
