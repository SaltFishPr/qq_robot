#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import threading


def sss():
    print('start')
    time.sleep(3)
    print('stop')


if __name__ == '__main__':
    # t1 = threading.Timer(1, function=sss)
    # t1.start()
    # print(t1.is_alive())
    # print(type(t1))
    # time.sleep(5)
    # print(t1.is_alive())

    t2 = threading.Thread(target=sss)
    t2.start()
    print(t2.is_alive())
    print(type(t2))
    time.sleep(5)
    print(t2.is_alive())
    pass
