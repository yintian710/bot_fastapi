#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: score.py
@Desc
"""

from fastapi import APIRouter

from component.score import search_score, daily_score

score = APIRouter(
    prefix="/score",
    tags=["score"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@score.post('/daily')
async def score_daily(user_id: int):
    """
    用户签到
    :param user_id:
    :return:
    """
    result = daily_score(user_id)
    return result


@score.post('/search')
async def score_search(user_id: int):
    """
    查询积分入口
    :return:
    """
    result = search_score(user_id)
    return result


if __name__ == '__main__':
    pass
