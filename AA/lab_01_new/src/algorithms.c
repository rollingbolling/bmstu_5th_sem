#include "algorithms.h"
#include "alloc_mtrx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void print_mtrx(int **mtrx, int n, int m)
{
    printf("\n"); 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            printf("%d ", mtrx[i][j]);
        printf("\n");    
    }
}

void set_mtrx(int **mtrx, int n, int m, int num)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mtrx[i][j] = num;
}

int get_min(int a, int b, int c)
{
    if (a < b && a < c)
        return a;
    if (b < c && b < a)
        return b;
    return c;
}

int LevNoRec(char *word1, char *word2)
{
    int res = -1;

    int n = strlen(word1) + 1;
    int m = strlen(word2) + 1;

    int **mtrx = create_mtrx(n, m);

    if (mtrx != NULL) 
    {
        mtrx[0][0]= 0;
        for (int i = 1; i < n; i++)
            mtrx[i][0] = i;
        for (int j = 1; j < m; j++)
            mtrx[0][j] = j;

        int insert = 0;
        int delet = 0;
        int replace = 0;
        
        for (int i = 1; i < n; i++)
            for (int j = 1; j < m; j++)
            {
                insert = mtrx[i][j - 1] + 1;
                delet = mtrx[i - 1][j] + 1;
                replace = mtrx[i - 1][j - 1] + (int)(word1[i - 1] != word2[j - 1]);

                mtrx[i][j] = get_min(insert, delet, replace);
            }

        res = mtrx[n - 1][m - 1];
        delete_mtrx(mtrx, n);
    }

    return res;
}

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

int LevRecurse(char *word1, char *word2)
{
    return LevRec(word1, word2, strlen(word1), strlen(word2));
}

void LevRecCashIter(char *word1, char *word2, int n, int m, int **mtrx)
{
    if (n == 0) mtrx[n][m] = m;
    else if (m == 0) mtrx[n][m] = n;
    else
    {
        if (mtrx[n][m - 1] == -1)
            LevRecCashIter(word1, word2, n, m - 1, mtrx);
        if (mtrx[n - 1][m] == -1)
            LevRecCashIter(word1, word2, n - 1, m, mtrx);
        if (mtrx[n - 1][m - 1] == -1)
            LevRecCashIter(word1, word2, n - 1, m - 1, mtrx);
    
        mtrx[n][m] = get_min(mtrx[n][m - 1] + 1,
                             mtrx[n - 1][m] + 1,
                             mtrx[n - 1][m - 1] + (int)(word1[n-1] != word2[m-1]));
    }
}

int LevRecCash(char *word1, char *word2)
{
    int res = -1;

    int n = strlen(word1) + 1;
    int m = strlen(word2) + 1;
    
    int **mtrx = create_mtrx(n, m);
    
    if (mtrx != NULL)
    {
        set_mtrx(mtrx, n, m, -1);
        LevRecCashIter(word1, word2, n - 1, m - 1, mtrx);
        res = mtrx[n - 1][m - 1];
        delete_mtrx(mtrx, n);
    }

    return res;
}

int DemLevNoRec(char *word1, char *word2)
{
    int res = -1;
    int n = strlen(word1) + 1;
    int m = strlen(word2) + 1;
    int **mtrx = create_mtrx(n, m);
    for (int i = 0; i < n; i++)
        mtrx[i][0] = i;
    for (int j = 0; j < m; j++)
        mtrx[0][j] = j;
    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
        {
            if (word1[i - 1] == word2[j - 1])
                mtrx[i][j] = mtrx[i - 1][j - 1];
            else 
                mtrx[i][j] = 1 + get_min(mtrx[i - 1][j], mtrx[i][j - 1], mtrx[i - 1][j - 1]);
        }

    if (mtrx != NULL)
    {
        res = mtrx[n - 1][m - 1];
        delete_mtrx(mtrx, n);
    }

    return res;
}
