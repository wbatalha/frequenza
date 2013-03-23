# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces/aluno_editor.ui'
#
# Created: Wed Mar 13 10:38:11 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(324, 160)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cartaoLineEdit = QtGui.QLineEdit(Form)
        self.cartaoLineEdit.setEnabled(False)
        self.cartaoLineEdit.setAccessibleName(_fromUtf8(""))
        self.cartaoLineEdit.setAccessibleDescription(_fromUtf8(""))
        self.cartaoLineEdit.setAutoFillBackground(False)
        self.cartaoLineEdit.setPlaceholderText(_fromUtf8(""))
        self.cartaoLineEdit.setObjectName(_fromUtf8("cartaoLineEdit"))
        self.horizontalLayout_3.addWidget(self.cartaoLineEdit)
        self.cartaoPushButton = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/rfid-icon_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cartaoPushButton.setIcon(icon)
        self.cartaoPushButton.setObjectName(_fromUtf8("cartaoPushButton"))
        self.horizontalLayout_3.addWidget(self.cartaoPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.matriculaLineEdit = QtGui.QLineEdit(Form)
        self.matriculaLineEdit.setObjectName(_fromUtf8("matriculaLineEdit"))
        self.horizontalLayout_2.addWidget(self.matriculaLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.nomeLineEdit = QtGui.QLineEdit(Form)
        self.nomeLineEdit.setObjectName(_fromUtf8("nomeLineEdit"))
        self.horizontalLayout.addWidget(self.nomeLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.salvarPushButton = QtGui.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/floppy_2_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvarPushButton.setIcon(icon1)
        self.salvarPushButton.setObjectName(_fromUtf8("salvarPushButton"))
        self.gridLayout.addWidget(self.salvarPushButton, 3, 0, 1, 1)
        self.label_3.setBuddy(self.cartaoLineEdit)
        self.label_2.setBuddy(self.matriculaLineEdit)
        self.label.setBuddy(self.nomeLineEdit)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cartaoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.get_rfid_card)
        QtCore.QObject.connect(self.salvarPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.salvar)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nomeLineEdit, self.matriculaLineEdit)
        Form.setTabOrder(self.matriculaLineEdit, self.cartaoLineEdit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Editar Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Cartão:", None, QtGui.QApplication.UnicodeUTF8))
        self.cartaoLineEdit.setText(QtGui.QApplication.translate("Form", "Ler Cartão", None, QtGui.QApplication.UnicodeUTF8))
        self.cartaoPushButton.setText(QtGui.QApplication.translate("Form", "Ler Cartão", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Matrícula:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nome:", None, QtGui.QApplication.UnicodeUTF8))
        self.salvarPushButton.setText(QtGui.QApplication.translate("Form", "Salvar", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

