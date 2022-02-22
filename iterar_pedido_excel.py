from openpyxl import load_workbook
import os
import time
from getpass import getuser

usuario = getuser()

def traer_entregas():
    ruta = "C:/Users/" + usuario + "/Desktop/OyP/IMPLEMENTACION CON GITHUB/Bot OC - CdF/ejemplos.xlsx"
    excel = load_workbook(ruta)
    hoja_trabajo = excel["Hoja1"]
    cantidad_pedidos = len(hoja_trabajo["A"])
    print(cantidad_pedidos)

# traer_entregas()