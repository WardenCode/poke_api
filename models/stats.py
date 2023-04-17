#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Stat(BaseModel, Base):
    """Representation of a Stat"""
    __tablename__ = 'stats'

    id = Column(String(128), ForeignKey('pokemon.id'), primary_key=True)
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_attack = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)

    pokemon = relationship("Pokemon", back_populates="stats", uselist=False)

    def __init__(self, *args, **kwargs):
        """initializes Stat"""
        super().__init__(*args, **kwargs)
