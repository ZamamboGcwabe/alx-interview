#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

def print_stats():
    """ Print the statistics """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate line length and the status code
        if len(parts) < 7:
            continue

        # Extract file size and status code
        try:
            size = int(parts[-1])
            code = parts[-2]
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
        except ValueError:
            continue

        # Print every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
