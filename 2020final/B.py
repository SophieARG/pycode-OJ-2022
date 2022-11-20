n = int(input())
nums = [int(x) for x in input().split()]
a = [1]
for i in range(1, n):
    if nums[i] > nums[i-1]:
        a.append(a[-1] + 1)
    elif nums[i] == nums[i-1]:
        a.append(a[-1])
    else:
        a.append(1)
b = [1]
res = 0
for i in range(n-1, 0, -1):
    res += max(a[i], b[-1])
    if nums[i] < nums[i-1]:
        b.append(b[-1] + 1)
    elif nums[i] == nums[i-1]:
        b.append(b[-1])
    else:
        b.append(1)
print(res + max(a[0], b[-1]))
