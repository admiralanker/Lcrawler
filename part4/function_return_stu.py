'''
函数的返回值
'''

def func_with_return():
    print('函数被调用')

p = func_with_return()
print(p)
print(type(p))

def func_with_return(p):
    return p

p = func_with_return('段誉')
print(p)
print(type(p))

# 多个返回值

def funct_with_return(name,age):
    return name,age

n,a = funct_with_return('段誉',25)
print(n,a)

s = funct_with_return('段誉',25)
print(s)

# 返回一个函数
def func_with_return2(x):
    if x == 2:
        def inner_func(y):
            return y * y

    if x == 3:
        def inner_func(y):
            return y * y * y
    return inner_func

calc = func_with_return2(3)
print(calc(4))