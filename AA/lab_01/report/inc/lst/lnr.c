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