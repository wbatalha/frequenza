# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from interfaces.cartaoDialogUi import Ui_Dialog
from cartao_utils import LerCartao

class CartaoDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.value = None
        
        serial = self.parent().parent().parent().parent().parent().parent().ser
        
        self.thread = LerCartao(self, serial)
        self.connect(self.thread, QtCore.SIGNAL('finished()'), self.accept)
        self.connect(self.thread, QtCore.SIGNAL("erro()"), self.erro_serial)
        self.thread.start()

    def erro_serial(self):
        msg = u"""Não foi possível ler o código do cartão.
        Verifique a configuração da plataforma Arduino®."""
        QtGui.QMessageBox.information(self, u'Ler Cartão', msg,
                                                QtGui.QMessageBox.Ok)
        self.reject()
            
    def get_value(self):
        return self.value