#!/usr/bin/env python
import argparse
from logging import basicConfig, DEBUG
from heartscry.url_db import UrlDB
from heartscry.crawler import race_result_url

FETCH_TARGETS = ['race_result_url']


def init_urldb(args):
    db = UrlDB()
    db.init_table('race_result_urls')


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True

    parser_init_urldb = subparsers.add_parser('init_urldb')
    parser_init_urldb.set_defaults(func=init_urldb)

    # fetch
    parser_fetch = subparsers.add_parser('fetch')
    parser_fetch_sub = parser_fetch.add_subparsers(dest='target')
    parser_fetch_sub.required = True

    parser_race_result_url = parser_fetch_sub.add_parser('race_result_url')
    parser_race_result_url.add_argument('year')
    parser_race_result_url.add_argument('month')
    parser_race_result_url.add_argument('day')
    parser_race_result_url.set_defaults(func=race_result_url)
    return parser.parse_args()


def main():
    basicConfig(
        format='%(asctime)s %(name)s [%(levelname)s] %(message)s',
        level=DEBUG)
    args = parse_args()
    print(args)
    args.func(args)
