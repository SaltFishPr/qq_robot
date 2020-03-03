#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import jieba
from jieba import posseg
jieba.load_userdict('F:/Programming/Python/qq_robot/app/res/user_dict.txt')
if __name__ == '__main__':
    t1 = '关闭闹钟：1'
    word_list = []
    pop_list = []
    temp = posseg.cut(t1)
    for x in temp:
        x = tuple(x)
        word_list.append(x[0])
        pop_list.append(x[1])
    print(word_list, '\n', pop_list)
    pass
