#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Irina'
AUTHOR_URL = 'http://github.com/j-bennet'
AUTHORS = {
    'Irina': 'http://github.com/j-bennet'
}
SITENAME = 'wharfee'
SITEURL = 'http://wharfee.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/j-bennet/wharfee'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DIRECT_TEMPLATES = {}

STATIC_PATHS = {'images', 'extra/CNAME', 'extra/custom.css'}
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/custom.css': {'path': 'styles/custom.css'}
}

THEME = '../pelican-themes/chameleon'
#BS3_THEME = 'http://bootswatch.com/simplex/bootstrap.min.css'
BS3_THEME = 'http://bootswatch.com/flatly/bootstrap.min.css'
CSS_OVERWRITE = '/styles/custom.css'

MENUITEMS = [
    ('Home', '/'),
    ('Features', '/features.html'),
    ('Powered by', '/poweredby.html'),
    ('Thanks', '/thanks.html'),
    ('Contact', '/contact.html'),
    ('Blog', '/category/blog.html'),
]

GOOGLE_ANALYTICS = "UA-66237704-1"
