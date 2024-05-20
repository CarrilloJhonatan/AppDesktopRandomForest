import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QCheckBox, QComboBox
from Subir_Data_ui import Ui_MainWindow as Ui_SubirDataWindow
from Parametros_ui import Ui_MainWindow as Ui_ParametrosWindow
from Analisis_ui import Ui_MainWindow as Ui_AnalisisWindow
from Formulario_ui import Ui_MainWindow as Ui_FormularioWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SubirDataWindow()
        self.ui.setupUi(self)
        # Conectar el botón "Escoger Data" a la función cargar_data
        self.ui.escogerData.clicked.connect(self.cargar_data)
        # Conectar los botones de menú a las funciones correspondientes
        self.ui.menu1.clicked.connect(self.abrir_subir_data)
        self.ui.menu2.clicked.connect(self.abrir_parametros_ui)
        self.ui.menu3.clicked.connect(self.abrir_analisis_ui)
        self.ui.menu4.clicked.connect(self.abrir_formulario_ui)

        # Mantener instancias de las ventanas secundarias
        self.subir_data_window = SubirDataWindow()
        self.parametros_window = ParametrosWindow()
        self.analisis_window = AnalisisWindow()
        self.formulario_window = FormularioWindow()
        
    def cargar_data(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo CSV
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo CSV", "", "CSV Files (*.csv);;All Files (*)")
        if file_name:
            # Leer el archivo CSV usando pandas
            df = pd.read_csv(file_name)
            # Mostrar los datos en la tabla
            self.mostrar_datos_en_tabla(df)
            # Actualizar los checkboxes en la ventana de Parámetros
            self.actualizar_checkboxes(df.columns)
            # Actualizar el combobox en la ventana de Parámetros
            self.actualizar_combobox(df.columns)
    
    def mostrar_datos_en_tabla(self, df):
        # Configurar la tabla para mostrar el DataFrame
        self.ui.tableDatos.setColumnCount(len(df.columns))
        self.ui.tableDatos.setRowCount(len(df.index))
        self.ui.tableDatos.setHorizontalHeaderLabels(df.columns)
        
        # Llenar la tabla con datos del DataFrame
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.ui.tableDatos.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

        # Actualizar los campos de cantidad de filas y columnas
        self.ui.cantidadfilas.setText(str(len(df.index)))
        self.ui.cantidascolumnas.setText(str(len(df.columns)))
        
    def abrir_subir_data(self):
        # Mostrar la ventana de Subir Data
        self.subir_data_window.show()

    def abrir_parametros_ui(self):
        # Verificar si hay datos en la tabla antes de abrir la ventana de Parámetros
        if self.ui.tableDatos.rowCount() == 0:
            QMessageBox.warning(self, "Advertencia", "No hay datos en la tabla.")
            return
        # Mostrar la ventana de Parámetros
        self.parametros_window.show()
        # Habilitar la ventana de Parámetros y sus widgets
        self.parametros_window.setEnabled(True)
        self.parametros_window.selectpredictor.setEnabled(True)
        for checkbox in self.parametros_window.columnas_checkboxes:
            checkbox.setEnabled(True)

    def abrir_analisis_ui(self):
        # Mostrar la ventana de Análisis
        self.analisis_window.show()

    def abrir_formulario_ui(self):
        # Mostrar la ventana de Formulario
        self.formulario_window.show()
    
    def actualizar_checkboxes(self, column_names):
        # Limpiar los checkboxes existentes
        self.parametros_window.clear_checkboxes()
        # Crear nuevos checkboxes con los nombres de las columnas
        for col_name in column_names:
            checkbox = QCheckBox(col_name)
            self.parametros_window.layout().addWidget(checkbox)
            self.parametros_window.columnas_checkboxes.append(checkbox)
    
    def actualizar_combobox(self, column_names):
        # Limpiar el combobox existente
        self.parametros_window.selectpredictor.clear()
        # Agregar los nombres de las columnas al combobox
        self.parametros_window.selectpredictor.addItems(column_names)
        # Habilitar el combobox
        self.parametros_window.selectpredictor.setEnabled(True)

class SubirDataWindow(QMainWindow, Ui_SubirDataWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class ParametrosWindow(QMainWindow, Ui_ParametrosWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.columnas_checkboxes = []

    def clear_checkboxes(self):
        # Limpiar todos los checkboxes existentes
        for checkbox in self.columnas_checkboxes:
            checkbox.deleteLater()
        self.columnas_checkboxes = []

class AnalisisWindow(QMainWindow, Ui_AnalisisWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class FormularioWindow(QMainWindow, Ui_FormularioWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
