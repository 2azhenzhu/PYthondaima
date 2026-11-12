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
if __name__ == '__main__':
    # nood21()
    # nood22()
    nood23()