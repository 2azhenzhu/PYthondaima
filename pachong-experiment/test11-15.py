import sys
import math
#多组输入a+b  ||
def nood29():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
    print(a+b)

#多组数据a+b
def nood30():
    for line in sys.stdin:
        if not line.strip():
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        print(a + b)

#素数判断
def nood31():
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n <= 1:
            print("No")
            continue

        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Yes")
        else:
            print("No")
#牛牛学数列
def nood32():
    n = int(input())
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
        else:
            s -= i
    print(s)


if __name__ == '__main__':
    # nood29()
    # nood30()
    # nood31()
    nood32()