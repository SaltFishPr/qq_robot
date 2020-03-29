#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import aiocqhttp
import nonebot
import json
bot = nonebot.get_bot()
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")


@bot.on_message()
async def _(event: aiocqhttp.Event):
    with open(data_folder, 'a', encoding='utf-8') as f:
        f.write(json.dumps({"sender": event.sender, "message": event.message}) + '\n')
