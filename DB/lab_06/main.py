from db import VetClinic

MENU = "Menu:\n" \
       "1. Выполнить скалярный запрос;\n" \
       "2. Выполнить запрос с несколькими соединениями (JOIN);\n" \
       "3. Выполнить запрос с ОТВ(CTE) и оконными функциями;\n" \
       "4. Выполнить запрос к метаданным;\n" \
       "5. Вызвать скалярную функцию (написанную в третьей лабораторной работе);\n"\
       "6. Вызвать многооператорную или табличную функцию \
(написанную в третьей лабораторной работе);\n" \
       "7. Вызвать хранимую процедуру (написанную в третьей лабораторной работе);\n" \
       "8. Вызвать системную функцию или процедуру;\n" \
       "9. Создать таблицу в базе данных, соответствующую тематике БД;\n" \
       "10. Выполнить вставку данных в созданную таблицу с использованием  \
инструкции INSERT или COPY.\n"

def input_command():
    try:
        command = int(input(MENU))
    except:
        command = -1
        
    if command < 0 or command > 10:
        print("Incorrect value\n")
        
    return command


def main():
    command = -1
    VC = VetClinic()
    
    while command != 0:
        command = input_command()
        
        if command == 1:
            VC.get_scalar_query()
        elif command == 2:
            VC.get_join_query()
        elif command == 3:
            VC.get_otb_query()
        elif command == 4:
            VC.get_metadata_query()
        elif command == 5:
            VC.get_scalar_func()
        elif command == 6:
            VC.call_multioper_query()
        elif command == 7:
            VC.get_stored_proc()
        elif command == 8:
            VC.get_sys_func()
        elif command == 9:
            VC.create_table()
        elif command == 10:
            VC.insert_data()
        else:
            continue
  
if __name__ == "__main__":
    main()           
