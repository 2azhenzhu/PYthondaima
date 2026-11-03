import datetime  # 导入日期时间模块

# ===== 任务 ②：打印 Hello World、自己的名字和当前日期 =====
print("Hello World")
my_name = "张三"
print(f"我的名字是：{my_name}")
# 获取当前日期和时间，并格式化输出
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"当前日期和时间：{current_time}")
print("-" * 30)
# ===== 任务 ③：用 input 接收用户输入并回显 =====
user_input = input("请输入你想说的话：")
print(f"你刚才输入的内容是：{user_input}")