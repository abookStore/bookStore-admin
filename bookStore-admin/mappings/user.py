# -*- coding: utf-8 -*-
from flask_login import UserMixin
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db


class User(db.Model, UserMixin):
    """
    登录会员表
    """
    __table_name__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    nickname = Column(String)
    realname = Column(String)
    password = Column(String)
    question = Column(String)
    answer = Column(String)
    gender = Column(String)
    mail = Column(String)
    phone = Column(String)
    qq = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
