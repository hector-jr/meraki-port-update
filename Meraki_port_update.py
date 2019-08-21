import requests
import json

# Which switch to update
serial = input("Serial Number of Switch:")
# Files need to be in json format (.json) and full path.
file= input("Json File Name:")

#totalPort = input("Number of ports on switch:")
## Total ports was hardcoded into loop

headers = {
    'X-Cisco-Meraki-API-Key': "{0}".format(str(apiKey)),
    'Content-Type': "application/json",
    }

with open(file, 'r') as data:
    jsonFile = json.load(data)
    data.close()

List = 0

print("######################### PORTS UPDATING ###################################")

for List in jsonFile:
    # Stores port number from json file into variable
    portNum = List['number']
    if(portNum > 48):
        break
    else:
        # Prints current updates being made on port/switch
        print(" Port number being updated: " + str(portNum))
        url = "https://api.meraki.com/api/v0/devices/{0}/switchPorts/{1}".format(str(serial),str(portNum))
        print(" Url applied in PUT request: " + url)
        payload = jsonFile[portNum-1] # port number -1 for json indexing
        print(" Configurations being applied")
        print(payload)
        response = requests.put(url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Request status: " + str(response.status_code))
            print("Reference W3C documentation or additional status code troubleshooting at https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html")
            print(response.raise_for_status())
        else:
            print("'PUT' status code: " + str(response.status_code))
        print("############################################################")
