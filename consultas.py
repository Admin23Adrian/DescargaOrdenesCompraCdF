import requests
import json

from login import loguearse
import time
from descarga_oc import descarga_documento
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Funcion que busca por orden de compra + observaciones: OC
def buscar_por_orden(orden_compra, header, url_base):
    id_descarga = None
    cliente = None
    convenio = None
    observaciones = None

    params = (
        ('filter', '[{"key":"orden_de_compra","value":"' + str(orden_compra) + '"}]'),
        ('allfields', 'true'),
    )

    response = requests.get(url=url_base, headers=header, params=params, verify=False)
    contenido_json = response.json()
    status = response.status_code

    if status == 200:
        print("Status 200. Conexion exitosa.")
        time.sleep(2)
        print(f"Buscando la orden: {orden_compra} ...")
        time.sleep(3)
        datos_json = contenido_json["message"]["results"]

        if datos_json != []:
            for campos in datos_json:
                print("Orden encontrada.. Buscando id...")
                campos = datos_json[0]
                observaciones = campos["observaciones"]
                print("Imprimiendo observaciones", observaciones)
                if observaciones == "OC" or observaciones == "oc":
                    id_descarga = campos["id"]
                    cliente = campos["id_cliente"]
                    convenio = campos["convenio"]
                    break
                else:
                    observaciones = "Sin OC"
        else:
            return False  # Contenido vacio. No encontro nada
    else:
        return "Estatus 400. Error en la peticion."

    if observaciones != "Sin OC":
        return id_descarga, cliente, convenio, orden_compra, observaciones  # Devolvemos los datos cuando los encontramos
    else:
        return observaciones


# Funcion que busca por Pedido Sap + Observaciones: OC
def buscar_ped_sap(pedido, headers, url_consulta):
    id_descarga = None
    cliente = None
    convenio = None
    observaciones = None
    oc = None

    params = (
        ('filter', '[{"key":"pedido_sap","value":"' + str(pedido) + '"}]'),
        ('allfields', 'true'),
    )

    request = requests.get(url=url_consulta, headers=headers, params=params, verify=False)
    response = request.json()
    status = request.status_code

    if status == 200:
        print("Status 200. Conexion establecida")
        time.sleep(2)
        print(f"Buscando datos para {pedido}...")
        datos_json = response["message"]["results"]

        if datos_json:
            # campos = datos_json[0]
            for campos in datos_json:
                observaciones = campos["observaciones"]
                print("Imprimiendo observaciones:", observaciones)
                if observaciones == "OC" or observaciones == "oc":
                    id_descarga = campos["id"]
                    cliente = campos["id_cliente"]
                    convenio = campos["convenio"]
                    break
                else:
                    observaciones = "Sin OC"
        else:
            return False
    else:
        return "Status 400. Error en la solicitud."

    if observaciones != "Sin OC":
        return id_descarga, cliente, convenio, pedido, observaciones
    else:
        return observaciones


# Funcion que busca por pedido + usuario sramos@scienza.com.ar
def buscar_usuario_orden(orden, header, url_consulta):
    id_descarga = None
    cliente = None
    convenio = None
    usuario = None
    sramos = "sramos@scienza.com.ar"
    resultado_it = None
    param_por_usuario = (
        ('filter', '[{"key":"orden_de_compra","value":"' + str(orden) + '"}]'),
        ('allfields', 'true')
    )

    request = requests.get(url=url_consulta, headers=header, params=param_por_usuario, verify=False)
    response = request.json()
    status = request.status_code

    if status == 200:
        datos_json = response["message"]["results"]
        if datos_json != []:
            campos = datos_json[0]
            usuario = campos["usuario"]
            orden_json = campos["orden_de_compra"]

            if usuario == sramos:
                id_descarga = campos["id"]
                cliente = campos["id_cliente"]
                convenio = campos["convenio"]
                usuario = campos["usuario"]
                return id_descarga, cliente, convenio
            else:
                # Si devuelvo False es porque no encontre ni el pedido ni la orden con el usuario sramos
                # ni con la descripcion OC 
                return False
        else:
            # Json vacio para criterio orden + usuario
            return False
    else:
        return request.text


