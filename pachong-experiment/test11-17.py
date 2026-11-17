#数列
def nood35():
    n = int(input())
    s = 0
    a = 0
    for i in range(1, n + 1):
        s += i
        a += s
    print(a)
#斐波那契数列
def nood34():
    n=int(input())
    a = 1
    b = 1
    print(a,b,end=" ")
    for i in range(1, n + 1):
        c=a+b
        print(c,end=" ")
        a,b=b,c
    print()
if __name__ == '__main__':
    nood35()