#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class PokemonTypeAssociation(BaseModel, Base):
    """Representation of a Pokemon Type association"""
    __tablename__ = 'pokemon_type'

    pokemon_id = Column(String(128), ForeignKey('pokemon.id'), primary_key=True)
    type_id = Column(String(128), ForeignKey('types.id'), primary_key=True)

    def __init__(self, *args, **kwargs):
        """initializes Pokemon"""
        super().__init__(*args, **kwargs)