#牛牛学数列
def nood33():
    n = int(input())
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    print(f"{h:.6f}")
#最大的差
def nood34():
    n = int(input()),
    a = list(map(int, input().split()))
    s = max(a) - min(a)
    print(s)

if __name__ == '__main__':
    # nood33()
    nood34()