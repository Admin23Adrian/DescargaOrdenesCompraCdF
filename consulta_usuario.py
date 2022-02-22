import requests
import time
# import os
# import sys
# from login import loguearse
# import json
# from getpass import getuser
# from openpyxl import load_workbook

# token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")

# def consultaUser(pedido):
#     url_consulta = "https://api.nosconecta.com.ar:443/search/398"
#     # header = {'Authorization':token, 'accept': 'application/json'}
#     parametro = (
#         ('filter', '[{"key":"pedido_sap","value":"'+str(pedido)+'"}]'),
#         ('allfields', 'true'),
#     )

#     # req = requests.get(url=url_consulta, headers=header, params=parametro, verify=False)
#     status = req.status_code
#     all_content = req.json()
#     datos_json = all_content["message"]["results"]
    
#     if datos_json != []:
#         campos = datos_json[0]
#         usuario = campos["usuario"]
#         return usuario
#     else:
#         return "Sin resultados de usuario"
    

    # print(f"Pedido: {pedido}, usuario: {usuario}")
# consultaUser("4707082")

# user = getuser()
# ruta = "C:/Users/" + user + "/Desktop/ordenes.xlsx"
# excel = load_workbook(ruta)
# hoja_trabajo = excel["Hoja1"]
# cantidad_pedidos = len(hoja_trabajo["A"])

# pedidos = hoja_trabajo["C"]
# resultados = hoja_trabajo["F"]

# for i in range(125, 166):
#     try:
#         pedido = pedidos[i].value
#         print(pedido)
#         res_user = consultaUser(pedido)
#         # print(res_user)
#         if res_user != False:
#             resultados[i].value = res_user
#         else:
#             resultados[i].value = "Sin Resultados Usuario"
#     except:
#         excel.save("C:/Users/" + user + "/Desktop/ordenes.xlsx")
#         excel.close()

# excel.save("C:/Users/" + user + "/Desktop/ordenes.xlsx")
# excel.close()
