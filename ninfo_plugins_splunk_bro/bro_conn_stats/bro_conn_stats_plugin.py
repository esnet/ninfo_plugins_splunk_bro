from ninfo.helpers.splunk import SplunkBase

class bro_conn_stats(SplunkBase):
    """This plugin returns Bro connection stats information from splunk"""

    name = "bro_conn_stats"
    title = "Bro connection stats"
    description = "Bro connection status from splunk"
    types  = ['ip','ip6']
    TEMPLATE = 'hoursago=4 source="*conn.log" %s | timechart span=20m count'

    def get_info(self, arg):
        query = self.TEMPLATE % arg
        events = self.do_search(query)
        times = {}
        for e in events:
            time = e['_time'].split(".")[0]
            times[time] = int(e['count'])
        times = list(sorted(times.items()))
        return {'times': times}

plugin_class = bro_conn_stats
