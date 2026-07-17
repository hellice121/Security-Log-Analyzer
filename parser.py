from models import Request,IP



def data_retrieval():
    #data being seprated and obj creation
    with open("sample_access.log","r") as file:
        for line in file:
            data = line.split(" ")
            log = Request(data)
            logs.append(log)
            
                
            if log.ip not in ip_data:
                ip_obj = IP(log.ip)
                stats(ip_obj,log.status_code)
                ip_data[log.ip] = ip_obj

            else:
                ip_obj = ip_data[log.ip]
                stats(ip_obj,log.status_code)
    
    return logs,ip_data



def stats(ip_obj,log):
    ip_obj.t_attempts += 1
    if log == "200":
        ip_obj.success_attempts += 1
    elif log == "401":
        ip_obj.failed_attempts += 1
    elif log == "404":
        ip_obj.not_found += 1

    

logs = []
ip_data = {}