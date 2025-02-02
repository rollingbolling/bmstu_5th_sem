from algorithms import *

MENU = """MENU:
1. Полный перебор
2. Бинарный поиск
3. Все алгоритмы
0. Выход
INPUT:
"""

def print_res(res, count):
    if res:
        print(res, count)
    else:
        print("No key found")

def menu(src):
    in_work = True
    while in_work:
        print(MENU)
        cmd = int(input())
        
        if cmd == 0:
            in_work = False
        elif cmd in [1, 2, 3]:
            aim = input("Input your search aim: ")
            if cmd == 1:
                result, count = locate(src, aim)
            elif cmd == 2:
                result, count = bin_locate(src, aim)
                
            if cmd != 3: print_res(result, count)
            else:
                print("Brute force")
                result, count = locate(src, aim)
                print_res(result, count)
                print("Bin search")
                result, count = bin_locate(src, aim)
                print_res(result, count)
                
if __name__ == '__main__':
    
