import sys
import PyQt5
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from consultas import proceso
from descarga_oc import *
from componentes import DescargaDeOc
from openpyxl import load_workbook
from getpass import getuser
from time import sleep
# from consulta_usuario import consultaUser

class Osde(QThread):
    signal = pyqtSignal()
    def __init__(self, clasePrincipal, modelo):
        super().__init__()
        self.modelo = modelo
        self.componentesHilo = clasePrincipal
        self.cont = 0

    def run(self):
        usuario = getuser()
        ruta = "C:/Users/" + usuario + "/Desktop/ordenes.xlsx"
        excel = load_workbook(ruta)
        hoja_trabajo = excel["Hoja1"]
        cantidad_pedidos = 0
        
        entregas = hoja_trabajo["A"]
        convenios = hoja_trabajo["B"]
        pedidos = hoja_trabajo["C"]
        ordenes = hoja_trabajo["D"]
        clientes = hoja_trabajo["E"]
        resultados = hoja_trabajo["H"]
        self.componentesHilo.componentes.num_sinDesc.setText(str(cantidad_pedidos))

        for i in range(2, len(hoja_trabajo["A"]) + 1):
            try:
                pedido = pedidos[i].value
                orden = ordenes[i].value
                convenio = convenios[i].value
                cliente = clientes[i].value
                entrega = entregas[i].value
                sleep(2)
                descarga = proceso(pedido, orden, cliente, convenio, entrega, self.modelo)
                sleep(2)
                if descarga == True:
                    self.cont = self.cont + 1
                    self.componentesHilo.componentes.num_descargadas.setText(str(self.cont))
                    resultados[i].value = "Descargada"
                elif descarga == False:
                    resultados[i].value = "Sin OC descargada"
                # dato_user = consultaUser(pedido)
                # if dato_user != False:
                #     resultados[i].value = str(dato_user)
            except:
                break
                excel.save("C:/Users/" + usuario + "/Desktop/ordenes.xlsx")
                excel.close()

        excel.save("C:/Users/" + usuario + "/Desktop/ordenes.xlsx")
        excel.close()
        self.componentesHilo.componentes.lbl_descargando.setText(f"{self.cont} Ordenes Descargadas.")
            


class InterfazOc(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.componentes = DescargaDeOc()
        self.componentes.setupUi(self)
        self.componentes.boton.clicked.connect(self.iniciar)
        self.componentes.num_sinDesc.setText("--")
        self.componentes.num_descargadas.setText("0")
        self.show()
    
    def iniciar(self):
        if self.componentes.check.isChecked() == False:
            print("Modelo OSDE.")
            self.osde = Osde(self, 1)
            self.osde.start()
            self.componentes.lbl_descargando.setText("Descargando...")
        else:
            print("Modelo NO OSDE.")
            self.osde = Osde(self, 2)
            self.osde.start()
            self.componentes.lbl_descargando.setText("Descargando...")



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ventana = InterfazOc()
    ventana.show()
    sys.exit(app.exec_())
