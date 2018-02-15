# -*- coding: utf-8 -*-
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL

from bookStore import db

class OrderDetail(db.Model):
    """
    订单详细信息表
    """
    __table_name__ = 'order_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    book_name = Column(String)
    isbn = Column(Integer)
    origin_price = Column(DECIMAL)
    actual_price = Column(DECIMAL)
    discount = Column(DECIMAL)
    order_quantity = Column(Integer)
    deliveried_quantity = Column(Integer)
    warehouse = Column(String)
