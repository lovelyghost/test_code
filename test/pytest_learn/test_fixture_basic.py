# # -*- coding:utf-8 -*-

import pytest

@pytest.fixture()
def before():
    print '\nbefore each test'

def test_1(before):
    print 'test_1()'

def test_2(before):
    print 'test_2()'
    assert 0
#test_1和test_2运行之前都调用了before，
    # 也就是before执行了两次。默认情况下，fixture是每个测试用例如果调用了该fixture就会执行一次的。