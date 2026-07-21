from .parser import data_retrieval,file_checker
from .detection import Brute_Force,Recon,method_abuse
from .models import Request,IP
from .ui import display_banner,get_log_path,display_security_alert,display_log_summary
def main():

    display_banner()

    path = file_checker(get_log_path())
    logs,ip_data,valid,non_valid = data_retrieval(path)

    display_log_summary(valid,non_valid)
    Brute_Force(ip_data)
    Recon(logs,ip_data)
    method_abuse(logs,ip_data)


    for ip,obj in ip_data.items():
        if obj.flagged:
            display_security_alert(ip,obj)

    



if __name__ == "__main__":
    main()
