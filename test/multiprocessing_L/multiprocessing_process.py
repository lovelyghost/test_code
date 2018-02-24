#coding=utf-8

from multiprocessing import Process
import time


# class MyProcess(Process):
#     '''
#     继承Process类，类似threading.Thread
#     '''
#     def __init__(self, arg):
#         super(MyProcess, self).__init__()
#         #multiprocessing.Process.__init__(self)
#         self.arg = arg
#
#     def run(self):
#         '''
#         重构run函数
#         '''
#         print 'nMask', self.arg
#         time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = MyProcess(i)
#         p.start()
#     for i in range(10):
#     	p.join()
#



from multiprocessing import Process  #导入Process模块
import os

def test(name):
    """
    函数输出当前进程ID，以及其父进程ID。
    此代码应在Linux下运行，因为windows下os模块不支持getppid()
    UID是用户ID，PID是进程ID，PPID是父进程ID
    """

    print "Process ID： %s" % (os.getpid())
    print "Parent Process ID： %s" % (os.getppid())

if __name__ == "__main__":

    proc = Process(target=test, args=('nmask',))
    proc.start()
    proc.join()