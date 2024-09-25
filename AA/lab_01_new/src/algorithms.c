#include "algorithms.h"
#include "alloc_mtrx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int LevRec(char *word1, char *word2, int n, int m)
{
    if (n == 0) return m;
    if (m == 0) return n;

    if (word1[n - 1] == word2[m - 1])
        return LevRec(word1, word2, n - 1, m - 1);
    
    int insert = LevRec(word1, word2, n, m - 1);
    int remove = LevRec(word1, word2, n - 1, m);
    int replace = LevRec(word1, word2, n - 1, m - 1);

    return 1 + fmin(insert, fmin(remove, replace));
}

int Lev(char *word1, char *word2)
{
    return LevRec(word1, word2, strlen(word1), strlen(word2));
}

int LevNoRec(char *word1, char *word2)
{
    int n = strlen(word1);
    int m = strlen(word2);

    int **mtrx = create_mtrx(n, m);

    if (mtrx != NULL) 
    {
        
        delete_mtrx(mtrx, n);
    }
}

void LevRecCash();
void DemLevNoRec();

