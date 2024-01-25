#!/usr/bin/python3
"""
Parses log lines from standard input line by line and counts the occurrences
of different HTTP status codes.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and/or a keyboard interruption (CTRL + C)
print these statistics from the beginning:

+ Total file size: File size: <total size>
  - Where <total size> is the sum of all previous <file size>
+ Number of lines by status code:
  - Possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  - If a status code doesn’t appear or is not an int, the script don’t print it
  - Format: <status code>: <number>
  - Status codes are printed in ascending order.
"""

import sys


def print_metrics(status_code_counts: dict, file_size: int) -> None:
    """ Prints the current status code counts and total file size """
    print("File size: {:d}".format(file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count:
            print("{}: {}".format(status_code, count))


def parse_log() -> None:
    """ Handles log parsing """
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in status_codes}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            log_data = line.split()

            try:
                status_code = log_data[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except (IndexError, ValueError):
                pass  # Handle invalid or incomplete log lines

            try:
                file_size += int(log_data[-1])
            except (IndexError, ValueError):
                pass  # Handle missing or invalid file size in log line

            if line_count % 10 == 0:
                print_metrics(status_code_counts, file_size)
        print_metrics(status_code_counts, file_size)

    except KeyboardInterrupt:
        print_metrics(status_code_counts, file_size)
        raise


if __name__ == "__main__":
    parse_log()
