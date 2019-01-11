def reorderLogFiles(logs):
    ordered_log_str = []
    ordered_log_dig = []
    for i in range(0, len(logs)):
        log = logs[i]
        log_str = log.split()
        if(log_str[1].isdigit):
            ordered_log_dig.append(log)
        else:
            ordered_log_str.appen(log)
    ordered_log_dig.sort()
    ordered_log_str.sort()
    ordered_log = ordered_log_dig+ordered_log_str
    print(ordered_log)

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
reorderLogFiles(logs)

