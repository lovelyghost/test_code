#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile,os,cProfile,pstats

def profile(column="time",list=5):
    def _profile(function):
        def __profile(*args,**kwargs):
            s = tempfile.mktemp()
            profiler = cProfile.Profile()
            profiler.runcall(function,*args,**kwargs)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            p.sort_stats(column).print_stats(list)
        return __profile
    return _profile

@profile("time",6)
def sum_t():
    k = []
    for i in range(1000):
        k.append(i)
    print(k)

sum_t()