#!/usr/bin/env python
from datetime import datetime
from netmiko import ConnectHandler
import os.path

#Main menu function
def main_menu():
    print(30 * "-","Menu",30 * "-" )
    print("1. Download Current Config")
    print("2. Quit")
    print(60 * "_")
    
command1 = 'show run'
command2 = 'sh run | i hostname'

#connect to cisco and get config
def get_cisco_config(command,IP):
    CONN = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': '',
        'password': '',
        'timeout': 20
        }
    with ConnectHandler(**CONN) as conn:
        conn.enable()
        sample_config = conn.send_command(command)
        conn.disconnect()
        return sample_config


#Loop the menu until it is quit is selected
loop = True
while loop:
    main_menu()
    try:
        choice = int(input("What do you want to do?: [1-2]"))
    except ValueError:
        print("Oops you have entered an invalid number.")
        continue
         
    if choice == 1:
        print("starting backup...")
        RIP=str(input ("enter ip of device - "))
        hostname = ((get_cisco_config(command2,RIP)).split()[1])
        sh_run = get_cisco_config(command1,RIP)
        date = datetime.today().strftime('%d%m%y-%H%M')
        filename=open("./backup-"+str(hostname)+"-"+str(date)+".txt","w")
        rec = filename.write(sh_run)
        filename.close()
        print("backup finished")
    elif choice == 2:
        loop = False
    else:
        print("Invalid choice selected")

