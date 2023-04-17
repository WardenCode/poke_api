#!/usr/bin/env python3
"""
Contains the class DBStorage
"""

import models
from models.pokemon import Pokemon
from models.abilities import Ability
from models.stats import Stat
from models.types import Type
from models.pokemon_ability import PokemonAbilityAssociation
from models.pokemon_type import PokemonTypeAssociation
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine, ClauseElement
from sqlalchemy.orm import scoped_session, sessionmaker

classes = { "Pokemon": Pokemon , "Ability": Ability, "Stat": Stat, "Type": Type }

class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        DB_USER = getenv('DB_USER')
        DB_PASSWORD = getenv('DB_PASSWORD')
        DB_HOST = getenv('DB_HOST')
        DB = getenv('DB')
        # ENV = getenv('ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(DB_USER,
                                             DB_PASSWORD,
                                             DB_HOST,
                                             DB))
        # if ENV == "development":
        #     Base.metadata.drop_all(self.__engine)

    @property
    def session(self):
        return self.__session

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def get_or_create(self, model, **kwargs):
        instance = self.__session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, True

        params = {k: v for k, v in kwargs.items() if not isinstance(v, ClauseElement)}
        instance = model(**params)
        self.new(instance)
        return instance, False

    def bulk_new(self, obj_list):
        """add the object to the current database session"""
        self.__session.bulk_save_objects(obj_list)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def clean(self):
        """
        Clean the DB
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
