# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog

from interfaces.arduinoDialogUi import Ui_Dialog

class ArduinoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    def get_values(self):
        values = []
        values.append(str(self.portComboBox.currentText()))
        values.append(self.baudRateSpinBox.value())
        return values