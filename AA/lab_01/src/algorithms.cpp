#include "../inc/algorithms.h"
#include "../inc/allocation.h"


int LevNoRec(wstring &string1, wstring &string2, bool print=false)
{
    size_t n = string1.length();
    size_t m = string2.length();
    int **matrix = create_matrix(n+1, m+1);
    int res = 0;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (i == 0)
                matrix[i][j] = j;
            else if (j == 0)
                matrix[i][j] = i;
            else if (string1[i - 1] == string2[j - 1])
                matrix[i][j] = matrix[i - 1][j - 1];
            else
                matrix[i][j] = min({matrix[i - 1][j], 
                                    matrix[i - 1][j - 1], 
                                    matrix[i][j - 1]});  
        }
    }

    res = matrix[n][m];
    delete_matrix(matrix, n);
    return res;
}

int DemLevNoRec(wstring &string1, wstring &string2, bool print=false)
{
    int res = 0;
    size_t n = string1.length();
    size_t m = string2.length();
    int **matrix = create_matrix(n + 1, m + 1);

    for (size_t i = 1; i <= n; i++)
    {
        for (size_t j = 1; j <= m; j++)
        {
            if (i == 0)
                matrix[i][j] = j;
            else if (j == 0)
                matrix[i][j] = i;
            else if (string1[i - 1] == string2[j - 1])
                matrix[i][j] = matrix[i - 1][j - 1];
            else
                matrix[i][j] = 1 + min({matrix[i - 1][j], 
                                        matrix[i - 1][j - 1],
                                        matrix[i][j - 1]});

            if (i > 1 && j > 1 && \
            string1[i - 1] == string2[j - 2] && string1[i - 2] == string2[j - 1])
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1);
        }
    }

    res = matrix[n][m];
    delete_matrix(matrix, n);
    return res;
}

int DemLevRecNoCache(wstring &string1, wstring &string2, size_t n, size_t m)
{
    int res = 0;

    if (m == 0)
        return 0;
    else if (n == 0)
        return 0;
    
    int cost = 0;
    if (string1[n - 1] != string2[m - 1])
        cost = 1;

    res = min({DemLevRecNoCache(string1, string2, n, m - 1) + 1, 
               DemLevRecNoCache(string1, string2, n - 1, m) + 1,
               DemLevRecNoCache(string1, string2, n - 1, m - 1) + cost});

    if (m > 1 && n > 1 && string1[n - 1] == string2[m - 2] && string1[n - 2] == string2[m - 1])
        res = min(res, DemLevRecNoCache(string1, string2, n - 2, m - 2) + 1);

    return res;
}

int DemLevNoCache(wstring &string1, wstring &string2)
{
    return DemLevRecNoCache(string1, string2, string1.length(), string2.length());
}

int DemLevRecCache(wstring &string1, wstring &string2, int **matrix, size_t n, size_t m)
{
    if (n == 0)
        return matrix[n][m] = m;
    else if (m == 0)
        return  matrix[n][m] = n;

    int cost = (string1[n - 1] == string2[m - 1]) ? 0 : 1;

    matrix[n][m] = min({DemLevRecCache(string1, string2, matrix, n, m - 1) + 1,
                        DemLevRecCache(string1, string2, matrix, n, m - 1) + 1,
                        DemLevRecCache(string1, string2, matrix, n - 1, m - 1) + cost});

    if (n > 1 && m > 1 && string1[n - 1] == string2[m - 2] && string1[n - 2] == string2[m - 1])
        matrix[n][m] = min(matrix[n][m], DemLevRecCache(string1, string2, matrix, n - 2, m - 2) + cost);

    return matrix[n][m];
}

int DemLevCache(wstring &string1, wstring &string2, bool print=false)
{
    size_t n = string1.length();
    size_t m = string2.length();

    int **matrix = create_matrix(n + 1, m + 1);

    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < m; j++)
            matrix[i][j] = -1;

    int res = DemLevRecCache(string1, string2, matrix, n, m);

    delete_matrix(matrix, n);

    return res;
}
