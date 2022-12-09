from string import ascii_uppercase
forest = []
counts = {char: 0 for char in ascii_uppercase}
for i in range(int(input())):
    forest.append(input())
    for char in forest[-1]:
        if char != ' ':
            counts[char] += 1
maxcount = 0
chars = []
for char, count in counts.items():
    if count > maxcount:
        chars.clear()
        maxcount = count
    if count == maxcount:
        chars.append(char)
print(*chars)
for line in forest:
    res = ''
    for char in line:
        if char == ' ':
            res += ' '
        elif char in chars:
            res += '*'
        else:
            res += '.'
    print(res)
