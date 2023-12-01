--1
create or replace function AvgWeightp() returns float4 as $$
	select avg(weightp) from pet;
$$ language sql;
select AvgWeightp();

--2
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
