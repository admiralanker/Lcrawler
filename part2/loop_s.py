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

'''
循环的中断
break:跳出该循环

continue：跳出本次循环，继续执行下次循环
'''

# while True:
#     print(1)
#     print(type(1))
#     break
#     print(2)
#
# while True:
#     print(1)
#     continue
#     print(2)

i = 1

while True:
    print('外层循环1')
    while True:
        print('内层循环')
        break
    print('外层循环2')
    if i == 1:
        print('外层循环3')
        break

'''
1、冒泡排序
nums =  [3,1,9,6]
1,3,9,6
1,3,9,6
1,3,6,9

'''

# nums =  [9,3,1,6]
# for i in range(len(nums)-1):
#     for j in range(len(nums) - i -1):
#         if nums[j] > nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]
#             print('第' + str(j+1) + '次内循环' + str(nums))
#         print('第' + str(j+1) + '次外循环' + str(nums))
#
# print('最后的结果：' + str(nums))

'''
作业：
已经有一个序列nums = [9,3,1,6]
1、将这个序列从大到小排序
2、声明一个变量，数字 i = 7 把这个i插入到序列中，他应该在的位置在哪
思路提示：在判断的时候，可以重新声明一个新的序列，然后第一个序列中的值跟i比较，比i大的，
可以直接放入新的序列中，如果比i小，那么放入i，然后放入剩下所有的值
'''

i1 = 7

nums =  [8,4,1,5]
for i in nums:
    if i1 > i:
        nums.append(7)
        break
print(nums)