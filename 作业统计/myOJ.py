import requests, time
from bs4 import BeautifulSoup

MAXTRY = 100
HEADERS = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
	}

class OJparser:
    def __init__(self, maxtry=MAXTRY, headers=HEADERS):
        self.maxtry = maxtry
        self.headers = headers

    def parse(self, groupname, title, logfile, datafile):
        page = 0
        while page < self.maxtry:
            page += 1
            url = f"http://{groupname}.openjudge.cn/{title}/ranking/?page={page}"
            resp = requests.get(url, headers=self.headers)
            bs = BeautifulSoup(resp.text, 'lxml')
            logfile.write(bs.prettify())
            for tr in bs.find_all('tr')[1:]:
                tddata = []
                for td in tr.find_all(name='td'):
                    _td = td.text.strip()
                    tddata.append(_td.replace(' ', '-') if _td else 'None')
                datafile.write(' '.join(tddata) + '\n')
            if bs.find(name='a', class_='nextprev', rel='next') is None:
                page = self.maxtry
            resp.close()
            time.sleep(0.5)
