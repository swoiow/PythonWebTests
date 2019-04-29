#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Under JMeter
pypy3      1k~1.2k+
python3    580~650+
"""

import simplejson as json
import tornado.ioloop
import tornado.web


class TestAPI(tornado.web.RequestHandler):

    def prepare(self):
        json_headers_flag = ["application/x-json", "application/json"]
        if self.request.headers.get("Content-Type") in json_headers_flag:
            self.args = json.loads(self.request.body)

            if not self.args:
                self.write_error(400, exc_info="JSON data must not be empty")
        else:
            self.args = dict(msg="Hello, world")

    def get(self):
        self.write_json(self.args)

    def post(self):
        self.write_json(self.args)
        self.on_finish()

    def write_json(self, chunk) -> None:
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(chunk))


def make_app():
    return tornado.web.Application([
        (r"/", TestAPI),
        (r"/api/v1/task/send", TestAPI),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(62300, "0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
