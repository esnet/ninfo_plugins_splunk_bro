from ninfo.helpers.splunk import SplunkBase

class bro_conn_stats(SplunkBase):
    """This plugin returns Bro connection stats information from splunk"""

    name = "bro_conn_stats"
    title = "Bro connection stats"
    description = "Bro connection status from splunk"
    types  = ['ip','ip6']
    TEMPLATE = 'daysago=7 source="*conn.log" %s | timechart span=1d count'

    def get_info(self, arg):
        query = self.TEMPLATE % arg
        events = self.do_search(query)
        days = {}
        for e in events:
            day = e['_time'].split()[0]
            days[day] = int(e['count'])
        days = list(sorted(days.items()))
        return {'days': days}

plugin_class = bro_conn_stats
