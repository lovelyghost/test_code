class SimpleMetaClass(type):
    dd = 4
    def __init__(self,uu):
        self.FF = uu
        print(self.FF)
        print("you have create a class instance by metaclass")
        # super(SimpleMetaClass, self).__init__(*args, **kwargs)
    def __call__(self):
        raise Exception("Prohibit to create objects")

class Earth(SimpleMetaClass):
    # __metaclass__ = SimpleMetaClass
    # def __init__(self,ii):
    #     super(SimpleMetaClass,self).__init__(self,ii)

    @classmethod
    def sayhello(cls):
        print(dir(Earth))
        print(cls.dd)
        print("hello world")

    def hh(self):
        print("gg")


if __name__ == "__main__":
    dd = Earth.sayhello()
    # print(d.sayhello())
    # print(d.__metaclass__)
    # print(hasattr(d,"ff"))

    print("do something that have nothing with SimpleMetaClass and Earth")
