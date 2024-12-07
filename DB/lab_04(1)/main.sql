--1 выводит имя питомца с заданным id
--select * from pg_language;

create or replace function get_pet_name(name_p int)
returns varchar
as $$
    res = plpy.execute(f"select name_p from pet where id = {name_p};")
    if res:
        return res[0]["name_p"]
$$ language plpython3u;

select * from get_pet_name(10) as "name";

--2 выводит количетсво питомцев с заданной кличкой
drop function if exists avg_weight_n cascade;
create or replace function avg_weight_n(a int, namep varchar)
returns int
as $$
    n = 0
    avg = 0
    result = plpy.execute(f"select * from pet")
    for i in result:
        if namep == i["namep"]:
            n += 1
    return n
$$ language plpython3u;

create aggregate pet_in_vet_n(varchar)
(
    sfunc = avg_weight_n,
    stype = int
);

select pet_in_vet_n('stool') from pet

--3
create or replace function get_pets(gender_for_search varchar)
returns table
(id int, namep varchar, weightp int)
as $$
	buff = plpy.execute(f"select id, namep, gender, weightp from pet")
	need_gender = None
	for elem in buff:
		if elem["gender"] == gender_for_search:
			need_gender = elem["gender"]
	res = []
	for elem in buff:
		if elem["gender"] == need_gender:
			res.append(elem)
	return res
$$ language plpython3u;

-- select id, namep, gender, weightp from pet;
select * from get_pets('m');

--4
create or replace procedure print_fl(weightp int)
as $$
    query = plpy.prepare(f"update pet set weightp = $1 where namep like 'stool';", ["int"])
    plpy.execute(query, [weightp])
$$ language plpython3u;

call print_fl(23);
select * from pet where namep like 'stool';

--5
create or replace function on_delete_tr()
returns trigger 
as $$
    del_id = TD["old"]["id"]
    run = plpy.execute(f"update pet set namep = 'trigger' where pet.id = {del_id}")
    return TD["new"]
$$ language plpython3u;

-- drop trigger trigger_delete on pet;
drop view pet_copy;
create view pet_copy as
select * from pet;

create trigger trigger_delete
instead of delete on pet_copy
for each row
execute procedure on_delete_tr();

delete from pet_copy
where id > 5000;

select * from pet_copy where id > 4999;

insert into pet(id, namep, gender, weightp, birthdate, roomnumber)
values (default, 'lampa', 'f', 21, '1999-11-11', 69);
select * from pet where id > 5000;

--6
create type most_weightp as
(
    roomnumber int,
    weightp int
);

create or replace function get_most_weight(room int)
returns most_weight
as $$
    plan = plpy.prepare("select roomnumber, weightp from pet where roomnumber = $1;", ["integer"])
    sq = plpy.execute(plan, [room])
    if (sq.nrows()):
        return (sq[0]["roomnumber"], sq[0]["weightp"])
$$ language plpython3u;

select * from get_most_weight('69');
