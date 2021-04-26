import json
import requests
import time
from login import loguearse

token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
# print(token)
url_request = "https://api.nosconecta.com.ar:443/file"
headers_file = {"Authorization":token, "accept":"application/json"}



request = requests.get(url = url_request, )
print(request.text)