create database rk3;

--1
create table if not exists satellite
(
    id serial primary key,
    name_satel text not null,
    date_maded date not null,
    country text not null
);

create type days as enum 
(
    'Понедельник', 
    'Вторник', 
    'Среда', 
    'Четверг', 
    'Пятница', 
    'Суббота', 
    'Воскресенье'
);

create table if not exists flight
(
    id serial primary key,
    id_satel int references satellite(id),
    date_launch date not null,
    time_launch time not null,
    dayofweek days not null,
    type int
);

insert into satellite (name_satel, date_maded, country)
values ('SIT-2086', to_timestamp('2050-01-01', 'YYYY-MM-DD'), 'Россия'),
       ('Шицзян 16-02', to_timestamp('2049-12-01', 'YYYY-MM-DD'), 'Китай');

insert into flight (id_satel, date_launch, time_launch, dayofweek, type)
values (1, to_timestamp('2050-05-11', 'YYYY-MM-DD'), '9:00', 'Среда', 1),
       (1, to_timestamp('2051-06-14', 'YYYY-MM-DD'), '23:05', 'Среда', 0),
       (1, to_timestamp('2051-10-10', 'YYYY-MM-DD'), '23:50', 'Вторник', 1),
       (2, to_timestamp('2050-05-11', 'YYYY-MM-DD'), '15:15', 'Среда', 1),
       (2, to_timestamp('2052-01-01', 'YYYY-MM-DD'), '12:15', 'Понедельник', 0);


--выводит аппарат с самым большим количеством прибытий/отбытий
select id_satel, count(*)
from flight f
group by id_satel
order by count(*) desc
limit 1;

--выводит аппараты с количеством записей в flight более 5
select id_satel
from flight f
group by id_satel
having count(*) > 5;
