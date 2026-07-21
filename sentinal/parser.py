from models import Request,IP
from pathlib import Path as p


# 0 - ip address
# 1 - user_name
# 2 - auth_user_name
# 3 - time
# 4 - method
# 5 - resource
# 6 - version
# 7 - status_code
# 8 - response_data

def file_checker(path):
    if p.exists(path):
        if p.is_file(path):
            return path
        else:
            print("the file does not exist")
            
    else:
        print("path doesnt exist")
        


def data_retrieval(filepath):
    RANGE = 255
    logs = []
    ip_data = {}
    valid_logs = 0
    non_valid_logs = 0
    #data being seprated and obj creation
    with open(f"{filepath}","r") as file:
        for line in file:
            data = line.split(" ")
            #ip validation
            ip = data[0].split(".")
            
            try:
                if int(ip[0])<255 and int(ip[1])< 255 and int(ip[2]) <255 and int(ip[3]) <255:
                    valid_logs += 1
                else:
                    non_valid_logs += 1
                    continue
            except (IndexError,ValueError):
                non_valid_logs += 1
                continue

            log = Request(data)
            logs.append(log)
            
                
            if log.ip not in ip_data:
                ip_obj = IP(log.ip)
                stats(ip_obj,log.status_code)
                ip_data[log.ip] = ip_obj

            else:
                ip_obj = ip_data[log.ip]
                stats(ip_obj,log.status_code)
    
    return logs,ip_data,valid_logs,non_valid_logs


def stats(ip_obj,log):
    ip_obj.t_attempts += 1
    if log == "200":
        ip_obj.success_attempts += 1
    elif log == "401":
        ip_obj.failed_attempts += 1
    elif log == "404":
        ip_obj.not_found += 1