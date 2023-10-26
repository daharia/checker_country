import requests, sys

def devide_chunks(l: [str]) -> [str]:
    CHUNK = 20
    for i in range(0, len(l), CHUNK):
        yield l[i:i + CHUNK]


def check(ips_in: [str]) -> [str]:
    ''' Receives a list of ips, returns a list of ip:geo. '''
    ips_out = []

    ips_len = len(ips_in)
    print('Len of list ips:', ips_len)

    for ips in devide_chunks(ips_in):
        url = f'https://get.geojs.io/v1/ip/country?ip=' + ','.join(ips)

        ret = requests.get(url)
        if ret.status_code != 200:
            geo = []
            for ip in ips:
                geo.append(ip + ':ERROR' )
        else:
            geo = ret.text.split('\n')
        
        ips_out.append(geo[:-1])

    return ips_out

def main():
    if len(sys.argv) != 3:
        print('Use: python main.py input_ip.txt output_ip.txt')
        exit(1)
    
    ips = []

    # Separate the ip:port lines and make a list [['ip', 'port'],...]
    with open(sys.argv[1]) as f:
        from re import findall

        data = f.read()

        ips = findall(r'\b(?:[1-2]?[0-9]{1,2}\.){3}[1-2]?[0-9]{1,2}\:(?:[0-9]){1,5}\b', data)
    
    ip = [ip_port.split(':')[0] for ip_port in ips]
    ip_geos = check(ip)

    with open(sys.argv[2], 'w') as f:
        for ip_geo in ip_geos:
            port = [ip_port.split(':')[1] for ip_port in ips]
            geo = [geo.split(':')[1] for geo in ip_geo]

            for i in range(len(ip_geo)):
                f.write(f'{ip[i]}:{port[i]} {geo[i]}\n')

if __name__ == '__main__':
    main()