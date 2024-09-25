#include "alloc_mtrx.h"
#include <stdlib.h>
#include <stdio.h>

void delete_mtrx(int **mtrx, size_t n)
{
    if (mtrx != NULL)
    {
        for (size_t i = 0; i < n; i++)
        {
            if (mtrx[i] != NULL)
                free(mtrx[i]);
        }
        free(mtrx);
    }
}

int **create_mtrx(size_t n, size_t m)
{
    if (n == 0 || m == 0)
        return NULL;
    int **mtrx = NULL;
    mtrx = (int**) malloc(sizeof(int *) * n);

    for (size_t i = 0; i < n; i++)
        mtrx[i] = (int*) malloc(sizeof(int) * m);
    
    return mtrx;
}
