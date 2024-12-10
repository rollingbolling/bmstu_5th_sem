--1
select row_to_json(c) result from pet c;
select row_to_json(c1) result from doctor c1;
select row_to_json(h) result from cage h;
select row_to_json(a) result from disease a;
select row_to_json(b) result from ptreatment b;

--2
create table if not exists ptreatment_copy(
    id int not null generated always as identity primary key,
    drugname varchar(100),
    duration int,
    contraindication varchar(100),
    sideeffect varchar(100)
);

\copy --terminal
(
    select row_to_json(c) result from ptreatment c
)
to '~/Desktop/ptreatment.json';

create table if not exists ptreatment_import(ptr json);
\copy ptreatment_import from '~/Desktop/ptreatment.json'; --terminal
select * from ptreatment_import;

insert into ptreatment_copy (drugname, duration, contraindication, sideeffect)
select ptr->>'drugname', cast(ptr->>'duration' as integer), ptr->>'contraindication', ptr->>'sideeffect'
from ptreatment_import;

select * from ptreatment_copy;

--3
create table if not exists ptreatment_json
(
    data json
);

insert into ptreatment_json
select * from json_object('{drugname, duration, contraindication, sideeffect}',
                          '{"chesterfield", 12, "blablala", "lalabla"}');

select * from ptreatment_json;

create table if not exists json_table
(
    id serial primary key,
    drugname varchar(100) not null,
    data json
);

insert into json_table(drugname, data) values
('kazar', '{"age": 22, "group": "IU7-55B"}'::json),
('kazar2', '{"age": 21, "group": "IU7-56B"}'::json);

select * from json_table;

--4.1
drop table ptreatment_name_dur;
create table if not exists ptreatment_name_dur
(
    drugname varchar(100),
    duration integer
);

select * from ptreatment_import, json_populate_record(NULL::ptreatment_name_dur, ptr);

select ptr->'drugname' name from ptreatment_import;
select ptr->'duration' duration from ptreatment_import;

--4.2
select data->'age' age from json_table;

--4.3
create or replace function get_json_table(u_id int)
returns varchar as '
    select case
                when count.cnt > 0
                    then ''true''
                else ''false''
                end as comment
    from (
                select count(data->''age'') cnt
                from json_table
         )as count;
' language sql;

select * from json_table;
select get_json_table(0);

drop function node_exists cascade;

create or replace function node_exists(json_check jsonb, key text)
returns varchar
as $$
begin
    return (json_check->key);
end
$$ language plpgsql;

select node_exists('{"name": "kazar", "age": 24}', 'name');

--4.4
drop table if exists json_st;
create table json_st(ptr jsonb);

insert into json_st values
('{"name": "kazar", "info":{"age": 22, "group": "IU7-55B"}}'),
('{"name": "kazar2", "info":{"age": 23, "group": "IU7-56B"}}');

update json_st
set ptr = ptr || '{"info":{"age": 24}}'::jsonb
where (ptr->'info'->'age')::int = 22;

select * from json_st;

--4.5
create or replace procedure split_json_file()
language plpgsql
as $$
declare object_tmp text;
begin
    select jsonb_pretty(ptr)
    into object_tmp
    from json_st;
    raise notice '%', object_tmp;
end
$$;

call split_json_file();
