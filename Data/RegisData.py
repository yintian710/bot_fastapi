#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-30
@file: RegisData.py
@Desc
"""
from Data.userData import UserData


class RegisData(UserData):
    openid: str = ''
    verify_code: str = ''



if __name__ == '__main__':
    pass
