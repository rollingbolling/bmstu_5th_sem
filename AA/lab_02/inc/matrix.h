#ifndef _MATRIX_H_
#define _MATRIX_H_

#include <iostream>
#include <vector>

using namespace std;

class Matrix
{
    public:
        Matrix() = default;
        Matrix(int rows, int columns);
        Matrix(int rows, int columns, vector<vector<int>>array);

        int inputSizes();
        int createMatrix();
        int fillMatrix();

        void fillRandom();

        int getRows() {return rows;};
        int getColumns() {return columns;};
        vector<vector<int>> getArray() {return array;};

        void printMatrix();

    private:
        int rows;
        int columns;
        vector<vector<int>>array;
};

#endif