#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: restaurant.py
@Desc
"""
from fastapi import APIRouter

from component.restaurant import get_user_restaurant, next_restaurant, go_restaurant, add_restaurants

restaurants = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@restaurants.get('/{user_id}/get_restaurants')
async def get_restaurants(user_id: int):
    result = get_user_restaurant(user_id)
    return result


@restaurants.get('/{user_id}/next')
async def random_food(user_id: int):
    result = next_restaurant(user_id)
    return result


@restaurants.get('/{user_id}/go')
async def random_food(user_id: int):
    result = go_restaurant(user_id)
    return result


@restaurants.post('/{user_id}/add')
async def random_food(user_id: int, add_str: str):
    result = add_restaurants(user_id, add_str)
    return result


if __name__ == '__main__':
    pass
