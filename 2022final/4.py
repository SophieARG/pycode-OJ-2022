left = 0
count = 0
for char in input():
    if char == '(':
        left += 1
    else:
        left -= 1
        if left == 0:
            count += 1
print(count)
