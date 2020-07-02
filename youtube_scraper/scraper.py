""" Library entry point """
import re, requests
from bs4 import BeautifulSoup


class YoutubeScrape(object):
    """ Scraper object to hold data """

    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        try:
            self.title = self.parse_string(".watch-title")
        except:
            self.title = self.parse_string(".title")
        try:
            self.poster = self.parse_string(".yt-user-info")
        except:
            self.poster = self.parse_string(".ytd-channel-name")
        try:
            self.views = self.parse_int(".watch-view-count")
        except:
            self.views = self.parse_int(".view-count")
        try:
            self.published = self.parse_string(".watch-time-text")
        except:
            self.published = self.parse_string("#date")
        self.published = re.sub(r"(Published|Uploaded) on", "", self.published).strip()
        try:
            self.like = self.parse_int(".yt-uix-clickcard", 4)
        except:
            pass
        try:
            self.dislike = self.parse_int(".yt-uix-clickcard", 5)
        except:
            pass

    def parse_int(self, selector, pos=0):
        """ Extract one integer element from soup """
        return int(re.sub("[^0-9]", "", self.parse_string(selector, pos)))

    def parse_string(self, selector, pos=0):
        """ Extract one particular element from soup """
        return self.soup.select(selector)[pos].get_text().strip()


def scrape_html(html):
    """ Return meta information about a video """
    return YoutubeScrape(BeautifulSoup(html, "html.parser"))


def scrape_url(url):
    """ Scrape a given url for youtube information """

    # set English as scraping language
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    html = requests.get(url, headers=headers).text
    return scrape_html(html)
