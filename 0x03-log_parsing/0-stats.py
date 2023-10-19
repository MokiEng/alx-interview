#!/usr/bin/python3
""" log parsing's module."""

import sys
import re


def parse_log_line(line):
    """ a script that reads stdin line by line and computes metrics.
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \
                [.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        ip, status_code, file_size = match.groups()
        return (int(status_code), int(file_size))
    else:
        return None


def main():
    """parses the input according to the specified format.
    """
    line_count = 0
    total_size = 0
    stat_ct = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_log_line(line)
            if parsed:
                stat_ct, file_size = parsed
                total_size += file_size
                stat_ct[stat_ct] += 1

            line_count += 1
            if line_count == 10:
                print(f"Total file size: {total_size}")
                for code, count in sorted(stat_ct.items()):
                    if count > 0:
                        print(f"{code}: {count}")
                line_count = 0

    except KeyboardInterrupt:
        print(f"Total file size: {total_size}")
        for code, count in sorted(stat_ct.items()):
            if count > 0:
                print(f"{code}: {count}")


if __name__ == '__main__':
    main()
