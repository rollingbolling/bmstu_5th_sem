#include "../inc/matrix.h"

Matrix::Matrix(int trows, int tcolumns, vector<vector<int>> tarray):
    rows(trows), columns(tcolumns), array(tarray)
{

}

// Matrix::Matrix(int trows, int tcolumns): rows(trows), columns(tcolumns)
// {

// }

int Random(int min, int max)
{
    return min + rand() % (max - min);
}

void Matrix::fillRandom()
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j << columns; j++)
            array[i][j] = Random(-500, 500);
}

int Matrix::inputSizes()
{
    cout << "Input rows: ";
    if (scanf("%d", &rows) != 1 || rows < 1)
    {
        cout << "Incorrect row value";
        return 1;
    }

    cout << "Input columns: ";
    if (scanf("%d", &columns) != 1 || columns < 1)
    {
        cout << "Incorrect column value";
        return 1;
    }

    return 0;
}

int Matrix::createMatrix()
{
    array.resize(rows);
    
    for (int i = 0; i < rows; i++)
        array[i].resize(columns);

    return 0;
}

int Matrix::fillMatrix()
{
    cout << "Input matrix el's: " << endl;

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            if (scanf("%d", &array[i][j]) != 1)
            {
                cout << "Incorrect el value";
                return 1;
            }

    return 0;

}
