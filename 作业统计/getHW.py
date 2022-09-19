import requests, time
from bs4 import BeautifulSoup

MAXTRY = 100

now = time.strftime('%Y%m%d%H%M%S')
log = open('log%s.txt' % now, 'w')
res = open('res%s.txt' % now, 'w')

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
	}

page = 0
while page < MAXTRY:
    page += 1
    url = "http://phyic.openjudge.cn/2022b0/ranking/?page=%d" % page
    resp = requests.get(url, headers=headers)
    bs = BeautifulSoup(resp.text, 'lxml')
    log.write(bs.prettify())
    for tr in bs.find_all('tr')[1:]:
        tddata = []
        for td in tr.find_all(name='td'):
            tddata.append(td.text)
        res.write(' '.join(tddata) + '\n')
    if bs.find(name='a', class_='nextprev', rel='next') is None:
        page = MAXTRY
    resp.close()
    time.sleep(0.5)

log.close()
res.close()
