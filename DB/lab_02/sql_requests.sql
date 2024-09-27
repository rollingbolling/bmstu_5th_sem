--1
select * from pet
where weightp > 37;

--2
select * from pet
where birthdate between '1990-09-01' and '1991-01-09';

--3 
select namedis 
from disease
where namedis like '%distinct%';

--4
select *
from pet
where roomnumber in (
	select roomnumber 
	from cage
	where roomnumber < 300);

--5
select namep from pet
where exists (select distinct *
			 from cage
			 where cagetype = 5
			 and roomnumber < 300
			 and pet.id = roomnumber);

--6
select * 
from ptreatment
where duration < ALL (select duration 
					  from ptreatment
					  where duration = 13);

--7
select avg(weightp) from pet;

--8
select namep,
(select avg(weightp) from pet, cage
where cage.roomnumber = 3 and cage.id = pet.roomnumber) as normal,
weightp
from pet
where weightp < 20 and id between 1 and 100;

--9
select surname,
case birthd
when '1982-08-16' then 'one'
when '1993-02-26' then 'two'
else 'dmetter'
end as "age"
from doctor;

--10
select surname,
case 
when birthd < '1974-01-01' then 'old'
when birthd between '1974-01-01' and '1990-01-01' then 'normal'
when birthd > '1990-01-01' then 'young'
end as "age"
from doctor;

--11
select namep, avg(weightp)
into temp avgwp
from pet
where birthdate < '1999-09-09'
group by id;

--12
select pet.namep, cage.cagetype, cage.roomnumber, cage.id
from pet
join cage
on cage.id = pet.roomnumber and cage.cagetype = 4 and cage.roomnumber < 6;

--13
select namep
from pet
where weightp = (
	select cagetype
	from cage 
	group by cagetype
	having sum(amount) = 
	(
		select max(am)
		from (select sum(amount) as am
			  from cage
			  group by cagetype) as od
	)
	limit 1
);

--14
select namep, weightp, gender
from pet
where weightp > 39 and gender = 'm'
group by namep, weightp, gender;

--15
select id, namep, avg(weightp)
from pet
group by id
having avg(weightp) > (select avg(dangerclassification) / 2
					   from disease);

--16
insert into pet (namep, gender, weightp, birthdate, roomnumber)
values ('Честер', 'm', 10, '2018-04-20', 69);

--17
insert into pet (namep)
select namedoc
from doctor
where namedoc = 'Игорь';

--18
update pet 
set weightp = 15
where namep like 'herbs';

--19
update pet 
set weightp = (select avg(weightp)
               from pet
               where gender = 'm')
where birthdate between '1999-01-01' and '2000-01-01';

--20
delete from pet 
where id = NULL;

--21
delete from pet 
where namep = (select namedoc
			   from doctor
			   where namedoc = 'Честер'
			   and surname = 'Футоглайн');

--22
WITH toc_cte (typec, countc) AS (
	select cagetype, count(*) 
	from cage 
	group by cagetype);
select * from toc_cte

--23
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

--24
select *, max(weightp) over (partition by roomnumber)
from pet;

--25
with dupl(Row) as (select row_number() 
				   over (partition by roomnumber order by namep) as row 
				   from pet)
select * from dupl where row = 1;

--имя врача, кличка питомца, duration, namediseas, причины по заданному заболеванию
with docdisfr as (
	select 
	dp.id_doctor,
	d.id as desease_id,
	d.nameDis as disease_name,
	count(*) as frequency
	from doctor_pet dp

	join disease_pet dpd on dp.id_pet = dpd.id_pet
	join disease d on dpd.id_disease = d.id

	group by dp.id_doctor, d.id, d.nameDis
),

mostfrdisperdoc as (
	select 
	id_doctor, disease_id, disease_name,
	row_number() over (partition by id_doctor order by frequency) as row_num
	from docdisfr
)
