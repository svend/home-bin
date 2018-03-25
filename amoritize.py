#!/usr/bin/env python3

import argparse
import sys
from itertools import islice


def montly_pi(*, amount, rate, years):
    n = years * 12
    r = rate / 12
    pi = (r * amount * (1 + r) ** n) / ((1 + r) ** n - 1)
    return pi


def amoritize(*, amount, rate, years):
    pi = montly_pi(amount=amount, rate=rate, years=years)
    while True:
        interest = amount * rate / 12
        principal = pi - interest
        amount -= principal
        if amount > 0:
            yield amount, principal, interest
        else:
            break


def run(*, amount, rate, years):
    am = amoritize(amount=amount, rate=rate / 100, years=years)

    fields = ['amount', 'principal', 'interest', 'PI']
    print(f'{"mo":>3}', *[f'{v:>9}' for v in fields])
    for month, (amount, principal, interest) in islice(enumerate(am), None, None, 1):
        pi = principal + interest
        fields = [f'{v:>9.2f}'
                  for v in (amount, principal, interest, pi)]
        print(f'{month + 1:>3}', *fields)


def parse_args():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] [command]',
        description='''Print amorization table''',
        argument_default=argparse.SUPPRESS)
    parser.add_argument(
        '--amount', help='loan ammount',
        type=int, required=True)
    parser.add_argument(
        '--rate', help='interest rate as percentage',
        type=float, required=True)
    parser.add_argument(
        '--years', help='loan period in years',
        type=int, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    sys.exit(run(**vars(args)))
