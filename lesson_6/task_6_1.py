lst_logs = []

with open("nginx_logs.txt",'r',encoding="utf-8") as f:
    for line in f:
        logs_tuple = (line.split()[0],line.split()[5].replace('"',''),line.split()[6])
        lst_logs.append(logs_tuple)

print(lst_logs)