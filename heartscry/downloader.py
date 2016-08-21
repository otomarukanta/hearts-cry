import requests


class Downloader():

    def download(self, url):
        res = requests.get(url)
        res.raise_for_status()
        return res.text
