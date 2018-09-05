from distutils.core import setup
from setuptools import find_packages

setup(name='ninfo-plugins-splunk-bro',
    version='0.1.0',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.3.0",
    ],
    entry_points = {
        'ninfo.plugin': [
            'bro_user_agents = ninfo_plugins_splunk_bro.bro_user_agents.bro_user_agents_plugin',
            'bro_notice  = ninfo_plugins_splunk_bro.bro_notice.bro_notice_plugin',
            'bro_conn_stats  = ninfo_plugins_splunk_bro.bro_conn_stats.bro_conn_stats_plugin',
            'bro_dhcp  = ninfo_plugins_splunk_bro.bro_dhcp.bro_dhcp_plugin',
        ]
    }
)
