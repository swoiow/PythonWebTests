install:
	pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple && \
	simplejson tornado Flask gunicorn gevent daphne asgiref

flask:
	python servers/web_flask.py

flask-gg:
	gunicorn -b 0.0.0.0:8888 servers.web_flask:app -k gevent

tornado:
	python servers/web_tornado.py

tornado-pypy:
	pypy3 servers/web_tornado.py

falcon-asgi:
	daphne -b 0.0.0.0 -p 8888 servers.web_falcon:asgiApp --access-log ./falon_access.log

cherrypy:
	python servers/web_cherrypy.py