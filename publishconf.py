#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://www.contenthere.net'
RELATIVE_URLS = False

S3_BUCKET="www.contenthere.net"

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_COPYRIGHT = 'Attribution 4.0 International (CC BY 4.0) https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""