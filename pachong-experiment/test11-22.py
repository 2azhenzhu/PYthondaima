from dataclasses import replace

# from av.error import name

from lianxi.test2 import count

# 1.replace()替换
# name = '好好学习，天天向上'
# # print(name.replace("天",'时'))  #好好学习，时时向上
# print(name.replace('天','时',1))  #好好学习，时天向上
# 2.split():指定分隔符来切字符
# st= 'hello,python'
# print(st.split(','))  #---以列表的形式返回['hello', 'python']
# print(st.split('a'))    #['hello,python']
# print(st.split('o',1))  #['hell', ',python']
# 3.capitalize():第一个字符大写，其他小写
# st='bingbing'
# print(st.capitalize())
# 4.lower():大写字母转为小写
# sd='bingBinG'
# print(sd.lower())
# 5.upper():小写字母转为大写
# st='bingBinG'
# print(st.upper())
# 判断1.startswith():是否以某个字符开头，是的话返回true，不是返回False
# st='sixstar'
# print(st.startswith('s',3,6))
# 2.endswith() 是否以某个字符结束，是的话返回true，不是返回False
# isupper():是否大写，是的话返回true，不是返回False
# islower():是否小写，是的话返回true，不是返回False
#  列表的常见操作
# 1.添加元素append ；extend；insert；
# li=['one','two','three']
# # li.append('four')   #append整体添加
# # li.extend('four')   #extend 分散添加，将另外一个类型中的元素逐一添加
# li.insert(3,'four')     #insert在指定位置插入
# print(li)
# li=[1,2,3]
# # li.extend([4,5,6]) #会报错，整形不是可迭代对象，
# # 可迭代对象有：列表、元组、字符串、字典、集合、range、文件、生成器、
# # enumerate/zip/map/filter 等结果，以及实现了 __iter__ 的自定义对象，都是可迭代对象。
# li.insert(3,4)
# print(li)
#===========================================================
#修改元素
# li=[1,2,3]
# li[1]='a'
# print(li)
# 查找元素
# li=['a','b','c','d']
# print('b' in li)\
# while True:
#     name_list=['张三','李四','王五']
#     name=input('请输入您的名称：')
#     if name in name_list:
#         print(f'您输入的名称{name}已存在')
#     else:
#         print(f'名称{name}已被您使用')
#         name_list.append(name)
#         print(name_list)
#         break
# index返回指定元素的下标// count统计指定元素在当前列表出现的次数
#删除列表
# del--删除整个列表//pop删除指定下标的元素,不屑默认删除最后一个元素
# li=['a','b','c','d']
# li.pop(1)
# print(li)
# remove：根据元素的值进行删除
# li=['a','b','c','d','e','f','b']
# li.remove('b')      #当列表中有多个一样的元素时，默认删除最开始（即最近的）指定元素
# print(li)
#排序sort：将列表按特定顺序排列，默认从小到大
# li=[1,445,326,45,888]
# li.sort()
# li.reverse()        #倒序
# print(li)
# 列表推导式====格式一[表达式 for 变量 in 列表/range/可迭代对象]
# li=[1,2,3,4,5,6]
# [print(i*5) for i in li]
# li =[]
# for i in range(1,6):
#     print(i)
#    li.append(i)
#  print(li)
# [li.append(i) for i in range(1,6)]
# print(li)
# li=[]
# [li.append(i) for i in range(1,12) if i%2==1]
# print(li)
# li=[1,2,3,[4,5,6]]      #列表嵌套
# print(li[3])
# print(li[3][0])
#==================================
#元组
# tua=(1,2,3,1)  #查询使用count(),index(),len(),与列表的用法相同
# print(tua.index(3))  #返回下标
# print(tua.count(1))
# print(len(tua))
# print(tua[1:])
#应用场景--函数的参数与返回值；格式化输后面的（）本质上就是一个元组-
# name='bingbing'
# age=18
# print("%s的年龄时：%d"% (name,age))
# info= (name,age)
# print(type(info))
# print("%s的年龄时：%d"% info)
#===========================
#字典dict
# dic={'name':'zhangsan','age':18} #查看元素，要根据键名，键名相当于索引
# print(dic['age'])
# print(dic.get('name'))
# print(dic.get('tel','不存在')) #若不存在---如果过没有这个键名，放回自己设置的默认值
#修改元素-==----列表通过小标修改，字典通过键名修改
# dic={'name':'zhangsan','age':18}
# dic['age']= 20
# dic['sex']='男'  #键名存在就修改，不存在就添加
# print(dic)
#========牛客网题==============================
def nood42():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        count = 0
        for j in range(i):
            if a[j] < a[i]:
                count += 1
        b.append(count)
    print(" ".join(map(str, b)))
if __name__ == '__main__':
    nood42()
#========牛客网题==============================
