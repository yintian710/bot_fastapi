#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: model.py
@Desc
"""

from sqlalchemy import Column, BIGINT, INT, VARCHAR, DATETIME, TEXT

from sql.config import Base


class dBase:

    def get(self, *args):
        return tuple(getattr(self, _) for _ in args)


class U(Base, dBase):
    __tablename__ = 'U'

    id = Column(BIGINT, primary_key=True, default=0)
    score = Column(INT, default=0)
    da = Column(VARCHAR(255), default=0)
    UR = Column(INT, default=0)
    SSR = Column(INT, default=0)
    SR = Column(INT, default=0)
    R = Column(INT, default=0)
    N = Column(INT, default=0)
    estate = Column(INT, default=0)
    rent = Column(INT, default=0)
    rent_time = Column(DATETIME, default='0000-00-00 00:00:00')
    investment = Column(INT, default=0)
    money = Column(INT, default=0)
    achievement = Column(TEXT)
    permission = Column(VARCHAR(255), default='user')


class wx(Base, dBase):
    __tablename__ = 'wx'

    id = Column(BIGINT, primary_key=True, default=0)
    openid = Column(VARCHAR(255))
    code = Column(VARCHAR(255))


class eat(Base, dBase):
    __tablename__ = 'eat'

    id = Column(BIGINT, primary_key=True, default=0)
    restaurants = Column(TEXT)
    did = Column(TEXT)
    active = Column(BIGINT)
    cache = Column(TEXT)


if __name__ == '__main__':
    pass
