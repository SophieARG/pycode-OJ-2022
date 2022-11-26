print(*map(lambda x: ' '.join(map(str, x)), sorted(([int(field) if field.isdigit() else field for field in input().split()] for i in range(int(input()))), key=lambda x: (-x[2], -x[3]))), sep='\n')
