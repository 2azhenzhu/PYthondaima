#斐波那契数列
def f(n):
    n = int(input())
    if n==1:
        return 1
    elif n==2:
        return 1
    return f(n-1)+f(n-2)


#数位之和
def nood37():
    n = input()
    s = 0
    for i in n:
        s = s + int(i)
    print(s)
#枚举
def nood38():
    n = int(input())
    m = []
    for i in range(1, n + 1):
        if i % 4 != 0 and '4' not in str(i):
            m.append(str(i))
    print('\n'.join(m))
if __name__ == '__main__':
    # print(f(n))
    # nood37()
    nood38()
