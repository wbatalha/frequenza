# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from datetime import date

from interfaces.aulaDialogUi import Ui_Dialog

class AulaDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, aula=None):
        QtGui.QDialog.__init__(self, parent)
        self.aula = aula
        self.setupUi(self)
        
        if self.aula:
            self.conteudoLineEdit.setText(self.aula.conteudo)
            dt = self.aula.data
            self.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
        else:
            dt = date.today()
            self.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
        
    def get_values(self):
        values=[]
        values.append(self.conteudoLineEdit.text())
        values.append(self.dateEdit.date().toPyDate())
        return values