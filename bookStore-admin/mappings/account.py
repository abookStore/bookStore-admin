# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class Account(db.Model):
    """
    登录会员表
    """
    __table_name__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    balance = Column(DECIMAL)
    bonus_point = Column(Integer)
    discount = Column(DECIMAL)