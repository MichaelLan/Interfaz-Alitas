# -*- coding: utf-8 -*-
# Created by: Michael Lan

import os
import sys
import re
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtGui, QtWidgets, QtCore
from ui_main import Ui_Dialog

from pyside_material import apply_stylesheet

from dbconnection import connect, insert_data, close, validate_duplicate


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.name, self.dni, self.phone, self.addres, self.birth = ('', '', '', '', '')
        self.dni_register = ''
        self.path = 'dbCrokiAlitas.db'
        
        self.ui.txtName.installEventFilter(self)
        self.ui.txtDNI.installEventFilter(self)
        self.ui.txtPhone.installEventFilter(self)
        self.ui.txtAddres.installEventFilter(self)
        self.ui.txtBirth.installEventFilter(self)

        self.ui.btnSaveUser.clicked.connect(self.save_user)

        
    
    #----------------------------------------------------------------------
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusOut:

            if self.ui.txtName is obj:
                if self.validate_txt(self.ui.txtName.text()):
                    self.name = self.ui.txtName.text().title().strip()
                    self.ui.txtName.setText(self.name)
                else:
                    self.name = ''
                    self.ui.txtName.setText('')
                    self.ui.txtName.setPlaceholderText('Por favor ingrese un nombre válido')

            if self.ui.txtDNI is obj:
                if self.validate_num(self.ui.txtDNI.text().replace(',','')):
                    self.dni = int(self.ui.txtDNI.text().replace(',',''))
                    self.ui.txtDNI.setText('{:,}'.format(self.dni))
                else:
                    self.dni = ''
                    self.ui.txtDNI.setText('')
                    self.ui.txtDNI.setPlaceholderText('Por favor, escriba un número')

            if self.ui.txtPhone is obj:
                if self.validate_num(self.ui.txtPhone.text()):
                    self.phone = int(self.ui.txtPhone.text())
                    self.ui.txtPhone.setText(str(self.phone))
                else:
                    self.phone = ''
                    self.ui.txtPhone.setText('')
                    self.ui.txtPhone.setPlaceholderText('Por favor, escriba un número')

            if self.ui.txtDNIRegister is obj:
                if self.validate_num(self.ui.txtDNIRegister.text()):
                    self.dni_register = int(self.ui.txtDNIRegister.text())
                else:
                    self.ui.txtDNIRegister.setText('')
                    self.ui.txtDNIRegister.setPlaceholderText('Por favor, escriba un número')

        return super(MainWindow, self).eventFilter(obj, event)
    

    #----------------------------------------------------------------------
    def save_user(self):
        user = dict(
            name = self.name,
            dni = self.dni,
            phone = self.phone,
            addres = self.ui.txtAddres.text(),
            birth = self.ui.txtBirth.text(),
        )
        
        self.conn = connect(self.path)

        if all([user[value] for value in ['name', 'dni', 'phone']]):
            if not validate_duplicate(self.conn, 'users', 'dni', user['dni']):
                print (user)
                try:
                    with self.conn as conn:
                        insert_data(conn, 'users', **user)
                except:
                    close(self.conn)
                finally:
                    close(self.conn)
                    self.ui.lblBanner.setText(f'Usuario {self.name} creado correctamente')
                    self.ui.txtName.setText('')
                    self.ui.txtDNI.setText('')
                    self.ui.txtPhone.setText('')
                    self.ui.txtAddres.setText('')
                    self.ui.txtBirth.setText('')
                    self.ui.txtName.setPlaceholderText('')
                    self.ui.txtDNI.setPlaceholderText('')
                    self.ui.txtPhone.setPlaceholderText('')

            else:
                self.ui.lblBanner.setText(f"El usuario {user['dni']} ya existe")

        else:
            self.ui.lblBanner.setText('Verifique los datos')

    
    #----------------------------------------------------------------------
    def validate_txt(self, *fields):
        validator = [re.match(r'^[a-z\sáéíóú.]+$', field, re.I) for field in fields]
        return all(validator)


    #----------------------------------------------------------------------
    def validate_num(self, *fields):
        validator = [re.match(r'^[0-9]+$', field) for field in fields]
        return all(validator)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    
    apply_stylesheet(app, theme='light_red.xml', light_secondary=True)

    font = QtGui.QFont()
    font.setFamily("Ubuntu Mono")
    font.setPointSize(15)
    font.setWeight(75)
    font.setBold(True)

    font2 = QtGui.QFont()
    font2.setPointSize(10)
    font2.setBold(True)

    window.ui.lblTitle.setFont(font)
    window.ui.lblBanner.setFont(font2)

    window.show()
    
    sys.exit(app.exec_())