from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

router_details = {
    "host" : input("Enter the ip address of remote device: "),
    "port" : "830" , 
    "username" : input("Enter your username : "),
    "password" : getpass("Enter your password: ") ,
    "hostkey_verify" : False
}

netconf = manager.connect(**router_details)

user_input = int(input("ENter the number of interfaces you want to configure: "))

for intdetails in range(0,user_input):
    interface_type = int(input("Select the type of interface you want to configure, \n 1. loopback interface: , \n 2. Physical iterface: "))
    if interface_type ==1:
        int_type = "softwareLoopback"

    elif interface_type ==2:
        int_type = "ethernetCsmacd"

    intname = input("Enter the interface name: ")
    ip_add = input("Enter the ip: ")
    mask = input("Enter the mask: ")

    int_payload = f"""
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>{intname}</name>
          <description>Configured using NETCONF</description>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{int_type}</type>
          <enabled>true</enabled>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>{ip_add}</ip>
              <netmask>{mask}</netmask>
            </address>
          </ipv4>
        </interface>
      </interfaces>
    </config>
     """

    intconf = netconf.edit_config(int_payload, target = "running")
    print(intconf)
    