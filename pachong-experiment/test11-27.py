# 包  新建包---时有__init__py文件
# 导入包时首先执行__init__.py文件中的代码
# import test
# from test import  reg
# reg.data()
# __all__:列表中的元素就代表要导入的模块
# from test import *
# login.log()
# reg.data()
# 递归函数
# def sum(n):
    # if n==1:        #   这里是必须的，若没有明确的结束条件，代码就会无限循环
    #     return 1
    # return n +sum(n-1)
# print(sum(100))
#斐波那契数列
# def funa(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     return funa(n-1) + funa(n-2)
# print(funa(7))

# def funa(n):
#     if n <= 1:
#         return n
#     return funa(n-1) + funa(n-2)
# print(funa(2))

# 闭包---特殊的函数
# 1.函数嵌套
# 2.内层函数使用外层函数的局部变量
# 3.外层函数的返回值是内层函数的函数名
def outer():    #外层函数
    n=10        #外层函数的局部变量
    def inner():
        print(n)
    return inner
print(outer())