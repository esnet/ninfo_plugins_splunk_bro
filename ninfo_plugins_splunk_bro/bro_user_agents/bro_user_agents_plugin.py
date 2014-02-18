from ninfo.helpers.splunk import SplunkBase
class useragents(SplunkBase):
    """This plugin returns recently seen user-agents as detected by Bro for this IP"""

    name = "bro_user_agents"
    title = "Recent User Agents"
    description = "Recently seen HTTP User Agents"
    types  = ['ip','ip6']
    TEMPLATE = "hoursago=48 source=*software.log* %s | dedup unparsed_version | fields unparsed_version"

plugin_class = useragents
