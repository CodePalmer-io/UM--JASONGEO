import urllib.request, urllib.error,  urllib.parse
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    URL = 'http://py4e-data.dr-chuck.net/json?'
else:
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input("Enter location: ")
print(location)
print("Retrieving", URL)

parms = dict()
parms['address'] = location
# address = URL + urllib.parse.urlencode({'address': location})

if api_key is not False:
    parms['key'] = api_key
address = URL + urllib.parse.urlencode(parms)

data = urllib.request.urlopen(address, context=ctx)
retrievedData = data.read().decode()
print("Retrieved ", len(retrievedData), "characters")

js = json.loads(retrievedData)

print("Place ID: ", js["results"][0]["place_id"])


# ChIJfanN3ayqL00RZy53yfrxSOM

