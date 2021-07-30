#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-30
@file: regis.py
@Desc
"""
from fastapi import APIRouter

from Data.RegisData import RegisData
from component.regis import get_login_openid, is_wx_regis, wx_regis

regis = APIRouter(
    prefix="/wx",
    tags=["wx"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@regis.post('/get_open_id')
async def _(params: dict):
    result = await get_login_openid(params)
    return result


@regis.post('/is_wx_regis')
async def _(data: dict):
    result = is_wx_regis(data['openid'])
    return result


@regis.post('/wx_regis')
async def _(data: RegisData):
    result = wx_regis(data.user_id, data.verify_code, data.openid)
    return result


if __name__ == '__main__':
    pass
