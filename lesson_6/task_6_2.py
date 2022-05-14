lst_logs = []
lst_spamers = []
lst_max_spamer = []
count_ip_max = 0
with open("nginx_logs.txt",'r',encoding="utf-8") as f:
    for line in f:
        lst_logs.append(line.split()[0])
    set_logs = set(lst_logs)
    for ip in set_logs:
        count_ip = lst_logs.count(ip)
        if count_ip > count_ip_max:
            spamer = ip,count_ip
            lst_spamers.append(spamer)
            count_ip_max = count_ip
        elif count_ip == count_ip_max:
            spamer = ip, count_ip
            lst_spamers.append(spamer)
    for ip,count in lst_spamers:
        if count == count_ip_max:
            spamer = ip,count
            lst_max_spamer.append(spamer)


print(spamer)