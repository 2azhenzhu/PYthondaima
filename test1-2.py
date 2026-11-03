import random
#1.猜数字游戏
def guess_number():
    print("--- 猜数字游戏 ---")
    # 生成 1 到 100 之间的随机整数
    target = random.randint(1, 100)
    count = 0
    while True:
        try:
            guess = int(input("请输入你猜的数字（1-100）："))
            count += 1

            if guess > target:
                print("猜大了，再试试！")
            elif guess < target:
                print("猜小了，再试试！")
            else:
                print(f"恭喜你，猜对了！数字就是 {target}。你一共猜了 {count} 次。")
                break  # 猜对后跳出循环
        except ValueError:
            print("输入无效，请输入一个整数。")

#2.打印九九乘法表
def print_multiplication_table():
    print("--- 九九乘法表 ---")
    # 外层循环控制行数 (1-9)
    for i in range(1, 10):
        # 内层循环控制列数，每一行的列数等于当前的行号
        for j in range(1, i + 1):
            # 使用 end="\t" 让同一行的输出用制表符隔开，不换行
            print(f"{j}*{i}={i*j}", end="\t")
        # 每一行打印结束后换行
        print()

#3.输入成绩输出等级
def grade_evaluation():
    print("--- 成绩等级判断 ---")
    try:
        score = float(input("请输入考试成绩（0-100）："))
        if score < 0 or score > 100:
            print("输入的分数不在有效范围内！")
        elif score >= 90:
            print("等级：优")
        elif score >= 80:
            print("等级：良")
        elif score >= 70:
            print("等级：中")
        elif score >= 60:
            print("等级：及格")
        else:
            print("等级：不及格")
    except ValueError:
        print("请输入有效的数字！")

#4.判断一个是否为素数
def check_prime():
    print("--- 素数判断 ---")
    try:
        num = int(input("请输入一个大于1的正整数："))

        if num <= 1:
            print(f"{num} 不是素数。")
            return
        is_prime = True
        # 从 2 循环到 num-1，如果能被整除就不是素数
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break  # 找到了因数，不需要再继续循环了
        if is_prime:
            print(f"{num} 是素数。")
        else:
            print(f"{num} 不是素数。")
    except ValueError:
        print("输入有误，请输入整数！")

#5.打印1-100中所有偶数
def print_even_numbers():
    print("--- 1-100中的偶数 ---")
    even_list = []
    for i in range(1, 101):
        if i % 2 == 0:
            even_list.append(str(i))  # 转成字符串方便拼接
    # 将列表中的偶数用逗号拼接并打印
    print(", ".join(even_list))
#函数调用
if __name__ == '__main__':
    guess_number()
    print_multiplication_table()
    grade_evaluation()
    check_prime()
    print_even_numbers()