#!/usr/bin/env python3
"""class Pokemon"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class PokemonAbilityAssociation(BaseModel, Base):
    """Representation of a Pokemon Ability association"""
    __tablename__ = 'pokemon_ability'

    pokemon_id = Column(String(128), ForeignKey('pokemon.id'), primary_key=True)
    ability_id = Column(String(128), ForeignKey('abilities.id'), primary_key=True)

    def __init__(self, *args, **kwargs):
        """initializes Pokemon"""
        super().__init__(*args, **kwargs)
