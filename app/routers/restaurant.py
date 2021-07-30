#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: restaurant.py
@Desc
"""
from fastapi import APIRouter

from component.restaurant import get_user_restaurant, next_restaurant, go_restaurant, add_restaurants, change_user_this, \
    change_user_restaurant_name, get_user_all_restaurant_data

restaurants = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@restaurants.post('/get_restaurants')
async def _(user_id: int):
    result = get_user_restaurant(user_id)
    return result


@restaurants.post('/next')
async def _(user_id: int):
    result = next_restaurant(user_id)
    return result


@restaurants.post('/all')
async def _(user_id: int):
    result = get_user_all_restaurant_data(user_id)
    return result


@restaurants.post('/go')
async def _(user_id: int):
    result = go_restaurant(user_id)
    return result


@restaurants.post('/add')
async def _(user_id: int, add_str: str):
    result = add_restaurants(user_id, add_str)
    return result


@restaurants.post('/change_this')
async def _(user_id: int, new_this_num: str):
    result = change_user_this(user_id, new_this_num)
    return result


@restaurants.post('/change_restaurant_name')
async def _(user_id: int, new_restaurant_name: str):
    result = change_user_restaurant_name(user_id, new_restaurant_name)
    return result


@restaurants.post('/go')
async def _(user_id: int):
    result = go_restaurant(user_id)
    return result


if __name__ == '__main__':
    pass
