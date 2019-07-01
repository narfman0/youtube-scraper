""" Library entry point """
import re, requests
from bs4 import BeautifulSoup

class YoutubeScrape(object):
    """ Scraper object to hold data """
    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        self.title = self.parse_string('.watch-title', 0)
        self.poster = self.parse_string('.yt-user-info', 0)
        self.views = self.parse_int('.watch-view-count', 0)
        self.published = self.parse_string('.watch-time-text', 0)
        self.published = re.sub(r'(Published|Uploaded) on', '', self.published).strip()
        self.like = self.parse_int('.yt-uix-clickcard', 4)
        self.dislike = self.parse_int('.yt-uix-clickcard', 5)

    def parse_int(self, selector, pos):
        """ Extract one integer element from soup """
        return int(re.sub('[^0-9]', '', self.parse_string(selector, pos)))

    def parse_string(self, selector, pos):
        """ Extract one particular element from soup """
        return self.soup.select(selector)[pos].get_text().strip()


def scrape_html(html):
    """ Return meta information about a video """
    return YoutubeScrape(BeautifulSoup(html, 'html.parser'))


def scrape_url(url):
    """ Scrape a given url for youtube information """
    html = requests.get(url).text

    #with open('test.html', 'w') as f:
    #    f.write(html.encode('utf-8'))

    return scrape_html(html)
