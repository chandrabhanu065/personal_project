from curses.ascii import isdigit


def valid_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

if __name__ == "__main__":
    ip = '10.10.0.500'
    result = valid_ip(ip)
    if result:
        print('{} is valid ip address'.format(ip))
    else:
        print('{} is not valid ip address'.format(ip))
