#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from . import setting


class User(setting.Base):
    """
    recipe
    """
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))


def main():
    setting.Base.metadata.create_all(bind=setting.ENGINE)


if __name__ == '__main__':
    main()
