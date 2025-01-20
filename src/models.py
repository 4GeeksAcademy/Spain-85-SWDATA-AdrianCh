import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet")
    character = relationship("Character")


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(320), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)
    favorites = relationship("Favorite", back_populates="user")


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    gender = Column(String(20), nullable=True)
    homeworld = relationship("Planet")


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')