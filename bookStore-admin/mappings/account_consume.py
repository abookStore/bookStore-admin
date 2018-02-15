# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class AccountConsume(db.Model):
    """
    登录会员表
    """
    __table_name__ = 'account_consume'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    amount = Column(DECIMAL)
    current_balance = Column(DECIMAL)
    day = Column(Integer)
    month = Column(Integer)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
