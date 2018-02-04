#!/usr/bin/env python3

import argparse
import fileinput
import ipaddress


def sort_ips(ips):
    def sortfn(s):
        return ipaddress.ip_address(s.strip())
    return sorted(ips, key=sortfn)


def run(args):
    lines = sort_ips(fileinput.input(files=args.files))
    print(''.join(lines), end='')


def parse_args():
    parser = argparse.ArgumentParser(description='Sort IP addresses')
    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        help='files to read, if empty, stdin is used')
    return parser.parse_args()


if __name__ == '__main__':
    run(parse_args())
