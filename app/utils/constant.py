#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定义常量类
"""
import sys


class _const():
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


# 将constant模块换为调用_const()
sys.modules[__name__] = _const()
