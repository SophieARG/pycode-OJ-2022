from functools import lru_cache
from itertools import permutations as perm

def generate(nums1, nums2):
    nums = {num1 / num2 for num1 in nums1 for num2 in nums2 if num2}
    nums.update({num1 + num2 for num1 in nums1 for num2 in nums2})
    nums.update({num1 - num2 for num1 in nums1 for num2 in nums2})
    nums.update({num1 * num2 for num1 in nums1 for num2 in nums2})
    return nums

def _judge(nums1, nums2):
    for num1 in nums1:
        for num2 in nums2:
            if num2 and abs(num1 / num2 - 24) < 0.01: return True
            if abs(num1 + num2 - 24) < 0.01: return True
            if abs(num1 - num2 - 24) < 0.01: return True
            if abs(num1 * num2 - 24) < 0.01: return True
    return False

@lru_cache()
def judge(a, b, c, d):
    if _judge(generate(generate({a}, {b}), {c}), {d}): return True
    if _judge(generate({a}, {b}), generate({c}, {d})): return True
    if _judge(generate({a}, generate({b}, {c})), {d}): return True
    if _judge({a}, generate(generate({b}, {c}), {d})): return True
    if _judge({a}, generate({b}, generate({c}, {d}))): return True
    return False
    
while True:
    cin = input()
    if cin[0] == '0': break
    for a, b, c, d in perm(map(int, cin.split())):
        if judge(a, b, c, d):
            print('YES')
            break
    else:
        print('NO')
