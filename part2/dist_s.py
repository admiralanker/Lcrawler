# 字典是一种可变容器类型，也是可以存储任意类型的对象

d = {'萧峰':11,'段誉':22,'虚竹':33}
print(d)

# 字典的操作
# 访问
keys = d.keys()
print(keys)
print(d['萧峰'])  # 切片可以通过key访问 不可以通过value访问

v = d.values()
print(v)

# 增加
d['ilex'] = 44
print(d)

# 删除
del d['萧峰']

# 更新
d['ilex'] = 55
print(d)

# 字典的函数操作

# 判断是否在字典中
d1 = 'ilex'in d
print(d1)

#清空字典
d.clear()
print(d)