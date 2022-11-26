N = int(input())
cubes = [pow(i, 3) for i in range(N + 1)]
for a in range(3, N + 1):
    for b in range(2, int(a / pow(3, 1 / 3)) + 1):
        target = cubes[a] - cubes[b]
        c, d = b, int(pow(target - cubes[b], 1 / 3))
        while c <= d:
            tempsum = cubes[c] + cubes[d]
            if tempsum < target:
                c += 1
            elif tempsum > target:
                d -= 1
            else:
                print('Cube = %d, Triple = (%d,%d,%d)' % (a, b, c, d))
                c += 1
                d -= 1
