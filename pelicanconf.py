#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Seth Gottlieb'
SITENAME = 'Content Here'
SITESUBTITLE = 'Where content meets technology'
SITEURL = 'https://www.contenthere.net'
COPYRIGHT = 'CreativeCommons'


PATH = 'content'

TIMEZONE = 'America/New_York'

S3_BUCKET="www.contenthere.net"

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['/Users/sgottlieb/lib/pelican-plugins']
PLUGINS = ['sitemap',]

SITEMAP = {
    'exclude': ['tag/', 'category/']
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (,)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


DEFAULT_CATEGORY = 'misc'

OUTPUT_PATH = "output/"
DELETE_OUTPUT_DIRECTORY = True

THEME = "blue-penguin-theme"

SITEDESCRIPTION = "Seth Gottlieb's personal blog"

ARCHIVES_URL       = 'archives/index.html'
ARCHIVES_SAVE_AS   = 'archives/index.html'
TAGS_URL           = 'tags/index.html'
TAGS_SAVE_AS       = 'tags/index.html'
DISPLAY_FOOTER = True

PAGINATION_PATTERNS = (
    (1, '{url}/index.html', '{save_as}'),
    (2, '{base_name}/page/{number}/index.html', '{base_name}/page/{number}/index.html'),
)

MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

MENUITEMS = (
    ('About', 'https://www.sethgottlieb.com/'),
)
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True