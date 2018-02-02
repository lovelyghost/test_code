# -*- coding:utf-8 -*-

import argparse


def cal(t, a, b):
    if t == 'add':
        print('{}{}{}={}'.format(a, '+', b, a + b))
    elif t == 'mul':
        print('{}{}{}={}'.format(a, '*', b, a * b))
    else:
        print('error')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate two number")
    parser.add_argument('-t', help='add/mul', type=str, default=0)
    parser.add_argument('-n1', help='First num', type=float, default=0)
    parser.add_argument('-n2', help='Second num', type=float, default=0)

    args = parser.parse_args()
    cal(args.t, args.n1, args.n2)