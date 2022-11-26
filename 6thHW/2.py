p, q, r = input().split()
for B in range(2, 17):
    try:
        if int(p, base=B) * int(q, base=B) == int(r, base=B):
            print(B)
            break
    except ValueError:
        continue
else:
    print(0)
