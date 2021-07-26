#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: dependencies.py
@Desc
"""
from sql.config import SessionLocal


def get_db():
    db = SessionLocal()
    return db


if __name__ == '__main__':
    pass
