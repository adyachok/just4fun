import inspect
import MySQLdb
import sys


class QueryManager(object):

    def get_all(self):
        raise NotImplemented

    def search_title(self, title):
        raise NotImplemented

    def order_by_date(self, order=None):
        raise NotImplemented


class MySQLQueryManager(QueryManager):

    def __init__(self, host, user, password, database):
        self._db = MySQLdb.connect(host, user, password, database)

    def get_all(self):
        data = []
        query = '''SELECT p.id, p.title, p.thumbnail, p.createdAt, u.name
                   FROM presentations as p
                   JOIN users as u ON p.creator = u.name'''

        cursor = self._db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return self._parse_result_set(data)

    def search_title(self, title):
        query = '''SELECT p.id, p.title, p.thumbnail, p.createdAt, u.name
               FROM presentations as p
               JOIN users as u ON p.creator = u.name
               WHERE p.title LIKE '{0}%' '''.format(title)
        cursor = self._db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return self._parse_result_set(data)

    def order_by_date(self, order='DESC'):
        query = '''SELECT p.id, p.title, p.thumbnail, p.createdAt, u.name
                   FROM presentations as p
                   JOIN users as u ON p.creator = u.name
                   ORDER BY p.createdAt %s''' % order
        cursor = self._db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return self._parse_result_set(data)

    def _parse_result_set(self, result):
        data = []
        for item in result:
            val = {'id': item[0],
                   'title': item[1],
                   'thumbnail': item[2],
                   'createdAt': item[3],
                   'creator': item[4]}
            data.append(val)
        return data


class MongoDBQueryManager(QueryManager):
    pass


class ManagerLoadException(Exception):
    pass


def load_query_manager(conf):
    for item in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if item[0].lower().startswith(conf.database):
            return item[1](**conf.database_settings)
    raise ManagerLoadException('Cannot find database manager')
