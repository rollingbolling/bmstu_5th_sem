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

copy
(
    select row_to_json(c) result from ptreatment c
)
to '/var/lib/postgresql/data/pgdata/json-tables/ptreatment.json';

