import json
import os.path as path

from bottle import route, run, template, TEMPLATE_PATH, response, static_file

from config import CONF
from repository.query_manager import load_query_manager

ROOT = path.abspath(path.dirname(__file__))
TEMPLATE_PATH.append(path.join(ROOT, 'templates'))

MANAGER = load_query_manager(CONF)


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError


@route('/')
def hello():
    return template('welcome')


@route('/presentations/')
def hello():
    data = MANAGER.get_all()
    response.content_type = 'application/json'
    return json.dumps({'data': data}, default=date_handler)


@route('/presentations/<name>')
def search_by_title(name=''):
    data = MANAGER.search_title(name)
    response.content_type = 'application/json'
    return json.dumps({'data': data}, default=date_handler)


@route('/presentations/order/<order>')
def order_by_date(order):
    if order.lower() not in ['asc', 'desc']:
        order = 'desc'
    data = MANAGER.order_by_date(order)
    response.content_type = 'application/json'
    return json.dumps({'data': data}, default=date_handler)


@route('/static/<file_path>')
def callback(file_path):
    return static_file(file_path, path.join(ROOT, 'static'))


run(host='127.0.0.1', port=8000, debug=True, reloader=True)
