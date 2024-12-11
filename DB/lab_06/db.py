import psycopg2

class VetClinic:
    def __init__(self) -> None:
        try:
            self.__connection = psycopg2.connect(
                database="vc",
                user="postgres",
                password="postgres",
                host="127.0.0.1",
                port="5432")
            self.__connection.autocommit = True
            self._cursor = self.__connection.cursor()
            self.table = []
            print("Успешное подключение к БД")
        except Exception as ex:
            print("Ошибка подключения к БД\n", ex)
            return
    
    def __del__(self):
        if self.__connection:
            self._cursor.close()
            self.__connection.close()
            print("Подключение к БД закрыто")
    
    def __sql_executer(self, sql):
       if not self.__connection:
           print("Нет соединения с БД")
           return False
       try:
           self._cursor.execute(sql)
           self.table = self._cursor.fetchall()
           print("Запрос выполнен")
           return True
       except Exception as ex:
           print("Ошибка выполнения запроса\n", ex)
           return False
        
    def get_scalar_query(self):
        print("Скалярный запрос. Количество питомцев в клинике:")
        sql_query = "SELECT COUNT(*) FROM pet"
        if self.__sql_executer(sql_query):
            print(self.table[0])
