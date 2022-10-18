chars = '0123456789ABCDEF'

def convert(x, a):
    res = ''
    while True:
        x, i = divmod(x, a)
        res = chars[i] + res
        if x == 0: break
    return res

a, n, b = input().split()
a, n, b = int(a), n.upper(), int(b)
print(convert(int(n, base = a), b))
