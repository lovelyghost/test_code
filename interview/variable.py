# （一）.global 用途：
#
# (1)、如果要修改函数体外定义的全局变量，需要在对应变量名前加"global"关键字来修饰。（类似授权的概念）
#
# (2)、函数体中的局部变量，如果要在函数体外访问到它，也需要在前加"global"


t = [lambda :x for x in range(10)]


# globle 第一种用法
n = 1
def func():
    n =+ 1
    print(n)
func()