"""Database models"""

from sqlalchemy import Column, ForeignKey, Integer, String, \
    DateTime, BigInteger, SmallInteger, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Factory(Base):
    """Model for factory"""
    __tablename__ = 'factory'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    resource_type = Column(SmallInteger)

    player_id = Column(BigInteger, ForeignKey('player.id'))
    player = relationship(
        'Player',
        backref=backref('factories', lazy='dynamic')
    )


class FactoryTrack(Base):
    """Model for facctory track"""
    __tablename__ = 'factory_track'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)

    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('factory_tracks', lazy='dynamic')
    )

class FactoryLocation(Base):
    """Model for factory location"""
    __tablename__ = 'factory_location'
    factory_id = Column(Integer, ForeignKey('factory.id'), primary_key=True)
    region_id = Column(Integer, ForeignKey('region.id'), primary_key=True)
    from_date_time = Column(DateTime, primary_key=True)
    until_date_time = Column(DateTime)
    region = relationship('Region')

class FactoryStat(Base):
    """Model for factory"""
    __tablename__ = 'factory_stat'
    id = Column(Integer, primary_key=True)
    level = Column(SmallInteger)
    workers = Column(SmallInteger)
    experience = Column(Integer)
    wage = Column(Integer)

    factory_id = Column(Integer, ForeignKey('factory.id'))
    factory = relationship(
        'Factory',
        backref=backref('factory_stats', lazy='dynamic')
    )
    factory_track_id = Column(Integer, ForeignKey('factory_track.id'))
    factory_track = relationship(
        'FactoryTrack',
        backref=backref('factory_stats', lazy='dynamic')
    )


class State(Base):
    """Model for state"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Region(Base):
    """Model for region"""
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Player(Base):
    """Model for player"""
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    nation = Column(String)
    registration_date = Column(Date)
