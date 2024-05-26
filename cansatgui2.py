# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cansatgui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import serial.tools.list_ports
from SerialReaderThread import SerialReaderThread
from MapWindow import MapWindow
from GyroWindow import GyroWindow
from MgnWindow import MgnWindow
from AccelWindow import AccelWindow
class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.serial_ports = []
        self.baudrates = [9600, 115200]
        self.gyro_window = None
        self.mgn_window = None
        self.accel_window = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pB_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_1.setEnabled(True)
        self.pB_1.setAutoFillBackground(False)
        self.pB_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("brujula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_1.setIcon(icon)
        self.pB_1.setIconSize(QtCore.QSize(40, 60))
        self.pB_1.setCheckable(False)
        self.pB_1.setAutoRepeat(False)
        self.pB_1.setDefault(False)
        self.pB_1.setFlat(True)
        self.pB_1.setObjectName("pB_1")
        self.verticalLayout.addWidget(self.pB_1)
        self.pB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pB_2.setAutoFillBackground(False)
        self.pB_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rotacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_2.setIcon(icon1)
        self.pB_2.setIconSize(QtCore.QSize(40, 60))
        self.pB_2.setFlat(True)
        self.pB_2.setObjectName("pB_2")
        self.verticalLayout.addWidget(self.pB_2)
        self.pB_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sistema.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_3.setIcon(icon2)
        self.pB_3.setIconSize(QtCore.QSize(40, 60))
        self.pB_3.setFlat(True)
        self.pB_3.setObjectName("pB_3")
        self.verticalLayout.addWidget(self.pB_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("gps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 60))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(480, 10, 311, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("conectar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(570, 150, 191, 391))
        self.horizontalWidget_2.setTabletTracking(False)
        self.horizontalWidget_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalWidget_2.setAutoFillBackground(False)
        self.horizontalWidget_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_12 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_5 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_13 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_10 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayout_4.addWidget(self.textEdit_10)
        self.textEdit_6 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_4.addWidget(self.textEdit_6)
        self.textEdit_4 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_4.addWidget(self.textEdit_4)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.textEdit_5 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_4.addWidget(self.textEdit_5)
        self.textEdit_12 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_12.setObjectName("textEdit_12")
        self.verticalLayout_4.addWidget(self.textEdit_12)
        self.textEdit_3 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_4.addWidget(self.textEdit_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_4.addWidget(self.textEdit_2)
        self.textEdit_11 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_11.setObjectName("textEdit_11")
        self.verticalLayout_4.addWidget(self.textEdit_11)
        self.textEdit_8 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_4.addWidget(self.textEdit_8)
        self.textEdit_7 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_4.addWidget(self.textEdit_7)
        self.textEdit_13 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_13.setObjectName("textEdit_13")
        self.verticalLayout_4.addWidget(self.textEdit_13)
        self.textEdit_9 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_4.addWidget(self.textEdit_9)
        self.textEdit_14 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_14.setEnabled(True)
        self.textEdit_14.setObjectName("textEdit_14")
        self.verticalLayout_4.addWidget(self.textEdit_14)
        self.textEdit_15 = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.textEdit_15.setObjectName("textEdit_15")
        self.verticalLayout_4.addWidget(self.textEdit_15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 822, 581))
        self.label_15.setSizeIncrement(QtCore.QSize(1, 1))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_15.raise_()
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_battery = QtWidgets.QLabel(self.centralwidget)
        self.label_battery.setObjectName("label_battery")
        self.horizontalLayout.addWidget(self.label_battery)
        self.main_window = MainWindow
        self.adjustSize(MainWindow)
        self.comboBox.addItems([str(baudrate) for baudrate in self.baudrates])
        self.serial_ports = self.get_serial_ports()
        self.readerThread = SerialReaderThread("","")
        self.readerThread.dataReceived.connect(self.update_data)
        self.connected = False
        self.pushButton.clicked.connect(self.connect_to_serial)
        self.pushButton_4.clicked.connect(self.open_map_window)
        self.pB_1.clicked.connect(self.open_mgn_window)
        self.pB_2.clicked.connect(self.open_gyro_window)
        self.pB_3.clicked.connect(self.open_accel_window)
        for i in range(1, 15):  # Esto iterará desde 1 hasta 14 incluido.
            label = getattr(self, f"label_{i}" if i != 1 else "label")
            label.setFont(font)
        for i in range(1, 16):  # Esto iterará desde 1 hasta 14 incluido.
            textEdit = getattr(self, f"textEdit_{i}" if i != 1 else "textEdit")
            textEdit.setFont(font)
            textEdit.setReadOnly(True)  # Configurar como solo lectura
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pB_1.setText(_translate("MainWindow", "Magnetometer"))
        self.pB_2.setText(_translate("MainWindow", "Gyroscope"))
        self.pB_3.setText(_translate("MainWindow", "Accelerometer"))
        self.pushButton_4.setText(_translate("MainWindow", "GPS"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Mag X:"))
        self.label_2.setText(_translate("MainWindow", "Mag Y:"))
        self.label_3.setText(_translate("MainWindow", "Mag Z:"))
        self.label_4.setText(_translate("MainWindow", "Gyro X:"))
        self.label_12.setText(_translate("MainWindow", "Gyro Y:"))
        self.label_5.setText(_translate("MainWindow", "Gyro Z"))
        self.label_11.setText(_translate("MainWindow", "Acce X:"))
        self.label_6.setText(_translate("MainWindow", "Acce Y:"))
        self.label_8.setText(_translate("MainWindow", "Acce Z:"))
        self.label_9.setText(_translate("MainWindow", "Pressure:"))
        self.label_7.setText(_translate("MainWindow", "Temperature:"))
        self.label_13.setText(_translate("MainWindow", "Altitude:"))
        self.label_14.setText(_translate("MainWindow", "Lat:"))
        self.label_10.setText(_translate("MainWindow", "Lon:"))
    def adjustSize(self,MainWindow):
        window_width = MainWindow.frameGeometry().width()
        window_height = MainWindow.frameGeometry().height()
        self.new_window = None
        icon_width = int(window_width * 0.03)
        icon_height = int(window_height * 0.065)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(
            20, 20, window_width * 0.3, window_height * 1))
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.05, window_width * 0.25, window_height * 0.13))
        self.horizontalWidget_2.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.28, window_width * 0.2, window_height * 0.67))
        self.label_15.setGeometry(QtCore.QRect(
            0, 0 , window_width, window_height))
        self.pB_1.setIconSize(QtCore.QSize(icon_width,icon_height))
        self.pB_2.setIconSize(QtCore.QSize(icon_width,icon_height))
        self.pB_3.setIconSize(QtCore.QSize(icon_width,icon_height))
        self.pushButton_4.setIconSize(QtCore.QSize(icon_width,icon_height))
        self.label_battery.setGeometry(window_width * 1.5, window_height * 1.3, icon_width*1.2, icon_height*1.1)
    def get_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        if ports:
            port_names = [port.device for port in ports]
            self.comboBox_2.addItems(port_names)
        else:
            self.comboBox_2.addItem("No devices")
    def set_battery_icon(self, value):
        if value > 75:
            icon = QtGui.QIcon("full-battery.png")  # Cambia el nombre del archivo según corresponda
        elif value > 50:
            icon = QtGui.QIcon("half-battery.png")  # Cambia el nombre del archivo según corresponda
        elif value > 25:
            icon = QtGui.QIcon("low-battery.png")  # Cambia el nombre del archivo según corresponda
        else:
            icon = QtGui.QIcon("empty-battery.png")  # Cambia el nombre del archivo según corresponda
        
        return icon
    def open_gyro_window(self):
        self.gyro_window = GyroWindow(self.main_window)
        self.gyro_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gyro_window.show()
    def open_mgn_window(self):
        self.mgn_window = MgnWindow(self.main_window)
        self.mgn_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.mgn_window.show()
    def open_accel_window(self):
        self.accel_window = AccelWindow(self.main_window)
        self.accel_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.accel_window.show()
    def open_map_window(self):
        self.map_window = MapWindow()
        self.map_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.map_window.show()   
    def connect_to_serial(self):
        if not self.connected:
            selected_baudrate = self.comboBox.currentText()
            selected_port = self.comboBox_2.currentText()
            if selected_port == "No devices":
                QMessageBox.warning(self.main_window, "No devices", "No se encontraron dispositivos disponibles.")
            else:
                self.readerThread.port = selected_port
                self.readerThread.baudrate = selected_baudrate
                self.readerThread.start()  
                self.connected = True
                self.pushButton.setText("Disconnect")
                QMessageBox.information(self.main_window, "Conexión exitosa",
                                        f"Conectado al puerto {selected_port} a {selected_baudrate} baudrate.")
        else:
            self.readerThread.stop()  # Stop the SerialReaderThread
            self.connected = False
            self.pushButton.setText("Connect")
            QMessageBox.information(self.main_window, "Desconexión exitosa", "Desconectado del puerto COM.")
    def update_data(self, data):
        if data:
            data_list = data.split(",")

            # Verificar si data_list tiene exactamente 16 elementos
            if len(data_list) != 16:
                # Puedes mostrar un mensaje de error aquí si lo deseas
                # QMessageBox.warning(self.main_window, "Error de datos", "Los datos recibidos no son válidos.")
                return  # Salir de la función sin hacer nada más

            print(data_list)
            self.textEdit_10.setText(data_list[0])
            self.textEdit_6.setText(data_list[1])
            self.textEdit_4.setText(data_list[2])
            self.textEdit.setText(data_list[3])
            self.textEdit_5.setText(data_list[4])
            self.textEdit_12.setText(data_list[5])
            self.textEdit_3.setText(data_list[6])
            self.textEdit_2.setText(data_list[7])
            self.textEdit_11.setText(data_list[8])
            self.textEdit_8.setText(data_list[9])
            self.textEdit_7.setText(data_list[10])
            self.textEdit_13.setText(data_list[11])
            self.textEdit_9.setText(data_list[12])
            self.textEdit_14.setText(data_list[13])
            self.textEdit_15.setText(data_list[14])
            battery_value = int(data_list[15])
            battery_icon = self.set_battery_icon(battery_value)
            self.label_battery.setPixmap(battery_icon.pixmap(40, 40))
            if self.gyro_window or self.accel_window:
                self.gyro_window.display_graph(data_list) 
            if self.mgn_window:
                self.mgn_window.display_graph(data_list) 
            if self.accel_window:
                self.accel_window.display_graph(data_list)  

        else:
            QMessageBox.warning(self.main_window, "Error de conexión", "No se pudo conectar al puerto seleccionado.")
