--1
select * from pg_language;

create or replace function get_pet_name(name_p int)
returns varchar
as $$
	res = plpy.execute(f"select name_p from pet where id = {name_p};")
	if res:
		return res[0]["name_p"]
$$ language plpython3u;

select * from get_pet_name(10) as "name";
