class Request:
    def __init__(self, data):
        

        self.ip = data[0]
        self.user_name = data[1]
        self.auth_user_name = data[2]

        self.time = " ".join([data[3], data[4]])

        self.method = data[5].strip('"').strip("'").strip(" ")
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
        self.detection = []
        self.brute_force = False
        self.reconnaissance = False
        self.suspicious_resources = {}
        self.method_abuse = False
        self.suspicious_methods = {}
        self.risk = 0

