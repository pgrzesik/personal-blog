#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piotr Grzesik'
SITENAME = 'Piotr Grzesik'
SITEURL = ''
SITESUBTITLE = 'Software developer'


THEME = 'clean-blog-theme'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('envelope', 'mailto:pj.grzesik@gmail.com'),
          ('twitter', 'https://twitter.com/p_grzesik'),
          ('github', 'https://github.com/pgrzesik'),
          ('linkedin', 'https://www.linkedin.com/in/piotr-grzesik-a8bb8067'))

# Menu items
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
