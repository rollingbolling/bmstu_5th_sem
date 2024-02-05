#include "../inc/allocation.h"

void delete_matrix(int **matrix, size_t n)
{
    if (matrix != nullptr)
    {
        for (size_t i = 0; i < n; i++)
        {
            if (matrix[i] != nullptr)
                free(matrix[i]);
        }
        free(matrix);
    }
}

int **create_matrix(size_t n, size_t m)
{
    if (n == 0)
        return nullptr;

    // int **mtr = static_cast<int **>(malloc(n * sizeof(int*)));
    // if (mtr != nullptr)
    //     for (size_t i = 0; mtr[i] != nullptr && i < n; i++)
    //     {
    //         mtr[i] = static_cast<int *>(malloc(m * sizeof(int)));
    //         if (mtr[i] == nullptr)
    //             delete_matrix(mtr, n);
    //     }
    int **mtr = new int*[n];
    for (int i = 0; i < n; i++)
        mtr[i] = new int[m];    

    return mtr;
}