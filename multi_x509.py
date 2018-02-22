#!/usr/bin/env python3

import argparse
import subprocess
import sys

COMMAND = ['cat']


def certs(iterator):
    '''Yield certificates from iterator.'''
    BEGIN = '-----BEGIN'
    END = '-----END'

    it = iter(iterator)
    cert_lines = []
    for line in it:
        if line.startswith(BEGIN) or cert_lines:
            cert_lines.append(line)
            if line.startswith(END):
                yield ''.join(cert_lines)
                cert_lines = []


def run(command, after=None):
    '''Run command.'''
    for cert in certs(sys.stdin):
        subprocess.run(command, input=str.encode(cert))
        if after is not None:
            print(after)


def parse_args():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] [command]',
        description='''Read certificates from stdin and run command on each
        one. Default command is `{}`. '''.format(' '.join(COMMAND)),
        argument_default=argparse.SUPPRESS
    )
    parser.add_argument(
        '--after', help='string to print after each result')
    return parser.parse_known_args()


if __name__ == '__main__':
    (args, command) = parse_args()
    sys.exit(run(command=command or COMMAND, **vars(args)))
