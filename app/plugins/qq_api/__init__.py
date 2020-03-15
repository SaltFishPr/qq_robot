#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nonebot import on_command, CommandSession
from nonebot.command.argfilter import extractors, validators, converters, controllers  # 提取器，（剪切器自己定义函数），验证器，转换器，控制器
from nonebot import on_natural_language, NLPSession, IntentCommand

from app.plugins.qq_api import data_source
from app.utils import word_cut


@on_command('翻译')
async def translate(session: CommandSession):
    target_language = session.get("target_language", prompt="你想翻译成哪个语言呢？(英语，日语，韩语)")
    message = session.get("message", prompt="请输入要翻译的内容")
    report = await data_source.translation_content(target_language, message)
    await session.send(report)


@translate.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg == "":
            return
        else:
            word_list, _ = await word_cut(stripped_arg)
            try:
                if word_list[0] in ["日语", "英语", "韩语"]:
                    session.state['target_language'] = word_list[0]
                session.state['message'] = ''.join(word_list[1:]).split()[0]
            finally:
                return

    # 判断用户回复是否为空
    if session.current_key is not None and stripped_arg == '':
        # 需要连续接收用户输入，并且过程中不需要改变 current_key 时，使用此函数暂停会话。
        session.pause('欸，隐形的字！')

    if stripped_arg in ['算了', '不查了']:
        # 结束当前的会话
        session.finish("拜拜~")

    # 如果是在补全语言参数
    if session.current_key == 'target_language':
        if stripped_arg in ["日语", "英语", "韩语"]:
            session.state['target_language'] = stripped_arg
        else:
            session.pause('暂时不支持这个语言喔')

    if session.current_key == 'message':
        session.state['message'] = stripped_arg


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
            await session.send(await data_source.chat_content(stripped_arg))
            session.pause()
    if stripped_arg == "":
        session.pause("欸，隐形的字！")
    if stripped_arg in ["不聊了", "拜拜"]:
        session.finish("拜拜~")
    session.pause(await data_source.chat_content(stripped_arg))


@on_natural_language(keywords={'来聊天吧'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
