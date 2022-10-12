a, b, op = input().split()
if op == '+':
    print(int(a) + int(b))
elif op == '-':
    print(int(a) - int(b))
elif op == '*':
    print(int(a) * int(b))
elif op == '/':
    print(int(int(a) / int(b)) if b != '0' else 'Divided by zero!')
else:
    print('Invalid operator!')
