#!/usr/bin/python3
"""displays github credentials"""
from requests import get, auth
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    re = get('https://api.github.com/user',
             auth=auth.HTTPBasicAuth(user, password))
    print(re.json().get('id'))
