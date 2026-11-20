#数列
def nood39():
    n = int(input())
    A = [0] * (n + 1)
    if n == 1:
        print(0)
    elif n == 2 or n == 3:
        print(1)
    else:
        A[1] = 0
        A[2] = 1
        A[3] = 1
        for i in range(4, n + 1):
            A[i] = A[i - 3] + 2 * A[i - 2] + A[i - 1]
        print(A[n])
#二位斐波那契额数列
import sys
def nood40():
    try:
        n, m = map(int, input().split())
    except EOFError:
        return
    MOD = 10**9 + 7
    dp = [1] * m
    for i in range(1, n):
        for j in range(1, m):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    print(dp[m - 1])


if __name__ == '__main__':
    # nood39()
    nood40()