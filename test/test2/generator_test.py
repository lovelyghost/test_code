#!/usr/bin/env python

# -*- coding:utf-8 -*-

def fibonacci():
    a = b = 1
    # yield a
    print("first:"+str(a))
    # yield b
    print("second:"+str(b))
    while True:
        print("fuck:" + str(b))
        a, b = b, a+b
        yield b
        print("third:" + str(b))


if __name__ == '__main__':

    for num in fibonacci():
        if num > 100: break
        print(num)