n = int(input())
target = int(input())
nums = list(map(int, input().split()))
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print(i, j)
            exit(0)
print(-1, -1)
