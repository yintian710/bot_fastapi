# -*- coding: utf-8 -*-
"""
@File  : restaurant.py
@Author: yintian
@Date  : 2021/6/11 23:43
@Desc  : 
"""
import json
import random
import time

from sql.employ import select_restaurant, update_restaurant
from tool.CONTANT import GO_WEIGHT, NEXT_WEIGHT, RESTAURANT_LIST
from tool.common import is_regis, get_return


def save_restaurants_data(user_id, restaurant, this, go=None) -> None:
    """
    存储用户更改后的食府数据
    :param this:
    :param go:
    :param restaurant:
    :param user_id:
    :return:
    """
    restaurant = json.dumps(restaurant)
    update_data = {'go': go, this: restaurant, 'active': time.time()}
    if go is None:
        update_data.pop('go')
    update_restaurant(user_id, update_data)


def get_restaurants_did(user_id) -> list:
    """
    获取用户历史数据
    :param user_id:
    :return:
    """
    did = select_restaurant(user_id, 'did')[0]
    did = json.loads(did)
    return did


def did_restaurant(user_id, food):
    """
    保存历史go数据
    :param user_id:
    :param food:
    :return:
    """
    did = get_restaurants_did(user_id)
    did.append({'food': food, 'time': time.time()})
    did = json.dumps(did)
    update_restaurant(user_id, {'did': did, 'active': time.time()})


def save_restaurants_cache(user_id, cache):
    """
    保存缓存
    :param user_id:
    :param cache:
    :return:
    """
    cache = json.dumps(cache)
    update_restaurant(user_id, {'cache': cache, 'active': time.time()})


def get_all_restaurant(user_id):
    """
    获取所有数据
    :param user_id:
    :return:
    """
    res = select_restaurant(user_id, '*')
    return res


def get_one_restaurant(user_id, restaurant_name) -> dict:
    """
    获取单个食府数据
    :param user_id:
    :param restaurant_name:
    :return:
    """
    restaurant = select_restaurant(user_id, restaurant_name)
    restaurant = json.loads(restaurant)
    return restaurant


def get_restaurant(user_id) -> (str, dict):
    """
    获取用户当前选定食府数据
    :param user_id:
    :return:
    """
    this = get_this(user_id)
    restaurant = select_restaurant(user_id, this)[0]
    restaurant = json.loads(restaurant)
    return this, restaurant


@is_regis
def get_user_restaurant(user_id):
    """
    获取用户食府数据
    :param user_id:
    :return:
    """
    this, restaurant = get_restaurant(user_id)
    name = restaurant.get('name')
    food = restaurant.get('food')
    str1 = f'您当前食府为{this}号食府{name}，食物为：{"、".join(food.keys())}'
    return get_return(public_msg=str1, need={'restaurant': restaurant})


def get_restaurant_data(user_id):
    """
    获取食府当前go, did以及restaurant数据
    :param user_id:
    :return:
    """
    this = get_this(user_id)
    go, did, restaurant = select_restaurant(user_id, 'go', 'did', this)
    restaurant = json.loads(restaurant)
    return go, did, restaurant


def get_this(user_id) -> str:
    """
    获取当前用户选定食府id
    :param user_id:
    :return:
    """
    this = select_restaurant(user_id, 'this')
    if this:
        return this[0]
    change_this(user_id, 'restaurant1')
    return 'restaurant1'


def change_this(user_id, new_this) -> None:
    """
    改变用户当前选定食府id
    :param new_this:
    :param user_id:
    :return:
    """
    update_restaurant(user_id, {'this': new_this})


def get_random_food(food_dic: dict, ignore=None) -> str:
    """
    获取随即产生的食物
    :param food_dic: 食府中的食物数据
    :param ignore: 需要被忽略的一个食物，往往是已经去了两次的
    :return:
    """
    food = food_dic.copy()
    if ignore:
        food.pop(ignore)
    foods = list(food.keys())
    weights = list(food.values())
    random_food = random.choices(foods, weights=weights)
    return random_food[0]


