# -*- coding: utf-8 -*-
"""
@File  : regis.py
@Author: yintian
@Date  : 2021/5/14 14:27
@Desc  : 
"""
import json
from random import randint

import aiohttp

from sql.employ import select_wx, update_wx, insert_wx, select_openid_in_wx, select_base, insert_base
from tool.CONTANT import pa
from tool.common import get_return
from tool.common import is_regis


async def get_login_openid(data):
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = data['params']
    headers = {
        'Content-Type': 'application/json'
    }
    async with aiohttp.ClientSession() as s:
        async with s.get(url=url, params=params, headers=headers) as res:
            if res.status != 200:
                return get_return('获取失败', code=1)
            data_json = await res.text()
            data_json = json.loads(data_json)
            if data_json.get('openid'):
                return get_return('获取成功', need=data_json)
            else:
                return get_return('获取失败', code=1)


def regis(user_id):
    bases = ['u', 'bank', 'game', 'card']
    for base in bases:
        res = select_base(base, user_id, 'id')
        if not res:
            print(base, '-', user_id)
            insert_base(base, user_id)
            # return

    print(user_id)


def is_wx_regis(openid):
    """
    查询是否已经绑定小程序
    :param openid:
    :return:
    """
    res = select_openid_in_wx(openid)
    if not res:
        return get_return('', need={'user_id': None}, code=0)
    return get_return('', need={'user_id': res[0]})


@is_regis
def wx_regis(user_id, code, openid):
    if not code:
        return pa
    verify_code = select_wx(user_id, 'code')[0]
    if not verify_code:
        return pa
    if verify_code != code:
        update_wx(user_id, {'code': ''})
        return get_return('您输入的验证码不正确，请是重新获取', code=1)
    update_wx(user_id, {"openid": openid, 'code': ''})
    return get_return(f'绑定成功，您的QQ号为：{user_id}')


@is_regis
def delete_wx_regis(user_id):
    update_wx(user_id, {'code': '', 'openid': ''})
    return get_return(f'删除成功：{user_id}')


@is_regis
def get_verify_code(user_id):
    verify_code = str(randint(1000, 9999))
    if not select_wx(user_id, 'Id'):
        insert_wx(user_id)
    update_wx(user_id, {'code': verify_code})
    private_msg = f'您的验证码为:{verify_code}， 注意，验证码仅一次有效，请慎重输入'
    return get_return('', private_msg=private_msg, private_id=user_id)


if __name__ == '__main__':
    # a = get_verify_code(1327960105)
    # print(a)
    # a = is_wx_regis('123')
    regis('12345')
    pass
