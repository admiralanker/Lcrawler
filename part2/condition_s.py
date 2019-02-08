'''
条件控制
1、比较运算符  ==  >  <  >=  <= !=
'''

i = "a"
j = "B"

if i < j:
    print('a小')
else:
    print('a大')

'''
ascii码表
'''
print(ord(i))
print(ord(j))

print(chr(99))

'''
成员运算符
in    not in
'''

s = '123456'
if '1' in s:
    print('1在s里')

if 'a' not in s:
    print('a不在s')

'''
逻辑运算符
and  or  not
'''

pmj = ['萧峰','段誉','虚竹','ilex']
if '萧峰' in pmj and '段誉' in pmj and '虚竹' in pmj and 'ilex' in pmj:
    print('他们在打麻将')
else:
    print('他们没打麻将')

if '萧峰' not in pmj:
    print('萧峰没在打麻将')
else:
    print('萧峰在打麻将')

# 关于True和False的讨论
print(True and False)
print(True or False)
print(not True)

print(1 and 0)
print(1 or 0)
print(not 1)

'''
1及1以上代表了True，0代表了False
and 需要判断到最后一个，只有全部为真的时候，才返回真
or的判断逻辑，只要碰到真值，就直接返回真，后边的不用再判断了
'''

print(1 and 2 and 3)
print(6 and 2 and 3)
print(4 or 5 or 6)
print(7 or 5 or 6)

'''
身份运算符
is
is not
'''

i = 1
j = 1
print(i == j)
print(i is j)
print(id(i))
print(id(j))

'''
作业：
了解运算符的优先级
'''
