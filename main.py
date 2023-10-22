import json, requests, sys

def check(ips: [str]) -> [str]:
    ''' Receives a list of ips, returns a list of ips with geo. '''
    ips_out = []
    ips_prepair = [[]]
    
    ips_len = len(ips)
    print('Len of list ips:', ips_len)

    # Finding the middle variable for dividing a list of ips
    ips_len += 0 if ips_len % 2 == 0 else 1 # 
    x = 15
    while ips_len % x != 0:
        x += 1

    # Making a new list
    i = 0
    j = 0
    for ip in ips:
        if i > x:
            j += 1
            i = 0
            ips_prepair.append([])

        ips_prepair[j].append(ip)
        i += 1
    
    datas = []
    for ips in ips_prepair:
        print('Ips prepair:', len(ips))
        req = ','.join(ips)
        url = f'https://get.geojs.io/v1/ip/country?ip={req}'
        
        ret = requests.get(url)
        if ret.status_code != 200:
            print(ret.status_code)
            return ips_out
        print(ret.text)
        break
        data = json.dump(ret.text)
        datas.append(data)

    return ips_out

def main():
    if len(sys.argv) != 2:
        print('Use: py main.py ip')
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

if __name__ == '__main__':
    main()