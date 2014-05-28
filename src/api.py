#
# -*- coding: utf-8 -*-
#


import os
import base64
import urllib
import traceback


## use Ultrajson (https://github.com/esnme/ultrajson) if available
try:
   import ujson
   json_lib = ujson
   json_loads = ujson.loads
   json_dumps = lambda x: ujson.dumps(x, ensure_ascii = False)
except:
   import json
   json_lib = json
   json_loads = json.loads
   json_dumps = json.dumps


from txgittip import \
    version as txgittip_version

from twisted import \
    version as twisted_version

from twisted.internet import \
    defer, task, reactor, threads
from twisted.internet.defer import \
    inlineCallbacks, returnValue, Deferred, DeferredList, \
    maybeDeferred, gatherResults, _DefGen_Return
from twisted.internet.task import \
    deferLater
from twisted.internet.threads import \
    deferToThread

from twisted.web.client import \
    getPage, Agent, HTTPConnectionPool, FileBodyProducer
from twisted.web.http_headers import \
    Headers


os_sysname, os_nodename, os_release, os_version, os_machine = os.uname()

user_agent = 'TxGittip {} ({}; {}) {}'.format(txgittip_version, os_sysname, os_machine, twisted_version)
url = 'https://www.gittip.com/'


class RequestError(Exception):
    pass


def make_endpoint_address(endpoint, username):
    global url
    return u'%(url)s/%(username)s/%(endpoint)s' % dict(url=url,
                                                      username=username,
                                                      endpoint=endpoint
                                                     )
    return address

@inlineCallbacks
def endpoint(endpoint, username='about'):
    address = make_endpoint_address(endpoint, username)
    result = yield getPage(address.encode('utf-8'))
    returnValue(json_loads(result))


def paydays():
    return endpoint('paydays.json', 'about')


def stats():
    return endpoint('stats.json', 'about')


def charts(username='about'):
    return endpoint('charts.json', username)


def public(username):
    return endpoint('public.json', username)


@inlineCallbacks
def tips(username, apikey, data):
    global url, user_agent
    address, make_endpoint_address(endpoint, username)
    agent = Agent(reactor)
    headers = Headers({
        'Accept': ['application/json,*/*;q=0.8'],
        'Accept-Encoding': ['gzip,deflate,sdch'],
        'Connection': ['keep-alive'],
        'User-Agent': [user_agent],
        'Content-Type': ['application/json'],
    })
    body = FileBodyProducer(StringIO(json_dumps(data)))
    response = yield agent.request('POST', address.encode('utf-8'), headers, body)
    if (response.code == 200):
        finished = Deferred()
        collector = WebBodyCollector(finished)
        response.deliverBody(collector)
        x = yield finished
        returnValue(json_loads(collector.body))
    else:
        raise RequestError(response.phrase)


__all__ = [
    'paydays',
    'stats',
    'charts',
    'public',
    'tips',
]