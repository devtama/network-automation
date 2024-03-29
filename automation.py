import paramiko
import os
import sys
import time
from getpass import getpass

print(sys.version)
print(sys.executable)

try:
    print("Network Automation")
    print("==================")

    while True:
        try:
            ip = input("insert ip text: ")
            r_ip = open(ip, "r").readlines()
            break
        except IOError:
            print("File not Found!")
            continue

    ip_list = []
    for x in r_ip:
        ip_list.append(x.strip())

    ip_list_ok = []
    print("\n\ncek koneksi")
    for ip in ip_list:
        response = os.system("\nping {}".format(ip))

        if response == 0:
            print(f"\n{ip} is up!")
            ip_list_ok.append(ip)
        else:
            print(f"\n{ip} is down!")

    while True:
        try:
            router = input("insert router config text: ")
            r_router = open(router, "r").readlines()
            break
        except IOError:
            print("File not found!")
            continue

    username = input("Username: ")
    password = getpass

    print("Configurating... \n")
    for ip in ip_list_ok:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname=ip,username=username,password=password)
        print(f"login to {ip} successed!")
        for config in r_router:
            ssh_client.exec_command(config)
            time.sleep(1)
        print(f"configuration to {ip} successed!")

except KeyboardInterrupt:
    print("Your program exits!")
    sys.exit()