#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging

import falcon
import simplejson
from asgiref import wsgi


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class TestAPI(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = simplejson.dumps(dict(msg="Hello, world"))

    def on_post(self, req, resp):
        data = json.load(req.bounded_stream)
        resp.body = simplejson.dumps(data)


app = falcon.API()

TSApi = TestAPI()
app.add_route("/", TSApi)
app.add_route("/api/v1/task/send", TSApi)

asgiApp = wsgi.WsgiToAsgi(app)
