int LevRecCashIter(char *string_1, char *string_2, int n, int m, int **cash)
{
    if (cash == NULL) return -1;
    if (n == 0) return m;
    else if (m == 0) return n;
    else if (cash[n][m] != -1) return cash[n][m];
    int cost = (string_1[n-1] != string_2[m-1]) ? 1 : 0;
    int insert = LevRecCashIter(string_1, string_2, n, m - 1, cash) + 1;
    int remove = LevRecCashIter(string_1, string_2, n - 1, m, cash) + 1;
    int replace = LevRecCashIter(string_1, string_2, n - 1, m - 1, cash) + cost;
    cash[n][m] = get_min(
        insert,
        remove,
        replace
    );

    return cash[n][m];
}