def new_restaurant(user_id, this, default=None):
    """
    新建食府
    :param user_id:
    :param this:
    :param default:
    :return:
    """
    if not default:
        default = {
            "name": this,
            "last_time": time.time(),
            "food": {}
        }
    default = json.dumps(default)
    update_restaurant(user_id, {this: default})


def change_restaurant_name(user_id, restaurant_name, _this=None):
    """
    更改食府名称
    :param _this:
    :param user_id:
    :param restaurant_name:
    :return:
    """
    this, restaurant = get_restaurant(user_id)
    if _this not in RESTAURANT_LIST:
        return False
    restaurant['name'] = restaurant_name
    save_restaurants_data(user_id, restaurant, this)
    return this


@is_regis
def go_restaurant(user_id):
    """
    选定当前食物
    :param user_id:
    :return:
    """
    this = get_this(user_id)
    go, did, restaurant = get_restaurant_data(user_id)
    if not go:
        return get_return(public_msg=f'不要两次选同一个呀，再摇一下叭~', need={'food': go})
    restaurant['food'][go] += GO_WEIGHT
    restaurant['last_time'] = time.time()
    did_restaurant(user_id, go)
    save_restaurants_data(user_id, restaurant, this, '')
    return get_return(public_msg=f'你选择了{go}， 冲鸭！', need={'food': go})


@is_regis
def next_restaurant(user_id):
    """
    下一个随机食物
    :param user_id:
    :return:
    """
    this = get_this(user_id)
    go, did, restaurant = get_restaurant_data(user_id)
    now = time.time()
    if go:
        restaurant['food'][go] += NEXT_WEIGHT
    food_dic = restaurant['food']
    did = get_restaurants_did(user_id)
    if (len(did) > 2) and (did[-1]['food'] == did[-2]['food'] == go) and (did[-1]['time'] - did[-2]['time'] < 86400) \
            and (now - did[-1]['time'] < 86400):
        ignore = go
    else:
        ignore = None
    food = get_random_food(food_dic, ignore)
    go = food
    restaurant['last_time'] = now
    save_restaurants_data(user_id, restaurant, this, go)
    return get_return(public_msg=f'当前食物为：{food}', need={'food': food})


@is_regis
def add_restaurants(user_id, add):
    """
    添加食府食物
    :param user_id:
    :param add:
    :return:
    """
    this = get_this(user_id)
    go, did, restaurant = get_restaurant_data(user_id)
    add = add.split(' ')
    foods = restaurant['food']
    repeat = ''
    for _ in add:
        if _ in foods:
            repeat += _ + ' '
            continue
        foods[_] = 100
    restaurant['food'] = foods
    save_restaurants_data(user_id, restaurant, this, go)
    return get_return(public_msg=f'添加成功{"!" if not repeat else f", 其中{repeat}重复！"}')


@is_regis
def change_user_this(user_id, new_this_num):
    """
    更改用户当前选择食府
    :param user_id:
    :param new_this_num:
    :return:
    """
    new_this = f'restaurant{new_this_num}'
    if new_this not in RESTAURANT_LIST:
        return get_return('食府id输入错误！')
    if not select_restaurant(user_id, new_this)[0]:
        new_restaurant(user_id, new_this)
    change_this(user_id, new_this)
    return get_return(f'成功切换至食府{new_this}')


@is_regis
def change_user_restaurant_name(user_id, restaurant_name):
    """
    更改用户当前食府名称
    :param user_id:
    :param restaurant_name:
    :return:
    """
    this = change_restaurant_name(user_id, restaurant_name)
    if not this:
        return get_return(f'食府选择出错')
    return get_return(f'{this}成功命名为：{restaurant_name}')


@is_regis
def get_user_all_restaurant_data(user_id):
    """
    获取用户所有食府数据
    :param user_id:
    :return:
    """
    restaurant = get_all_restaurant(user_id)
    result = {}
    for key, value in restaurant.items():
        if not value:
            result[key] = {}
        elif ':' in str(value):
            result[key] = json.loads(value)
        else:
            result[key] = value
    return get_return('获取成功', need=result)


if __name__ == '__main__':
    res = get_user_all_restaurant_data(1327960105)
    print(res)
