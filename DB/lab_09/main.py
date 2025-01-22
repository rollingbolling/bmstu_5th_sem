from time import time

import matplotlib.pyplot as plt

import psycopg2
import redis
import json
import threading
from random import randint

N_REPEATS = 5

MENU = """MENU:
1. Питомцы из команты 10
2. Приложение выполняет запрос каждые 5 секунд на стороне БД. (задание 3.1)
3. Приложение выполняет запрос каждые 5 секунд через Redis в качестве кэша. (задание 3.2)
4. Гистограммы (задание 3.3)
"""

def connection():
    try:
        con = psycopg2.connect(
                database="vc",
                user="postgres",
                password="changeme",
                host="127.0.0.1",
                port="5432")
    except:
        print("Ошибка подключения")
        return
    
    print("Подключение к БД успешно")
    return con

# 1. Питомцы из команты 10
def get_pets_in_room(cur):
    redis_client = redis.Redis(host="localhost", port = 6379, db = 0)
    cache_val = redis_client.get("pets_in_room")
    if cache_val is not None:
        redis_client.close()
        return json.loads(cache_val)
    cur.execute("select namep from pet where roomnumber = 10")
    res = cur.fetchall()
    
    redis_client.set("pets_in_room", json.dumps(res))
    redis_client.close()
    
    return res

# 2. Приложение выполняет запрос каждые 5 секунд на стороне БД.
def task_02(cur, id):
    threading.Timer(5.0, task_02, [cur, id]).start()

    cur.execute(f"select namep from pet where roomnumber = {id}")

    result = cur.fetchall()

    return result

# 3. Приложение выполняет запрос каждые 5 секунд через Redis в качестве кэша.
def task_03(cur, id):
    threading.Timer(5.0, task_02, [cur, id]).start()

    redis_client = redis.Redis(host="localhost", port=6379, db=0)

    cache_value = redis_client.get(f"dep{id}_workers")
    if cache_value is not None:
        redis_client.close()
        return json.loads(cache_value)

    cur.execute(f"select namep from pet where roomnumber = {id}")

    result = cur.fetchall()
    data = json.dumps(result)
    redis_client.set(f"dep{id}_workers", data)
    redis_client.close()

    return result

# 4.
def dont_do(cur):
    redis_client = redis.Redis()#host="localhost", port=6379, db=0)

    t1 = time()
    cur.execute("select namep from pet where roomnumber = 6")
    t2 = time()

    result = cur.fetchall()

    data = json.dumps(result)
    cache_value = redis_client.get("w1")
    if cache_value is not None:
        pass
    else:
        redis_client.set("w1", data)

    t11 = time()
    redis_client.get("w1")
    t22 = time()

    redis_client.close()

    return t2 - t1, t22 - t11

def del_pet(cur, con):
    redis_client = redis.Redis()

    wid = randint(1, 1000)

    t1 = time()
    cur.execute(f"delete from pTreatment_pet where id_pet = {wid};")
    cur.execute(f"delete from disease_pet where id_pet = {wid};")
    cur.execute(f"delete from doctor_pet where id_pet = {wid};")
    cur.execute(f"delete from pet where id = {wid};")
    t2 = time()

    t11 = time()
    redis_client.delete(f"w{wid}")
    t22 = time()

    redis_client.close()

    con.commit()

    return t2 - t1, t22 - t11

