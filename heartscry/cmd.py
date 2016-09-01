#!/usr/bin/env python
import argparse
from logging import basicConfig, DEBUG
from heartscry.crawler import race_result_url, race_result
from heartscry.manager import UrlManager


FETCH_TARGETS = ['race_result_url']


def init_urldb(args):
    UrlManager().init_url_tables()


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True

    parser_init = subparsers.add_parser('init')
    parser_init_sub = parser_init.add_subparsers(dest='target')
    parser_init_sub.required = True

    parser_init_url = parser_init_sub.add_parser('url')
    parser_init_url.set_defaults(func=init_urldb)

    # fetch
    parser_fetch = subparsers.add_parser('fetch')
    parser_fetch_sub = parser_fetch.add_subparsers(dest='target')
    parser_fetch_sub.required = True

    # race_result_url
    parser_race_result_url = parser_fetch_sub.add_parser('race_result_url')
    parser_race_result_url.add_argument('year')
    parser_race_result_url.add_argument('month')
    parser_race_result_url.add_argument('day')
    parser_race_result_url.set_defaults(func=race_result_url)

    # race_result
    parser_race_result = parser_fetch_sub.add_parser('race_result')
    parser_race_result.set_defaults(func=race_result)
    return parser.parse_args()


def main():
    basicConfig(
        format='%(asctime)s %(name)s [%(levelname)s] %(message)s',
        level=DEBUG)
    args = parse_args()
    print(args)
    args.func(args)
