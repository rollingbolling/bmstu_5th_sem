--1 средний вес питомца
create or replace function AvgWeightp() returns float4 as $$
	select avg(weightp) from pet;
$$ language sql;
select AvgWeightp();

--2 все питомцы, у которых врач игорь
create or replace function test()
	returns table(
		namep text,
		docname text,
		docsurname text)
	as $$ 
		select pet.namep, doctor.namedoc, doctor.surname
		from pet
		join doctor_pet on pet.id = doctor_pet.id_pet
		join doctor on doctor.id = doctor_pet.id_doctor
		where doctor.namedoc = 'Игорь'
	$$ language sql;
	
select * from test();

--3
create or replace function func()
returns table(namep text, docname text, docsurname text, queu int) as $$
BEGIN
	RETURN QUERY 
	select pet.namep, doctor.namedoc, doctor.surname, 0
	from pet
	join doctor_pet on pet.id = doctor_pet.id_pet
	join doctor on doctor.id = doctor_pet.id_doctor
	where doctor.namedoc = 'Игорь';

	RETURN QUERY 
	select pet.namep, doctor.namedoc, doctor.surname, 1
	from pet
	join doctor_pet on pet.id = doctor_pet.id_pet
	join doctor on doctor.id = doctor_pet.id_doctor
	where doctor.namedoc = 'Олег';

	RETURN QUERY 
	select pet.namep, doctor.namedoc, doctor.surname, 2
	from pet
	join doctor_pet on pet.id = doctor_pet.id_pet
	join doctor on doctor.id = doctor_pet.id_doctor
	where doctor.namedoc = 'Тарас';
END;
$$ language plpgsql;
	
select * from func();

--4
create or replace function pdrec()
returns table(id int, namep text, weight int, room_number_next int) as $$
	with recursive most_weight_pet(id, name, weight, room_number_next) as (
		select id, namep, weightp, 2
		from pet
		where weightp = (select max(weightp)
						from pet 
						where roomnumber = 1)
		and roomnumber = 1

		union all

		select p.id, p.namep, p.weightp, mwp.room_number_next + 1
		from pet as p 
		join most_weight_pet as mwp
		on p.roomnumber = mwp.room_number_next
		where p.weightp = (select max(weightp) 
						   from pet 
						   where roomnumber = p.roomnumber)
	)
	select * from most_weight_pet;
$$ language sql
returns null on null input;
	
select * from pdrec();

--5
create or replace procedure pr()
language sql
as $$
	insert into pet(namep, gender, weightp, birthdate, roomnumber)
	values ('Честер', 'm', 10, '2018-06-06', 69);
$$;
	
call pr();

select namep 
from pet
where id > 5027

--6

