res = ''
for char in input():
    cid = ord(char)
    if 65 <= cid <= 90:
        res += chr(cid + 32)
    elif 97 <= cid <= 122:
        res += chr(cid - 32)
    else:
        res += char
print(res)
