""" Library entry point """
import re, requests
from bs4 import BeautifulSoup

class YoutubeScrape(object):
    """ Scraper object to hold data """
    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        self.title = self.parse_string('.watch-title')
        self.poster = self.parse_string('.yt-user-info')
        self.views = self.parse_int('.watch-view-count')
        self.published = self.parse_string('.watch-time-text')
        self.published = re.sub(r'(Published|Uploaded) on', '', self.published).strip()
        self.like = self.parse_int('.yt-uix-clickcard', 4)
        self.dislike = self.parse_int('.yt-uix-clickcard', 5)

    def parse_int(self, selector, pos=0):
        """ Extract one integer element from soup """
        return int(re.sub('[^0-9]', '', self.parse_string(selector, pos)))

    def parse_string(self, selector, pos=0):
        """ Extract one particular element from soup """
        return self.soup.select(selector)[pos].get_text().strip()


def scrape_html(html):
    """ Return meta information about a video """
    return YoutubeScrape(BeautifulSoup(html, 'html.parser'))


def scrape_url(url):
    """ Scrape a given url for youtube information """

    # set English as scraping language
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    html = requests.get(url, headers=headers).text
    return scrape_html(html)
