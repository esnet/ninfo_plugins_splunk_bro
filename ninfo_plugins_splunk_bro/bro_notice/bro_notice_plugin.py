from ninfo.helpers.splunk import SplunkBase

class bro_notice(SplunkBase):
    """This plugin returns Bro notice information from splunk"""

    name = "bro_notice"
    title = "Recent Bro notices"
    description = "Recently logged bro notices from splunk"
    types  = ['ip','ip6','hostname',"username"]
    TEMPLATE = 'hoursago=48 source="*notice.log" %s | fields src dst note msg sub'

plugin_class = bro_notice
