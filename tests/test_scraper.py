import unittest
from youtube_scraper.scraper import scrape_html, scrape_url

TEST_DATA = '<html>\
    <span id="eow-title" class="watch-title " dir="ltr" title="thetitle">\
thetitle\
    </span>\
    <div class="yt-user-info">\
      <a href="/channel/asdkjasdkjashdkaljsdhasl" class=" yt-uix-sessionlink     spf-link  g-hovercard" data-name="" data-ytid="askdjahsdkaljshdaskasljd" data-sessionlink="asdasdjasdahsdjaksdllsjjs">theposter</a>\
    </div>\
    <div class="watch-view-count">9,999</div>\
    <strong class="watch-time-text">Published on Apr 1, 2013</strong>\
    <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button-unclicked  yt-uix-post-anchor yt-uix-tooltip" type="button" onclick=";return false;" aria-label="like this video along with 168 other people" title="I like this" id="watch-like" data-position="bottomright" data-post-action="/watch_actions_ajax?action_like_video=1&amp;video_id=7dlcxXxDGUI" data-force-position="true" data-orientation="vertical" data-post-data="" data-tooltip-text="I like this"><span class="yt-uix-button-content">168</span></button>\
    <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button-unclicked  yt-uix-post-anchor yt-uix-tooltip" type="button" onclick=";return false;" aria-label="dislike this video along with 8 other people" title="I dislike this" id="watch-dislike" data-position="bottomright" data-post-action="/watch_actions_ajax?action_dislike_video=1&amp;video_id=7dlcxXxDGUI" data-force-position="true" data-orientation="vertical" data-post-data="" data-tooltip-text="I dislike this"><span class="yt-uix-button-content">8</span></button>\
</html>'

class TestScraper(unittest.TestCase):
    def test_scrape_html(self):
        data = scrape_html(TEST_DATA)
        self.assertEqual(data.title, 'thetitle')
        self.assertEqual(data.poster, 'theposter')
        self.assertEqual(data.views, 9999)
        self.assertEqual(data.published, 'Apr 1, 2013')
        self.assertEqual(data.like, 168)
        self.assertEqual(data.dislike, 8)

    def test_scrape_url(self):
        data = scrape_url('http://youtube.com/watch?v=7dlcxXxDGUI')
        self.assertEqual(data.poster, 'TheViperAOC')

if __name__ == '__main':
    unittest.main()
