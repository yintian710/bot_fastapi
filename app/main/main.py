#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: yintian
@date: 2021-07-26
@file: main.py
@Desc
"""
from logging import INFO

import uvicorn as uvicorn
from fastapi import FastAPI

from app.routers.eat import restaurants
from app.routers.score import score

app = FastAPI()

app.include_router(score)
app.include_router(restaurants)


@app.get("/")
async def root(): return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=7100, log_level=INFO)
