#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Ability(BaseModel, Base):
    """Representation of a Ability"""
    __tablename__ = 'abilities'

    name = Column(String(128), nullable=False)
    pokemon = relationship("Pokemon", secondary="pokemon_ability",
                           back_populates='abilities',
                           viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes Ability"""
        super().__init__(*args, **kwargs)
