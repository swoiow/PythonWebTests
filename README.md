# PythonWebTests

> python web framework tests.

  + default port in docker container is 8888
  + default port in docker host is 8080


## How To Run

```
docker-compose up tornado
docker-compose up tornado-pypy
docker-compose up flask
docker-compose up flask-gg
```


## Siege Test Case
```
siege -c 100 -r 100 --content-type "application/json" 'http://127.0.0.1:62300/ POST {"data":{"agent_uuid":"8e526156-b6c2-49d4-ad2d-89d676e4bb7d","complex_uuid":"54edbab0-7a7d-46ef-a44b-8f2c56d15a6e"},"task":"complex.checkExists.request"}'
```

### Siege Test Results
```
flask

Lifting the server siege...
Transactions:                  41299 hits
Availability:                 100.00 %
Elapsed time:                  60.00 secs
Data transferred:               6.07 MB
Response time:                  0.14 secs
Transaction rate:             688.32 trans/sec
Throughput:                     0.10 MB/sec
Concurrency:                   99.75
Successful transactions:       41299
Failed transactions:               0
Longest transaction:            0.20
Shortest transaction:           0.00

- - - - -
flask-gg (gunicorn + gevent)

Lifting the server siege...
Transactions:                  55728 hits
Availability:                 100.00 %
Elapsed time:                  59.18 secs
Data transferred:               8.18 MB
Response time:                  0.11 secs
Transaction rate:             941.67 trans/sec
Throughput:                     0.14 MB/sec
Concurrency:                   99.75
Successful transactions:       55728
Failed transactions:               0
Longest transaction:            0.17
Shortest transaction:           0.00

- - - - -
tornado

Lifting the server siege...
Transactions:                  75746 hits
Availability:                 100.00 %
Elapsed time:                  59.70 secs
Data transferred:              11.49 MB
Response time:                  0.08 secs
Transaction rate:            1268.78 trans/sec
Throughput:                     0.19 MB/sec
Concurrency:                   99.45
Successful transactions:       75746
Failed transactions:               0
Longest transaction:            0.15
Shortest transaction:           0.00
```

