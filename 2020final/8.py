n = int(input())
nums = [[0 for j in range(n)] for i in range(n)]
count = 1
for s in range(2 * n - 1):
    if s % 2 == 0:
        i, j = s, 0
        while True:
            if i >= n: i, j = n - 1, s - n + 1
            if i < 0 or j >= n: break
            nums[i][j] = pow(count, 2) * (-1 if count % 2 == 0 else 1)
            count += 1
            i, j = i - 1, j + 1
    else:
        i, j = s, 0
        while True:
            if i >= n: i, j = n - 1, s - n + 1
            if i < 0 or j >= n: break
            nums[j][i] = pow(count, 2) * (-1 if count % 2 == 0 else 1)
            count += 1
            i, j = i - 1, j + 1
for line in nums: print(*line)
