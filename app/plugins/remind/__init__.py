#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


# @nonebot.scheduler.scheduled_job('cron', hour='*')
# async def _():
#     bot = nonebot.get_bot()
#     try:
#         await bot.send_group_msg(group_id=672076603, message=f'现在{now.hour}点整啦！')
#     except CQHttpError:
#         pass
