#A python script to retrieve APC Smart PDU's statistics, Using SNMPV1. Get KWh usage, port status and other cool stuf.
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902
from pysnmp.hlapi import *

#Retrieve APC PDU info to connect

print(" ")
print ("Welkom to the APC Smart PDU control tool")
print ("-" * 41)

ip = input("Enter the APC PDU ip address: ")
port = input("Enter the APC PDU SNMP port: ")
community_name = input("Enter Cummunity name: ")

#Option menu 

i = 0
while i <= 10:  
        print(" ")
        print("APC Control options")
        print ("-" * 20)

        def menu():
            print("[1] Get device info")
            print("[2] Get current device load (Watts)")
            print("[3] Get current device load (Amp)")
            print("[4] Get device hostname")
            print("[5] Get device outlet status")

        menu()
        print ("       ")
        option = input("Enter your option: ")
        print(" ")

#Get system info

        if option == "1":
        
            iterator = getCmd(
            SnmpEngine(),
            CommunityData(community_name, mpModel=0),
            UdpTransportTarget((ip, port)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
            )

            errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

            if errorIndication:
                print(errorIndication)

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

            else:
                for varBind in varBinds:
                    print(' = '.join([x.prettyPrint() for x in varBind]))
                
#Get current Kwh load

        elif option == "2":
            print ("       ")
            result = nextCmd(
                SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ip, port)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.4.1.318.1.1.12.1.16')),
                lookupMib=True, lookupValues=True
                )

            errorIndication, errorStatus, errorIndex, varBinds = next(result)

            if errorIndication:
                print(errorIndication)

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

            else:
                for varBind in varBinds:
                 print('Device load (Watts) : ',' = '.join([x.prettyPrint() for x in varBind]),'watts')

#Get current Amp load
                
        elif option == "3":
            print ("       ")
            result = nextCmd(
                SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ip, port)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.4.1.318.1.1.26.6.3.1.5')),
                lookupMib=True, lookupValues=True
                )

            errorIndication, errorStatus, errorIndex, varBinds = next(result)

            if errorIndication:
                print(errorIndication)

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

            else:
                for varBind in varBinds:
                 print('Device load (Amp) : ',' = '.join([x.prettyPrint() for x in varBind]), 'Amp')

#Get device hostname

        elif option == "4":
            print ("       ")
            result = nextCmd(
                SnmpEngine(),
                CommunityData(community_name, mpModel=0),
                UdpTransportTarget((ip, port)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.4.1.318.1.1.12.1.1')),
                lookupMib=True, lookupValues=True
                )

            errorIndication, errorStatus, errorIndex, varBinds = next(result)

            if errorIndication:
                print(errorIndication)

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

            else:
                for varBind in varBinds:
                 print('Device hostname : ',' = '.join([x.prettyPrint() for x in varBind]))

#Get outlet status 
        
        elif option == "5": 
            from pysnmp.entity.rfc3413.oneliner import cmdgen  

            print(" ")
            print("-" * 10, ip ,"-" * 10)
            print(" ")
                
            outlet_state = {1:'ON',2:'OFF',4:'UNKNOWN'}
            outlets = dict(zip(range(1,9),[4]*8))
            for outlet in range(1,25):
                errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
                    cmdgen.CommunityData('my-agent', community_name , 0), 
                    cmdgen.UdpTransportTarget((ip, port)),
                        (1,3,6,1,4,1,318,1,1,4,4,2,1,3,outlet))

                if len(varBinds) == 0:
                    print(ip + " is niet bereikbaar")
                    break

                outlets[outlet] = varBinds[0][1]
                print (ip,' ','outlet-',outlet,' ',outlet_state[varBinds[0][1]])

        else:
            print("done")


print("     ")