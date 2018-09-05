"""
Optional config section:

[bro_notice]
hoursago = 48
source = *notice.log
fields = src dst note msg sub
"""

from ninfo.helpers.splunk import SplunkBase

class bro_notice(SplunkBase):
    """This plugin returns Bro notice information from splunk"""

    name = "bro_notice"
    title = "Recent Bro notices"
    description = "Recently logged bro notices from splunk"
    types  = ['ip','ip6','hostname',"username"]
    hoursago = self.config.get('bro_notice', {}).get('hoursago', "48")
    source = self.config.get('bro_notice', {}).get('source', "*notice.log")
    fields = self.config.get('bro_notice', {}).get('fields', "src dst note msg sub")
    
    TEMPLATE = 'hoursago=%s source="%s" %%s | fields %s' % (hoursago, source, fields)

plugin_class = bro_notice
