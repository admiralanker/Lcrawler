# 声明一个字符串

# 单引号声明
s = 'hello world'
print(s)
# 双引号声明
s = "hello world"
print(s)

# 三引号声明
s = """
hello 
world
"""
print(s)

#字符串的操作
#单个访问字符串中的字符

s = 'hello python'
print(s[1])

# 访问字符串的子串  切片操作
print(s[0:7])

# 左闭右开 ， 位置>=0   <6

#字符串相加计算
s1 = 'Hello '
s2 = 'Python'
print(s1 + s2)
print('我是' + s2)

#字符串更新操作
s1 = 'Hello World'
s2 = 'Python'
print(s1[:6] + s2)

# 字符串的成员运算
s1 = 'Hello Python'
s2 = 'Hello'

#包含运算  in
print(s2 in s1)
#不包含运算 not in
print(s2 not in s1)

#转义字符  \
print('\'')
print('\"')
print('\""')

#换行符  \n
print('Hello\nPython')

#制表符  tab键 或 4个空格 符号：\t
print('Hello\tPython')

#回车  符号：\r
print('Hello\rPython')  # 光标到行首，打印\r之后的内容

#输出字符串：Hello\nPython
#原是字符串
print(r'Hello\nPython')
print(R'Hello\nPython')

# 字符串的格式化输出  我叫某某某，今天是我第某天学习Python！
print('我叫%s,今天是我第%d天学习Python！'%('小明',10))

# 字符串的内建函数
#查找字符串
s = 'Hello Python'.find('l')
print(s)

#转换为小写字符
print("Hello Python".lower())
# 转换为大写字符
print('Hello Python'.upper())

#返回字符串长度 __len__() 这个函数返回的是自然长度
print('Hello Python'.__len__())

#判断字符串是否只包含空格
print('a '.isspace())

#字符串替换
print('Hello Python'.replace('h','1'))
