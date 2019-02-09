'''
函数定义的格式
'''

# 函数定义的基本格式
def my_func():
    pass

# 函数的参数
# 必须参数
def my_func_with_param(p1,p2):
    print(p1,p2)

my_func_with_param(1,2)

'''
形参：形式参数，只是意义上的一种参数，在定义的时候不占内存地址
实参：实实在在的参数，是实际占用内存地址的
'''

# 关键字参数：是在调用的时候指定参数名称，可以不按顺序传参数

def my_function_with_params(name,age):
    print(name + '来了，他今年：' + str(age) + '岁！')

my_function_with_params('CC',22)
my_function_with_params(name='C',age=23)
my_function_with_params(age=33,name='CCC')

#默认参数：如果调用者没有传值，那么就用默认值，可以不指定名字

def my_function_with_paramss(name = '段誉',age = 28):
    print(name + '来了，他今年：' + str(age) + '岁！')

my_function_with_paramss()
my_function_with_paramss(age=26)
my_function_with_paramss(age=26,name='萧峰')

#参数的混合使用

def my_function_with_paramsss(name,sex,age = 28):
    print(name + '来了，他今年：' + str(age) + '岁！' + str(sex))

my_function_with_paramsss('cc','男')