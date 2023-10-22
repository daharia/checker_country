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
            print(ip, ret.status_code)
            continue
        
        ips_out.append(ret.text.split('\n')[0])

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
            if type(ip) == type(list):
                ip = ip[0]

            ips.append(str(ip[0]))
    
    ips = check(ips)

    with open(sys.argv[2], 'w') as f:
        for ip in ips:
            f.write(ip + '\n')

if __name__ == '__main__':
    main()