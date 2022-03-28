import json
import requests
import time
from getpass import getuser
import os
import urllib3
from login import loguearse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def descarga_documento(iddoc, entrega, cliente, convenio, modelo):
    no_osde = None
    osde = None
    usuario = getuser()
    token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
    # print(token)
    url_request = f"https://api.nosconecta.com.ar:443/file/398/{iddoc}"
    headers_file = {"Authorization": token, "accept": "application/json"}

    response = requests.get(url_request, headers=headers_file, stream=True, verify=False)
    ruta_guardado = f"C:/Users/{usuario}/Desktop/Ordenes De Compra/{cliente}"

    # Modelo para OSDE: cliente/entrega
    if modelo == 1:
        nom_pdf = f"{ruta_guardado}/{entrega}.pdf"
        if os.path.isdir(ruta_guardado):
            with open(nom_pdf, "wb") as file:
                for doc in response.iter_content():
                    file.write(doc)
                print(f"Descarga completa. Carpeta: {cliente}, PDF: {nom_pdf}.")
        else:
            os.mkdir(ruta_guardado)
            time.sleep(2)
            with open(nom_pdf, "wb") as file:
                for doc in response.iter_content():
                    file.write(doc)
                print(f"Descarga completa. Carpeta: {cliente}, PDF: {nom_pdf}.")
            response.close()
        osde = True
        return osde

    # Modelo para No OSDE: cliente/convenio-entrega
    elif modelo == 2:
        pdf_no_esde = f"{ruta_guardado}/{convenio} - {entrega}.pdf"
        if os.path.isdir(ruta_guardado):
            with open(pdf_no_esde, "wb") as file:
                for doc in response.iter_content():
                    file.write(doc)
                print(f"Descarga completa. Carpeta: {cliente}, PDF: {pdf_no_esde}.")
        else:
            os.mkdir(ruta_guardado)
            time.sleep(2)
            with open(pdf_no_esde, "wb") as file:
                for doc in response.iter_content():
                    file.write(doc)
                print(f"Descarga completa. Carpeta: {cliente}, PDF: {pdf_no_esde}.")
            response.close()
        no_osde = True
        return no_osde

