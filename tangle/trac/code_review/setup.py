#!/usr/bin/env python

from setuptools import setup

PACKAGE = 'Code Review'
VERSION = '0.1'

setup(
    name = PACKAGE,
    version = VERSION,
    author = 'Exoweb Internal Products Research and Development Team',
    author_email = 'research@exoweb.net',
    description = 'Trac plugin to aid code review',
    license = 'BSD',
    keywords = 'trac code review plugin exoweb',
    url = 'http://contrib.exoweb.net/contrib/trac/wiki/CodeReview',
    packages = ['codereview'],
    package_data = {'codereview': ['templates/*.cs', 'htdocs/*.*', 'htdocs/css/*.*']},
    entry_points = {'trac.plugins': '%s = codereview' % PACKAGE}
)
