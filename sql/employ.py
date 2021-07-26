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


def insert_base(base_name: str, user_id: int):
    db = get_db()
    base = SQL_DICT[base_name]
    base.id = user_id
    db.add(base)
    db.commit()


def select_base(base_name: str, user_id: int, *args):
    db = get_db()
    base = SQL_DICT[base_name]
    result = db.query(base).filter(base.id == user_id).first()
    result = result.get(*args)
    return result


def update_base(base_name: str, user_id: int, **kwargs):
    db = get_db()
    base = SQL_DICT[base_name]
    db.query(base).filter(base.id == user_id).update(kwargs)
    db.commit()


def delete_base(base_name: str, user_id: int):
    db = get_db()
    base = SQL_DICT[base_name]
    db.query(base).filter(base.id == user_id).delete()
    db.commit()


if __name__ == '__main__':
    pass
