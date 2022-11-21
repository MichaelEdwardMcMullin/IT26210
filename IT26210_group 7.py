import re

from socket import socket

from requests import get

import socket



import colorama

from colorama import Fore, Back, Style

colorama.init(autoreset=True)



#Parameters for checking what type of IP is being used

V4 = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

V6 = "^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"



#get user's hostname

hNm = socket.gethostname()

print("\nGreetings, " + hNm + "!\n")



cntU = True



#Begin loop

while cntU:



    #asks user for their ip address or other's ip address

    print(Fore.YELLOW + "Whose IP address do you wish to look up?\n")

    print(Fore.MAGENTA + "1 - My IP address\n")

    print(Fore.MAGENTA + "2 - Other's IP address\n")

    uIn = input(Fore.GREEN + "Choice: ")

    

    if(uIn == '1'):

        #gets host's ip address and inputs it as "ip_address"

        ip_address = get('https://api.ipify.org').content.decode('utf8')

    elif(uIn == '2'):

        #User input for ip address

        ip_address = input(Fore.GREEN + "Enter IP Address: ")

    else:

        print(Fore.RED + "Invalid Option!")



    #Define the check function

    #note: uses api from ipapi.co

    def check(Ip,chc):

        if(re.search(V4, Ip)):

            if(chc == '1'):

                #if user chose 1 earlier, it outputs local ip too

                print(Fore.CYAN + 'Local IP Address: ' + socket.gethostbyname(hNm))

                print(Fore.CYAN + 'Public IP Address: ' + ip_address)

            elif(chc == '2'):

                print(Fore.CYAN + 'IP Address: ' + ip_address)

            print(Fore.CYAN + 'Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)

            print(Fore.CYAN + 'City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)

            print(Fore.CYAN + 'Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)

            print(Fore.CYAN + 'ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)

            print(Fore.CYAN + 'ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)

        elif(re.search(V6, Ip)):

            if(chc == '1'):

                #if user chose 1 earlier, it outputs local ip too

                print(Fore.CYAN + 'Local IP Address: ' + socket.gethostbyname(hNm))

                print(Fore.CYAN + 'Public IP Address: ' + ip_address)

            elif(chc == '2'):

                print(Fore.CYAN + 'IP Address: ' + ip_address)

            print(Fore.CYAN + 'Country: ' + get('https://ipapi.co/'+ip_address+'/country_name/').text)

            print(Fore.CYAN + 'City: ' + get('https://ipapi.co/'+ip_address+'/city/').text)

            print(Fore.CYAN + 'Geolocation: ' + get('https://ipapi.co/'+ip_address+'/latlong/').text)

            print(Fore.CYAN + 'ASN: ' + get('https://ipapi.co/'+ip_address+'/asn/').text)

            print(Fore.CYAN + 'ORG: ' + get('https://ipapi.co/'+ip_address+'/org/').text)

        else:

            print(Fore.RED + "Invalid IP address")



    #Checking and printing the ip address and details ref. to V4/V6 parameters 

    if __name__ == '__main__' :

        print(Fore.YELLOW + "\nDetails:")

        check(ip_address,uIn)



    #Ask user if they want to loop program

        rst = True

        while rst:

            

            rst = input(Fore.YELLOW + "\nDo you want to try again?[Y/N]: ")

            print(" ")

            

            if rst == 'Y' or rst == 'y':

                break

            elif rst == 'n' or rst == 'N':

                cntU = False

                break

            else:

                print(Fore.RED + "Error! Please Try Again.")

                rst

