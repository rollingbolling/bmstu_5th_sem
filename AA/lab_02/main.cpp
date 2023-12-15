#include <iostream>

using namespace std;

int main()
{
    setbuf(stdout, NULL);

    string menu = "Выбирите пункт меню:\n\
                   1. Классическое умножение матриц\n\
                   2. Алгоритм Виноградова\n\
                   3. Оптимизированный алгоритм Виноградова\n\
                   4. Замер и вывод времени реализованных алгоритмов\n\
                   0. Выход\n\
                   ";
    int choice = -1;
    while (choice != 0)
    {
        if (choice == 1)
        {
            cout << "d";
        }
        else if (choice == 2)
        {
            cout << "d";
        }
        else if (choice == 3)
        {
            cout << "d";
        }
    } 

    return 0;
}