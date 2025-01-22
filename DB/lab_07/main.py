import sqlalchemy
from sqlalchemy import create_engine, select, insert, update, delete, func, text
from sqlalchemy.orm import Session, sessionmaker, class_mapper

from json import dumps, load, dump

from models import *

MENU = """\nMenu:
LINQ to Object
1. Вывести всех питомцев
2. Вывести питомцев, чей вес совпадает с номером клетки
3. Вывусти средний вес питомцев
4. Вывести количество питомцев в каждой комнате с клетками
5. Вывести питомца и его врача
LINQ to XML/JSON
6. Запись в файл
7. Чтение из файла
8. Обновление файла
LINQ to SQL
9. Однотабличный запрос на выборку
10. Многотабличный запрос на выборку
11. Добавление данных в БД
12. Изменение данных в БД
13. Удаление данных в БД 
14. select * from pet
15. Получение доступа к данным, выполняя только хранимую процедуру
"""

# 1. Вывести всех питомцев
def get_name_pet(session):
    data = session.query(Doctor).all()
    for row in data:
        print(row.namedoc)

# 2. Вывести питомцев, чей вес совпадает с номером клетки
def get_pet_weight(session):
    data = session.query(Pet).join(Pet.room_number_rel).where(Pet.weightp == Cage.roomnumber).order_by(Pet.id).all()
    for row in data:
        print(row.id, row.namep, row.weightp, row.roomnumber)
        
# 3. Вывусти средний вес питомцев
def get_avg_weight(session):
    data = session.query(func.avg(Pet.weightp).label('avg'))
    for row in data:
        print(row.avg)
        
# 4. Вывести количество питомцев в каждой комнате с клетками
def get_count_pet(session):
    data = session.query(Cage.roomnumber, func.count(Pet.namep).label('count_pet')).join(Cage).group_by(Cage.roomnumber).all()
    for row in data:
        print(row.count_pet, row.roomnumber)
        
# 5. Вывести питомца и его врача
def get_pets_and_doctors(session):
    data = session.query(Pet.namep, Doctor.namedoc).filter(Pet.id == DoctorPet.id_pet).filter(Doctor.id == DoctorPet.id_doctor)
    for row in data:
        print(row)

# 6. Запись в файл        
def serialize_all(model):

    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def pet_to_json(session):
    serialized_labels = [
        serialize_all(label)
        for label in session.query(Pet).order_by(Pet.id).all()
    ]

    for dt in serialized_labels:
        dt["namep"] = str(dt["namep"])
        dt["gender"] = str(dt["gender"])
        dt["birthdate"] = str(dt["birthdate"])

    with open('pets.json', 'w') as f:
        f.write(dumps(serialized_labels, indent=4))

# 7. Чтение из файла
def pet_from_json(session):
    with open('pets.json', 'r') as f:
        pets = load(f)
    for row in pets:
        print(row)        

# 8. Обновление файла
def update_pet_json(session):
    try:
        with open('pets.json', 'r') as f:
            pets = load(f)

        for pet in pets:
            if pet['namep'] == 'digit' and pet['gender'] == 'm':
                pet['gender'] = 'f'

        with open('pets.json', 'w') as f:
            dump(pets, f, indent=4)

        print("Файл успешно обновлен.")
    except FileNotFoundError:
        print("Файл pets.json не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
  
# 9. Однотабличный запрос на выборку
def get_pet(session):
    data = session.execute(select(Pet.namep, Pet.weightp, Pet.roomnumber))
    for row in data:
        print(row)

# 10. Многотабличный запрос на выборку
def get_pet_and_doctor(session):
    data = session.execute(select(Pet.namep, Doctor.namedoc)
        .join(DoctorPet, Pet.id == DoctorPet.id_pet)
        .join(Doctor, Doctor.id == DoctorPet.id_doctor))
    for row in data:
        print(row)

# 11. Добавление данных в БД
def insert_into_pet(session):
    try:
        name = input("name:")
        contri = input("contri:")
        effect = input("effect:")
        dur = int(input("duration:"))
        
        session.execute(insert(Treatment).values(drugname = name, duration = dur, contraindication = contri, sideeffect = effect))
        session.commit()
        print("Sucess")
    except Exception as e: 
        print(f"Error: {e}")
        return
    
# 12. Изменение данных в БД
def update_pets(session):
    name = input("Имя питомца: ")
    weigth = int(input("Вес: "))
    gen = input("Пол: ")
    # spec = input("Новая специальность доктора: ")

    exists = session.query(
        session.query(Pet).where(Pet.namep == name and Pet.weightp == weigth).exists()
    ).scalar()

    if not exists:
        print("Такого Питомца нет!")
        return

    session.execute(
        update(Pet).where(Pet.namep == name and Pet.weightp == weigth).values(gender = gen)
    )
    session.commit()
    print("Данные успешно измененны!")
    
# 13. Удаление данных в БД 
def delete_pets(session):
    name = input("Имя питомца: ")
    weigth = int(input("Вес: "))
    gen = input("Пол: ")

    exists = session.query(
        session.query(Pet).where(Pet.namep == name and Pet.weightp == weigth and Pet.gender == gen).exists()
    ).scalar()

    if not exists:
        print("Такого Питомца нет!")
        return

    session.execute(
        delete(Pet).where(Pet.namep == name and Pet.weightp == weigth and Pet.gender == gen)
    )
    session.commit()
    print("Данные успешно удалены!")

# 14. select * from pet
def select_pets_all(session):
    data = session.query(Pet).order_by(Pet.id).all()
    for d in data:
        print(d.namep, d.weightp, d.gender)

# 15. Вызов функци
def call_func(session):
    data = session.execute(text("SELECT current_timestamp")).all()
    for row in data:
        print(row)

def input_command():
    try:
        command = int(input(MENU))
        print()
    except:
        command = -1
    
    if command < 0 or command > 15:
        print("\nERROR\n")

    return command

def main():
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        f'postgresql://postgres:changeme@localhost:5432/vc',
        pool_pre_ping=True)
    
    try:
        engine.connect()
        print("БД под именнем  tp успешно подключена!")
    except:
        print("Ошибка соединения к БД!")
        return

    Session = sessionmaker(bind=engine)
    session = Session()
    command = -1
    
    while command != 0:
        command = input_command()
        
        if command == 1:
            get_name_pet(session)
        if command == 2:
            get_pet_weight(session)
        if command == 3:
            get_avg_weight(session)
        if command == 4:
            get_count_pet(session)
        if command == 5:
            get_pets_and_doctors(session)
        if command == 6:
            pet_to_json(session)
        if command == 7:
            pet_from_json(session)
        if command == 8:
            update_pet_json(session)
        if command == 9:
            get_pet(session)
        if command == 10:
            get_pet_and_doctor(session)
        if command == 11:
            insert_into_pet(session)
        if command == 12:
            update_pets(session)
        if command == 13:
            delete_pets(session)
        if command == 14:
            select_pets_all(session)
        if command == 15:
            call_func(session)
        else:
            continue
        
if __name__ == "__main__":
    main()