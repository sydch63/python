import re

def parsed_raw(raw_str):
    try:
        with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
            str_file = f.read()
            parse_ip = re.findall("(\d{1,3}\.\d{1,3}\.+\d{1,3}\.\d{1,3})\s",str_file)
            parse_ipv6 = re.findall("((?:([a-f0-9]){1,4}:?|::){8})\s-",str_file)
            print(f"Длина списка всех IP-адресов: {len(set(parse_ip))+len(set(parse_ipv6))}")
        parse_str = re.findall( "(\d{1,3}\.\d{1,3}\.+\d{1,3}\.\d{1,3}).+\[(\d+\/\w+\/\d+:\d+:\d+:\d+.+)\].+\"(\w+).(\/\w+\/\w+)\s\S+.(\d+).(\d+)", raw_str)
        if parse_str != []:
            return parse_str[0]
    except ValueError as exc:
        raise ValueError((f"wrong str: {raw_str}"))  from exc
    except IndexError as exc:
        raise ValueError((f"wrong str: {raw_str}"))  from exc
# продумать исключения
print(parsed_raw('144.92.16.161 - - [17/May/2015:12:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'))


