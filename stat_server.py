from statsd import StatsClient

def users_stat():
    statsd  = StatsClient(host = 'localhost',
                          port = 8125,
                          prefix = None,
                          maxudpsize = 512)

    statsd.incr('people', count=1)
