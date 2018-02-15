# -*- coding:utf-8 -*-

from bookStore import db, app
from bookStore.mappings.address_info import AddressInfo

class AddressInfoService():
    def address_info_query(self, user_id):
        """
        查询收货地址的信息
        """
        address_info_list = []
        if user_id:
            rows = db.session.query(AddressInfo).filter_by(
                user_id=user_id).all()

            if rows:
                for row in rows:
                    address_info = {}
                    address_info['id'] = row.id
                    address_info['user_id'] = row.user_id
                    address_info['name'] = row.name
                    address_info['address'] = row.address
                    address_info['post_code'] = row.post_code
                    address_info['phone'] = row.phone
                    address_info['is_default'] = row.is_default

                    address_info_list.append(address_info)

            return address_info_list

        return None

    def address_add(self, address_info):
        """
        新增收货地址
        """
        if address_info:
            info = AddressInfo()
            info.user_id = address_info.get('user_id')
            info.name = address_info.get('name')
            info.address = address_info.get('address')
            info.post_code = address_info.get('post_code')
            info.phone = address_info.get('phone')
            info.is_default = 0

            db.session.commit()

            return True

        return False

    def address_update(self, address_info):
        """
        更新收货地址
        """
        if address_info:
            info_id = address_info.get('id')
            info = db.session.query(AddressInfo).filter_by(
                id=info_id).first()

            info.user_id = address_info.get('user_id')
            info.name = address_info.get('name')
            info.address = address_info.get('address')
            info.post_code = address_info.get('post_code')
            info.phone = address_info.get('phone')
            info.is_default = address_info.get('is_default')

            db.session.flush()
            db.session.commit()

            return True
        return False

    def address_remove(self, address_id):
        """
        删除指定收货地址
        """
        sql = """
        DELETE FROM address_info
        WHERE id = :id
        LIMIT 1;
        """
        if address_id:
            db.session.execute(sql, {'id': address_id})
            db.session.commit()

            return True

        return False


