import copy

a = [1,2,3,4,[1,2]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append(3)
print(a)
print(b)
print(c)
print(d)

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3,[4,5,6])
f(3)