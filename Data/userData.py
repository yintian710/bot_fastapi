#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-30
@file: userData.py
@Desc
"""
from pydantic import BaseModel


class UserData(BaseModel):
    user_id: int

if __name__ == '__main__':
    pass
