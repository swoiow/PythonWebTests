#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import cherrypy
import simplejson


@cherrypy.expose
class TestAPI(object):

    @cherrypy.tools.accept(media="text/plain")
    def GET(self, *args, **kwargs):
        return simplejson.dumps(dict(msg="Hello, world"))

    def POST(self, *args, **kwargs):
        cl = cherrypy.request.headers["Content-Length"]
        body = cherrypy.request.body.read(int(cl))
        data = json.loads(body)
        return simplejson.dumps(data)


conf = {
    "/": {
        "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
        "tools.response_headers.on": True,
    },
    "/api/v1/task/send": {
        "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
        "tools.response_headers.on": True,
    }
}
cherrypy.tree.mount(TestAPI(), config=conf)

if __name__ == "__main__":
    cherrypy.config.update({
        "global": {
            "server.socket_host": "0.0.0.0",
            "server.socket_port": 8888,
            "environment": "production"
        },
        "log.screen": False,
        "log.access_file": "/.access.log",
        "log.error_file": "./error.log"
    })

    if hasattr(cherrypy.engine, "block"):
        # 3.1 syntax
        cherrypy.engine.start()
        cherrypy.engine.block()

    else:
        # 3.0 syntax
        cherrypy.server.quickstart()
        cherrypy.engine.start()
