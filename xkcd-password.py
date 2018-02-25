#!/usr/bin/env python3

import argparse
import math
import random
import re
import subprocess
import sys


ASPELL_DICT = 'en_US'
MIN_BITS = 44


def get_words():
    '''Return a word list consisting of lowercase words.'''
    only_lowercase = re.compile('[a-z]+$').match
    lines = subprocess.check_output(['aspell', 'dump', 'master', ASPELL_DICT],
                                    universal_newlines=True).splitlines()
    words = [w for w in lines if only_lowercase(w)]
    return words


def min_length(num_symbols, min_bits):
    '''Return the minimum length to satisfy min_bits.'''
    length = math.log(2 ** min_bits, num_symbols)
    return math.ceil(length)


def run(*, min_bits):
    '''Run application.'''
    words = get_words()
    length = min_length(len(words), min_bits)
    password = ' '.join(random.choice(words) for i in range(length))
    print(password)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate XKCD password',
        epilog=f'Requires aspell and {ASPELL_DICT} dictionary',
        argument_default=argparse.SUPPRESS)
    parser.add_argument(
        '--min-bits',
        help=f'minimum number bits of entropy (default {MIN_BITS})',
        default=MIN_BITS, type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    sys.exit(run(**vars(args)))
