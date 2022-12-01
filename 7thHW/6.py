import math
n = int(input())
print(int(n * math.log(2, 10)) + 1)
digits = str(pow(2, n, pow(10, 500)) - 1).zfill(500)
for i in range(0, 500, 50):
    print(digits[i: i + 50])
