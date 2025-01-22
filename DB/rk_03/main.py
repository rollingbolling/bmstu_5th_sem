import time 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, Time, CheckConstraint, Date
from sqlalchemy import func

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from operator import and_

Base = declarative_base()

class Satellite(Base):
    __tablename__ = 'satellite'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    name_satel = Column(Text, nullable=False)
    date_maded = Column(Date, default=time.time())
    country = Column(Text, nullable=False)

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    id_satel = Column(Integer, ForeignKey("satellite.id"), nullable=False)
    date_launch = Column(Date, default=time.time())
    dayofweek = Column(Text, CheckConstraint(f"days in {DAYS}"), nullable=False)
    time_launch = Column("time", Time, default=time.time())
    type = Column("type", Integer, CheckConstraint("type = 1 or type = 2"))
    satellite_fk = relationship("Satellite", foreign_keys=[id_satel])

#1
#найти все страны, в которых создано более 10 спутников
def get_countrys(session):
    res = session.execute(f"""
        SELECT country
        FROM satellite
        GROUP BY country
        HAVING COUNT(id) > 10;
    """)
    return res.fetchall()

def get_countrys_more_10(session):
    query = session.query(Satellite.country)\
    .group_by(Satellite.country)\
    .having(func.count(Satellite.id) > 10)\
    .all()

    result = query.all()
    return result

#2
#найти аппараты, которые приземлялись более чем на 100 дней 
def get_satellites_sql(session):
    res = session.execute(f"""
        SELECT s.name_satel
        FROM satellite s
        JOIN flight f1 ON s.id = f1.id_satel
        JOIN flight f2 ON s.id = f2.id_satel
        WHERE f1.type = 1 AND f2.type = 0 
        AND f2.date_launch > f1.date_launch
        AND f2.date_launch - f1.date_launch > 100;
    """)
    return res.fetchall()

def get_satellites(session):
    FlightLaunch = aliased(Flight)
    FlightLanding = aliased(Flight)

    query = session.query(Satellite.name_satel) \
        .join(FlightLaunch, Satellite.id == FlightLaunch.id_satel) \
        .join(FlightLanding, Satellite.id == FlightLanding.id_satel) \
        .filter(
            FlightLaunch.type == 1,
            FlightLanding.type == 0,
            FlightLanding.date_launch > FlightLaunch.date_launch,
            (FlightLanding.date_launch - FlightLaunch.date_launch) > 100
        ) \
        .distinct() \
        .all()

    result = query.all()
    return result
