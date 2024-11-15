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

int LevNoRec(char *string_1, char *string_2)
{
    int res = -1;

    int n = strlen(string_1) + 1;
    int m = strlen(string_2) + 1;

    int **mtrx = create_mtrx(n, m);

    if (mtrx != NULL) 
    {
        mtrx[0][0]= 0;
        for (int i = 1; i < n; i++)
            mtrx[i][0] = i;
        for (int j = 1; j < m; j++)
            mtrx[0][j] = j;

        int insert = 0;
        int remove = 0;
        int replace = 0;
        
        for (int i = 1; i < n; i++)
            for (int j = 1; j < m; j++)
            {
                insert = mtrx[i][j - 1] + 1;
                remove = mtrx[i - 1][j] + 1;
                replace = mtrx[i - 1][j - 1] + (int)(string_1[i - 1] != string_2[j - 1]);

                mtrx[i][j] = get_min(insert, remove, replace);
            }

        res = mtrx[n - 1][m - 1];
        delete_mtrx(mtrx, n);
    }

    return res;
}

int LevRec(char *string_1, char *string_2, int n, int m)
{
    if (n == 0) return m;
    if (m == 0) return n;

    if (string_1[n - 1] == string_2[m - 1])
        return LevRec(string_1, string_2, n - 1, m - 1);
    
    int insert = LevRec(string_1, string_2, n, m - 1);
    int remove = LevRec(string_1, string_2, n - 1, m);
    int replace = LevRec(string_1, string_2, n - 1, m - 1);

    return 1 + get_min(insert, remove, replace);
}

int LevRecurse(char *string_1, char *string_2)
{
    return LevRec(string_1, string_2, strlen(string_1), strlen(string_2));
}

void LevRecCashIter(char *string_1, char *string_2, int n, int m, int **cash)
{
    if (n == 0) cash[n][m] = m;
    else if (m == 0) cash[n][m] = n;
    else
    {
        if (cash[n][m - 1] == -1)
            LevRecCashIter(string_1, string_2, n, m - 1, cash);
        if (cash[n - 1][m] == -1)
            LevRecCashIter(string_1, string_2, n - 1, m, cash);
        if (cash[n - 1][m - 1] == -1)
            LevRecCashIter(string_1, string_2, n - 1, m - 1, cash);
    
        cash[n][m] = get_min(cash[n][m - 1] + 1,
                             cash[n - 1][m] + 1,
                             cash[n - 1][m - 1] + (int)(string_1[n-1] != string_2[m-1]));
    }
}

int LevRecCash(char *string_1, char *string_2)
{
    int result = -1;

    int n = strlen(string_1) + 1;
    int m = strlen(string_2) + 1;
    
    int **mtrx = create_mtrx(n, m);
    
    if (mtrx != NULL)
    {
        set_mtrx(mtrx, n, m, -1);
        LevRecCashIter(string_1, string_2, n - 1, m - 1, mtrx);
        result = mtrx[n - 1][m - 1];
        if (mtrx != NULL) delete_mtrx(mtrx, n);
    }

    return result;
}

int DemLevNoRec(char *string_1, char *string_2)
{
    int result = -1;
    int n = strlen(string_1) + 1;
    int m = strlen(string_2) + 1;
    int **mtrx = create_mtrx(n, m);
    if (mtrx != NULL)
    {
        mtrx[0][0]= 0;
        for (int i = 1; i < n; i++)
            mtrx[i][0] = i;
        for (int j = 1; j < m; j++)
            mtrx[0][j] = j;
        
        for (int i = 1; i < n; i++)
            for (int j = 1; j < m; j++)
            {
                int cost = string_1[i - 1] == string_2[j - 1] ? 0 : 1;
                mtrx[i][j] = get_min(mtrx[i - 1][j] + 1,\
                                     mtrx[i][j - 1] + 1,\
                                     mtrx[i - 1][j - 1] + cost);
                if (i > 1 && j > 1 && string_1[i - 1] == string_2[j - 2] && string_1[i - 2] == string_2[j - 1])
                {
                    int buff = mtrx[i - 2][j - 2] + cost;
                    if (buff < mtrx[i][j])
                        mtrx[i][j] = buff;
                }
            }
        result = mtrx[n - 1][m - 1];
        delete_mtrx(mtrx, n);
    }
    return result;
}
