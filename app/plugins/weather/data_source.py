#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from app.database.city_db import CityDB


async def verifying_city(s):
    return CityDB.search_city(s)


async def get_weather_of_city(location, target_time) -> str:
    data = requests.get(
        "http://wthrcdn.etouch.cn/weather_mini?city=%s" %
        location).text
    data = (json.loads(data))

    def arrange_info(choice, d):
        city = d['data']['city']
        res = ""
        if choice == '今天':
            today_data = d['data']['forecast'][0]
            res = "{choice}是{date}，{city}的最{high}，最{low}，天气{type}。".format(
                choice=choice, city=city, **today_data)
        elif choice == '明天':
            tomorrow_data = d['data']['forecast'][1]
            res = "{choice}是{date}，{city}的最{high}，最{low}，天气{type}。".format(
                choice=choice, city=city, **tomorrow_data)
        elif choice == '接下来五天':
            forecast = d['data']['forecast']
            info1 = "{date}：{type}，{high}，{low}；".format(**forecast[0])
            info2 = "{date}：{type}，{high}，{low}；".format(**forecast[1])
            info3 = "{date}：{type}，{high}，{low}；".format(**forecast[2])
            info4 = "{date}：{type}，{high}，{low}；".format(**forecast[3])
            info5 = "{date}：{type}，{high}，{low}；".format(**forecast[4])
            info6 = d['data']['ganmao']
            res = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
                city, info1, info2, info3, info4, info5, info6)
        return res

    reply = ""
    for t in target_time:
        reply += arrange_info(t, data) + "\n"
    return reply[:len(reply) - 1]
