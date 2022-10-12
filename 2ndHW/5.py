a = input()
b = input()
for i in range(1, len(a) + 1):
    if a[-i:] == b[:i]:
        print(len(a) - i)
        break
