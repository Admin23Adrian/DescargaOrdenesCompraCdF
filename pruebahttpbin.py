import requests
from login import loguearse

token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
header={'Authorization':token, 'accept': 'application/json'}
url_base = "https://api.nosconecta.com.ar:443/file"

files = {"archivo": ("Test.pdf", open("./test.pdf", "rb"))}
datos = {
    'datos':'{"pedido_sap": "123456", "ape_y_nom_afiliado":"OyP"}, "idaplicacion":398'
}


response = requests.post(url_base, data=datos, files={"archivo": ("Test.pdf", open("./test.pdf", "rb"))})
print(response.text)