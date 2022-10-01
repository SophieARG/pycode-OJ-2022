fib = [1, 1]
n = int(input())
for i in range(n):
    a = int(input())
    if a <= len(fib):
        print(fib[a-1])
    else:
        for j in range(a-len(fib)):
            fib.append(fib[-2]+fib[-1])
        print(fib[-1])
