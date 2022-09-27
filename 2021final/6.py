nums = sorted(map(int, input().split()))
n = len(nums)
if n < 3:
    print(0)
else:
    if nums[0] > 0 or nums[-1] < 0:
        print(0)
    elif nums[0] == 0 and nums[-1] == 0:
        print(1)
    else:
        p = 0
        count = 0
        while p < n - 2:
            p1, p2 = p + 1, n - 1
            while p1 < p2:
                tempsum = nums[p] + nums[p1] + nums[p2]
                if tempsum > 0:
                    p2 -= 1
                elif tempsum < 0:
                    p1 += 1
                else:
                    count += 1
                    temp = nums[p1]
                    while p1 < n and nums[p1] == temp:
                        p1 += 1
                    temp = nums[p2]
                    while p2 > p1 and nums[p2] == temp:
                        p2 -= 1
            temp = nums[p]
            while p < n-2 and nums[p] == temp:
                p += 1
        print(count)
