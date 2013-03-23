# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from interfaces.alunoEditorUi import Ui_Form

from cartao_dialog import CartaoDialog
import models

class AlunoEditor(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.item=None
    
    def get_rfid_card(self):  
        dialog = CartaoDialog(self)
        if dialog.exec_():
            value = dialog.get_value()
            if value:
                self.ui.cartaoLineEdit.setText(unicode(value))

    def editar(self, item):
        """Carregando o conteudo do item no formulário"""
        self.item = item

        aluno = models.Aluno.get_by(matricula = unicode(self.item.text(1)))

        self.ui.nomeLineEdit.setText(aluno.nome)
        self.ui.matriculaLineEdit.setText(aluno.matricula)
        self.ui.cartaoLineEdit.setText(unicode(aluno.rfid_card))
        
        self.show()
        
    def salvar(self):

        aluno = models.Aluno.get_by(matricula = unicode(self.item.text(1)))
 
        aluno.nome = unicode(self.ui.nomeLineEdit.text())
        aluno.matricula = unicode(self.ui.matriculaLineEdit.text())
        aluno.rfid_card = unicode(self.ui.cartaoLineEdit.text())
        
        try:
            models.saveData()
        except:
            models.rollBack()
            error = QtGui.QErrorMessage(parent=self)
            error.showMessage(u'Não foi possível salvar os dados. Verifique duplicidade da matrícula ou cartão.')
            
            return
        
        self.item.setText(0, aluno.nome)
        self.item.setText(1, aluno.matricula)
        self.hide()