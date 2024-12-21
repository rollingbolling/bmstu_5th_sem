import psycopg2

class VetClinic:
    def __init__(self) -> None:
        try:
            self.__connection = psycopg2.connect(
                database="vc",
                user="postgres",
                password="changeme",
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
        
    # 1. Скалярный запрос
    def get_scalar_query(self):
        sql_query = "SELECT COUNT(*) FROM pet"
        if self.__sql_executer(sql_query):
            print("Скалярный запрос. Количество питомцев в клинике:")
            print(self.table[0][0])
    
    # 2.
    def get_join_query(self):
        sql_query = "select pet.namep, cage.cagetype, cage.roomnumber, cage.id \
from pet join cage \
on cage.id = pet.roomnumber and cage.cagetype = 4 and cage.roomnumber = 6;"
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
            
    # 3.
    def get_otb_query(self):
        sql_query = """WITH toc_cte (typec, countc) AS (select cagetype, count(*) from cage group by cagetype)\

select * from toc_cte order by typec;"""
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
    
    # 4. метаданные
    def get_metadata_query(self):
        sql_query = """select * from information_schema.columns where table_schema = 'public';"""
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
    
    # 5.
    def get_scalar_func(self):
        sql_query = """select AvgWeightp();"""
        if self.__sql_executer(sql_query):
            print(self.table[0][0]); 
    
    # 6.
    def call_multioper_query(self):
        sql_query = """select * from func();"""
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
                
    # 7.
    def get_stored_proc(self):
        sql_query = """call pr(); select namep from pet where id > 5000;"""
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
                
    # 8.
    def get_sys_func(self):
        sql_query = "select inet_server_port();"
        if self.__sql_executer(sql_query):
            print(self.table[0][0])

    # 9.
    def create_table(self):
        sql_query = """drop table if exists pet_lab cascade;
create table if not exists pet_lab(
  id int not null generated always as identity primary key,
  nameP varchar(64),
  gender varchar(1),
  weightP int,
  birthDate date not null,
  roomNumber int
);
select * from pet_lab;"""
        if self.__sql_executer(sql_query):
            print("Table was created")

    # 10.
    def insert_data(self):
        sql_query = """insert into pet_lab (namep, gender, weightp, birthdate, roomnumber)
values ('Честер', 'm', 10, '2018-04-20', 69);
select * from pet_lab"""
        if self.__sql_executer(sql_query):
            for row in self.table:
                print(row)
