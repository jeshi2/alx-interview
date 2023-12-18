#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys


def print_stats(total_size, status_codes):
    """print stats"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """line parsing"""
    try:
        elements = line.split()
        status_code = int(elements[-2])
        file_size = int(elements[-1])

        """Check if status code is one of the specified values"""
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

        total_size += file_size
    except (ValueError, IndexError):
        """Ignore lines that do not match the specified format"""
        pass

    return total_size, status_codes


def main():
    """call"""
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(
                line.strip(), total_size, status_codes)
            line_count += 1

            """Print stats every 10 lines"""
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        """Handle KeyboardInterrupt (Ctrl+C)"""
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
