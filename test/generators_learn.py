# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
# f = fab(10)
# for i in f:
#     print(i)
# from contextlib import contextmanager
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
# with tag("h1") as ww:
#     print("hello")
#     print("world")
def read_file(fpath):
   BLOCK_SIZE = 10
   n =2
   with open(fpath, 'rb') as f:
       while True:
           n+=2
           block = f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return
d = read_file('100001053122.csv')
for i in d:
    print(i)