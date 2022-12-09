n = int(input())
forest = []
for i in range(n):
    forest.append(list(input()))
stack = [(0, 0)]
used = {(0, 0)}
def update(pos):
    if pos in used: return
    used.add(pos)
    stack.append(pos)
count = 0
while stack:
    i, j = stack.pop()
    if forest[i][j] == '.':
        if i > 0: update((i-1, j))
        if i < n - 1: update((i+1, j))
        if j > 0: update((i, j-1))
        if j < n - 1: update((i, j+1))
        for _i in range(max(0, i-1), min(n, i+2)):
            for _j in range(max(0, j-1), min(n, j+2)):
                if forest[_i][_j] == ' ':
                    forest[i][j] = '*'
                    count += 1
                    break
            else:
                continue
            break
print(count)
for line in forest:
    print(''.join(line))
