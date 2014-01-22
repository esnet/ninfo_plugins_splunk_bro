from ninfo.helpers.splunk import SplunkBase
class dhcp(SplunkBase):
    """This plugin returns recently seen entries from the Bro DHCP Log"""

    name = "bro_dhcp"
    title = "Bro DHCP"
    description = "Entries from the Bro DHCP Log"
    types  = ['ip','mac']
    TEMPLATE = "hoursago=48 source=*dhcp.log %s | dedup mac assigned_ip | fields  mac assigned_ip | rename assigned_ip to ip"
    remote = False

    def get_macs_for_ip(self, ip):
        ret = self.get_info(ip)
        macs = [x['mac'] for x in ret['events']]
        return macs

    def get_ips_for_mac(self, mac):
        ret = self.get_info(mac)
        ips = [x['ip'] for x in ret['events']]
        return ips

    converters = {
        ('ip',  'mac'): "get_macs_for_ip",
        ('mac', 'ip'):  "get_ips_for_mac",
    }

plugin_class = dhcp
