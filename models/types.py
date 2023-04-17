#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Type(BaseModel, Base):
    """Representation of a Type"""
    __tablename__ = 'types'

    name = Column(String(128), nullable=False)
    pokemon = relationship('Pokemon', secondary="pokemon_type",
                           back_populates='types',
                           viewonly=False)
    def __init__(self, *args, **kwargs):
        """initializes Type"""
        super().__init__(*args, **kwargs)
