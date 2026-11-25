# 函数参数
# 1.必备参数（位置参数）
# def funa(name,age,sex) :
#     print(name)
#     print(age)
#     print(sex)
# funa('zhangsan ',18,'男')
# 2.默认参数
# 注意：所有的位置参数必须出现再默认参数前，包括函数定义和调用
# def funa(b,a=8):
#     print(a)
# funa()
# funa(200)
# 3.可变参数
# 注意：传入的值的数量是可以改变的，可以传入多个或者不传
# def func(*args):    #可以把args改为其他参数名
#     print(args)
# func(1,2,'nihao')       #以元组形式接收
# 4.关键字参数
# def funa(**kwargs):
#     print(kwargs)
# funa()      #返回字典
# funa(name='zhangsan',age=35)        #传值时需要采用键=值的形式
# 函数嵌套
# 1.嵌套调用
# def study():
#     print("study")
# def course():
#     study()
#     print("python")
# course()
# 2.嵌套定义
# def study():        #外函数
#     print("study")
#     def course():       #内函数
#         print("python")
#     course()
# study()
# 作用域
# 1.全局变量
# a=200
# def test1():
#     print("njk:",a)
# def test2():
#     a=500   #局部变量
#     print("njk:",a)
# test1()
# test2()     #a的之没有被覆盖是因为函数内部如果要使用变量，会先从函数内部找，有的话直接使用，没有才会去函数外面寻找
# 在函数内部修改为全局变量的值，可以使用global关键字
# a=200
# def test1():
#     print("njk:",a)
# def test2():
#     global a
#     a=500   #局部变量
#     print("njk:",a)
# print("调用前a的值：",a)
# test1()
# test2()
# print("调用后a的值：",a)
# nonlocal :用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal
# a=10
# def outer():
#     a=2
#     def inner():
#         nonlocal a #使用nonlocal时会对该函数的上一级的变量进行修改
#         a=40
#         def inner2():
#             a=30
#             print("inner2函数中的a的值：",a)
#         inner2()
#         print("inner函数中a的值：",a)
#     inner()
#     print("outer函数中a的值:",a)
# outer()
# 匿名函数
# 普通函数
# def add(x,y):
#     return x+y
# print(add(3,4))
# 匿名函数
# add=lambda x,y:x+y        # x,y就是匿名函数的形参，a+b是返回值的表达式
# print(add(3,4))
# lambda 不需要写return来返回值，表达式本身结果就是返回
# 参数--1.无参数
# funa= lambda :"水"
# print(funa())
# 2.一个参数
# funa=lambda name:name
# print(funa('张三'))
# 3.默认参数
# funa=lambda name,age=18:(name,age)
# print(funa("张三",148))
# print("zhansan")
# funa=lambda a,b,c=12: a+b+c
# print(funa(3,4,5))
# print(funa(3,4))
# 默认参顺必须写在非默认参数的后面
# 关键字参数
# funa=lambda **kwargs:kwargs
# print(funa(name='zhangsan',age=35))
# lambda 的应用
# 1.结合if else  三目运算
# comp=lambda  a,b:"a比b小" if a<b else "a大于等于b"
# print(comp(7,5))
# lambda 只能实现简单的逻辑，若逻辑复杂且代码量较大，不建议使用lambda，降低代码的可读性，为后期的代码维护增加困难
# 内置函数
# 查看所有的内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般是内置常量名，小写字母开头一般为内置函数名
# print(abs(-152))
# print(sum([1,2,3]))     #sum里面要放可迭代对象
# zip:将可迭代对象作为参数，将对象中对应的元素打包chengyigeyuanzu
# li=[1,2,3,4]
# li2=['a','b','c']
# print(zip(li,li2))
# 取出元素的方式
# for i in zip(li,li2):  #第一种
#     print(i)
# print(list(zip(li,li2)))    #转换成列表打印，必须为可迭代对象
# map：可以对可迭代对象中的每一个元素进行映射，分别去执行
# map(func,iterl):func自己定义的函数，iterl---要放进去的可迭代对象
# 即是：对象中的每一个元素都会去执行这个函数
# li=[1,2,3]
# def funa(x):
#     return  x*6
# funa=lambda x:x*6
# mp=map(funa,li)
# print(mp)
# for i in mp:
#     print(i)
# print(list(mp))
# reduce:先把对象中的两个元素取出来，计算出一个值然后保存着，接下来把这个计算值与第三个元素进行计算
# from functools import reduce
# # reduce(function,sequence) # function--函数：必须是有两个参数的函数，sequence--序列：可迭代对象
# li2=[1,2,3,4]
# def add(a,b):
#     return a+b      #累加，只能为两个
# result = reduce(add, li2)
# print(result)
# ===========
# 拆包
# tua=(1,2,3,4)
# print(tua)
# 取出数据
# a,b,c,d=tua     #一般在获取元组值时使用
# print(a,b,c,d)      #要求元组内的个数与接收的变量个数相同

# a,*b=tua        #*取出多个
# print(a,b)
# def funa(a,b,*args):
#     print(a,b)
#     print(args,type(args))
# funa(1,2,3,4,5,6)

T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    j=max(a)-min(a)
    mean=sum(a)/n
    f=sum((x-mean)**2 for x in a)/n
    print(j,format(f,'.3f'))
