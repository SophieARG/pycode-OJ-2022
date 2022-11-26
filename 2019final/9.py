from bisect import bisect
n = int(input())
m = (n + 1) // 2
nums1 = list(map(int, reversed(input().split())))
nums2 = list(map(int, input().split()))
i = 0
while i < m:
    if bisect(nums1, nums2[i]) < m - i:
        print('no')
        break
    i += 1
else:
    print('yes')
