# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame ({'交易时间' : np.random.randn(6),
             '学习时间' : ['foo', 'bar'] * 3,
             'dont know' : np.random.randn(6)})

def my_test(a):
    return str(a)

df[['交易时间','dont know']]= df[['交易时间','dont know']].apply(my_test)
print df