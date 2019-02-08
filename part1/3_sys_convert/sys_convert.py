'''
进制运算
什么叫做进制？
十进制、二进制、八进制
十进制：0,1,2,3,4,5,6,7,8,9,10
二进制：0,1,10
八进制：0,1,2,3,4,5,6,7,10
'''

#十进制转换成其他进制

#十进制转换成二进制
i = 16
j = bin(i)
print(j)

#十进制转换成八进制
i = 16
j = oct(i)
print(j)

#十进制转换成十六进制
i = 16
j = hex(i)
print(j)

#二进制转换成十进制
i = '10'
j = int(i, 2)
print(j)

 