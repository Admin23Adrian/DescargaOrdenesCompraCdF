import requests
import json
from login import loguearse


def consultas(entrega):
    token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
    header={'Authorization':token, 'accept': 'application/json'}
    url_base = "https://api.nosconecta.com.ar:443/search/353"

    params = (
        ('filter', '[{"key":"entrega_id","value":" ' + str(entrega) + '"}]'),
    )
    payload = {}

    response = requests.get(url = url_base, headers=header, params=params)
    # print(requests.utils.unquote(response.url))
    text_contenido = response.json()
    status = response.status_code

    if status == 200:
        print()
        print("(°_°)====== Solicitud exitosa ======(°_°)")
        contenido_respuesta = text_contenido["message"]["results"][0] # Mostramos el Json con los datos
        
        for content in contenido_respuesta:
            if contenido_respuesta[content] != None:
                # print(content, ":", contenido_respuesta["entrega_pedido"])
                print(content, contenido_respuesta[content])



entrega = 83459240
resultado = consultas(entrega)
# print(resultado)