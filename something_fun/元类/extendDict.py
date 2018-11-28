class A(dict):
    pass

a = A()
a['name'] = 10
print(type(type(a).__name__))