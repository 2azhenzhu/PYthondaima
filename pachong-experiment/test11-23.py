#=====删除元素=====
# dic={'name':'zhangsan','age':18}
# del dic     #删除整个字典
# print(dic)
# dic={'name':'zhangsan','age':18}
# del dic['name']     #删除指定键值，键名不存就会报错 del字典名[键名]
# print(dic)
# dic={'name':'zhangsan','age':18}
# dic.clear()     #清空整个字典里面的东西，但保留了这个字典，清空之后可以直接加元素进入字典，不用重新创建字典
# dic['age'] =18
# print(dic)
# dic={'name':'zhangsan','age':18}
# dic.pop('age') #删除指定键值对
# dic.pop('tel')      #删除不存在的键名，会报错
# dic.popitem()       #3.7之前随机删除，3.7之后默认删除最后一个元素
# print(dic)
# dic={'name':'zhangsan','age':18,'tel':'123'}
# print(len(dic))     #len求长度
# li =[1,2,3,4]
# print(len(li))
# st='hello'
# print(len(st))
# dic={'name':'zhangsan','age':18,'tel':'123'}
# print(dic.keys())       #dict_keys(['name', 'age', 'tel'])
# for i in dic.keys():        #只取出键名--for循环取出键名
#     print(i)
# dic={'name':'zhangsan','age':18,'tel':'123'}
# # print(dic.values())   #返回字典里面包含所有的值
# for i in dic.values():
#     print(i)
# dic={'name':'zhangsan','age':18,'tel':'123'}
# print(dic.items())      #返回字典里面包含的所有键值对，键值对以元组形式呈现
# for i in dic.items():
#     print(i,type(i))
#==========集合====================================
# s1={'a','b','c','d','e','f','g'}
# print(s1)           #每次运行结果都不相同----集合无序的实现方式涉及hash表
# print(hash('a'))
# print(hash('b'))
# print(hash('c'))
# print(hash('d'))        #每次运行结果不同，hash值不同，那么在hash表中的位置也不同，这就实现了集合的无序性
# print(hash(1))
# print(hash(2))
# print(hash(3))
# print(hash(4))  #pyhton中int整型的hash值就是他本省，在hash表中的位置不会发生改变，所以顺序也不会改变
# print(hash('5'))
# print(hash('6'))  #用引号括起来整型变成了字符串类型，所以hash值还是会发生改变
# s1={1,2,3,4,4,1,23,5,4,68,4,8,4,56,6,5}
# print(s1)   #去重
from abc import update_abstractmethods
from operator import add

# 1.add添加一个整体
# s2 = {1,2,3,4}
# print("原集合：",s2)
# s2.add(5)
# # s2.add(6,7)     #报错，一次只能添加一个元素
# s2.add((6,7))
# print('现集合：',s2)
# 2.update把传入的元素拆分，一个个放进集合中
# s2 = {1,2,3,4}
# print("原集合：",s2)
# s2.update((5,6,7))      #元素必须是能被我们for循环取值的可迭代对象
# print('现集合：',s2)
# 3.删除元素remove选择删除的元素，若集合中有就删除，无就会报错
# s2 = {1,2,3,4}
# s2.remove(1)
# print('删除后:',s2)
# 4.pop对集合进行无序排列，然后将左边的第一个元素删除
# s2 = {'a','b','c'}
# print('原集合:',s2)
# s2.pop() #默认删除根据hash表排序后的第一个元素
# print('删除后:',s2)
# 5.discard:选中要删除的元素，有就会删除，没有在不会发生任何改变
# s2 = {1,2,3,4}
# s2.discard(1)
# print('删除后:',s2)
#===============================
#交集&与并集‘|’
#===============================
#类型转换
# a=1.2
# print(type(a))
# b=int(a)        #int(只能转换由纯数字组成的字符串)
# print(b,type(b))
# c=int('123')
# print(c,type(c))
# print(int('zhangsan'))      #报错
# n= 100
# print(type(n))
# n2=str(n)
# print(n2,type(n2))
#===========
#eval()
print(10+10)
print(eval('10'+'10'))