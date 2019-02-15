# Simple Example of calling REST API from Python
# This is all that is required to call a REST API from python

# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->


# import requests library
import requests

#import json library
import json

controller='sandboxapic.cisco.com'
#controller='devnetapi.cisco.com/sandbox/apic_em'


# put the ip address or dns of your apic-em controller in this url
url = "https://" + controller + "/api/v1/ticket"

#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#convert response to json format
r_json=response.json()

print(r_json)
#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://sandboxapic.cisco.com/api/v1/host"

#Content type must be included in the header as well as the ticket
header = {"content-type": "application/json", "X-Auth-Token":"ST-112-UcRk2hJkrYVlylTVgEmq-cas"}

# this statement performs a GET on the specified host url
response = requests.get(url, headers=header, verify=False)

# json.dumps serializes the json into a string and allows us to
# print the response in a 'pretty' format with indentation etc.
#print ("Hosts = ")
print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()
d={}
for item in r_resp['response']:
	#print(item)
	d[(item["connectedNetworkDeviceId"],item["hostIp"])]=item["hostMac"]  #as all the three responce doesnot have hostname i took networkid of devices
print(d)
