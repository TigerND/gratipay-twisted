#
# -*- coding: utf-8 -*-
#


import os
import six
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
from twisted.internet.protocol import \
    Protocol

from twisted.web.client import \
    getPage, Agent, HTTPConnectionPool, FileBodyProducer
from twisted.web.http_headers import \
    Headers


os_sysname, os_nodename, os_release, os_version, os_machine = os.uname()

user_agent = 'TxGittip {} ({}; {}) {}'.format(txgittip_version, os_sysname, os_machine, twisted_version)
url = 'https://www.gittip.com/'


class RequestError(Exception):
    pass


def encode_apikey(apikey):
    apikey = apikey.encode('utf-8') if (isinstance(apikey, unicode)) else apikey
    return base64.urlsafe_b64encode(apikey + ':').encode('utf-8')


def make_endpoint_address(endpoint, username):
    global url
    return u'%(url)s/%(username)s/%(endpoint)s' % dict(url=url,
                                                      username=username,
                                                      endpoint=endpoint
                                                     )
    return address


class WebBodyCollector(Protocol):
    def __init__(self, finished):
        self.finished = finished
        self.body = ''

    def dataReceived(self, bytes):
        self.body += bytes

    def connectionLost(self, reason):
        self.finished.callback(None)


@inlineCallbacks
def endpoint(endpoint, username='about', apikey=None, data=None):
    global url, user_agent
    def encode_body(data):
        if (data):
            if (isinstance(data, six.string_types)):
                data = json_loads(data)
            return ('POST', FileBodyProducer(six.StringIO(json_dumps(data))))
        else:
            return ('GET', None)
    address = make_endpoint_address(endpoint, username)
    headers = Headers({
        'Accept': ['application/json,*/*;q=0.8'],
        'Accept-Encoding': ['gzip,deflate,sdch'],
        'Connection': ['keep-alive'],
        'User-Agent': [user_agent],
        'Content-Type': ['application/json'],
    })
    if (apikey):
        headers.addRawHeader('Authorization', 'Basic ' + encode_apikey(str(apikey)))
    method, body = encode_body(data)
    agent = Agent(reactor)
    response = yield agent.request(method, address.encode('utf-8'), headers, body)
    if (response.code == 200):
        finished = Deferred()
        collector = WebBodyCollector(finished)
        response.deliverBody(collector)
        x = yield finished
        returnValue(json_loads(collector.body))
    else:
        raise RequestError(response.phrase)



def paydays():
    return endpoint('paydays.json')


def stats():
    return endpoint('stats.json')


def charts(username='about'):
    return endpoint('charts.json', username)


def public(username):
    return endpoint('public.json', username)


def tips(username, apikey, data):
    return endpoint('tips.json', username, apikey, data)


__all__ = [
    'paydays',
    'stats',
    'charts',
    'public',
    'tips',
]
