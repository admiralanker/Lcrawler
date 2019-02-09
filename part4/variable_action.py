'''
变量的作用域
'''

# if True:
#     name = 'CC'
#
# print(name)

'''
在Python中没有块级的作用域
代码块里的变量，外部是可以调用的
'''
# name = 'CX'
#
# def func():
#     name = "c"
# print(name)

'''
变量的作用域链
1、变量先在本级找，找到直接使用
2、本级找不到时，逐级向上找，向上找到的第一个直接使用
3、本级找不到，逐级向上也找不到，就会报错
'''
name = 'B'
def func1():
    name = 'C'

    def func2():
        name = 'V'
        print(name)
    func2()
    print(name)

func1()
print(name)

# 作用域的练习

name = 'a'

def f1():
    print(name)

def f2():
    name = 'b'
    print(name)
    f1()
f2()
