# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces/arduino_dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(290, 134)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.portComboBox = QtGui.QComboBox(Dialog)
        self.portComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.portComboBox.setObjectName(_fromUtf8("portComboBox"))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.portComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.portComboBox, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.baudRateSpinBox = QtGui.QSpinBox(Dialog)
        self.baudRateSpinBox.setEnabled(False)
        self.baudRateSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.baudRateSpinBox.setMaximum(19200)
        self.baudRateSpinBox.setProperty("value", 19200)
        self.baudRateSpinBox.setObjectName(_fromUtf8("baudRateSpinBox"))
        self.gridLayout.addWidget(self.baudRateSpinBox, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configuração da Plataforma Arduino®.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Configuração da Plataforma Arduino®.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Porta:", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB0", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB1", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB2", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB3", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB4", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB5", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(6, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB6", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(7, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB7", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(8, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB8", None, QtGui.QApplication.UnicodeUTF8))
        self.portComboBox.setItemText(9, QtGui.QApplication.translate("Dialog", "/dev/ttyUSB9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Baud Rate:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

