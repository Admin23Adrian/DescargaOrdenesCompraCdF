import requests
import json
import time
import os
import json

def loguearse(usuario, password):
    url_auth = "https://api.nosconecta.com.ar:443/auth"
    headers_log = {"user": usuario, "password":password}
    payload = {}

    request = requests.get(url = url_auth, headers = headers_log, data = payload)
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