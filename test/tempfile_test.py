# # -*- coding:utf-8 -*-

# 实例一：

import os
import tempfile

print 'Building a file name yourself:'
filename = '/tmp/guess_my_name.%s.txt' % os.getpid()
temp = open(filename, 'w+b')
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()
    os.remove(filename)  # Clean up the temporary file yourself

print
print 'TemporaryFile:'
temp = tempfile.TemporaryFile()
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close() # Automatically cleans up the file

    # 这个例子说明了普通创建文件的方法与TemporaryFile()
    # 的不同之处，注意：用TemporaryFile()
    # 创建的文件没有文件名
    #
    # 输出：
#
# 默认情况下使用w + b权限创建文件，在任何平台中都是如此，并且程序可以对它进行读写。这个例子说明了普通创建文件的方法与TemporaryFile()
# 的不同之处，注意：用TemporaryFile()
# 创建的文件没有文件名
#
# 默认情况下使用w + b权限创建文件，在任何平台中都是如此，并且程序可以对它进行读写。
#
# 实例二：
#
import os
import tempfile

temp = tempfile.TemporaryFile()
try:
    temp.write('Some data')
    print "``````````"
    temp.seek(0)
    print temp.seek(0)
    temp.seek(1)
    print temp.seek(1)
    temp.seek(5)
    print temp.seek(5)
    print temp.read()
finally:
    temp.close()
#
# 写入侯，需要使用seek()，为了以后读取数据。
#
# 如果你想让文件以text模式运行，那么在创建的时候要修改mode为
# 'w+t'。
#
# 实例三：
import tempfile

f = tempfile.TemporaryFile(mode='w+t')
try:
    f.writelines(['first\n', 'second\n'])
    f.seek(0)

    for line in f:
        print line.rstrip()
finally:
    f.close()
#
# 如果临时文件会被多个进程或主机使用，那么建立一个有名字的文件是最简单的方法。这就是NamedTemporaryFile要做的，可以使用name属性访问它的名字
#
import os
import tempfile

temp = tempfile.NamedTemporaryFile()
try:
    print "`````````````"
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    # Automatically cleans up the file
    temp.close()
print 'Exists after close:', os.path.exists(temp.name)
#
# 尽管文件带有名字，但它仍然会在close后自动删除
#
#
# tempfile.mkdtemp
#
# 创建临时目录，这个不多说，直接看例子：
#
import os
import tempfile

directory_name = tempfile.mkdtemp()
print directory_name
# Clean up the directory yourself
os.removedirs(directory_name)
#
#
# 用3个参数来控制文件名，名字产生公式：dir + prefix + random + suffix
#
# 实例：
#
import tempfile

temp = tempfile.NamedTemporaryFile(suffix='_suffix',
                                   prefix='prefix_',
                                   dir='/tmp',
                                   )
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()
#

# tempfile.mkstemp([suffix = ''[, prefix = 'tmp'[, dir = None[, text = False]]]])
#
# # mkstemp方法用于创建一个临时文件。该方法仅仅用于创建临时文件，调用tempfile.mkstemp函数后，返回包含两个元素的元组，第一个元素指示操作该临时文件的安全级别，第二个元素指示该临时文件的路径。参数suffix和prefix分别表示临时文件名称的后缀和前缀；dir指定了临时文件所在的目录，如果没有指定目录，将根据系统环境变量TMPDIR, TEMP或者TMP的设置来保存临时文件；参数text指定了是否以文本的形式来操作文件，默认为False，表示以二进制的形式来操作文件。
#
# tempfile.mktemp([suffix = ''[, prefix = 'tmp'[, dir = None]]])
#
# # mktemp用于返回一个临时文件的路径，但并不创建该临时文件。
#
# tempfile.tempdir
#
# # 该属性用于指定创建的临时文件（夹）所在的默认文件夹。如果没有设置该属性或者将其设为None，Python将返回以下环境变量TMPDIR, TEMP, TEMP指定的目录，如果没有定义这些环境变量，临时文件将被创建在当前工作目录。
#
# tempfile.gettempdir()
#
# gettempdir()
# 则用于返回保存临时文件的文件夹路径。