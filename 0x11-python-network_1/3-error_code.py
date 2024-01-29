#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""


import sys
from urllib.request import Request, urlopen
from urllib.error import URLError
if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code:', e.code)
    else:
        print(body)
