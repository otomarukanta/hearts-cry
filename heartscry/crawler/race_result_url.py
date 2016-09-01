import itertools
from heartscry import Downloader
from heartscry.parser import ScheduleListParser, RaceListParser
from heartscry.manager import UrlManager


YAHOO_KEIBA_URL = "http://keiba.yahoo.co.jp"
URL = "{}/schedule/list/{}/?month={}"
downloader = Downloader()
sche_list_parser = ScheduleListParser()
race_list_parser = RaceListParser()
url_manager = UrlManager()


def fetch_race_list_urls(year, month, day):
    page = downloader.download(URL.format(YAHOO_KEIBA_URL, year, month))
    sche_list_parser.set_day(day)
    sche_list_parser.set_page(page)
    return sche_list_parser.parse()


def fetch_race_result_urls(race_list_url):
    page = downloader.download("{}{}".format(YAHOO_KEIBA_URL, race_list_url))
    race_list_parser.set_page(page)
    return race_list_parser.parse()


def race_result_url(args):
    urls = fetch_race_list_urls(args.year, args.month, args.day)
    race_result_urls = itertools.chain.from_iterable(
            [fetch_race_result_urls(url) for url in urls])

    url_manager.insert_urls(race_result_urls)
