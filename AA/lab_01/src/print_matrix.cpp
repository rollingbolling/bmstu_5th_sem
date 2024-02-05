#include "../inc/print_matrix.h"

void printLevMtr(wstring &string1, wstring &string2, int **mtr, size_t n, size_t m)
{
    for (size_t i = 0; i <= n + 1; i++)
    {
        for (size_t j = 0; j <= m + 1; j++)
        {
            if (i == 0 && j == 0)
                wcout << "  ";
            else if (i == 0)
            {
                if (j == 1)
                    wcout << "  ";
                else
                    wcout << string2[j - 2] << " ";
            }
            else if (j == 0)
            {
                if (i == 1)
                    wcout << "  ";
                else
                    wcout << string1[i - 2] << " ";
            }
            else 
                wcout << mtr[i - 1][j - 1] << " ";
        }
        wcout << endl;
    }
}
