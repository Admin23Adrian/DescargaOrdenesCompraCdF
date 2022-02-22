import requests
import json
import time
import os
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def loguearse(usuario, password):
    url_auth = "https://api.nosconecta.com.ar:443/auth"
    headers_log = {"user":usuario, "password":password}
    payload = {}

    request = requests.get(url = url_auth, headers = headers_log, verify=False)
    response_code = request.status_code
    response_json = request.json()

    if response_code == 200:
        pass
        token_response = response_json["message"]["token"]
        token = "Bearer " + token_response
        return token
    else:
        error = "Ah ocurrido un error " + str(response_code)
        return error

# resultado = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
# print(resultado)