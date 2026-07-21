from parser import data_retrieval




def Brute_Force(ip_data):
    for ip,obj in ip_data.items():
        brute_force = 5
        if obj.failed_attempts >brute_force:
            obj.detection.append("Brute Force")
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
        local_risk = 0
        count = len(obj.suspicious_resources)
        ratio = (obj.not_found/obj.t_attempts)*100
        if count > 4:
            local_risk += 20

        if ratio > 80:
            local_risk += 30
        elif ratio > 60:
            local_risk += 10
        elif ratio > 35:
            local_risk += 5
        
        if local_risk >= 20:
            obj.detection.append("Reconnaissance")
            obj.reconnaissance = True
            obj.flagged = True

        obj.risk += local_risk
    
def method_abuse(logs,ip_data):
    allowed_methods = ["GET","POST"]
    
    for log in logs:
        obj = ip_data[log.ip]

        if log.method not in allowed_methods:
            if log.method in obj.suspicious_methods:
                obj.suspicious_methods[log.method] += 1
            else:
                obj.suspicious_methods[log.method] = 1
            obj.method_abuse = True
            obj.flagged = True
            if "Method Abuse" in obj.detection:
                continue
            else:
                obj.detection.append("Method Abuse")
        else:
            continue

        