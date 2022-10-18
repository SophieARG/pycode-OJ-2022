row, col = map(int, input().split())

nums = []
for i in range(row):
    nums.append(input().split())
    
for s in range(row + col - 1):
    i, j = 0, s
    while j >= 0:
        if j >= col: i, j = s - col + 1, col - 1
        if i >= row: break
        print(nums[i][j])
        i += 1
        j -= 1
