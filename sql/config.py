#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: config.py
@Desc
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ignore.sql_config import SQL_CONFIG

engine = create_engine(SQL_CONFIG, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(engine)

if __name__ == '__main__':
    pass
