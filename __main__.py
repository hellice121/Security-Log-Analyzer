from parser import data_retrieval,stats
from detection import Brute_Force,Recon
from models import Request,IP

def main():
    logs,ip_data = data_retrieval()
    Brute_Force(ip_data)
    Recon(logs,ip_data)

    for ip,obj in ip_data.items():
        if obj.flagged :
            if obj.brute_force:
                print("brute force detected")
                print(f"ip : {obj.ip}")
                print(f"total attempts : {obj.t_attempts}")
                print(f"failed attempts : {obj.failed_attempts}\n\n")
                print(f"risk score : {obj.risk}")

            if obj.reconnaissance:
                print("reconnaissance detected")
                print(f"ip : {obj.ip}")
                print(f"resources accessed : \n{obj.suspicious_resources}")
                print(f"risk score : {obj.risk}")


if "__name__" == "__main__":
    main()
main()
