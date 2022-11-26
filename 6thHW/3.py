solutions = []

def queen(solution, i=0):
    if i == 8:
        solutions.append(''.join(map(lambda x: str(x + 1), solution)))
        return
    for col in range(8):
        solution[i] = col
        for row in range(i):
            if solution[row] == col or abs(col - solution[row]) == i - row:
                break
        else:
            queen(solution, i + 1)
            
queen([0 for i in range(8)])
for i in range(int(input())):
    print(solutions[int(input()) - 1])
