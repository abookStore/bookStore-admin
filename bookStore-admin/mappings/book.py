# -*- coding: utf-8 -*-

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, DECIMAL, String
from bookStore import db


class Book(db.Model):
    """
    书目信息表
    """
    __table_name__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    author = Column(String)
    press = Column(String)
    isbn = Column(Integer)
    quantity = Column(Integer)
    description = Column(String)
    price = Column(DECIMAL)
    is_active = Column(Integer)