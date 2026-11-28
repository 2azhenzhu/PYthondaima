# 异常
# 抛出异常-- 1.创建一个Exception（‘xxx’）对象，xxx--异常提示信息
# 2.raise抛出这个对象（异常对象）
# raise Exception("张三抛出异常")
# def funa():
#     raise Exception("张三抛出异常")
#     print("失败了")
# funa()

#需求：密码长度不足就报异常
#分析：户输入判断输入的长度是否大于等于6，如果输入长度不足6位，.就报错，即抛出自定义异常，并捕获该异常）
# def login():
#     pwd=input("请输入您的密码：")
#     if len(pwd)>=6:
#         return  '密码输入成功'
#     raise Exception("长度不足六位，密码输入失败")
# print(login())
# try:
#     print(login())
# except Exception as e:
#     print(e)
# # 捕获异常是为了检测到异常是代码还能继续往下运行，即程序不会终止

# 模块---本质上是一个py文件
# 内置模块--random，time，os，logging，直接导入即可使用
# 第三方模块（第三方库）---cmd窗口输入pip install  模块名
# 自定义模块--自己在项目中定义的模块--注意命名要遵循标识符规定以及变量的命名规范、并且不要与内置模块起冲突--就会导致模块功能无法使用

# 导入模块
# import  block
# print(block.name)
# block.funa()
# 2.方式二
# from block import funa,funb
# funa()      #调用时直接输入功能即可，不需要添加模块名
# funb()      #导入函数只需要函数名就可，不需要（）
#3.方式三
# from block import*
# funa()      #注意，不建议过多使用from。。 import。。声明，有时候命名冲突会造成一些错误
# 给模块起别名
# import block as pt
# pt.funa()
# print(pt.name)
# 给功能起别名
# from block import funa as f,funb as b
# f()
# print()
# b()
# 内置全局变量 __name__
# if __name__=='__main__':        #用来控制oy文件在不同的应用场景执行不同的逻辑
    # 1.文件在当前程序执行（即自己执行自己）：__name__=="__main__"
    # 2.文件被当做模块被其他文件导入：__name__ ===模块名
# import block
# block.test()

