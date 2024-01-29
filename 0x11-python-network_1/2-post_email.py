#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        body = response.read().decode('utf-8')
        print('Your email is:', email)
