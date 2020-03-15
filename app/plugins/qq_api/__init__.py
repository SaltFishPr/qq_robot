#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nonebot import on_command, CommandSession
from nonebot.command.argfilter import extractors, validators, converters, controllers  # 提取器，（剪切器自己定义函数），验证器，转换器，控制器
from nonebot import on_natural_language, NLPSession, IntentCommand

from app.plugins.qq_api import data_source


@on_command('翻译')
async def translate(session: CommandSession):
    pass


@translate.args_parser
async def _(session: CommandSession):
    pass


@on_command('来聊天')
async def chat(session: CommandSession):
    pass


@chat.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg == "":
            session.pause("想聊些什么呢？(●ˇ∀ˇ●)")
        else:
            await session.send(data_source.chat_content(stripped_arg))
            session.pause()
    if stripped_arg == "":
        session.pause("欸，隐形的字！")
    if stripped_arg in ["不聊了", "拜拜"]:
        session.finish("拜拜~")
    session.pause(data_source.chat_content(stripped_arg))


@on_natural_language(keywords={'来聊天吧'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
