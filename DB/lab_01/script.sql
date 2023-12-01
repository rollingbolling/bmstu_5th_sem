drop table if exists cage cascade;
create table if not exists cage(
	id int not null generated always as identity primary key check (id >= 0 AND id <= 1500),
    roomNumber int check (roomNumber >= 1 and roomNumber <= 10),
	cageType int check (cageType >= 0 and cageType <= 10),
	max_amount int check (max_amount >= 1 and max_amount <= 6),
    amount int check (amount <= 6),
);

drop table if exists pTreatment cascade;
create table if not exists pTreatment(
	id int not null generated always as identity primary key,
    drugName varchar(100),
    duration int check (duration <= 60),
    contraindication varchar(100),
    sideEffect varchar(100)
);

drop table if exists disease cascade;
create table if not exists disease(
	id int not null generated always as identity primary key,
	nameDis varchar(64),
    symphtoms varchar(100),
	reasons varchar(100),
    deagnosis varchar(100),
    dangerClassification int check (dangerClassification >= 0 and dangerClassification <= 100)
);

drop table if exists doctor cascade;
create table if not exists doctor(
	id int not null generated always as identity primary key,
	nameDoc varchar(64),
	surname varchar(64),
	midname varchar(64),
	phone varchar(14),
	mail varchar(18),
	birthD date not null
);

drop table if exists pet cascade;
create table if not exists pet(
	id int not null generated always as identity primary key,
	nameP varchar(64),
    gender varchar(1) check (gender = 'm' or gender = 'f'),
	weightP int check (weightP >= 0 and weightP <= 40),
	birthDate date not null,
    roomNumber int check (roomNumber >= 0 and roomNumber <= 1500),
	-- refs
	foreign key (roomNumber) references cage(id)
);

drop table if exists pTreatment_pet cascade;
create table if not exists pTreatment_pet
(
	id_pet int not null,
	foreign key (id_pet) references pet(id),
	id_pTreatment int not null,
	foreign key (id_pTreatment) references pTreatment(id)
);

drop table if exists disease_pet cascade;
create table if not exists disease_pet
(
	id_pet int not null,
	foreign key (id_pet) references pet(id),
	id_disease int not null,
	foreign key (id_disease) references disease(id) 
);

drop table if exists doctor_pet cascade;
create table if not exists doctor_pet
(
	id_pet int not null,
	foreign key (id_pet) references pet(id),
	id_doctor int not null,
	foreign key (id_doctor) references doctor(id)
);