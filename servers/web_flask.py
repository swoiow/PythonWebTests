#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Under JMeter
pypy3
python3    650~900+
"""

from flask import Flask, jsonify, request
from flask.views import MethodView


class TestAPI(MethodView):

    def get(self):
        return jsonify(dict(msg="Hello, world"))

    def post(self):
        data = request.get_json(force=True, silent=True)
        return jsonify(**data), 200


app = Flask(__name__)
app.add_url_rule('/', view_func=TestAPI.as_view('index'))
app.add_url_rule('/api/v1/task/send', view_func=TestAPI.as_view('tests'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="62300")
