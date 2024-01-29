#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


if __name__ == "__main__":
    req = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as response:
        res = response.read()

        print('Body response:')
        print('\t- type:', type(res))
        print("\t- content:", res)
        print('\t- utf8 content:', res.decode('utf-8'))
