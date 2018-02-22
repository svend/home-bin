#!/usr/bin/env python3

import argparse
import fileinput
import ipaddress
import sys


def sort_ips(ips):
    def sortfn(s):
        return ipaddress.ip_address(s.strip())
    return sorted(ips, key=sortfn)


def run(*, files=None):
    lines = sort_ips(fileinput.input(files=files))
    print(''.join(lines), end='')


def parse_args():
    parser = argparse.ArgumentParser(description='Sort IP addresses')
    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        help='files to read, if empty, stdin is used')
    return parser.parse_args()


def args_to_dict(args):
    '''Return a dictionary containing args that were set.'''
    return {k: v for (k, v) in vars(args).items() if v}


if __name__ == '__main__':
    args = parse_args()
    sys.exit(run(**args_to_dict(args)))
