#!/usr/bin/python3
"""ends a request to the URL and displays the value of 
the X-Request-Id variable found in the header of the response"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(f"{sys.argv[1]}") as response:
        print(response.headers['X-Request-Id'])