import requests, sys

def check(ips: [str]) -> [str]:
    ''' Receives a list of ips, returns a list of ips with geo. '''
    ips_out = []

    ips_len = len(ips)
    print('Len of list ips:', ips_len)

    for ip in ips:
        url = f'https://get.geojs.io/v1/ip/country?ip={ip}'

        ret = requests.get(url)
        if ret.status_code != 200:
            geo = 'ERROR'
        else:
            geo = ret.text.split(' ')[1]

        ips_out.append(geo)

    return ips_out

def main():
    if len(sys.argv) != 3:
        print('Use: python main.py input_ip.txt output_ip.txt')
        exit(1)
    
    ips = []
    with open(sys.argv[1]) as f:
        for ip in f.readlines():
            if ip[0] == ' ':
                ip = ip[1:]
            if ip[-1] == '\n':
                ip = ip[:-1]

            ip = ip.split(':')
            if len(ip) < 2:
                ip.append('0')

            ips.append(ip)
    
    geo = check([f for f,_ in ips])

    with open(sys.argv[2], 'w') as f:
        for i in range(len(ips)):
            f.write(f'{ips[i][0]}:{ips[i][1]} {geo[i]}')

if __name__ == '__main__':
    main()