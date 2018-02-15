# -*- coding: utf-8 -*-
from bookStore import db
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import OrderDetail

class OrderService():

    @staticmethod
    def order_query(uid):
        """
        根据用户名查询 全部order
        """
        payload = {}
        if uid:
            sql = """
            SELECT
                *
            FROM `order`
            WHERE user_id = :user_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"user_id": uid}).fetchall()
            for row in rows:
                order = {
                    'order_id': row.order_id,
                    'user_id': row.user_id,
                    'quantity': row.quantity,
                    'origin_cost': float(row.origin_cost),
                    'actual_cost': float(row.actual_cost),
                    'order_status': row.order_status,
                    'delivery_status': row.delivery_status,
                    'pay_status': row.pay_status
                }
                payload[row.order_id] = order
            return payload

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def order_detail_query(order_id):
        """
        根据订单名查询 订单的详细书目信息
        """
        payload = {}
        if order_id:
            sql = """
            SELECT
                *
            FROM order_detail
            WHERE order_id = :order_id
            ORDER BY id DESC
            """
            rows = db.session.execute(sql, {"order_id": order_id}).fetchall()
            for row in rows:
                order_detail = {
                    'order_id': row.order_id,
                    'book_name': row.book_name,
                    'isbn': row.isbn,
                    'origin_price': float(row.origin_price),
                    'actual_price': float(row.actual_price),
                    'discount': float(row.discount),
                    'order_quantity': row.order_quantity,
                    'deliveried_quantity': row.deliveried_quantity,
                    'warehouse': row.warehouse
                }
                payload[row.book_name] = order_detail
            return payload

        raise NotImplementedError('不支持的查询方式')
