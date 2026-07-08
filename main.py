class Request:
    def __init__(self, data):
        

        self.ip = data[0]
        self.user_name = data[1]
        self.auth_user_name = data[2]

        self.time = " ".join([data[3], data[4]])

        self.method = data[5]
        self.resource = data[6]
        self.version = data[7]

        self.status_code = data[8]
        self.response_size = data[9]

class IP:
    def __init__(self,addr):
        self.ip = addr
        self.t_attempts= 0
        self.success_attempts = 0
        self.failed_attempts = 0
        self.not_found = 0 
        self.flagged = False




def data_retrieval():
    #data being seprated and obj creation
    with open("sample_access.log","r") as file:
        for line in file:
            data = line.split(" ")
            log = Request(data)

            
            
                
            if log.ip not in ip_data:
                ip_obj = IP(log.ip)
                stats(ip_obj,log.status_code)
                ip_data[log.ip] = ip_obj

            else:
                ip_obj = ip_data[log.ip]
                stats(ip_obj,log.status_code)

def stats(ip_obj,log):
    ip_obj.t_attempts += 1
    if log == "200":
        ip_obj.success_attempts += 1
    elif log == "401":
        ip_obj.failed_attempts += 1
    elif log == "404":
        ip_obj.not_found += 1

    
def analysis():
    # 0 - ip address
    # 1 - user_name
    # 2 - auth_user_name
    # 3 - time
    # 4 - method
    # 5 - resource
    # 6 - version
    # 7 - status_code
    # 8 - response_data

    risk_score = 0
    brute_force = 5
    for ip,obj in ip_data.items():
        if obj.failed_attempts >5:# brute force detection 
            obj.flagged = True
            risk_score += 20

        
    pass

def main():
    for i,obj in ip_data.items():
        if obj.flagged:
            print(i)
    pass


ip_data = {}
data_retrieval()
main()