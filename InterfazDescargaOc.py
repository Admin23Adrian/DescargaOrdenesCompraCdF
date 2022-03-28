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
        self.ind = 2

    def run(self):
        usuario = getuser()
        ruta = "C:/Users/" + usuario + "/Desktop/ordenes.xlsx"
        excel = load_workbook(ruta)
        hoja_trabajo = excel["Hoja1"]
        cantidad_pedidos = len(hoja_trabajo["A"])
        
        entregas = hoja_trabajo["A"]
        convenios = hoja_trabajo["B"]
        pedidos = hoja_trabajo["C"]
        ordenes = hoja_trabajo["D"]
        clientes = hoja_trabajo["E"]
        resultados = hoja_trabajo["H"]
        self.componentesHilo.componentes.num_sinDesc.setText(str(cantidad_pedidos))

        try:
            while hoja_trabajo[f"A{self.ind}"].value != None:

                pedido = hoja_trabajo[f"C{self.ind}"].value
                orden = hoja_trabajo[f"D{self.ind}"].value
                convenio = hoja_trabajo[f"B{self.ind}"].value
                cliente =  hoja_trabajo[f"E{self.ind}"].value
                entrega =  hoja_trabajo[f"A{self.ind}"].value

                sleep(2)
                descarga = proceso(pedido, orden, cliente, convenio, entrega, self.modelo)
                sleep(2)
                if descarga:
                    self.cont = self.cont + 1
                    self.componentesHilo.componentes.num_descargadas.setText(str(self.cont))
                    hoja_trabajo[f"H{self.ind}"].value = "Descargada"
                elif not descarga:
                    hoja_trabajo[f"H{self.ind}"].value = "Sin OC descargada"
                print(f"Valor de la fila {self.ind} -", hoja_trabajo[f"A{self.ind}"].value)
                self.ind += 1

        except Exception as e:
            print(f"Excepcion en Modulo InterfazDescargaOc - Entre lineas 39 y 55. Detalles:", e)

        finally:
            print("Guardando y cerrando Excel de Ordenes...")
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
        if not self.componentes.check.isChecked():
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
