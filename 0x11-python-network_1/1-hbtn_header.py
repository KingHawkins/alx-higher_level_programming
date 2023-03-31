#!/usr/bin/python3
"""sends a request to a url and displays the value"""
import urllib.request
import sys

if __name__ == '__main__':
    form = '{}'.format(sys.argv[1])
    with urllib.request.urlopen(form) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
