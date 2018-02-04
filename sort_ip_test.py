import ipaddress
import random

import sort_ip


def gen_sorted_ips():
    MAX_IP = 2**32
    ints = sorted([random.randrange(0, MAX_IP) for _ in range(10)])
    return [str(ipaddress.ip_address(i)) for i in ints]


def test_sort_ips():
    sorted_ips = gen_sorted_ips()
    random_ips = random.sample(sorted_ips, k=len(sorted_ips))
    assert sort_ip.sort_ips(random_ips) == sorted_ips
