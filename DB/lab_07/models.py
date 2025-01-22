from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, Numeric, CheckConstraint, Date, JSON
from sqlalchemy import PrimaryKeyConstraint

BASE = declarative_base()

class Cage(BASE):
    __tablename__ = 'cage'
    id = Column(Integer, primary_key=True)
    roomnumber = Column(Integer, nullable=False)
    cage_type = Column(Integer, nullable=False)
    max_amount = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    
class Treatment(BASE):
    __tablename__ = 'ptreatment'
    id = Column(Integer, primary_key=True)
    drugname = Column(Text, nullable=False)
    duration = Column(Integer, nullable=False)
    contraindication = Column(Text, nullable=False)
    sideeffect = Column(Text, nullable=False)

class Disease(BASE):
    __tablename__ = 'disease'
    id = Column(Integer, primary_key=True)
    nameDis = Column(Text, nullable=False)
    symphtoms = Column(Text, nullable=False)
    reasons = Column(Text, nullable=False)
    deagnosis = Column(Text, nullable=False)
    dangerClassification = Column(Integer, nullable=False)

class Doctor(BASE):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    namedoc = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    midname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    mail = Column(Text, nullable=False)
    birthd = Column(Date, nullable=False)  

class Pet(BASE):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    namep = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    weightp = Column(Integer, nullable=False)
    birthdate = Column(Date, nullable=False)
    roomnumber = Column(Integer, ForeignKey('cage.id'))
    
    room_number_rel = relationship("Cage", foreign_keys=[roomnumber])

class TreatmentPet(BASE):
    __tablename__ = 'treatment_pet'
    treatment_number = Column(Integer, ForeignKey('treatment.id'), primary_key=True)
    pet_number = Column(Integer, ForeignKey('pet.id'), primary_key=True)


class DiseasePet(BASE):
    __tablename__ = 'disease_pet'
    disease_number = Column(Integer, ForeignKey('disease.id'), primary_key=True)
    pet_number = Column(Integer, ForeignKey('pet.id'), primary_key=True)

class DoctorPet(BASE):
    __tablename__ = 'doctor_pet'
    id_doctor = Column(Integer, ForeignKey('doctor.id'), primary_key=True)
    id_pet = Column(Integer, ForeignKey('pet.id'), primary_key=True)
    