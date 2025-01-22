create database rk2;

create table if not exists parents(
	id int not null generated always as identity primary key,
    FIO text,
    age int,
    gender varchar(1)
);

create table if not exists children(
	id int not null generated always as identity primary key,
    FIO text,
    birth date,
    gender varchar(1),
    adress varchar(100),
    cafedra varchar(30)
);

create table if not exists groupe(
	id int not null generated always as identity primary key,
    name text,
    FIO text,
    max_hour int
);

create table if not exists parents_children
(
	id_parents int not null,
	foreign key (id_parents) references parents(id),
	id_children int not null,
	foreign key (id_children) references children(id)
);

create table if not exists groupe_children
(
	id_groupe int not null,
	foreign key (id_groupe) references groupe(id),
	id_children int not null,
	foreign key (id_children) references children(id)
);

---------------------

insert into parents (FIO, age, gender) 
values ('Lambert F.F.', 34, 'm'),
                           ('Konker J.J.', 56, 'f'),
                           ('Norton L.J.', 43, 'm'),
                           ('Gordon F.S.', 54, 'm'),
                           ('Huston G.D.', 28, 'f'),
                           ('Jakson I.R.', 50, 'm'),
                           ('Frankel J.B.', 41, 'm'),
                           ('Haton K.R.', 38, 'f'),
                           ('Ranker K.P.', 27, 'f'),
                           ('Tambler U.I.', 32, 'f');

insert into children (FIO, birth, gender, adress, cafedra)
values  ('Hundai 1', '2015-11-20', 'm', 'moscow, kromel 4', 'IU2'),
        ('Hundai 2', '2008-11-20', 'f', 'moscow, kromel 3', 'IU3'),
        ('Hundai 3', '2002-11-20', 'f', 'moscow, kromel 8', 'IU2'),
        ('Hundai 4', '2000-11-20', 'm', 'moscow, kromel 7', 'IU6'),
        ('Hundai 5', '2001-11-20', 'm', 'moscow, kromel 5', 'IU4'),
        ('Hundai 6', '2006-11-20', 'm', 'moscow, kromel 9', 'IU8'),
        ('Hundai 7', '2005-11-20', 'f', 'moscow, kromel 12', 'FN10'),
        ('Hundai 8', '2002-11-20', 'm', 'moscow, kromel 43', 'GH6'),
        ('Hundai 9', '2006-11-20', 'f', 'moscow, kromel 342', 'HJ9'),
        ('Hundai 10', '2003-11-20', 'f', 'moscow, kromel 1', 'DF1');

insert into groupe (name, FIO, max_hour)
values ('pen 1', 'Konker J.J.', 23),
       ('pen 2', 'Norton L.J.',43),
       ('pen 3', 'Tambler U.I', 56),
       ('pen 4', 'Ranker K.P.', 104),
       ('pen 5', 'Jakson I.R.', 23),
       ('pen 6', 'Haton K.R.', 78)
       ('pen 7', 'Huston G.D.', 59),
       ('pen 8', 'Lambert F.F', 98),
       ('pen 9', 'Frankel J.B.', 80),
       ('pen 10','Gordon F.S.', 38);

insert into parents_children
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

insert into groupe_children
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

--task2.1 Выводит ФИО родителей и оценку возраста
select FIO, 
CASE 
when age > 40 then 'old'
when age < 40 then 'young'
end as "conclusion" 
from parents;

--task2.2 обновляет max_hour меньше 24 на максимальное значение 
update groupe
set max_hour = (select max(max_hour) from groupe)
where max_hour < 24;

--task2.3 Выводит всех родителей моложе среденего возраста сгрупированных по полу
select * from parents
group by id, gender like 'f'
having age < (select avg(age) from parents);

--task3 
create or replace procedure find_exec()
as $$
declare 
    rec record;
begin
    for rec in 
        select 
            n.nspname as schema_name,
            p.proname as obj_name,
            case
            when p.prokind = 'p' then 'procedure'
            when p.prokind = 'f' then 'function'
            else 'n/a'
            end as obj_type,
            pg_get_functiondef(p.oid) as obj_def
        from (SELECT * FROM pg_proc p2 WHERE NOT p2.prokind = 'a') p
		join pg_namespace n on n.oid = p.pronamespace
		where n.nspname != 'pg_catalog'
		and n.nspname != 'information_schema'
        and pg_get_functiondef(p.oid) like '%EXEC%'
    loop
    	raise notice 'schema:%, object:%, type:%, def:%',
    	rec.schema_name, rec.obj_name, rec.obj_type, rec.obj_def;
    end loop;

end;
$$ language plpgsql;

call find_exec();
