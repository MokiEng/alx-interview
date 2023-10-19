#!/usr/bin/python3
""" log parsing's module."""
import sys
import re


def extract_input(input_line):
    """parse sections of a line from an HTTP request log,
    and it returns a dictionary containing specific pieces 
    of information extracted from that log line.
    """
    pa = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(pa[0], pa[1], pa[2], pa[3], pa[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log."""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """update and maintain metrics based on the information extracted 
    from an HTTP request log line.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """a function processes lines from an HTTP request log."""
    line_num = 0
    total_file_size = 0
    status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_counts,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_counts)


if __name__ == '__main__':
    run()
