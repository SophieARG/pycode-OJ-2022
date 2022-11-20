def part(length, N):
    if length < nums[0]: return False
    used = [False for i in range(n)]
    def _part(i, left, full):
        if full == N - 1: return True
        if left == 0: return _part(0, length, full + 1)
        if i == n: return False
        while i < n:
            if i == 0 or nums[i] != nums[i-1] or used[i-1]:
                if nums[i] <= left and not used[i]:
                    used[i] = True
                    if _part(i + 1, left - nums[i], full): return True
                    used[i] = False
                    if left == length or left == nums[i]: break
            i += 1
        return False
    return _part(0, length, 0)

while True:
    n = int(input())
    if n == 0: break
    nums = sorted(map(int, input().split()), reverse=True)
    nums_sum = sum(nums)
    sqrt_sum = int(pow(nums_sum, 0.5))
    choice = None
    cache = []
    for length in range(1, sqrt_sum + 1):
        if nums_sum % length == 0:
            N = nums_sum // length
            cache.append((N, length))
            if part(length, N):
                choice = length
                break
    if choice is None:
        if pow(sqrt_sum, 2) == nums_sum: cache.pop()
        while cache:
            length, N = cache.pop()
            if part(length, N):
                choice = length
                break
    print(choice)
