#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nonebot import on_command, CommandSession
from nonebot.command.argfilter import extractors, validators, converters, controllers  # 提取器，（剪切器自己定义函数），验证器，转换器，控制器
from nonebot import on_natural_language, NLPSession, IntentCommand

from app.utils import word_cut
from .data_source import get_music_id, get_music_styles


@on_command('分享歌曲')
async def music(session: CommandSession):
    t = session.get('type', prompt="你想用QQ还是网易呢？")
    style = session.get('style', prompt="想听哪种歌呢？")
    print(t, style)
    music_share = await get_music_id(t, style)
    print(music_share)
    await session.send(music_share)


@music.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    # 使用！命令需要指定type和style，如果不指定type则默认为163
    if session.is_first_run:
        my_args = stripped_arg.split()
        if my_args:
            try:
                if my_args[0] in ['qq', 'QQ', '网易', '163']:
                    if my_args[0] == 'qq' or my_args[0] == 'QQ':
                        session.state['type'] = 'qq'
                    else:
                        session.state['type'] = '163'
                else:
                    session.state['type'] = '163'
                    session.state['style'] = my_args[0]
                    return
                session.state['style'] = my_args[1]
            except IndexError:
                print("")
            finally:
                return

    # 判断用户回复是否为空
    if session.current_key is not None and stripped_arg == '':
        # 需要连续接收用户输入，并且过程中不需要改变 current_key 时，使用此函数暂停会话。
        session.pause('我看不见啦！')

    if stripped_arg == '算了':
        # 结束当前的会话
        session.finish("拜拜~")

    # 如果是在补全style参数
    if session.current_key == 'style':
        style_list = await get_music_styles()
        if stripped_arg not in style_list:
            session.pause("没有这种曲风喔")
        session.state['style'] = stripped_arg


@on_natural_language(keywords={'歌'})
async def _(session: NLPSession):
    # 播首歌吧（默认163 华语）
    # 搜歌
    stripped_msg = session.msg_text.strip()
    if "播首歌吧" in stripped_msg:
        return IntentCommand(90.0, name='歌曲分享', current_arg="163 华语")
    else:
        word_list, _ = await word_cut(stripped_msg)
        return
