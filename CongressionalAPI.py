#!/bin/python3

import urllib.request

baseUrl = 'https://congress.api.sunlightfoundation.com/'
apiKey = '00cfb5178ea846c4a082db883ca80f11'

req = urllib.request.Request(baseUrl + 'legislators?apikey=' + apiKey + '&state=GA')
with urllib.request.urlopen(req) as apiResponse:
    response = apiResponse.read()

print(response)