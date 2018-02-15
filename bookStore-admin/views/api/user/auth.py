# -*- coding: utf-8 -*-
import logging

from flask import request
from flask_login import current_user, login_user, logout_user

from bookStore import app, db
from bookStore.service.user.user import UserService
from bookStore.views.api import exports
from bookStore.views import make_api_response

logger = logging.getLogger(__name__)


# 登录
@exports('/login', methods=['POST'])
def login():
    """
    @api {POST} /login 登录
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于用户登录
    @apiParam {String} username 用户账户名
    @apiParam {String} password 密码
    @apiParamExample {json} 请求样例：
                    {
                        "username": "bs",
                        "password": "pwd"
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {"status":"ok", "message": ""}
    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "参数错误：缺少用户名或密码"}
                   {"status": "fail", "message": "参数错误：用户名或密码错误"}
    """
    username = request.json['username']
    password = request.json['password']
    app.logger.error(username)
    app.logger.error(password)
    if not username or not password:
        return make_api_response(message='参数错误：缺少用户名或密码', statusCode=400)

    (result, user) = UserService.login(username, password)

    if not result:
        return make_api_response(message='用户名或密码错误', statusCode=400)

    login_user(user)
    app.logger.info('%s Login' % user.username)

    return make_api_response()


# 退出
@exports('/logout', methods=['GET'])
def logout():
    """
    @api {GET} /logout 退出登录
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于用户退出登录
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {"status":"ok", "message": ""}
    """
    logout_user()
    return make_api_response()


# 注册
@exports('/register', methods=['POST'])
def register():
    """
    @api {POST} /register 注册用户
    @apiGroup Users
    @apiVersion 0.0.1
    @apiDescription 用于注册用户
    @apiParam {String} username 用户账户名
    @apiParam {String} nickname 昵称
    @apiParam {String} realname 真实姓名
    @apiParam {String} password 密码
    @apiParam {String} pwdquestion 密码提示问题
    @apiParam {String} pwdanswer 密码提示问题答案
    @apiParam {String} gender 性别
    @apiParam {String} mail 邮箱
    @apiParam {String} phone 联系电话
    @apiParam {String} qq QQ
    @apiParamExample {json} 请求样例：
                    {
                        "username": "bs",
                        "nickname": "guest",
                        "realname": "132",
                        "password": "pwd",
                        "pwdquestion": "none",
                        "pwdanswer": "none",
                        "gender": "23",
                        "mail": "xxx@xxx.com",
                        "phone": 1231232,
                        "qq":12312
                    }
    @apiSuccess (200) {String} msg 信息
    @apiSuccess (200) {int} code 0 代表无错误 1代表有错误
    @apiSuccessExample {json} 返回样例:
                   {"status":"ok", "message": ""}

    @apiError (400) {String} msg 信息
    @apiErrorExample {json} 返回样例:
                   {"status": "fail", "message": "参数错误：缺少用户名或密码"}
                   {"status": "fail", "message": "参数错误：用户名已存在"}
    """
    # 获取参数
    user_name = request.json['username']
    display_name = request.json['nickname']
    real_name = request.json['realname']
    password = request.json['password']
    pwd_question = request.json['pwdquestion']
    pwd_answer = request.json['pwdanswer']
    gender = request.json['gender']
    mail = request.json['mail']
    phone = request.json['phone']
    qq = request.json['qq']

    if not user_name or not password:
        return make_api_response(message='参数错误：缺少用户名或密码', statusCode=400)

    user = UserService.query_user_by_name(username=user_name)
    logger.debug(user)
    if user is not None:
        return make_api_response(message='用户名已存在', statusCode=400)

    userinfo = {
        'username': user_name,
        'nickname': display_name,
        'realname': real_name,
        'password': password,
        'question': pwd_question,
        'answer': pwd_answer,
        'gender': gender,
        'mail': mail,
        'phone': phone,
        'qq': qq
    }
    # 创建用户的操作
    ok = UserService.create_user(userinfo)
    db.session.commit()

    return make_api_response()
