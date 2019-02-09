'''
__name__
只有在本模块启动时，__name__等于__main__
在什么时候使用
1、今天作为这个模块的入口，在其他语言中，叫做main函数
2、也可以作为调试使用，原因是在其他模块调用本模块时，__name__ == 'main'
判断结果为False，所以就不会执行
'''


def my_print():
    print(__name__)

if __name__ == '__main__':
    my_print()
    print(1)
    print(__name__)