# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# http://py4e-data.dr-chuck.net/json?

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Storing the given parameters
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
# TODO: actual question address: Indiana University
data_address = "Indiana University"
address_wanted = data_address

# Setting the GET parameters on the URL
parameters = {"address": address_wanted, "key": api_key}
paramsurl = urllib.parse.urlencode(parameters)

# Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl.strip() + paramsurl.strip()
print("DATA URL: ", queryurl)

# Obtaining and reading the data
data_read = urllib.request.urlopen(queryurl).read()
data = data_read.decode()

# Parsing the data and looking for the field we want.
# That field is inside the "Results" array, in its first item (if our address is correct we can assume that the result would be the correct one) and on its "place_id" field
js = json.loads(data)
place_id = js["results"][0]["place_id"]
print("PLACE ID: ", place_id)