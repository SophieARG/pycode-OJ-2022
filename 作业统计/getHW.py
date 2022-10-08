import time
from myOJ import OJparser
from myCSV import CSVmaker

ojparser = OJparser()

GROUPNAME = 'phyic'
TITLE = '2022b01'

now = time.strftime('%Y%m%d%H%M%S')
suffix = '-%s-%s-%s.txt' % (GROUPNAME, TITLE, now)

logfile = open('log' + suffix, 'w')
datafile = open('data' + suffix, 'w')

ojparser.parse(GROUPNAME, TITLE, logfile, datafile)

logfile.close()
datafile.close()

csvmaker = CSVmaker()
csvmaker.update('data' + suffix)
