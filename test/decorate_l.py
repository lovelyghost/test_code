#!/usr/bin/env python
# -*- coding: utf-8 -*-


def makebold(fn):
    def wrapped():
        print(1)
        print(fn)
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        print(2)
        print(fn)
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    print(3)
    return "hello world"

print hello() ## returns <b><i>hello world</i></b>