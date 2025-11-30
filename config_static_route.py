from netmiko import ConnectHandler
from getpass import getpass

username = input(' Enter your username" ')
password = getpass("Enter your password: ")

deviceinfo = int(input("Enter the number of devices that you would like to connect to: ")) ##"You can specifiy n number of device to connect to"

devicelist = [] ##"This is an empty list where the ip addresses of remote device you provide will be appended and the loop will go through those ip's"

for devices in range(0,deviceinfo):
    ip = input(f"Enter the ip address of device that you want to connect to {devices +1 }: ")
    devicelist.append(ip)


for routers in devicelist:
    device = {
        "host" : routers,
        "username" : username,
        "password" : password,
        "device_type" : "cisco_ios"
    }

    ssh = ConnectHandler(**device)
    print(f"connection to device {routers} is succesful... ")

    routecount = int(input(" Enter the number of routes you would like to add: "))
    for static in range(0,routecount):
        nwid = input("enter the network id: ")
        netmask = input('Enter the mask: ')
        hop = input("Enter the next hop: ")
        commands = [f"ip route {nwid} {netmask} {hop}"]
        staticroute = ssh.send_config_set(commands)
        print(staticroute)

        routecheck = ssh.send_command("show run | in route")
        print(routecheck)

    
    ssh.save_config() ##"To save the config when using netmiko"
    ssh.disconnect()  ##"To disconnect from the device"
