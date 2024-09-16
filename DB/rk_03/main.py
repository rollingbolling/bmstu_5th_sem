import time 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, Time, CheckConstraint, Date
from sqlalchemy import func

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from operator import and_

Base = declarative_base()

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    fio = Column(Text, nullable=False)
    birthday = Column(Date, default=time.time())
    department = Column(Text)

class Staff_track(Base):
    __tablename__ = 'staff_track'
    id = Column(Integer, primary_key=True)
    id_staff = Column(Integer, ForeignKey("staff.id"), nullable=False)
    date = Column(Date, default=time.time())
    dayofweek = Column(Text, CheckConstraint(f"days in {DAYS}"), nullable=False)
    time = Column("time", Time, default=time.time())
    type = Column("type", Integer, CheckConstraint("type = 1 or type = 2"))
    staff_fk = relationship("Staff", foreign_keys=[id_staff])

#1
#найти отделы, в которых работает хотя бы один Иванов
def get_may_staff(session):
    res = session.execute(f"""
        SELECT DISTINCT department 
        FROM staff 
        WHERE fio LIKE '%Иванов%';
    """)
    return res.fetchall()

def get_deps_like_Ivanov(session):
    query = session.query(Staff.department)\
    .filter(Staff.fio.like('%Иванов%'))\
    .distinct()\
    .all()

    result = query.all()
    return result

#2
#найти сотрудников которые не выходят с рабочего места в течении всего рабочего дня 
def get_may_staff(session):
    res = session.execute(f"""
        SELECT s.fio, st.date
        FROM staff s 
        LEFT JOIN staff_track st ON s.id = st.id_staff 
        GROUP BY st.date, s.fio
        HAVING COUNT(st.id) <= 3;
    """)
    return res.fetchall()

def get_employes_dont_exit(session):
    query = session.query(Staff.fio, StaffTrack.date) \
    .outerjoin(StaffTrack, Staff.id == StaffTrack.id_staff) \
    .group_by(StaffTrack.date, Staff.fio) \
    .having(func.count(StaffTrack.id) <= 3) \
    .all()

    result = query.all()
    return result



#3
#найти все оттделы в которых есть сотрудники опоздавшие в определенную дату. дату задавать динамическим параметром
def get_may_staff(session):
    res = session.execute(f"""
        SELECT DISTINCT s.department, st.time
        FROM staff s 
        JOIN staff_track st ON s.id = st.id_staff 
        WHERE st.date = :target_date AND st.time > '09:00:00';
    """)
    return res.fetchall()

def get_employes_dont_exit(session):
    query = session.query(Staff.department)\
    .join(Staff_track, Staff.id == Staff_track.id_staff)\
    .filter(Staff_track.date == target_date, Staff_track.time > '09:00:00')\
    .distinct()\
    .all()


    result = query.all()
    return result
