# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db

class Order(db.Model):
    """
    订单表
    """
    __table_name__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    quantity = Column(Integer)
    origin_cost = Column(DECIMAL)
    actual_cost = Column(DECIMAL)
    order_status = Column(Integer)
    delivery_status = Column(Integer)
    pay_status = Column(Integer)
