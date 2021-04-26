# Entregas que contienen numero de OC en la 353 y que puedo usar ese numero en la 398:
# Entregas sacadas del legajo de la z_sd_estados_hist cliente OSPEDYC
# saque el numero de pedido externo y el pedido:
# Entegas que sirve: 83837188, 83835032




# Estructura response de la aplicacion 398 con la solicitud get.

json_398 = {
    "message":{
        "results":{
            "id": "nro identificador tsdocs",
            "archivo": "nombre del archivo pdf",
            "pedido_sap": "el nro de pedido scienza",
            "ape_y_nom_afiliado": "",
            "orden_de_compra": "el nro de pedido externo - OC del cliente",
            "id_afiliado": "nro de id afiliad",
            "id_cliente": "nro id cliente",
            "observaciones": "deberia decir si es OC o es una Receta"
        }
    }
}

lista = [{"key":"pedido_sap", "value":"4544264"}]