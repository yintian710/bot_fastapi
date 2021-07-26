#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: employ.py
@Desc
"""
from app.dependencies import get_db
from tool.CONTANT import SQL_DICT


def select_u(user_id, *args):
    """
    查询"u"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('u', user_id, *args)


def update_u(user_id, kwargs):
    """
    更新"u"表中的数据,调用update_base接口
    :param user_id:
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('u', user_id, **kwargs)


def insert_u(user_id):
    """
    注册u表
    :param user_id:
    :return:
    """
    insert_base('u', user_id)


def select_restaurant(user_id, *args):
    """
    查询"restaurant"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('restaurant', user_id, *args)


def update_restaurant(user_id, kwargs):
    """
    更新"restaurant"表中的数据,调用update_base接口
    :param user_id:
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('restaurant', user_id, **kwargs)


def insert_restaurant(user_id):
    """
    注册eat表
    :param user_id:
    :return:
    """
    insert_base('restaurant', user_id)


def select_wx(user_id, *args):
    """
    查询"wx"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('wx', user_id, *args)


def update_wx(user_id, kwargs):
    """
    更新"wx"表中的数据,调用update_base接口
    :param user_id:
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('wx', user_id, **kwargs)


def insert_wx(user_id):
    """
    注册wx表
    :param user_id:
    :return:
    """
    insert_base('wx', user_id)


def select_card(user_id, *args):
    """
    查询"card"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('card', user_id, *args)


def update_card(where_dict, kwargs):
    """
    更新"card"表中的数据,调用update_base接口
    :param where_dict: 查询条件dict,{字段名：值}
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('card', where_dict, **kwargs)


def insert_card(user_id):
    """
    注册card表
    :param user_id:
    :return:
    """
    insert_base('card', user_id)


def select_game(user_id, *args):
    """
    查询"game"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('game', user_id, *args)


def update_game(user_id, kwargs):
    """
    更新"game"表中的数据,调用update_base接口
    :param user_id:
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('game', user_id, **kwargs)


def insert_game(user_id):
    """
    插入游戏用户信息
    :param user_id:
    :return:
    """
    insert_base('game', user_id)


def select_bank(user_id, *args):
    """
    查询"bank"表中的数据,调用select_base接口
    :param user_id: 被查询的用户id
    :param args: 所有被查询的字段名
    :return:
    """
    return select_base('bank', user_id, *args, )


def update_bank(user_id, kwargs):
    """
    更新"bank"表中的数据,调用update_base接口
    :param user_id:
    :param kwargs: 需要更改的数据dict,{需要更改的字段名:更改之后的值,...}
    :return:
    """
    update_base('bank', user_id, **kwargs)


def insert_bank(user_id):
    """
    注册bank表信息
    :param user_id:
    :return:
    """
    insert_base('bank', user_id)


def select_openid_in_wx(openid):
    """
    查询"wx"表中的数据,调用select_base接口, 不以user_id为查询
    :return:
    """
    db = get_db()
    base = SQL_DICT['wx']
    result = db.query(base.id).filter(base.openid == openid).all()
    db.close()
    return result


def insert_base(base_name: str, user_id: int):
    db = get_db()
    base = SQL_DICT[base_name]
    base.id = user_id
    db.add(base)
    db.commit()
    db.close()


def select_base(base_name: str, user_id: int, *args):
    db = get_db()
    base = SQL_DICT[base_name]
    result = db.query(base).filter(base.id == user_id).first()
    if not result:
        return None
    result = result.get(*args)
    db.close()
    return result


def update_base(base_name: str, user_id: int, **kwargs):
    db = get_db()
    base = SQL_DICT[base_name]
    db.query(base).filter(base.id == user_id).update(kwargs)
    db.commit()
    db.close()


def delete_base(base_name: str, user_id: int):
    db = get_db()
    base = SQL_DICT[base_name]
    db.query(base).filter(base.id == user_id).delete()
    db.commit()
    db.close()


if __name__ == '__main__':
    pass
