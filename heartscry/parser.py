from abc import ABCMeta, abstractmethod
import re
import bs4


class Parser(metaclass=ABCMeta):

    def set_page(self, page):
        self.soup = bs4.BeautifulSoup(page, "lxml")

    @abstractmethod
    def parse(self):
        pass


class ScheduleListParser(Parser):

    def set_day(self, day):
        self.day = day

    def parse(self):
        return list(self.__parse())

    def __parse(self):
        for line in self.soup.find(class_='scheLs').find_all('tr'):
            tds = line.find_all('td')
            if not tds:
                continue
            if re.match("\d*", tds[0].text).group() == self.day:
                yield tds[1].a.get('href')


class RaceListParser(Parser):

    def parse(self):
        return list(self.__parse())

    def __parse(self):
        for line in self.soup.find(class_='scheLs').find_all('tr'):
            tds = line.find_all('td')
            if not tds:
                continue
            yield tds[1].a.get('href')
