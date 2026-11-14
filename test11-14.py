import sys
input = lambda:sys.stdin.readline().strip()
#最大值最小值
def nood27():
    # 1. 读取输入的一行内容，按空格分割，并转换为整数赋值给 a, b, c
    a, b, c=map(int,input().split())
    max_val =max(a,b,c)
    min_val =min(a,b,c)
    print(f"The maximum number is : {max_val}")
    print(f"The minimum number is : {min_val}")

#四级
def nood28():
    s=input().strip()
    #获取月份
    month=int(s[4:6])
    if 3<= month <=5:
        print("spring")
    elif 6<= month <=8:
        print("summer")
    elif 9<= month <=11:
        print("autumn")
    else:
        print("winter")
#多组输入a+b  ||
def nood29():
    a=
if __name__ == '__main__':
    # nood27()
    # nood28()