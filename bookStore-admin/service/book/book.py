# -*- coding: utf-8 -*-

from bookStore import db
from bookStore.mappings.book import Book

class BookService():

    def book_query_by_isbn(self, isbn):
        """
        根据 isbn 来搜索书目
        """
        if isbn:
            row = db.session.query(Book).filter_by(isbn=isbn, is_active=1).first()

            book_info = {}
            if row:
                book_info['id'] = row.id
                book_info['name'] = row.name
                book_info['author'] = row.author
                book_info['press'] = row.press
                book_info['isbn'] = row.isbn
                book_info['quantity'] = row.quantity
                book_info['description'] = row.description
                book_info['price'] = row.price

            return book_info

        return None

    def book_query_by_name(self, name):
        """
        根据书名来搜索书目
        """
        if name:
            rows = db.session.query(Book).filter_by(name=name).all()

            book_info_all = {}
            for row in rows:
                book_info = {}
                book_info['id'] = row.id
                book_info['name'] = row.name
                book_info['author'] = row.author
                book_info['press'] = row.press
                book_info['isbn'] = row.isbn
                book_info['quantity'] = row.quantity
                book_info['description'] = row.description
                book_info['price'] = row.price

                book_info_all[row.id] = book_info
            return book_info_all

        return None

    def book_add(self, book_info):
        """
        新增书目
        """
        if book_info:
            book = Book()
            book.isbn = book_info.get('isbn')
            book.name = book_info.get('name')
            book.author = book_info.get('author')
            book.press = book_info.get('press')
            book.quantity = book_info.get('quantity')
            book.description = book_info.get('description')
            book.price = book_info.get('price')
            book.is_active = 1

            db.session.add(book)
            db.session.flush(book)
            db.session.commit()

            return True

        return False

    def book_update(self, book_id, book_info):
        """
        更新书目信息
        """
        if book_id and book_info:
            book = db.session.query(Book).filter_by(id=book_id)
            if not book:
                return False

            book.isbn = book_info.get('isbn')
            book.name = book_info.get('name')
            book.author = book_info.get('author')
            book.press = book_info.get('press')
            book.quantity = book_info.get('quantity')
            book.price = book_info.get('price')
            book.description = book_info.get('description')

            db.session.flush(book)
            db.session.commit()

            return True

        return False

    def book_remove(self, book_id):
        """
        删除书目
        """
        if book_id:
            book = db.session.query(Book).filter_by(id=book_id)
            if not book:
                return False

            book.is_active = 0

            db.session.flush(book)
            db.session.commit()

            return True

        return False
