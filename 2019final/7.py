data = [[], [], []]
for pid in range(1, int(input()) + 1):
    name, uid = map(int, input().split(','))
    data[name - 1].append((uid, pid))
for _data in data:
    for uid, pid in sorted(_data):
        print(pid)
