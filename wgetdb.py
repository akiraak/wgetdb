#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''wgetdb

Usage:
  wgetdb <database_path> <url> [--label=]
  wgetdb -h | --help
  wgetdb --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  [--label]     Add label to data.
'''

from __future__ import unicode_literals, print_function
import datetime
import urllib2
import sqlite3
from docopt import docopt


__version__ = "0.1.0"
__author__ = "Akira Kozakai"
__license__ = "MIT"

TABLE_NAME = "datas"
URLOPEN_TIME_OUT = 10


def urldata(url):
    response = urllib2.urlopen(url, timeout=URLOPEN_TIME_OUT)
    if response.code != 200:
        return None
    return response.read()


def add_db(db_path, url, data, label):
    con = sqlite3.connect(db_path, isolation_level=None)

    # Create table
    cur = con.execute(
        "SELECT * FROM sqlite_master WHERE type='table' and name=?",
        (TABLE_NAME,))
    if cur.fetchone() is None:
        sql = """
            CREATE TABLE %s (
              data_id INTEGER PRIMARY KEY,
              url VARCHAR(4095),
              label VARCHAR(255),
              data BLOB,
              created_date DATE,
              UNIQUE(url, label)
            );
        """ % TABLE_NAME
        con.execute(sql)

    # Add record
    sql = ('INSERT INTO %s ("url", "label", "data", "created_date")'
           'VALUES (?, ?, ?, ?);') % TABLE_NAME
    args = (url, label, buffer(data), datetime.datetime.utcnow())
    cur = con.execute(sql, args)
    con.close()


def main():
    try:
        args = docopt(__doc__, version=__version__)
        db_path = args.get('<database_path>')
        url = args.get('<url>')
        label = args.get('--label')
        if not label:
            label = None
        data = urldata(url)

        if data:
            add_db(db_path, url, data, label)
            print('SUCCESS!')
    except Exception as e:
        print(u'=== ERROR ===')
        print(u'type:' + str(type(e)))
        print(u'args:' + str(e.args))
        print(u'message:' + e.message)


if __name__ == '__main__':
    main()
