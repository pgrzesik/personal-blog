#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piotr Grzesik'
SITENAME = 'Piotr Grzesik'
SITEURL = ''

THEME = 'flex-theme'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('envelope', 'mailto:pj.grzesik@gmail.com'),
          ('twitter', 'https://twitter.com/p_grzesik'),
          ('github', 'https://github.com/pgrzesik'),
          ('linkedin', 'https://www.linkedin.com/in/piotr-grzesik-a8bb8067'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
