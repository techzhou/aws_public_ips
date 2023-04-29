#!/usr/bin/env python
import requests

proxies = {
    'https': 'http://127.0.0.1:7890',
}
ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json', proxies=proxies).json()['prefixes']
amazon_ips = [item['ip_prefix'] for item in ip_ranges if 'cn' not in item["region"]]

rules = list(map(lambda x: '  - IP-CIDR,'+x, amazon_ips))
# save to yaml file
with open('aws-ip.yaml', 'w') as f:
    f.write('payload:\n')
    f.write('\n'.join(rules))