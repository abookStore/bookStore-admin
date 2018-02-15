# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required

from bookStore import app
from bookStore.service.user.account import AccountService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/account/query', methods=['GET'])
@login_required
def query_user_info():
    """
    @api {GET} /account/query 查询用户账户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于查询用户资料
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {
                        "status": "ok",
                        "payload":{
                            "realname": "132",
                            "username": "bs",
                            "phone": "pwd",
                            "mail": "xxx@xxx.com",
                            "nickname": "guest",
                            "gender": "23",
                            "password": "pwd",
                            "qq": "12312"
                        }
                    }
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "用户不存在"}
    """
    user_id = current_user.id
    app.logger.info(user_id)
    account_info = AccountService.account_query(user_id=user_id)

    if account_info:
        return make_api_response(payload=account_info)
    else:
        return make_api_response(message="用户不存在", statusCode=400)


@exports('/account_consume/query', methods=['GET'])
@login_required
def query_account_consume():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_consume_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload


@exports('/account_prepare/query', methods=['GET'])
@login_required
def query_account_prepare():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_prepay_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload

@exports('/account_refund/query', methods=['GET'])
@login_required
def query_account_refund():
    user_id = current_user.id

    account_service = AccountService()
    rvs = account_service.account_refund_query(user_id)

    if not rvs:
        return make_api_response()

    payload = {}
    for rv in rvs:
        consume = {}
        consume[rv.id] = rv.id
        consume[rv.amount] = rv.amount
        consume[rv.current_balance] = rv.current_balance

        payload[rv.id] = consume

    return payload
