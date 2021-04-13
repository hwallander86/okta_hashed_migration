import requests
import base64
import hashlib
import json
import uuid

## Hashed Password Migration w/o Salt Example 

# Enter API Token from Okta tenant: https://developer.okta.com/docs/guides/create-an-api-token/overview/
API_Token = "API TOKEN"

# Enter your okta url
# Okta Url Format: subdomain.okta.com
okta_url = "subdomain.okta.com"
query_url = "https://" + okta_url + "/api/v1/users"
print (type(query_url))

querystring = {"activate":"true"}

# Example password, can be changed
password = "TestPw123"
print ("password - plain text: " + password)

print ("")
print ("")


# SHA 512 Hashed + B64 Encoded
pw_b64 = base64.b64encode(hashlib.sha512(password).digest())
print ("sha512 password - base64 encrypted: " + pw_b64)

print ("")

payload = {
	"profile": {
		"firstName": "Isaac",
		"lastName": "Brock",
		"email": "isaac@willywonkta.com",
		"login": "isaac@willywonkta.com"
	},
	"credentials": {
		"password" : {  "hash": {
						"algorithm": "SHA-512",
						"value": "%s" % pw_b64
			} }
	}
} 


payload = json.dumps(payload)
print (payload)
print (type(payload))
print (" ")

stop

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "SSWS " + API_Token
    }


response = requests.request("POST", query_url, data=str(payload), headers=headers, params=querystring)

print(response.text)