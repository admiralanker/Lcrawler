'''
比较运算符  ==
比较两个变量的值是否相等
x == y
'''

# 单行注释

'''
多行注释1
'''

"""
多行注释2
"""

'''
表现形式
if 条件:
    语句
'''

# if_see = True
# if if_see:
#     print('买两个包子和一个西瓜')

'''
表现形式
if 条件:
    语句
else:
    语句
'''

# if_see = False
# if if_see:
#     print('买俩个包子和一个西瓜')
# else:
#     print('买俩个包子')

'''
if 条件:
    语句
elif:
    语句
elif:
    语句
elif:
    语句
... 可以无限多个elif
else:
    语句
'''

name = input('请输入你的名字：')
if name == '紫萱':
    print('紫萱你好')
elif name == '语嫣':
    print('语嫣你好')
elif name == '段誉':
    print('段誉你好')
else:
    print('我不认识你')
