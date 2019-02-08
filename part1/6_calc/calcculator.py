'''
计算器
'''

first_number = input('请输入第一个数字:')
operation = input('请输入运算符:')
second_number = input('请输入第二个数字:')

#类型转换
# first_number = int(first_number)
# second_number = int(second_number)

# s1 = '.'
#用户输入的数字是否包含小数点
s2 = '.' in first_number or second_number
if s2 == True:
    first_number = float(first_number)
    second_number = float(second_number)
else:
    first_number = int(first_number)
    second_number = int(second_number)

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number
    elif operation == '%':
        result = first_number % second_number
    elif operation == '**':
        result = first_number ** second_number
    elif operation == '//':
        result = first_number // second_number
    elif operation == '+=':
        first_number += second_number
        result = first_number
    elif operation == '-=':
        first_number -= second_number
        result = first_number
    elif operation == '*=':
        first_number *= second_number
        result = first_number
    elif operation == '/=':
        first_number /= second_number
        result = first_number
    elif operation == '%=':
        first_number %= second_number
        result = first_number
    elif operation == '**=':
        first_number **= second_number
        result = first_number
    elif operation == '//=':
        first_number //= second_number
        result = first_number
    else:
        print('请输入正确的运算符！')

result = str(result)

print('运算后的结果:' + result)

# elif n1 not in second_number and second_number:
#     first_number = int(first_number)
#     second_number = int(second_number)