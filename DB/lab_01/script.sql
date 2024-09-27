drop table if exists cage cascade;
create table if not exists cage(
  id int not null generated always as identity primary key,
  roomNumber int,
  cageType int,
  max_amount int,
  amount int
);

drop table if exists pTreatment cascade;
create table if not exists pTreatment(
  id int not null generated always as identity primary key,
  drugName varchar(100),
  duration int,
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
  dangerClassification int
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
  gender varchar(1),
  weightP int,
  birthDate date not null,
  roomNumber int,
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
