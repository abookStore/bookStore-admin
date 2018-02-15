# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.account import Account
from bookStore.mappings.account_consume import AccountConsume
from bookStore.mappings.account_prepay import AccountPrepay
from bookStore.mappings.account_refund import AccountRefund

class AccountService():
    @staticmethod
    def account_query(user_id):
        """
        查询用户账户相关的信息
        """
        payload = {}
        if user_id:
            account = db.session.query(Account).filter_by(user_id=user_id).first()

            if account:
                payload['user_id'] = account.user_id
                payload['balance'] = account.balance
                payload['bonus_point'] = account.bonus_point
                payload['discount'] = account.discount

            return payload

        return None

    def account_consume_query(self, user_id):
        """
        查询用户消费相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountConsume).filter_by(
            user_id=user_id).order_by(AccountConsume.id.desc()).all()

        return rows

    def account_prepay_query(self, user_id):
        """
        查询用户充值相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountPrepay).filter_by(
            user_id=user_id).order_by(AccountPrepay.id.desc()).all()

        return rows

    def account_refund_query(self, user_id):
        """
        查询用户退款相关的记录
        """
        if not user_id:
            return None

        rows = db.session.query(AccountRefund).filter_by(
            user_id=user_id).order_by(AccountRefund.id.desc()) .all()

        return rows
