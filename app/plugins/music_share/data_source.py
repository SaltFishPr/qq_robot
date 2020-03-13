#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

from app.database.music_db import MusicDB


def get_music_list(list_id):
    url = "http://music.163.com/api/playlist/detail?id={}".format(list_id)
    data = requests.get(url)
    data = json.loads(data.text)
    for music in data['result']['tracks']:
        MusicDB.add_music(music['id'], '华语', '163')


async def get_music_id(t, style):
    temp = MusicDB.get_music_id_by_random(style, t)
    print(temp)
    if not temp:
        return "哎呀，仓库需要补货了！"
    return "[CQ:music,type={},id={}]".format(t, temp[0][0])


async def get_music_styles():
    temp = MusicDB.get_all_styles()
    return list(temp[0])


if __name__ == '__main__':
    # get_music_list(2201879658)
    # get_music_id('163', '日语')
    get_music_styles()

