# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required
from bookStore.mappings.order import Order
from bookStore.mappings.order_detail import OrderDetail
from bookStore.service.order.order import OrderService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/order/query', methods=['GET'])
@login_required
def query_orders():
    """
    @api {GET} /order/query 查询用户对应的订单信息
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 用于查询用户订单信息
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "12": {
                                "user_id": 123,
                                "order_id": 12,
                                "quantity": 1,
                                "origin_cost": 22.0,
                                "pay_status": 1,
                                "order_status": 1,
                                "actual_cost": 22.0,
                                "delivery_status": 1
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    orders = OrderService.order_query(user_id)

    if orders:
        return make_api_response(payload=orders)
    else:
        return make_api_response(message="用户不存在", statusCode=400)

@exports('/order/detail', methods=['GET'])
@login_required
def query_order_detail():
    """
    @api {GET} /order/detail 查询订单对应的书目详情
    @apiGroup Order
    @apiVersion 0.0.1
    @apiDescription 用于查询用户订单信息
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                        {
                            "payload": {
                                "论语": {
                                "isbn": 12311233,
                                "order_quantity": 42,
                                "book_name": "论语",
                                "origin_price": 1.0,
                                "discount": 3.0,
                                "warehouse": "北京2",
                                "actual_price": 22.0,
                                "order_id": 12,
                                "deliveried_quantity": 21
                                },
                                "诗经": {
                                "isbn": 12312321,
                                "order_quantity": 11,
                                "book_name": "诗经",
                                "origin_price": 12.0,
                                "discount": 2.0,
                                "warehouse": "北京1",
                                "actual_price": 123.0,
                                "order_id": 12,
                                "deliveried_quantity": 2
                                }
                            },
                            "status": "ok"
                        }

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    # 获取参数
    order_id = current_user.id
    order_detail = OrderService.order_detail_query(order_id)

    if order_detail:
        return make_api_response(payload=order_detail)
    else:
        return make_api_response(message="订单不存在", statusCode=400)
