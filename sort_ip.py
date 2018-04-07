#!/usr/bin/env python3

import argparse
import fileinput
import ipaddress
import sys

from typing import Iterable, List, Optional


def sort_ips(ips: Iterable[str]) -> List[str]:
    """Return sorted list of `ips`."""

    def sortfn(s):
        return ipaddress.ip_address(s.strip())

    return sorted(ips, key=sortfn)


def run(files: Optional[List[str]] = None):
    lines = sort_ips(fileinput.input(files=files))
    print("".join(lines), end="")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sort IP addresses", argument_default=argparse.SUPPRESS
    )
    parser.add_argument(
        "files",
        help="files to read, if empty, stdin is used",
        metavar="FILE",
        nargs="*",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    sys.exit(run(**vars(args)))
