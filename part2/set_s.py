'''
集合，是一个无序的不重复元素的序列
共俩重声明方法：
{}
set()
'''

# 声明集合

# set_1 = {'萧峰','段誉','虚竹','ilex','ani','萧峰','CC'}
# set_2 = set('0123450')
# # 乱序 去重（去除重复）
# print(set_1)
# print(set_2)
#
#
# # 判断元素是否在集合内
# print('a' in set_1)
# print('ilex' in set_1)

# 俩个集合间的运算
a = set('12345')
b = set('34567')

print(a & b) # 既在a集合又在b集合
print(a | b) # 在a集合或在b集合
print(a ^ b) # a和b集合里不相同的元素

# 集合添加元素  .add
c = set(('萧峰','段誉'))
c.add('虚竹')
print(c)

# 移除指定元素 .remove
c.remove('段誉')
print(c)

# 随机移除一个元素 .pop
p_c = c.pop()
print(p_c)

# 统计集合的个数 len
print(len(c))

# 清空集合 .clear
c.clear()
print(c)