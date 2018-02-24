# -*- coding: utf-8 -*-

from mock import mock
import unittest

from module import Count


# test Count class
class TestCount(unittest.TestCase):

    # # 成功用例
    def test_add(self):
        count = Count()
        # 通过Mock类模拟被调用的方法add()方法，return_value 定义add()方法的返回值。
        count.add = mock.Mock(return_value=13)
        # 　接下来，相当于在正常的调用add()方法，传两个参数2和5，然后会得到相加的结果7。然后，7的结果是我们在上一步就预先设定好的。
        result = count.add(8,5)
        self.assertEqual(result,13)

    # 失败用例
    def test_add1(self):
        count = Count()
        # 通过Mock类模拟被调用的方法add()方法，return_value 定义add()方法的返回值。
        count.add = mock.Mock(return_value=13)
        # 　接下来，相当于在正常的调用add()方法，传两个参数2和5，然后会得到相加的结果7。然后，7的结果是我们在上一步就预先设定好的。
        result = count.add(8, 5)
        # 自定义错误返回信息
        self.assertEqual(result, 12, msg="fuck ,something is wrong")

    # 失败用例
    def test_add2(self):
        count = Count()
        # 通过Mock类模拟被调用的方法add()方法，return_value 定义add()方法的返回值。
        # side_effect参数和return_value是相反的。它给mock分配了可替换的结果，
        # 覆盖了return_value。简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。
        ff = mock.Mock(return_value=13, side_effect=count.add)
        print("fuck me ")
        print(ff)
        print("fuck me ")
        result = ff(8, 8)
        # 检查mock方法是否获得了正确的参数。
        count.add.assert_called_with(3, 8)
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()