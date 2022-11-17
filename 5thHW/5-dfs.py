sodoku = [[0 for j in range(9)] for i in range(9)]
row = [set(range(1, 10)) for i in range(9)]
col = [set(range(1, 10)) for i in range(9)]
block = [set(range(1, 10)) for i in range(9)]
for i in range(9):
    ci = input()
    for j in range(9):
        if ci[j] != '0':
            cij = int(ci[j])
            sodoku[i][j] = cij
            row[i].remove(cij)
            col[j].remove(cij)
            block[i // 3 + j // 3 * 3].remove(cij)
            
def solve():
    minv = 10
    besti = bestj = bestp = None
    for i in range(9):
        for j in range(9):
            if sodoku[i][j] == 0:
                p = row[i] & col[j] & block[i // 3 + j // 3 * 3]
                if len(p) < minv:
                    minv = len(p)
                    besti, bestj, bestp = i, j, p
    if minv == 10: return True
    r, c, b = besti, bestj, besti // 3 + bestj // 3 * 3
    for p in bestp:
        sodoku[besti][bestj] = p
        row[r].remove(p)
        col[c].remove(p)
        block[b].remove(p)
        if solve(): return True
        row[r].add(p)
        col[c].add(p)
        block[b].add(p)
    sodoku[besti][bestj] = 0
    return False

solve()
for line in sodoku: print(*line, sep='')
