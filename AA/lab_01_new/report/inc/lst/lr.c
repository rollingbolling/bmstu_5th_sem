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