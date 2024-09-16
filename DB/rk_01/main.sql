create database rk2;

create table if not exists drivers(
	id int not null generated always as identity primary key,
    DriverLicense int,
    FIO text,
    Phone varchar(18)
);

create table if not exists cars(
	id int not null generated always as identity primary key,
    Model text,
    Color text,
    Year date not null,
    RegistretionDate date not null
);

create table if not exists fines(
	id int not null generated always as identity primary key,
    FineType text,
    Amount int,
    FineDate date not null
);

create table if not exists Drivers_Cars
(
	id_drivers int not null,
	foreign key (id_drivers) references drivers(id),
	id_cars int not null,
	foreign key (id_cars) references cars(id)
);

create table if not exists Drivers_Fines
(
	id_drivers int not null,
	foreign key (id_drivers) references drivers(id),
	id_fines int not null,
	foreign key (id_fines) references fines(id)
);

---------------------

insert into drivers (DriverLicense, FIO, Phone) 
values (2345, 'Lambert F.F.', +73844305631),
                           (52345, 'Konker J.J.', +73844305634),
                           (1235, 'Norton L.J.', +73844305634),
                           (8072, 'Gordon F.S.', +73844305498),
                           (54368, 'Huston G.D.', +73844309805),
                           (7834, 'Jakson I.R.', +73844305665),
                           (75203, 'Frankel J.B.', +73844305637),
                           (75382, 'Haton K.R.', +73844306890),
                           (34953, 'Ranker K.P.', +73844301276),
                           (75342, 'Tambler U.I.', +73844359087);

insert into cars (Model, Color, Year, RegistretionDate)
values  ('Hundai 1', 'black', '2015-11-20', '2015-12-20'),
        ('Hundai 2', 'wight', '2008-11-20', '2015-11-10'),
        ('Hundai 3', 'red', '2002-11-20', '2015-11-26'),
        ('Hundai 4', 'green', '2000-11-20', '2015-11-12'),
        ('Hundai 5', 'wight', '2001-11-20', '2015-11-11'),
        ('Hundai 6', 'red', '2006-11-20', '2015-11-15'),
        ('Hundai 7', 'black', '2005-11-20', '2015-11-17'),
        ('Hundai 8', 'wight', '2002-11-20', '2015-10-20'),
        ('Hundai 9', 'black', '2006-11-20', '2015-11-19'),
        ('Hundai 10','red', '2003-11-20', '2015-11-29');

insert into fines (FineType, Amount, FineDate)
values ('pen 1', 1500,'2020-12-30'),
       ('pen 2', 6500,'2020-12-19'),
       ('pen 3', 4500,'2020-12-14'),
       ('pen 4', 2500,'2020-12-18'),
       ('pen 5', 7500,'2020-12-26'),
       ('pen 6', 2500,'2020-12-25'),
       ('pen 7', 1500,'2020-12-29'),
       ('pen 8', 1000,'2020-12-28'),
       ('pen 9', 500, '2020-12-30'),
       ('pen 10',8500,'2020-12-31');

insert into Drivers_Fines
values (10,1),
        (9,2),
        (8,3),
        (7,4),
        (6,10),
        (5,9),
        (4,8),
        (3,7),
        (2,6),
        (1,5);

insert into Drivers_Cars
values (10,1),
        (9,2),
        (8,3),
        (7,4),
        (6,10),
        (5,9),
        (4,8),
        (3,7),
        (2,6),
        (1,5);

--task2.1 выводит всех водителей, у которых имя и отчество F.F.
select * 
from drivers 
where FIO like '%F.F.%';

--task2.2 удаляет fine с датой меньше максимальной датой регистрации
delete * from fines 
where FineDate < (select max(RegistretionDate) 
                from cars as c
                where c.RegistretionDate > fines.FineDate);

--task2.3 обновляет fines amount меньше 2000 на максимальное значение где в типе fine есть 1
update fines
set amount = (select max(amount) from fines where FineType like '%1%')
where amount < 2000;

--task3 
CREATE OR REPLACE FUNCTION drop_tables_in_schema(schema_name text) 
RETURNS void AS $$
DECLARE
    table_rec record;
BEGIN
    FOR table_rec IN 
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = schema_name 
        AND table_name LIKE 'tablename%'
    LOOP
        EXECUTE 'DROP TABLE ' || schema_name || '.' || table_rec.table_name || ' CASCADE';
    END LOOP;
END;
$$ LANGUAGE plpgsql;

create table tablename1();
SELECT drop_tables_in_schema('public');
