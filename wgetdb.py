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
URLOPEN_TIMEOUT = 10


def download_url(url):
    response = urllib2.urlopen(url, timeout=URLOPEN_TIMEOUT)
    if response.code != 200:
        return None
    return response.read()


def create_table(con):
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


def insert_data(con, url, data, label):
    sql = ('INSERT INTO %s ("url", "label", "data", "created_date")'
           'VALUES (?, ?, ?, ?);') % TABLE_NAME
    args = (url, label, buffer(data), datetime.datetime.utcnow())
    con.execute(sql, args)


def store_data(db_path, url, data, label):
    con = sqlite3.connect(db_path, isolation_level=None)
    try:
        create_table(con)
        insert_data(con, url, data, label)
    finally:
        con.close()


def main():
    try:
        args = docopt(__doc__, version=__version__)
        db_path = args.get('<database_path>')
        url = args.get('<url>')
        label = args.get('--label') or None
        data = download_url(url)

        if data:
            store_data(db_path, url, data, label)
            print('SUCCESS!')
    except Exception as e:
        print(u'=== ERROR ===')
        print(u'type:{0}'.format(type(e)))
        print(u'args:{0}'.format(e.args))
        print(u'message:{0}'.format(e.message))


if __name__ == '__main__':
    main()
