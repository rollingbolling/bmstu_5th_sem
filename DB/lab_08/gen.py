import csv
import datetime
import os
import time
from faker import Faker
import random as r

faker = Faker('ru_RU')
SLEEP_TIME_SEC = 300  # 5 минут

id = 0  # идентификатор файла
name_table = 'users'  # имя таблицы в которую загружаются данные из этого файла
date_mask = '%Y-%m-%d-%H.%M.%S'  # маска для даты и времени формирования файла
file_mask = '{}_{}_{}.csv'  # маска для файла
dir = './nifi/in_file/'  # путь к файлу
user_type = ["физ", "юр"]


def generate_users(count):
    users = []
    for _ in range(count):
        cur_user_type = r.choice(user_type)
        if cur_user_type == "физ":
            name = faker.name()
        else:
            name = faker.company()        
            user = {
                "user_type": cur_user_type,
                "name": name,
                "phone": faker.unique.phone_number(),
                "email": faker.unique.email()
            }
            users.append(user)
    return users


def generate_file(tablename):
    global id
    name = file_mask.format(tablename, id,
                            datetime.datetime.now().strftime(date_mask))
    return os.path.join(dir, name)


def main():
    global id
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        for name in os.listdir(dir):
            file_path = os.path.join(dir, name)
            os.remove(file_path)
            print("Удален файл -", file_path)
        print("Данные удалены!")
        print("=====================================")

    while True:
        fname = generate_file(name_table)
        users = generate_users(10)
        with open(fname, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=users[0].keys())
            writer.writeheader()
            writer.writerows(users)
        print("Файл создан -", fname)
        id += 1
        time.sleep(SLEEP_TIME_SEC)


if __name__ == "__main__":
    main()