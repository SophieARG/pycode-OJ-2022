import re, datetime

t0 = datetime.datetime(2000, 1, 1)
DAYS = 146097  # 400 years
PATTERN = '(\d+):(\d+):(\d+) (\d+)\.(\d+)\.(\d+)'

for i in range(int(input())):
    H, M, S, d, m, Y = map(int, re.fullmatch(PATTERN, input()).group(*range(1, 7)))
    Y1, Y2 = divmod(Y - 2000, 400)
    dt = datetime.datetime(Y2 + 2000, m, d, H, M, S) - t0
    t = dt.seconds * 100000 / 86400
    t, S = divmod(t, 100)
    t, M = divmod(t, 100)
    t, H = divmod(t, 10)
    t = Y1 * DAYS + dt.days
    t, d = divmod(t, 100)
    Y, m = divmod(t, 10)
    print('%d:%d:%d %d.%d.%d'%(H, M, S, d+1, m+1, Y))
