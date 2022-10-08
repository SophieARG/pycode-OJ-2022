import csv, os, re

class CSVmaker:
    def __init__(self):
        self.load()
        if not os.path.exists('scores.csv'):
            self.setup()

    def load(self):
        with open('students.txt', 'r') as f:
            self.uids = {}
            self.names = []
            for index, line in enumerate(f.readlines()):
                uid, name = line.split()
                self.uids[uid] = index
                self.names.append(name)

    def setup(self):
        with open('scores.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.uids.keys())
            writer.writerow(self.names)

    def update(self, path):
        with open('scores.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            scores = [0 for i in range(len(self.names))]
            with open(path, 'r') as f:
                for line in f.readlines():
                    data = line.split()
                    userid, score = data[1], data[3]
                    index = self.search(userid)
                    if index is not None:
                        assert scores[index] == 0
                        scores[index] = score
            writer.writerow(scores)

    def search(self, userid):
        match = re.search('\d{10}', userid)
        if match is not None:
            uid = match.group()
            if uid in self.uids:
                return self.uids[uid]
        for index, name in enumerate(self.names):
            if name in userid:
                return index
 
