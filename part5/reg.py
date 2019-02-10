# 什么是正则表达式：记录文本规则的代码
# 是一个特殊的字符序列
# 普通字符和元字符组成的。其实就是对元字符的学习

import re

reg_string = 'dhi214ajshdoisr21&^$*&r12ahdoan15isjhiodj$%7as'
reg = 'a'

result = re.findall(reg,reg_string)
print(result)

'''
元字符
. 匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或结束
^ 匹配字符串的开始
$ 匹配字符串的结束
'''

reg_string = 'dhi214ajshdoisr21&^$兮*&r12ahdoan15isjhiodj$%7as'
reg = '\d'

s = re.findall(reg,reg_string)
print(s)

c = re.findall('\w',reg_string)
print(c)

'''
反义代码
\W 匹配任意不是字母、数字、下划线、汉字的字符
\S 匹配任意不是空白符的字符
\D 匹配非数字
\B 匹配不是单词开头或结束的位置

[^a]匹配除了a以外的任意字符
'''

'''
限定符
* 重复零次或多次
+ 重复一次或多次
? 重复零次或一次
{n} 重复n次
{n,} 重复n次或更多次
{n,m} 重复n到m次
{,m} 重复最多m次
'''

# reg_string = 'dhi214ajshdoisr21&^$兮*&r12ahdoan15isjhiodj$%7as'
# reg = '\d{2}'
# result = re.findall(reg,reg_string)
# print(result)
#
# #
# ip = 'this is ip:192.168.1.1 : 222.213.1.3'
# reg = '\d{3}.\d*.\d+.\d+'
# result = re.findall(reg,ip)
# print(result)

'''
search和findall
search只匹配第一个
findall匹配所有
'''

'''
组匹配
'''

# 贪婪与非贪婪    贪婪与懒惰

'''
什么是贪婪：尽可能多的匹配
非贪婪：尽可能少的匹配
非贪婪操作符：?
这个操作符是用在 * + ? 后边的，要求正则匹配的越少越好
'''