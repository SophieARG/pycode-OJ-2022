class DLX:
    def __init__(self, r, c, total=None):
        self.first = [0 for i in range(r + 1)]
        self.size = [0 for i in range(c + 1)]
        if total is None:
            total = (r + 1) * c + 1
        else:
            total = total + c + 1
        self.L = [0 for i in range(total)]
        self.R = [0 for i in range(total)]
        self.U = [0 for i in range(total)]
        self.D = [0 for i in range(total)]
        self.r = [0 for i in range(total)]
        self.c = [0 for i in range(total)]
        for i in range(c + 1):
            self.L[i] = i - 1
            self.R[i] = i + 1
            self.U[i] = i
            self.D[i] = i
        self.L[0] = c
        self.R[c] = 0
        self.total = c

    def insert(self, r, c):
        self.total += 1
        self.r[self.total] = r
        self.c[self.total] = c
        self.size[c] += 1
        self.D[self.total] = self.D[c]
        self.U[self.D[c]] = self.total
        self.U[self.total] = c
        self.D[c] = self.total
        if self.first[r]:
            self.R[self.total] = self.R[self.first[r]]
            self.L[self.R[self.first[r]]] = self.total
            self.L[self.total] = self.first[r]
            self.R[self.first[r]] = self.total
        else:
            self.first[r] = self.total
            self.L[self.total] = self.total
            self.R[self.total] = self.total

    def remove(self, c):
        self.L[self.R[c]] = self.L[c]
        self.R[self.L[c]] = self.R[c]
        i = self.D[c]
        while i != c:
            j = self.R[i]
            while j != i:
                self.U[self.D[j]] = self.U[j]
                self.D[self.U[j]] = self.D[j]
                self.size[self.c[j]] -= 1
                j = self.R[j]
            i = self.D[i]

    def recover(self, c):
        i = self.U[c]
        while i != c:
            j = self.L[i]
            while j != i:
                self.U[self.D[j]] = j
                self.D[self.U[j]] = j
                self.size[self.c[j]] += 1
                j = self.L[j]
            i = self.U[i]
        self.L[self.R[c]] = c
        self.R[self.L[c]] = c

    def dance(self, lst):
        i = self.R[0]
        if i == 0: return lst
        c = i
        while True:
            i = self.R[i]
            if i == 0: break
            if self.size[i] < self.size[c]:
                c = i
        self.remove(c)
        i = self.D[c]
        while i != c:
            lst.append(self.r[i])
            j = self.R[i]
            while j != i:
                self.remove(self.c[j])
                j = self.R[j]
            _lst = self.dance(lst)
            if _lst is not None: return _lst
            j = self.L[i]
            while j != i:
                self.recover(self.c[j])
                j = self.L[j]
            lst.pop()
            i = self.D[i]
        self.recover(c)
        
if __name__ == '__main__':
    dlx = DLX(729, 324, 2916)
    sodoku = [input() for i in range(9)]
    def insert(i, j, num):
        row = 81 * i + 9 * j + num
        dlx.insert(row, 9 * i + num)
        dlx.insert(row, 81 + 9 * j + num)
        dlx.insert(row, 162 + 9 * i + j + 1)
        dlx.insert(row, 243 + 9 * (i // 3 * 3 + j // 3) + num)
        
    for i in range(9):
        for j in range(9):
            if sodoku[i][j] == '0':
                for num in range(1, 10):
                    insert(i, j, num)
            else:
                insert(i, j, int(sodoku[i][j]))

    res = [[0 for j in range(9)] for i in range(9)]   
    for choice in dlx.dance([]):
        div, mod = divmod(choice - 1, 9)
        i, j = divmod(div, 9)
        res[i][j] = mod + 1
    for line in res:
        print(*line, sep='')
