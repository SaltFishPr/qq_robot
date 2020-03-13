#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jieba.posseg as pseg


async def word_cut(text_message):
    word_list, pop_list = [], []  # 分词以及词性列表
    temp = pseg.cut(text_message)
    for x in temp:
        x = tuple(x)
        word_list.append(x[0])
        pop_list.append(x[1])
    word_list.append(' ')
    pop_list.append('x')
    return word_list, pop_list


class Constant:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key: str, value):
        if key in self.__dict__:
            raise self.ConstError("Can't change const %s" % key)
        if not key.isupper():
            raise self.ConstCaseError(
                "const name %s is not all uppercase" % key)
        self.__dict__[key] = value