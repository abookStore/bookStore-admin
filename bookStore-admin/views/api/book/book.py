# -*- coding: utf-8 -*-

from flask import request
from flask_login import current_user, login_required
from bookStore.mappings.book import Book
from bookStore.service.book.book import BookService
from bookStore.views.api import exports
from bookStore.views import make_api_response

@exports('/book/query_by_isbn/<isbn>', methods=['GET'])
@login_required
def query_book_by_isbn(isbn):
    """
    根据 isbn 查询书目信息
    """
    if isbn:
        book_service = BookService()
        rv = book_service.book_query_by_isbn(isbn)
        if rv:
            return make_api_response(payload=rv, message='ok', statusCode=200)
        return make_api_response(message='没有对应书目', statusCode=500)
    
    return make_api_response(message='缺少isbn')


@exports('/book/query_by_name/<name>', methods=['GET'])
@login_required
def query_book_by_name(name):
    """
    根据 name 查询书目信息
    """
    if name:
        book_service = BookService()
        rv = book_service.book_query_by_name(name)
        if rv:
            return make_api_response(payload=rv, message='ok', statusCode=200)
        return make_api_response(message='没有对应书目', statusCode=500)

    return make_api_response(message='缺少isbn')


@exports('/book/remove/<book_id>', methods=['GET'])
@login_required
def book_remove(book_id):
    """
    根据 id 删除书目信息
    """
    if book_id:
        book_sevice = BookService()
        rs = book_sevice.book_remove(book_id)
        if rs:
            return make_api_response()
        else:
            return make_api_response('书目id不存在')
    return make_api_response(message='缺少书目id')

@exports('/book/update', methods=['POST'])
@login_required
def book_update():
    """
    更新书目信息
    """
    book_id = request.json['id']
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    press = request.json['press']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description
    }
    book_service = BookService()
    rv = book_service.book_update(book_id, book_info)

    if rv:
        return make_api_response()
    else:
        return make_api_response(message='更新失败', statusCode=400)


@exports('/book/add', methods=['POST'])
@login_required
def book_add():
    """
    更新书目信息
    """
    isbn = request.json['isbn']
    name = request.json['name']
    author = request.json['author']
    press = request.json['press']
    quantity = request.json['quantity']
    price = request.json['price']
    description = request.json['description']

    book_info = {
        'isbn': isbn,
        'name': name,
        'author': author,
        'press': press,
        'quantity': quantity,
        'price': price,
        'description': description,
        'is_active': 1
    }
    book_service = BookService()
    rv = book_service.book_add(book_info)

    if rv:
        return make_api_response()
    else:
        return make_api_response(message='更新失败', statusCode=400)
