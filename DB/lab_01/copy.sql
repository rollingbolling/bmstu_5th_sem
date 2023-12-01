copy cage(roomNumber,cageType,max_amount,amount) from 'C:\Users\danya\Desktop\db_lab_01\data\cages.csv' DELIMITER ',' CSV HEADER;

copy pTreatment(drugName,duration,contraindication,sideEffect) from 'C:\Users\danya\Desktop\db_lab_01\data\pTreatment.csv' DELIMITER ',' CSV HEADER;

copy disease(nameDis,symphtoms,reasons,deagnosis,dangerClassification) from 'C:\Users\danya\Desktop\db_lab_01\data\diseas.csv' DELIMITER ',' CSV HEADER;

copy doctor(nameDoc,surname,midname,phone,mail,birthD) from 'C:\Users\danya\Desktop\db_lab_01\data\doctors.csv' DELIMITER ',' CSV HEADER;

copy pet(nameP,gender,weightP,birthDate,roomNumber) from 'C:\Users\danya\Desktop\db_lab_01\data\pet.csv' DELIMITER ',' CSV HEADER;

copy pTreatment_pet(id_pet,id_pTreatment) from 'C:\Users\danya\Desktop\db_lab_01\data\pTreatment_pet.csv' DELIMITER ',' CSV HEADER;

copy disease_pet(id_pet,id_disease) from 'C:\Users\danya\Desktop\db_lab_01\data\disease_pet.csv' DELIMITER ',' CSV HEADER;

copy doctor_pet(id_pet,id_doctor) from 'C:\Users\danya\Desktop\db_lab_01\data\doctor_pet.csv' DELIMITER ',' CSV HEADER;
