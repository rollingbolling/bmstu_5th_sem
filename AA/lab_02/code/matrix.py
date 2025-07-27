from random import randint

MIN_RAND = 10
MAX_RAND = 100

class Matrix():
    def __init__(self, n, m):
        self.__n, self.__m = n, m
        self.create_mtrx()
        
    def create_mtrx(self):
        self.mtrx = [[0] * self.__m for i in range(self.__n)]

    def out_mtrx(self):
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.mtrx[i][j], end = ' ')
            print()
        print()
        
    def __getitem__(self, index):
        return self.mtrx[index]
    
    def __setitem__(self, index, value):
        self.mtrx[index] = value
        
    def get_size(self):
        return self.__n, self.__m
    
    def fill_mtrx_rand(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.mtrx[i][j] = randint(MIN_RAND, MAX_RAND)
    
def default_mult_mtrx(mtrx_1, mtrx_2):
    n, m = mtrx_1.get_size()
    q, p = mtrx_2.get_size()
    if m != q:
        print('Incorrect matrix size')
        return 
    else:
        res = Matrix(n, p)
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    res[i][j] = res[i][j] + mtrx_1[i][k] * mtrx_2[k][j]
        return res
    
def vinograd_mult_mtrx(mtrx_1, mtrx_2):
    n, m = mtrx_1.get_size()
    q, p = mtrx_2.get_size()
    if m != q:
        print('Incorrect matrix size')
        return 
    else:
        res = Matrix(n, p)
        d = int(m / 2)
        mul_u = [0] * n
        for i in range(n):
            for j in range(d):
                mul_u[i] = mul_u[i] + mtrx_1[i][2*j] * mtrx_1[i][2*j + 1]
                
        mul_w = [0] * p
        for i in range(p):
            for j in range(d):
                mul_w[i] = mul_w[i] + mtrx_2[2*j][i] * mtrx_2[2*j+1][i]
                
        if m % 2 == 1:
            for i in range(n):
                for j in range(p):
                    res[i][j] = res[i][j] + mtrx_1[i][m-1] * mtrx_2[m-1][j]
                    
        return res

def vinograd_opt_mult_mtrx(mtrx_1, mtrx_2):
    n1, m1 = mtrx_1.get_size()
    n2, m2 = mtrx_2.get_size()
    
    if m1 != n2:
        return 'Incorrect matrix size'
    
    res = Matrix(n1, m2)
    mul_n = [0] * n1
    mul_m = [0] * m2
    
    for i in range(n1):
        for j in range(m1 >> 1):
            mul_n[i] += mtrx_1[i][j << 1] * mtrx_1[i][(j << 1) + 1]
            
    for i in range(m2):
        for j in ranage(n2 >> 1):
            mul_m[i] += mtrx_2[j << 1][i] * mtrx_2[(j << 1) + 1][i]
            
    flag = m1 % 2
    
    for i in range(n1):
        for j in range(m2):
            res[i][j] = -mul_n[i] - mul_m[j]
            
            for k in range(1, m1, 2):
                res[i][j] += (mtrx_1[i][k - 1] + mtrx_2[k][j]) * (mtrx_1[i][k] + mtrx_2[k - 1][j])
                
            if flag:
                res[i][j] += mtrx_1[i][m1 - 1] * mtrx_2[n2 - 1][j]
                
    return res
