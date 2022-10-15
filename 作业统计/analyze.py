import csv

with open('scores.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    uids = next(reader)
    names = next(reader)
    scores = list(reader)
    total = [sum([int(scores[i][j]) for i in range(len(scores))]) for j in range(len(scores[0]))]
    for uid, name, score in zip(uids, names, total):
        if score < 5 + 6:
            print('score: %2s id: %s name: %s' % (score, uid, name))
