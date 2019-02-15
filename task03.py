import requests
import json

url = 'https://sandboxapicem.cisco.com/api/v1/ticket'


body = {"username":"devnetuser","password":"Cisco123!"}


header = {"content-type": "application/json"}

response= requests.post(url,data=json.dumps(body), headers=header, verify=False)

ret=response.json()
print(json.dumps(ret,indent=4))
print('=========================================================')
serviceticket=ret['response']['serviceTicket']


url = "https://sandboxapicem.cisco.com/api/v1/host"

# Include the content type and ticket in the header
header[ "X-Auth-Token"]=serviceticket

# This statement performs a GET on the specified host url
response = requests.get(url, headers=header, verify=False)

print (response)
