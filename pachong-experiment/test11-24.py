#===深浅拷贝==============================
#赋值：会随着原对象一起变化
# li=[1,2,3,4]
# print(li)
# li2=li
# print('li',li)
# print('li2',li2)
# print("li内存地址：",id(li))
# print("li2内存地址：",id(li2))   #内存地址一样，说明是同一个对象
# li2.append(5)
# print("新增后的li:", li)
# print("新增后的li2:", li2)       #赋值：等于完全共享资源，一个值的改变会被另一个值共享
#深浅拷贝就是应--”保留原数据，新数据改变”而出想的
#浅拷贝（数据半共享 ）：会创建的对象，拷贝第一层数据，嵌套层会指向原来的内存地址
#外层的内存地址不同，但是内存的内存地址相同
# import copy
# li=[1,2,3,4,[4,5,6]]
# li2=copy.copy(li)       #浅拷贝，只拷贝外层的对象
# print('li',li)
# print('li2',li2)
#查看内存地址 id（）
# print("li内存地址：",id(li))
# print("li2内存地址：",id(li2))       #内存地址不一样，说明不是同一个对象
# li.append(7)
# print(li)
# print(li2)
# print(li[4])
# li[4].append(8)
# print("li[4]内存地址：",id(li[4]))       #列表内层的id没有发生改变
# print("li2[4]内存地址：",id(li2[4]))
# print("新增后的li:", li)
# print("新增后的li2:", li2)
#应用场景：大部分场景，都是浅拷贝，只有特定需求才会使用深拷贝
#优点：拷贝速度快，占用空间小，效率高
#=========深拷贝==========================
#深拷贝：数据完全共享，外层对象和内部元素都拷贝一遍
# import copy
# li=[1,2,3,[4,5,6]]
# li2=copy.deepcopy(li)
# print("li",li)
# print("li2",li2)
# print("lim",id(li),id(li2))
# li.append(8)
# print(li)
# print(li2)
# #再嵌套列表添加元素
# li[3].append(7)
# print(li)
# print(li2)
# print(id(li[3]))
# print(id(li2[3]))       #深拷贝数据变化只影响自己本身，跟原来的对象没有关联
#可变对象：存储空间保存的数据允许被修改，这种数据就是可变类型---常见的有list、dict、set
# 可变类型：变量对应的值可以修改，但内存地址不会发生改变
# li=[1,2,3,4]
# print("li的id:",id(li))
# li.append(5)
# print(li)
# print("li现在的id:",id(li))
# dic={'name':'zhangsan','age':18}
# print(dic,id(dic))
# dic['name']='rmf'
# print(dic,id(dic))
# set={1,2,3,4,5}
# print(set,id(set))
# set.remove(5)
# print(set,id(set))

#========================================
#不可变类型：存储空间保存的数据不允许被修改
# 若被修改就会生成一个新的值从而分配新的内存空间
# int,bool,float,complex,--str--tuple
# n=10
# print("原地址：",n,id(n))
# n=15
# print("修改后地址：",n,id(n))
# tua=(1,2,3)
# print("tua-id",id(tua))
# tua=('a','b','c')
# print("tua-id",id(tua))     #修改后内存地址就会改变，深浅拷贝只针对可变对象
# =============函数==============
# def demo1():
#     print("你好！")
# demo1()
# 返回值return（）
# def buy():
#     return "一杯冰鲜柠檬水"，20      #一个返回值也没有时，返回记过为None，return返回多个值--以元组的形式返回
#     return 20       #函数中遇到return，return下面的语句不执行
# print(buy())
# return与print的区别---1.return表示函数技术，print表示一直执行
# 2.return是返回计算值，print是打印结果
def add(x,y):
    return x+y
print(add(1,2))