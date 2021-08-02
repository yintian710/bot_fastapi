# -*- coding: utf-8 -*-
"""
@File  : yiban.py
@Author: yintian
@Date  : 2021/8/1 22:14
@Desc  : 
"""
import asyncio
import re

import aiohttp
import time
import hashlib


class YiBan:
    def __init__(self):
        self.login_url = "http://xggl.hnie.edu.cn/website/login"
        self.data_url = "http://xggl.hnie.edu.cn/content/report/student/temp/zzdk/rep/ckzzdkxx"
        self.session = aiohttp.ClientSession()
        self.user_name = '20864'
        self.password = '016565'

    async def start(self):
        await self.login()
        res = await self.get_data()
        await self.session.close()
        result = self.proce_data(res)
        # print(result)
        p_r = self.print_data(result)
        print(p_r)

    async def login(self):
        headers = {
            'Host': "xggl.hnie.edu.cn",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'Connection': "keep-alive",
            'Referer': "http://xggl.hnie.edu.cn/index",
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 3 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 yiban_android'
        }
        data = {
            'username': self.user_name,
            'password': self.get_pw(),
            'action': "signin"
        }
        res = await self.session.post(self.login_url, data=data, headers=headers)
        # print(await res.text())
        return res

    async def get_data(self):
        now = time.strftime("%Y-%m-%d", time.localtime())
        data = f'nj=&yxb=&zy=&bj=&xs=&s_type=2&dkrq={now}&dkdz=&sheng=&shi=&xian=&print_type=1'
        headers = {
            'Host': "xggl.hnie.edu.cn",
            'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'Connection': "keep-alive",
            'Referer': f'http://xggl.hnie.edu.cn/content/menu/student/temp/zzdk/rep/ckzzdkxx'
            f'?_t_s_={int(time.time() / 1000)}',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MIX 3 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 yiban_android',
            'Origin': "http://xggl.hnie.edu.cn",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
        }
        res = await self.session.post(self.data_url, data=data, headers=headers)
        # print(await res.text())
        return await res.text()

    @staticmethod
    def proce_data(data):
        re_role = '>(.*?)<'
        res1 = re.findall(re_role, data)
        res_string = '|'.join(res1)
        res_list = res_string.split('班级：')
        results = {}
        for _ in res_list[1:]:
            result = []
            res_one = _
            one_list = res_one.split('|')
            nums = int((len(one_list) - 8)/5)
            class_name = one_list[0]
            for i in range(nums):
                name = one_list[8 + i * 5]
                result.append(name)
            results[class_name] = result
        return results

    @staticmethod
    def print_data(result):
        str1 = ''
        for k, v in result.items():
            str1 += f'{k}班级当前未打卡人员共{len(v)}人， 名单如下：{",".join(v)} \n'
        return str1[:-1]

    @staticmethod
    def md5(str1):
        m = hashlib.md5()
        m.update(str1.encode("utf8"))
        return m.hexdigest()

    def get_pw(self):
        str1 = self.md5(self.password)
        if len(str1) > 5:
            str1 = str1[:5] + 'a' + str1[5:]
        if len(str1) > 10:
            str1 = str1[:10] + 'b' + str1[10:]
        return str1[:-2]


if __name__ == '__main__':
    yb = YiBan()
    loop = asyncio.get_event_loop()
    resp = loop.run_until_complete(yb.start())
