import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
if n % 2 == 0:
    print(int(n/2))
else:
    print(3*n + 1)
#明天是星期几？
def nood21():
    d=int(input())
    print(d%7+1)

#判断闰年
def nood22():
    n  = int(input())
    if n%4==0 and n%100!=0 :
        print(f"{n}年为闰年")
    elif n%400!=0 :
        print(f"{n}年为闰年")
    else:
        print(f"{n}N年不为闰年")

#比大小
def nood23():
    a,b=map(int,input().split())
    if a<b:
        print("<")
    elif a>b:
        print(">")
    else:
        print("=")
#卡拉子函数========2026.11-13
def nood24():
    n = int(input())
    if n % 2 == 1:
        result = 3 * n + 1
    else:
        result = n // 2
    print(result)
#牛妹数
def nood25():
    n = int(input())
    if n % 2 == 0 and n > 50:
        print("yes")
    else:
        print("no")
#牛牛是否被叫家长
def nood26():
    a, b, c = map(int, input().split(' '))
    avg = (a + b + c) / 3
    if avg >= 60:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    # nood21()
    # nood22()
    # nood23()
    nood24()