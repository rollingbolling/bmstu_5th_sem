create database rk3;

--1
create table if not exists staff
(
    id serial primary key,
    fio text not null,
    birthday date not null,
    department text
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

create table if not exists type_track
(
    id serial primary key,
    name text not null
);

create table if not exists staff_track
(
    id serial primary key,
    id_staff int references staff(id),
    date date not null default CURRENT_DATE,
    dayofweek days not null,
    time time not null,
    type int references type_track(id)
);

INSERT INTO staff (fio, birthday, department)
            values ('Иванов Иван Иванович', to_timestamp('25-09-1990', 'DD-MM-YYYY'), 'ИТ'),
                   ('Петров Петр Петрович', to_timestamp('12-11-1987', 'DD-MM-YYYY'), 'Бухгалтерия');

INSERT into type_track (name)
    values ('пришел'), ('вышел');

INSERT INTO staff_track(idstaff, date, dayofweek, time, type)
    values (1, to_timestamp('14-12-2018', 'DD-MM-YYYY'), 'Суббота', '9:00', 1),
       (1, to_timestamp('14-12-2018', 'DD-MM-YYYY'), 'Суббота', '9:20', 2),
       (1, to_timestamp('14-12-2018', 'DD-MM-YYYY'), 'Суббота', '9:25', 1),
       (2, to_timestamp('14-12-2018', 'DD-MM-YYYY'), 'Суббота', '9:05', 1);



--
CREATE OR REPLACE FUNCTION absent_employees(today_date date)
RETURNS TABLE (fio text, birthday date, department text)
AS $$
BEGIN
    RETURN QUERY
    SELECT s.fio, s.birthday, s.department
    FROM staff s
    WHERE s.id NOT IN (
        SELECT st.id_staff
        FROM staff_track st
        WHERE st.date = today_date
    );
END;
$$ LANGUAGE plpgsql;

SELECT * FROM absent_employees(CURRENT_DATE);
