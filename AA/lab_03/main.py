from algorithms import *
from test import run_tests
from measure import run_measure
from random import randint

MENU = """MENU:
1. Ручной ввод для поиска в целочисленном массиве
2. Тестирование работы алгоритмов 
3. Исследование работы алгоритмов
0. Выход
"""

def print_res(res, count):
    if res:
        print(res, count)
    else:
        print("No key found")

def create_array(lenght):
    src = []
    while len(src) < lenght:
        el = randint(-1000, 1000)
        if el not in src:
            src.append(el)
    return src

def main(length):
    in_work = True
    src = create_array(length)
    while in_work:
        print(MENU)
        cmd = int(input("Input: "))
        
        if cmd == 0:
            in_work = False
        elif cmd == 1:
            key = int(input("Input element to search: "))
            
            index_l, amount_l = locate(src, key)
            print_res(index_l, amount_l)
            
            src_buff = sorted(src)
            index_b, amount_b = bin_locate(src_buff, key)
            print_res(index_b, amount_b)
            
        elif cmd == 2:
            run_tests()
        elif cmd == 3:
            run_measure(src)


if __name__ == "__main__":
    X = 2034
    length = X % 1000 if X / 8 + ((X >> 2) % 10 == 0) else ((X >> 2) % 10 * (X % 10) + (X >> 1) % 10)
    main(length)