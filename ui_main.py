# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sun Mar 15 09:31:11 2020
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 591)
        self.tabMain = QtWidgets.QTabWidget(Dialog)
        self.tabMain.setEnabled(True)
        self.tabMain.setGeometry(QtCore.QRect(2, 1, 691, 591))
        self.tabMain.setObjectName("tabMain")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtName = QtWidgets.QLineEdit(self.tab)
        self.txtName.setGeometry(QtCore.QRect(186, 90, 301, 41))
        self.txtName.setObjectName("txtName")
        self.lblName = QtWidgets.QLabel(self.tab)
        self.lblName.setGeometry(QtCore.QRect(40, 95, 111, 31))
        self.lblName.setObjectName("lblName")
        self.txtDNI = QtWidgets.QLineEdit(self.tab)
        self.txtDNI.setGeometry(QtCore.QRect(186, 147, 301, 41))
        self.txtDNI.setObjectName("txtDNI")
        self.lblDNI = QtWidgets.QLabel(self.tab)
        self.lblDNI.setGeometry(QtCore.QRect(40, 150, 111, 31))
        self.lblDNI.setObjectName("lblDNI")
        self.txtPhone = QtWidgets.QLineEdit(self.tab)
        self.txtPhone.setGeometry(QtCore.QRect(186, 207, 301, 41))
        self.txtPhone.setObjectName("txtPhone")
        self.lblPhone = QtWidgets.QLabel(self.tab)
        self.lblPhone.setGeometry(QtCore.QRect(40, 210, 111, 31))
        self.lblPhone.setObjectName("lblPhone")
        self.txtAddres = QtWidgets.QLineEdit(self.tab)
        self.txtAddres.setGeometry(QtCore.QRect(185, 267, 301, 41))
        self.txtAddres.setObjectName("txtAddres")
        self.lblAddres = QtWidgets.QLabel(self.tab)
        self.lblAddres.setGeometry(QtCore.QRect(39, 270, 111, 31))
        self.lblAddres.setObjectName("lblAddres")
        self.lblBirth = QtWidgets.QLabel(self.tab)
        self.lblBirth.setGeometry(QtCore.QRect(39, 325, 131, 31))
        self.lblBirth.setObjectName("lblBirth")
        self.txtBirth = QtWidgets.QLineEdit(self.tab)
        self.txtBirth.setGeometry(QtCore.QRect(185, 322, 301, 41))
        self.txtBirth.setObjectName("txtBirth")
        self.lblTitle = QtWidgets.QLabel(self.tab)
        self.lblTitle.setGeometry(QtCore.QRect(140, 10, 381, 51))
        self.lblTitle.setTextFormat(QtCore.Qt.RichText)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 54, 691, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnSaveUser = QtWidgets.QPushButton(self.tab)
        self.btnSaveUser.setGeometry(QtCore.QRect(130, 420, 141, 51))
        self.btnSaveUser.setStyleSheet("")
        self.btnSaveUser.setObjectName("btnSaveUser")
        self.lblBanner = QtWidgets.QLabel(self.tab)
        self.lblBanner.setGeometry(QtCore.QRect(0, 510, 681, 41))
        self.lblBanner.setText("")
        self.lblBanner.setTextFormat(QtCore.Qt.RichText)
        self.lblBanner.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBanner.setObjectName("lblBanner")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(0, 510, 691, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabMain.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.txtDNIRegister = QtWidgets.QLineEdit(self.tab_2)
        self.txtDNIRegister.setGeometry(QtCore.QRect(180, 20, 301, 41))
        self.txtDNIRegister.setObjectName("txtDNIRegister")
        self.lblDNIRegister = QtWidgets.QLabel(self.tab_2)
        self.lblDNIRegister.setGeometry(QtCore.QRect(55, 26, 111, 31))
        self.lblDNIRegister.setObjectName("lblDNIRegister")
        self.tabMain.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.lblName.setText(QtWidgets.QApplication.translate("Dialog", "Nombre Completo", None, -1))
        self.lblDNI.setText(QtWidgets.QApplication.translate("Dialog", "Cédula", None, -1))
        self.lblPhone.setText(QtWidgets.QApplication.translate("Dialog", "Celular", None, -1))
        self.lblAddres.setText(QtWidgets.QApplication.translate("Dialog", "Dirección", None, -1))
        self.lblBirth.setText(QtWidgets.QApplication.translate("Dialog", "Fecha de Nacimiento", None, -1))
        self.txtBirth.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "dd/mm/aaaa", None, -1))
        self.lblTitle.setText(QtWidgets.QApplication.translate("Dialog", "REGISTRAR NUEVO USUARIO", None, -1))
        self.btnSaveUser.setText(QtWidgets.QApplication.translate("Dialog", "Guardar", None, -1))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab), QtWidgets.QApplication.translate("Dialog", "Nuevo Usuario", None, -1))
        self.lblDNIRegister.setText(QtWidgets.QApplication.translate("Dialog", "Cédula", None, -1))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tab_2), QtWidgets.QApplication.translate("Dialog", "Registrar Compra", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
