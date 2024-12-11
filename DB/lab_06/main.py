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
            pass
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            pass
        elif command == 6:
            pass
        elif command == 7:
            pass
        elif command == 8:
            pass
        elif command == 9:
            pass
        elif command == 10:
            pass
        else:
            continue
  
if __name__ == "__main__":
    main()           
