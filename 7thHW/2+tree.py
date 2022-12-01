from copy import deepcopy
from functools import lru_cache
from itertools import permutations as perm

Target = 24
N = 4

Epsilon = 0.01

class exprTree:
    
    __slots__ = ['isroot', 'isleaf', 'lchild', 'rchild']
    
    def __init__(self):
        self.isroot = False
        self.isleaf = False
        self.lchild = None
        self.rchild = None

    def solve(self, _iter):
        if self.isleaf:
            return {next(_iter)}
        lnums = self.lchild.solve(_iter)
        rnums = self.rchild.solve(_iter)
        if self.isroot:
            for lnum in lnums:
                for rnum in rnums:
                    if rnum and abs(lnum / rnum - Target) < Epsilon: return True
                    if abs(lnum + rnum - Target) < Epsilon: return True
                    if abs(lnum - rnum - Target) < Epsilon: return True
                    if abs(lnum * rnum - Target) < Epsilon: return True
            return False
        nums = {lnum / rnum for lnum in lnums for rnum in rnums if rnum}
        nums.update({lnum + rnum for lnum in lnums for rnum in rnums})
        nums.update({lnum - rnum for lnum in lnums for rnum in rnums})
        nums.update({lnum * rnum for lnum in lnums for rnum in rnums})
        return nums
        
def build(n):
    
    def _build(n, node):
        if n == 1:
            node.isleaf = True
            return [node]
        else:
            res = []
            for l in range(1, n):
                for ltree in _build(l, exprTree()):
                    for rtree in _build(n - l, exprTree()):
                        node.lchild = ltree
                        node.rchild = rtree
                        res.append(deepcopy(node))
            return res
        
    root = exprTree()
    root.isroot = True
    return _build(n, root)

trees = build(N)

@lru_cache()
def myjudge(nums):
    for tree in trees:
        if tree.solve(iter(nums)): return True
    return False

while True:
    cin = input()
    if cin[0] == '0': break
    print('YES' if True in map(myjudge, perm(map(int, cin.split()))) else 'NO')
