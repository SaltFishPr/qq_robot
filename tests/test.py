#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import inspect
import ctypes
from urllib.request import urlretrieve


def callbackinfo(down, block, size):
    '''
    回调函数：
    down：已经下载的数据块
    block：数据块的大小
    size：远程文件的大小
    '''
    per = 100.0 * (down * block) / size
    if per > 100:
        per = 100
    time.sleep(1)
    print('%.2f%%' % per)


# 图片下载函数
def downpic(url):
    urlretrieve(url, 'test.jpg', callbackinfo)


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    for i in range(2):
        if i == 0:
            url = 'https://s1.tuchong.com/content-image/201909/98cac03c4a131754ce46d51faf597230.jpg'
        else:
            break
        t = threading.Thread(target=downpic, args=(url,))
        t.start()
        t.join(5)
        print(t.is_alive())
        if t.is_alive():
            stop_thread(t)
        print("t is kill")
        time.sleep(100)