# Funcion que busca por pedido + usuario sramos@scienza.com.ar
def buscar_usuario_pedido(pedido, header, url_consulta):
    id_descarga = None
    cliente = None
    convenio = None
    usuario = None
    sramos = "sramos@scienza.com.ar"

    param_por_usuario = (
        ('filter', '[{"key":"pedido_sap","value":"' + str(pedido) + '"}]'),
        ('allfields', 'true'),
    )

    request = requests.get(url=url_consulta, headers=header, params=param_por_usuario, verify=False)
    response = request.json()
    status = request.status_code

    result_iteracion = True

    if status == 200:
        datos_json = response["message"]["results"]
        if datos_json != []:
            # Recorrer la lista de diccionarios en caso de tener mas de un documento para la busqueda por pedido.
            for campos in datos_json:
                usuario = campos["usuario"]
                pedido_json = campos["pedido_sap"]

                # Buscar coincidencia de pedido + usuario.
                if usuario == sramos:
                    id_descarga = campos["id"]
                    cliente = campos["id_cliente"]
                    convenio = campos["convenio"]
                    usuario = campos["usuario"]
                    print(usuario, pedido)
                    return id_descarga, cliente, convenio, pedido, usuario
                else:
                    # cambiar la variable a False en caso de no encontrar resultados.
                    result_iteracion = False
            return result_iteracion
        else:
            # Json vacio para criterio de busqueda pedido + usuario
            return False
    else:
        return request.text


def proceso(pedido_sap, orden, cliente, convenio, nro_entrega, modelo):
    token = loguearse("aalarcon@scienza.com.ar", "Adrian2020")
    header = {'Authorization': token, 'accept': 'application/json'}
    url_base = "https://api.nosconecta.com.ar:443/search/398"
    resultado_descarga = None

    nro_entrega = str(nro_entrega)

    # Se comienza buscando por pedido scienza
    resultado_pedido = buscar_ped_sap(pedido_sap, header, url_base)
    print(resultado_pedido)
    #print("")

    if resultado_pedido == "Sin OC" or resultado_pedido == False:
        print("Buscando por pedido + sramos@scienza.com.ar")

        resultado_usuario_pedido = buscar_usuario_pedido(pedido_sap, header, url_base)
        print(resultado_usuario_pedido)

        if resultado_usuario_pedido:
            print(resultado_usuario_pedido, "Listo para descargar")
            id_descarga = str(resultado_usuario_pedido[0])
            cliente = str(cliente)
            convenio = str(convenio)
            print(f"Descargando OC para orden: {pedido_sap}")
            # Se descarga la OC de tsdocs #
            resultado_descarga = descarga_documento(id_descarga, nro_entrega, cliente, convenio, modelo)
            print("")

        else:
            print("Buscando por orden...")
            resultado_orden = buscar_por_orden(orden, header, url_base)
            print(resultado_orden)

            if resultado_orden == "Sin OC" or resultado_orden == False:
                print("Buscando coincidencias orden + sramos@scienza.com.ar")
                resultado_usuario_orden = buscar_usuario_orden(orden, header, url_base)

                if resultado_usuario_orden:
                    print(resultado_usuario_orden, "Listo para descargar")
                    id_descarga = str(resultado_usuario_orden[0])
                    cliente = str(cliente)
                    convenio = str(convenio)
                    print(f"Descargando OC para orden: {orden}")
                    resultado_descarga = descarga_documento(id_descarga, nro_entrega, cliente, convenio, modelo)
                    print("")

                else:
                    print("Sin resultados para descargar el archivo.")
                    resultado_descarga = False
                    print("")

            else:
                print("Orden + Observacion encontrado. Descargando archivo OC...")
                id_descarga = str(resultado_orden[0])
                cliente = str(cliente)
                convenio = str(convenio)
                resultado_descarga = descarga_documento(id_descarga, nro_entrega, cliente, convenio, modelo)
                print("")

    else:
        # ir a descargargar la orden
        print("Pedido + Observacion encontrada. Descargando archivo OC...")
        id_descarga = str(resultado_pedido[0])
        cliente = str(cliente)
        convenio = str(convenio)
        resultado_descarga = descarga_documento(id_descarga, nro_entrega, cliente, convenio, modelo)
        print("")

    if resultado_descarga == True:
        return True
    else:
        return False
