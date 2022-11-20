n = int(input())
nums = [float(x) for x in input().split()]
_sum = 0
_min = float('inf')
_max = -float('inf')
for num in nums:
    _sum += num
    _min = min(_min, num)
    _max = max(_max, num)
_mean = _sum / n
print(*map(lambda x: '%.2f' % ((x - _mean) / (_max - _min)), nums))
