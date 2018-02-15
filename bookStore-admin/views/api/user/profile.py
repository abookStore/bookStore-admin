# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_required
from bookStore.service.user.user import UserService
from bookStore.views.api import exports
from bookStore.views import make_api_response


@exports('/profile/query', methods=['GET'])
@login_required
def query_user_info():
    """
    @api {GET} /profile/query 查询用户信息
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
    userinfo = UserService.query_user_by_id(userid=user_id)

    if userinfo:
        return make_api_response(payload=userinfo)
    else:
        return make_api_response(message="用户不存在", statusCode=400)

@exports('/profile/update', methods=['POST'])
@login_required
def update_user_info():
    """
    @api {POST} /profile/query 查询用户信息
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于更新用户资料
    @apiParam {String} username 用户账户名
    @apiParamExample {json} 请求样例：
                    {
                        "realname": "132",
                        "username": "bs",
                        "phone": "1312312312",
                        "mail": "xxx@xxx.com",
                        "nickname": "guest",
                        "gender": "23",
                        "qq": "123122"
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    """
    # 获取参数
    user_name = request.json['username']
    display_name = request.json['nickname']
    real_name = request.json['realname']
    gender = request.json['gender']
    mail = request.json['mail']
    phone = request.json['phone']
    qq = request.json['qq']

    userinfo = {
        'username': user_name,
        'nickname': display_name,
        'realname': real_name,
        'gender': gender,
        'mail': mail,
        'phone': phone,
        'qq': qq
    }
    # 创建用户的操作
    UserService.update_userinfo(userinfo)

    return make_api_response()