def ins_pet(cur, con):
    redis_client = redis.Redis()

    pet_id = None
    t1 = time()
    
    try:
        # Используем параметризованный запрос для вставки
        cur.execute(
            "INSERT INTO pet (namep, gender, weightp, birthdate, roomnumber) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
            ('Честер', 'm', 10, '2018-04-20', 69)
        )
        pet_id = cur.fetchone()[0]  # Получаем ID только что вставленной записи
        con.commit()  # Фиксируем изменения в базе данных
    except Exception as e:
        con.rollback()  # Откатываем изменения в случае ошибки
        print("Ошибка при вставке в базу данных:", e)
        return None, None

    t2 = time()

    if pet_id is not None:
        try:
            cur.execute("SELECT * FROM pet WHERE id = %s", (pet_id,))
            result = cur.fetchall()

            # Преобразуем данные в JSON
            data = json.dumps(result, default=str)  # Используем `default=str` для обработки даты
            t11 = time()
            redis_client.set(f"w{pet_id}", data)
            t22 = time()
        except Exception as e:
            print("Ошибка при работе с Redis:", e)
            return None, None

    return t2 - t1, t22 - t11

def upd_pet(cur, con):
    redis_client = redis.Redis()

    wid = randint(1, 1000)

    t1 = time()
    cur.execute(f"UPDATE pet SET weightp = 35 WHERE weightp = {wid}")
    t2 = time()

    cur.execute(f"select namep from pet where weightp = {wid};")

    result = cur.fetchall()
    data = json.dumps(result)

    t11 = time()
    redis_client.set(f"w{wid}", data)
    t22 = time()

    redis_client.close()

    con.commit()

    return t2 - t1, t22 - t11

# гистограммы
def task_04(cur, con):
    # simple 
    t1 = 0
    t2 = 0
    for i in range(N_REPEATS):
        print(i)
        b1, b2 = dont_do(cur)
        t1 += b1
        t2 += b2
    print("simple 100 db redis", t1 / N_REPEATS, t2 / N_REPEATS)
    index = ["БД", "Redis"]
    values = [t1 / N_REPEATS, t2 / N_REPEATS]
    plt.bar(index, values)
    plt.title("Без изменения данных")
    plt.show()

    # delete 
    t1 = 0
    t2 = 0
    for i in range(N_REPEATS):
        print(i)
        b1, b2 = del_pet(cur, con)
        t1 += b1
        t2 += b2
    print("delete 100 db redis", t1 / N_REPEATS, t2 / N_REPEATS)

    index = ["БД", "Redis"]
    values = [t1 / N_REPEATS, t2 / N_REPEATS]
    plt.bar(index, values)
    plt.title("При удалении строк каждые 10 секунд")
    plt.show()

    # insert 
    t1 = 0
    t2 = 0
    for i in range(N_REPEATS):
        print(i)
        b1, b2 = ins_pet(cur, con)
        t1 += b1
        t2 += b2
    print("ins_tour 100 db redis", t1 / N_REPEATS, t2 / N_REPEATS)

    index = ["БД", "Redis"]
    values = [t1 / N_REPEATS, t2 / N_REPEATS]
    plt.bar(index, values)
    plt.title("При добавлении новых строк каждые 10 секунд")
    plt.show()

    # updata 
    t1 = 0
    t2 = 0
    for i in range(N_REPEATS):
        print(i)
        b1, b2 = upd_pet(cur, con)
        t1 += b1
        t2 += b2
    print("updata 100 db redis", t1 / N_REPEATS, t2 / N_REPEATS)

    index = ["БД", "Redis"]
    values = [t1 / N_REPEATS, t2 / N_REPEATS]
    plt.bar(index, values)
    plt.title("При изменении строк каждые 10 секунд")
    plt.show()

if __name__ == '__main__':
    con = connection()
    cur = con.cursor()
    
    print(MENU)
    while True:
        c = int(input("Choise: "))
        if c == 1:
            res = get_pets_in_room(cur)
            for el in res:
                print(el[0])
        elif c == 2:
            dep_id = int(input("Номер клетки: "))
            res = task_02(cur, dep_id)
            for el in res:
                print(el[0])
        elif c == 3:
            dep_id = int(input("Номер клетки: "))
            res = task_03(cur, dep_id)
            for el in res:
                print(el[0])
        elif c == 4:
            task_04(cur, con)
        else:
            print("ERROR")
            break
    
    cur.close()
