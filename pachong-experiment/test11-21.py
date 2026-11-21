def nood41():
    nums = list(map(int, input().split()))
    result = nums[:-1][::-1]
    print(" ".join(map(str, result)))

if __name__ == '__main__':
    nood41()