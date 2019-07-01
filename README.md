youtube-scraper
===============

Provide information for youtube related metadata (title, user, views, likes, dislikes, publish date)

Usage
-----

This is a developer focused library to provide information from youtube.

    >>> from youtube_scraper.scraper import scrape_url
    >>> data = scrape_url('http://youtube.com/watch?v=7dlcxXxDGUI')
    >>> print(data.poster)
    'TheViperAOC'

License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
