import copy

a = (1,2,3,4,[1,2])
b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
a[4].append(5)
print(b)

a[4].pop()
print(b)

a[4].pop()
print(b)
a[4].pop()
print(b)





# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)
# f(3,[4,5,6])
# f(3)