# Form implementation generated from reading ui file 'e:\PROJECTS-VSCODE\AppDesktopRandomForest\Subir_Data.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 593)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 780, 211, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(660, 810, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 810, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1050, 780, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1140, 780, 201, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 771, 491))
        self.frame.setStyleSheet("background-color: rgb(252, 249, 242);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.menu1siguente = QtWidgets.QPushButton(parent=self.frame)
        self.menu1siguente.setGeometry(QtCore.QRect(620, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.menu1siguente.setFont(font)
        self.menu1siguente.setStyleSheet("background-color: rgb(56, 77, 89);\n"
"color: rgb(252, 249, 242);\n"
"border: none;")
        self.menu1siguente.setObjectName("menu1siguente")
        self.escogerData = QtWidgets.QPushButton(parent=self.frame)
        self.escogerData.setGeometry(QtCore.QRect(620, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.escogerData.setFont(font)
        self.escogerData.setStyleSheet("color: rgb(56, 77, 89);")
        self.escogerData.setObjectName("escogerData")
        self.tableView = QtWidgets.QTableView(parent=self.frame)
        self.tableView.setGeometry(QtCore.QRect(40, 120, 691, 231))
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(40, 370, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(56, 77, 89);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(210, 370, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(56, 77, 89);")
        self.label_2.setObjectName("label_2")
        self.cantidadfilas = QtWidgets.QTextEdit(parent=self.frame)
        self.cantidadfilas.setEnabled(False)
        self.cantidadfilas.setGeometry(QtCore.QRect(130, 370, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.cantidadfilas.setFont(font)
        self.cantidadfilas.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.cantidadfilas.setObjectName("cantidadfilas")
        self.cantidascolumnas = QtWidgets.QTextEdit(parent=self.frame)
        self.cantidascolumnas.setEnabled(False)
        self.cantidascolumnas.setGeometry(QtCore.QRect(330, 370, 51, 21))
        self.cantidascolumnas.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.cantidascolumnas.setObjectName("cantidascolumnas")
        self.tableDatos = QtWidgets.QTableWidget(parent=self.frame)
        self.tableDatos.setGeometry(QtCore.QRect(40, 120, 691, 231))
        self.tableDatos.setObjectName("tableDatos")
        self.tableDatos.setColumnCount(0)
        self.tableDatos.setRowCount(0)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -1, 771, 81))
        self.frame_2.setStyleSheet("background-color: rgb(134, 153, 160);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.menu1 = QtWidgets.QPushButton(parent=self.frame_2)
        self.menu1.setGeometry(QtCore.QRect(40, 30, 75, 21))
        self.menu1.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.menu1.setFont(font)
        self.menu1.setStyleSheet("QWidget {\n"
"    background-color: rgb(56, 77, 89);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 57 7pt \"Montserrat SemiBold\";\n"
"    color: rgb(208, 229, 214);\n"
"    border:none;\n"
"}")
        self.menu1.setObjectName("menu1")
        self.menu2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.menu2.setGeometry(QtCore.QRect(150, 30, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.menu2.setFont(font)
        self.menu2.setStyleSheet("QWidget {\n"
"    background-color: rgb(208, 229, 214);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 57 7pt \"Montserrat SemiBold\";\n"
"    color: rgb(56, 77, 89);\n"
"    border:none;\n"
"}")
        self.menu2.setObjectName("menu2")
        self.menu3 = QtWidgets.QPushButton(parent=self.frame_2)
        self.menu3.setGeometry(QtCore.QRect(260, 30, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.menu3.setFont(font)
        self.menu3.setStyleSheet("QWidget {\n"
"    background-color: rgb(208, 229, 214);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 57 7pt \"Montserrat SemiBold\";\n"
"    color: rgb(56, 77, 89);\n"
"    border:none;\n"
"}")
        self.menu3.setObjectName("menu3")
        self.menu4 = QtWidgets.QPushButton(parent=self.frame_2)
        self.menu4.setGeometry(QtCore.QRect(370, 30, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.menu4.setFont(font)
        self.menu4.setStyleSheet("QWidget {\n"
"    background-color: rgb(208, 229, 214);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 57 7pt \"Montserrat SemiBold\";\n"
"    color: rgb(56, 77, 89);\n"
"    border:none;\n"
"}")
        self.menu4.setObjectName("menu4")
        self.frame.raise_()
        self.pushButton_3.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_11.raise_()
        self.pushButton_10.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "APLICAR ANALISIS EXPLORATORIO"))
        self.pushButton_8.setText(_translate("MainWindow", "SIGUENTE"))
        self.pushButton_9.setText(_translate("MainWindow", "ATRAS"))
        self.pushButton_11.setText(_translate("MainWindow", "ATRAS"))
        self.pushButton_10.setText(_translate("MainWindow", "CARGAR NUEVO CONJUNTO DE DATOS"))
        self.menu1siguente.setText(_translate("MainWindow", "Siguiente"))
        self.escogerData.setText(_translate("MainWindow", "Escoger Data"))
        self.label.setText(_translate("MainWindow", "Cantidad filas:"))
        self.label_2.setText(_translate("MainWindow", "Cantidad columnas:"))
        self.menu1.setText(_translate("MainWindow", "Subir Data"))
        self.menu2.setText(_translate("MainWindow", "Parametros"))
        self.menu3.setText(_translate("MainWindow", "Analisis"))
        self.menu4.setText(_translate("MainWindow", "Formulario"))
