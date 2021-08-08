spam_ip = []
set_api = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as read_file:
    list_logs = (list(read_file.read().split('\n')))
    for i in range(len(list_logs) - 1):
        remote_addr = (list_logs[i].split(' - - ')[0])
        spam_ip.append(remote_addr)
    for i in set(spam_ip):
        set_api[i] = spam_ip.count(i)
    print(max(set_api.values()))
    for k, v in set_api.items():
        if v == max(set_api.values()):
            print(k)
