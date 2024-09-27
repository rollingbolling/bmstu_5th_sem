alter table cage
  add constraint check_id check (id >= 0 AND id <= 1500),
  add constraint check_roomNumber check (roomNumber >= 0 and roomNumber <= 10),
  add constraint check_cageType check (cageType >= 0 and cageType <= 10),
  add constraint check_max_amount check (max_amount >= 0 and max_amount <= 6),
  add constraint check_amount check (amount <= 6);

alter table pTreatment
  add constraint check_duration check (duration <= 60);

alter table disease
  add constraint check_dangerClassification check (dangerClassification >= 0 and dangerClassification <= 100);

alter table pet
  add constraint check_gender check (gender = 'm' or gender = 'f'),
  add constraint check_weightP check (weightP >= 0 and weightP <= 40),
  add constraint check_roomNumber_pet check (roomNumber >= 0 and roomNumber <= 1500);