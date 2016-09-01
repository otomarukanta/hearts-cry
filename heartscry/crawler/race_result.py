import requests
import bs4
from collections import defaultdict
from heartscry.url_db import UrlDB
from logging import getLogger

logger = getLogger(__name__)

YAHOO_KEIBA_URL = "http://keiba.yahoo.co.jp"


def fetch_race_result_urls(race_list_url):
    res = requests.get("{}{}".format(YAHOO_KEIBA_URL, race_list_url))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for line in soup.find(class_='scheLs').find_all('tr'):
        tds = line.find_all('td')
        if not tds:
            continue
        yield tds[1].a.get('href')


def parse_pay_off(soup):
    keys = [x.text for x in soup.find_all("th")
            for i in range(int(x.attrs["rowspan"]))]
    v_keys = ['馬番', '金額', '人気']
    values = [{v_keys[i]: x.text for i, x in enumerate(line.find_all("td"))}
              for line in soup.find_all("tr")]

    d = defaultdict(list)
    for k, v in zip(keys, values):
        d[k].append(v)

    return dict(d.items())


def fetch_race_result(url):
    res = requests.get("{}{}".format(YAHOO_KEIBA_URL, url),
                       allow_redirects=False)
    res.raise_for_status()
    if res.status_code >= 300:
        logger.warn("'{}' is not a race result page.".format(url))
        logger.warn("Maybe it is a race denma page still.")
        return None

    soup = bs4.BeautifulSoup(res.text, "lxml")

    payoff = parse_pay_off(soup.find(class_='layoutCol2M'))
    return payoff


def race_result(args):
    db = UrlDB()
    fetched_data = [
            fetch_race_result(url) for url in db.get_urls('race_result_urls')]
    print(fetched_data)
