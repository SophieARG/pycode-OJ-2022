from bisect import insort
events = {}
years = [[] for i in range(2022 + 1)]
for i in range(int(input())):
    event, yi, yf = input().split()
    events[event] = yi + ' ' + yf
    for y in range(int(yi), int(yf) + 1):
        insort(years[y], event)
digits = set('0123456789')
while True:
    try:
        cmd = input()
        if cmd[0] in digits:
            print(*years[int(cmd)])
        else:
            print(events[cmd])
    except EOFError:
        break
