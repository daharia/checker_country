'''
    Application used https://www.geojs.io/docs/v1/endpoints/country/
    For test:
    https://www.countryipblocks.net/acl.php
    https://www.find-ip-address.org/ip-country/
'''

import json, requests, sys

def check(ips_in: [str]) -> [str]:
    ''' Receives a list of ips, returns a list of ips with geo. '''
    ips_out = []

    for ip in ips_in:
        pass

    return ips_out

def main():
    if len(sys.argv) < 2:
        print('Use: py main.py ip')
    

if __name__ == '__main__':
    main()