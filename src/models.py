from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped,relationship
from sqlalchemy import Integer, String,ForeignKey
from typing import List


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    favorite: Mapped[List["Favorites"]] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorite": self.favorite
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gender : Mapped[str] = mapped_column(nullable=False)
    eye_color : Mapped[str] = mapped_column(nullable=False)
    skin_color : Mapped[str] = mapped_column(nullable=False)
    favorite: Mapped[List["Favorites"]] = relationship()
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)
    terrain: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(nullable=False)
    favorite: Mapped[List["Favorites"]] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,            
            # do not serialize the password, its a security breach
        }
        
class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    people_id : Mapped[int] = mapped_column(ForeignKey('people.id'))
    planets_id : Mapped[int] = mapped_column(ForeignKey('planets.id'))
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planets_id": self.planets_id,                     
            # do not serialize the password, its a security breach
        }