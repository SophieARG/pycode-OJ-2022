def move(i, j, k, n):
    if n > 0:
        move(i, k, j, n - 1)
        print(f'{i}->{j}')
        move(k, j, i, n - 1)
move('A', 'C', 'B', int(input()))
