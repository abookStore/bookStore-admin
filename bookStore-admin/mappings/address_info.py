# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db

class AddressInfo(db.Model):
    """
    用户收货地址的信息表
    """
    __table_name__ = 'address_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String)
    address = Column(String)
    post_code = Column(String)
    phone = Column(Integer)
    is_active = Column(Integer)
