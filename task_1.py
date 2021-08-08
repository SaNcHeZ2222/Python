with open('nginx_logs.txt', 'r', encoding='utf-8') as read_file:
    list_logs = (list(read_file.read().split('\n')))
    for i in range(len(list_logs) - 1):
        remote_addr = (list_logs[i].split(' - - ')[0])  # ip
        request_type = (list_logs[i].split('"')[1].split()[0])  # get
        requested_resource = (list_logs[i].split('"')[1].split()[1])  # downloads
        print(f'{(remote_addr, request_type, requested_resource)}')