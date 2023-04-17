#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Pokemon(BaseModel, Base):
    """Representation of a Pokemon"""
    __tablename__ = 'pokemon'

    order = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)
    base_experience = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    sprite = Column(String(128), nullable=True)

    stats = relationship("Stat", back_populates="pokemon", uselist=False)
    abilities = relationship("Ability", secondary="pokemon_ability",
                        back_populates="pokemon",
                        viewonly=False)
    types = relationship("Type", secondary="pokemon_type",
                            back_populates="pokemon",
                            viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes Pokemon"""
        super().__init__(*args, **kwargs)
