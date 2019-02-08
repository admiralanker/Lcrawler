'''
列表：一组数据
list是有序的序列
序列中的每个元素分配一个数字，就是索引，也是位置角标/坐标
也是从0开始
'''

list1 = ['建国',13,'爱国',15,'卫国',18]
print(list1)
print(type(list1))

# 访问列表
print(list1[0])
print(list1[2:])

# 更新
list1[1] = 14
print(list1)

# 添加操作
list1.append('建军')
list1.append(21)
print(list1)

list1 = list1 + ['丫头', 25]
print(list1)

#删除
del list1[8:]
print(list1)

# 嵌套列表
list1 = [['建国','爱国','卫国'],[12, 15, 18]]
print(list1)
print(list1[0][1])

# 返回列表的个数
count = len(list1)
print(count)

# 移除列表中的元素
l = list1.pop(1)
print(l)
print(list1)

#对列表中的元素进行排序
list1 = [23, 15, 18]
list1.sort()
print(list1)

# 查找列表中第一个匹配的元素的索引值
list1 = [23, 16, 27]
i = list1.index(16)
print(i)

