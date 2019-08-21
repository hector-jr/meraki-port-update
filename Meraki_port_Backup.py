import requests
import json
import time
import os

#Saves files will save to your current working directory
## Enter the switch serial number you wish to a list port configuration for and your Meraki APIk key
### serial number of the switch needed to get switch port list
serialNum = input("*Enter Switch Serial Number: ")
apiKey = input("*Enter API key: ")
date = time.strftime("%m-%d-%Y_%Hhr%Mm")
cwd = os.getcwd() # gets the current working directory


url = "https://api.meraki.com/api/v0/devices/{0}/switchPorts".format(str(serialNum))
payload = ""
headers = {
    'X-Cisco-Meraki-API-Key': "{0}".format(str(apiKey)),
    'Content-Type':"application/json"
    }

# Leverage requests to get Switch port Congifs from specified switch
## Url specifies which switch to get configs from by serialNum
response = requests.request("GET",url, data=payload, headers=headers)

# validates if GET request was successful or not
## if not prints out status code, suggested W3C website for troubleshoot and raise status
if response.status_code != 200:
    print("Request status: " + str(response.status_code))
    print("Reference W3C documentation or additional status code troubleshooting at https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html")
    print(response.raise_for_status())
else:
    # Saves two files as .json: one Restore and one Update for editing
    with open('Restore_{0}_{1}.json'.format(str(serialNum),str(date)), 'w') as file:
        json.dump(response.json(), file, indent=4)
        file.close()
    print("Restore_{0}_{1}.json ".format(str(serialNum),str(date)) + "was saved to " + cwd)

    with open('Update_{0}.json'.format(str(serialNum)), 'w') as file:
        json.dump(response.json(), file, indent=4)
        file.close()
    print("Update_{0}.json ".format(str(serialNum)) + "was saved to " + cwd)

