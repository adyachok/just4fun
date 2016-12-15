#!/usr/bin/env python
# Script parses specified json file and maps data on
# MySQL tables
#
# Data schema:
#     "id":         <String>
#     "title":      <String>
#     "thumbnail":  <String>
#     "creator":    <Dict>
#           "name":         <String>
#           "profileUrl":   <String>
#     "createdAt":  <Date object>

import logging
import MySQLdb
import json
import optparse
import os.path as path
import sys
import time


ROOT = path.abspath(path.dirname(path.dirname(__file__)))

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
fh = logging.FileHandler(path.join(ROOT, "application.log"))
fh.setLevel(logging.DEBUG)
format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_string)
fh.setFormatter(formatter)
LOG.addHandler(fh)


def main():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()
    filename = options.filename
    if filename is None:
        filename = path.join(ROOT, 'dezis.json')
    map_json_2_sql(filename)


def parse_date(date):
    date = time.strptime(date, '%B %d, %Y')
    return time.strftime("%Y-%m-%d", date)


def map_json_2_sql(filename):
    presentations_data = {}
    with open(filename, 'r') as f:
        try:
            presentations_data = json.loads(f.read())
        except ValueError:
            LOG.error("Could not decode JSON from file %s" % filename)
            sys.exit(1)
    # On this point we have presentations data
    if presentations_data:
        # insert User into Users table
        # insert Presentation into presentations table
        users = set()
        parser = Parser()

        for presentation in presentations_data:
            user = presentation['creator']
            if user['name'] not in users:
                parser.add_user(user)
                users.add(user['name'])
            parser.add_presentation(presentation)

        parser.finish()
    else:
        LOG.warn("No JSON data found during execution JSON to SQL mapping")


class Parser(object):
    def __init__(self):
        self._db = MySQLdb.connect("localhost", "dezi", "dezi", "dezi")
        self._cursor = self._db.cursor()

    def add_user(self, user):

        query = ("INSERT INTO users(name, profileUrl) VALUES ('%s', '%s')" %
                 (user['name'], user['profileUrl']))
        self._execute_query(query)

    def add_presentation(self, presentation):
        query = ('''INSERT INTO
        presentations(id, title, thumbnail, creator, createdAt)
        VALUES ('%s', '%s', '%s', '%s', '%s')''' %
                 (presentation['id'],
                  presentation['title'],
                  presentation['thumbnail'],
                  presentation['creator']['name'],
                  parse_date(presentation['createdAt'])))
        self._execute_query(query)

    def finish(self):
        self._cursor.close()
        self._db.close()

    def _execute_query(self, query):
        try:
            self._cursor.execute(query)
            self._db.commit()
        except Exception as e:
            LOG.error(e)
            self._db.rollback()


if __name__ == '__main__':
    main()
