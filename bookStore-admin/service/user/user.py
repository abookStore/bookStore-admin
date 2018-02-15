# -*- coding: utf-8 -*-
import hashlib
from bookStore import db, app
from bookStore.mappings.user import User
from bookStore.mappings.account import Account


class SiteUser():
    user = None

    def __init__(self, user):
        self.user = user

    @property
    def is_authenticated(self):
        return self.user is not None

    @property
    def is_active(self):
        return False if self.user is None else self.user.is_active

    @property
    def is_anonymous(self):
        return self.user is None

    def get_id(self):
        return 0 if self.user is None else self.user.id

class UserService():

    @staticmethod
    def query_user_by_name(username=None):
        """
        根据用户昵称查询

        Returns:
            account 不存在时返回 None
        """
        payload = {}
        if username:
            rv = db.session.query(User).filter_by(
                username=username).first()
            if rv:
                payload['username'] = rv.username
                payload['nickname'] = rv.nickname
                payload['realname'] = rv.realname
                payload['password'] = rv.password
                payload['phone'] = rv.phone
                payload['gender'] = rv.gender
                payload['mail'] = rv.mail
                payload['qq'] = rv.qq

                return payload
            return None

        raise NotImplementedError('不支持的查询方式')

    @staticmethod
    def query_user_by_id(userid=None):
        """
        根据用户昵称查询

        Returns:
            account 不存在时返回 None
        """
        payload = {}
        if userid:
            rv = db.session.query(User).filter_by(
                id=userid).first()
            if rv:
                payload['username'] = rv.username
                payload['nickname'] = rv.nickname
                payload['realname'] = rv.realname
                payload['password'] = rv.password
                payload['phone'] = rv.phone
                payload['gender'] = rv.gender
                payload['mail'] = rv.mail
                payload['qq'] = rv.qq

                return payload
            return None

        raise NotImplementedError('不支持的查询方式')


    @staticmethod
    def create_user(userinfo):
        """
        创建新用户
        1. user 表
        2. account 表
        """
        # 用户基本信息的user表
        user = User()
        user.username = userinfo['username']
        user.nickname = userinfo['nickname']
        user.realname = userinfo['realname']
        user.password = userinfo['password']
        user.phone = userinfo['phone']
        user.question = userinfo['question']
        user.answer = userinfo['answer']
        user.gender = userinfo['gender']
        user.mail = userinfo['mail']
        user.qq = userinfo['qq']

        db.session.add(user)
        db.session.flush()

        # 用户账户的account表
        account = Account()
        account.user_id = user.id
        db.session.add(account)
        db.session.flush()

        return True

    @staticmethod
    def get(id):
        user = User.query.filter_by(id=id).first()
        return user

    @staticmethod
    def login(username, password):

        def md5(_):
            m = hashlib.md5()
            m.update(_.encode('utf-8'))
            return m.hexdigest()

        # password = md5(md5(password))
        app.logger.info(password)

        user = User.query.filter_by(
            username=username, password=password).first()
        return (user is not None, user)

    @staticmethod
    def get_usernames(user_ids):
        rows = db.session.query(User).\
            filter(User.id.in_(list(user_ids))).\
            all()
        return {row.id: row.username for row in rows}

    @staticmethod
    def update_userinfo(userinfo):
        username = userinfo['username']
        if username:
            rv = db.session.query(User).filter_by(
                username=username).first()
            if rv:
                rv.nickname = userinfo['nickname']
                rv.realname = userinfo['realname']
                rv.gender = userinfo['gender']
                rv.mail = userinfo['mail']
                rv.phone = userinfo['phone']
                rv.qq = userinfo['qq']

                db.session.commit()
