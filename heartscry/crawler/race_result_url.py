import requests
import bs4
import re
import itertools
from heartscry.url_db import UrlDB


YAHOO_KEIBA_URL = "http://keiba.yahoo.co.jp"
URL = "{}/schedule/list/{}/?month={}"


def fetch_race_list_urls(year, month, day):
    res = requests.get(URL.format(YAHOO_KEIBA_URL, year, month))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for line in soup.find(class_='scheLs').find_all('tr'):
        tds = line.find_all('td')
        if not tds:
            continue
        if re.match("\d*", tds[0].text).group() == day:
            yield tds[1].a.get('href')


def fetch_race_result_urls(race_list_url):
    res = requests.get("{}{}".format(YAHOO_KEIBA_URL, race_list_url))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for line in soup.find(class_='scheLs').find_all('tr'):
        tds = line.find_all('td')
        if not tds:
            continue
        yield tds[1].a.get('href')


def race_result_url(args):
    urls = fetch_race_list_urls(args.year, args.month, args.day)
    race_result_urls = list(itertools.chain.from_iterable(
        map(list, map(fetch_race_result_urls, urls))))

    db = UrlDB()
    [db.insert_url('race_result_urls', url) for url in race_result_urls]
