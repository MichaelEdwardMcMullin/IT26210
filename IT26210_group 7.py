import re
from requests import get

#Parameters for checking what type of IP is being used
V4 = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
V6 = "^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

cntU = True

#Begin loop
while cntU:

    #User input for ip address
    ip_address = input("Enter IP Address: ")

    #Define the check function
    #note: uses api from ipapi.co
    def check(Ip):
        if(re.search(V4, Ip)):
            print("\nDetails")
            print('IP Address: ' + ip_address)
            print('Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)
            print('City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)
            print('ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)
            print('ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)
        elif(re.search(V6, Ip)):
            print("\nDetails")
            print('IP Address: ' + ip_address)
            print('Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)
            print('City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)
            print('Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)
            print('ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)
            print('ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)
        else:
            print("Invalid IP address")

    #Checking the ip address ref. to V4/V6 parameters 
    if __name__ == '__main__' :
        check(ip_address)

    #Ask user if they want to loop program
        rst = True
        while rst:
            
            rst = input("\nDo you want to try again?[Y/N]: ")
            print(" ")
            
            if rst == 'Y' or rst == 'y':
                break
            elif rst == 'n' or rst == 'N':
                cntU = False
                break
            else:
                print("Error! Please Try Again.")
                rst
