from parser import data_retrieval
from models import Request,IP


# 0 - ip address
# 1 - user_name
# 2 - auth_user_name
# 3 - time
# 4 - method
# 5 - resource
# 6 - version
# 7 - status_code
# 8 - response_data


def Brute_Force(ip_data):
    brute_force = 5
    for ip,obj in ip_data.items():
        
        if obj.failed_attempts >brute_force:
            obj.brute_force = True
            obj.flagged = True
            obj.risk += 20

            
def Recon(logs,ip_data):
    suspicious_resources = ["/admin","/phpmyadmin","/wp-admin","/.env","/config.php","/backup.zip","/server-status","/login","/dashboard"]
    
    for log in logs:
        obj = ip_data[log.ip]
        if log.resource in suspicious_resources:
            try:
                obj.suspicious_resources[log.resource] += 1
            except KeyError:
                obj.suspicious_resources[log.resource] = 1


    for ip,obj in ip_data.items():
        count = len(obj.suspicious_resources)
        if count > 4:
            obj.reconnaissance = True
            obj.flagged = True
            obj.risk += 20

            
    
logs , ip_data = data_retrieval()
