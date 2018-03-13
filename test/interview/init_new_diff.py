# -*- coding: utf-8 -*-

class Person(object):
  """Silly Person"""

  # __new__方法接受的参数虽然也是和__init__一样，
  # 但__init__是在类实例创建之后调用，
  # 而 __new__方法正是创建这个类实例的方法。
 
  def __init__(self, name, age):
    # print '__init__ called.'
    self.name = name
    self.age = age

  def __new__(cls, name, age):
    # print '__new__ called.'
    return super(Person, cls).__new__(cls, name, age)
 
  def __str__(self):
    return '<Person: %s(%s)>' % (self.name, self.age)
 

piglei = Person('piglei', 24)
# print piglei

# 便是__init__最普通的用法了。
# 但__init__其实不是实例化一个类的时候第一个被调用 的方法。
# 当使用 Persion(name, age) 这样的表达式来实例化一个类时，
# 最先被调用的方法 其实是 __new__ 方法。

# 具体的执行逻辑是这样的：

# 1.p = Person(name, age)

# 2.首先执行使用name和age参数来执行Person类的__new__方法，这个__new__方法会 返回Person类的一个实例（通常情况下是使用 super(Persion, cls).__new__(cls, ... ...) 这样的方式）

# 3.然后利用这个实例来调用类的__init__方法，上一步里面__new__产生的实例也就是 __init__里面的的 self

# 所以，__init__ 和 __new__ 最主要的区别在于：

# 1.__init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
# 2.__new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。



# 用__new__来实现单例

class Singleton(object):
  def __new__(cls):
    # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
      print(cls)
      print(cls.instance)
      
    return cls.instance
 
obj1 = Singleton()
obj2 = Singleton()
print(id(obj1))
print(id(obj2))

obj1.attr1 = 'value1'
print obj1.attr1, obj2.attr1
print obj1 is obj2