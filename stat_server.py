from statsd import StatsClient

statsd  = StatsClient(host = 'localhost',
                      port = 8125,
                      prefix = None,
                      maxudpsize = 512)

def users_stat():
    statsd.incr('impressions', count=1)

def status_stat(status_code):
    statsd.incr('status_code.{}'.format(status_code), count=1)
