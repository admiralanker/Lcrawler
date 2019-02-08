# 如果没有循环条件变化

# i = 1
# while i < 10:
#     print('i<10就继续循环')

# while循环
# 求1到10的和

n = 1
count = 0
while n <= 10:
    count += n
    n += 1
print(count)

# for循环
list1 = [1,2,3,4,5,6,7,8,9, 10]
count = 0

for i in list1:
    count = count + i
print(count)

count = 0
for i in range(11):
    count += i
print(count)