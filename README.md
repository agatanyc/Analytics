This project defines an HTTP srever that counts number of users of given 
site.

## Dependencies

* graphite
* statsd

## Running the server

For development in seperate terminals run:

* Run carbon and graphite-web - parts of graphite
* `python /opt/graphite/bin/carbon-cache.py start`
* `python /opt/graphite/bin/run-graphite-devel-server.py /opt/graphite`
* Run statsd
* `node /opt/statsd/stats.js /opt/statsd/config.js`
* Run application `python main.py`

For testing and sending multiple requests use this command:
ab -n 10 -c 10 http://127.0.0.1:5000/page/47
