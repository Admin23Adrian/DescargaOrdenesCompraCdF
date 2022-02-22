from PyQt5 import QtCore, QtGui, QtWidgets


class DescargaDeOc(object):
    def setupUi(self, DescargaDeOc):
        DescargaDeOc.setObjectName("DescargaDeOc")
        DescargaDeOc.resize(500, 452)
        DescargaDeOc.setStyleSheet("#contenedor {\n"
"    background-color: #252849;\n"
"}\n"
"\n"
"#titulo {\n"
"    color: #31D2EA;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"#cajaSinDescargar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.769, y2:0.0397727, stop:0 rgba(253, 106, 2, 255), stop:0.509002 rgba(240, 133, 35, 255), stop:1 rgba(255, 178, 77, 255));\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"\n"
"#cajaDescargadas {\n"
"    background-color: qlineargradient(spread:pad, x1:0.00580552, y1:0.364, x2:0.509965, y2:0, stop:0 rgba(26, 55, 228, 255), stop:0.470247 rgba(47, 82, 236, 255), stop:1 rgba(72, 120, 247, 255));\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"\n"
"#lbl_titulo_cantidad {\n"
"    color: #FFFDF5;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"#lbl_titulo_descargas {\n"
"    color: #FFFDF5;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"#num_sinDesc, #num_descargadas {\n"
"    font-size: 35px;\n"
"    color: #F1F3FA;\n"
"}\n"
"\n"
"#lbl_descargando {\n"
"    color: #0093AB;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#boton {\n"
"    border-style: none;\n"
"    background-color: #56C1DB;\n"
"    border-radius: 20px;\n"
"    font-size: 18px;\n"
"    color: #202443;\n"
"}\n"
"\n"
"#boton:hover {\n"
"    background-color:  rgb(91, 234, 213);\n"
"}\n"
"\n"
"#check {\n"
"    font-size: 15px;\n"
"    color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(DescargaDeOc)
        self.centralwidget.setObjectName("centralwidget")
        self.contenedor = QtWidgets.QFrame(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.titulo = QtWidgets.QLabel(self.contenedor)
        self.titulo.setGeometry(QtCore.QRect(10, 30, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(-1)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.cajaSinDescargar = QtWidgets.QLabel(self.contenedor)
        self.cajaSinDescargar.setGeometry(QtCore.QRect(70, 140, 151, 121))
        self.cajaSinDescargar.setText("")
        self.cajaSinDescargar.setObjectName("cajaSinDescargar")
        self.cajaDescargadas = QtWidgets.QLabel(self.contenedor)
        self.cajaDescargadas.setGeometry(QtCore.QRect(290, 140, 151, 121))
        self.cajaDescargadas.setText("")
        self.cajaDescargadas.setObjectName("cajaDescargadas")
        self.lbl_titulo_cantidad = QtWidgets.QLabel(self.contenedor)
        self.lbl_titulo_cantidad.setGeometry(QtCore.QRect(70, 139, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lbl_titulo_cantidad.setFont(font)
        self.lbl_titulo_cantidad.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo_cantidad.setWordWrap(True)
        self.lbl_titulo_cantidad.setObjectName("lbl_titulo_cantidad")
        self.lbl_titulo_descargas = QtWidgets.QLabel(self.contenedor)
        self.lbl_titulo_descargas.setGeometry(QtCore.QRect(290, 140, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lbl_titulo_descargas.setFont(font)
        self.lbl_titulo_descargas.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo_descargas.setWordWrap(True)
        self.lbl_titulo_descargas.setObjectName("lbl_titulo_descargas")
        self.num_sinDesc = QtWidgets.QLabel(self.contenedor)
        self.num_sinDesc.setGeometry(QtCore.QRect(124, 212, 47, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(-1)
        self.num_sinDesc.setFont(font)
        self.num_sinDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.num_sinDesc.setObjectName("num_sinDesc")
        self.num_descargadas = QtWidgets.QLabel(self.contenedor)
        self.num_descargadas.setGeometry(QtCore.QRect(344, 210, 47, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(-1)
        self.num_descargadas.setFont(font)
        self.num_descargadas.setAlignment(QtCore.Qt.AlignCenter)
        self.num_descargadas.setObjectName("num_descargadas")
        self.lbl_descargando = QtWidgets.QLabel(self.contenedor)
        self.lbl_descargando.setGeometry(QtCore.QRect(66, 270, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lbl_descargando.setFont(font)
        self.lbl_descargando.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_descargando.setObjectName("lbl_descargando")
        self.boton = QtWidgets.QPushButton(self.contenedor)
        self.boton.setGeometry(QtCore.QRect(74, 360, 371, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Black")
        font.setPointSize(-1)
        self.boton.setFont(font)
        self.boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton.setObjectName("boton")
        self.check = QtWidgets.QCheckBox(self.contenedor)
        self.check.setGeometry(QtCore.QRect(214, 310, 81, 17))
        self.check.setObjectName("check")
        DescargaDeOc.setCentralWidget(self.centralwidget)

        self.retranslateUi(DescargaDeOc)
        QtCore.QMetaObject.connectSlotsByName(DescargaDeOc)

    def retranslateUi(self, DescargaDeOc):
        _translate = QtCore.QCoreApplication.translate
        DescargaDeOc.setWindowTitle(_translate("DescargaDeOc", "MainWindow"))
        self.titulo.setText(_translate("DescargaDeOc", "Descarga de ordenes de compra"))
        self.lbl_titulo_cantidad.setText(_translate("DescargaDeOc", "Cantidad a descargar"))
        self.lbl_titulo_descargas.setText(_translate("DescargaDeOc", "Cantidad descargadas"))
        # self.num_sinDesc.setText(_translate("DescargaDeOc", "50"))
        # self.num_descargadas.setText(_translate("DescargaDeOc", "10"))
        # self.lbl_descargando.setText(_translate("DescargaDeOc", "Descargando ..."))
        self.boton.setText(_translate("DescargaDeOc", "Descargar"))
        self.check.setText(_translate("DescargaDeOc", "No Osde"))
