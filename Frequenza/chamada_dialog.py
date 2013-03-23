# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from interfaces.chamadaDialogUi import Ui_Dialog

from cartao_utils import LerMultiplosCartoes

import models

class ChamadaDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, aula=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.aula = aula
        self.turmaLabel.setText("Turma: %s."%(unicode(self.aula.turma)))
        self.aulaLabel.setText("Aula: %s - %s."
                               %(self.aula.conteudo,
                                 self.aula.data.strftime("%d/%m/%Y")))
        
        self.alunosList.clear()
        for aluno in self.aula.turma.alunos:
            item = QtGui.QTreeWidgetItem(["Falta", aluno.nome, aluno.matricula])
            aluno_aula = models.AlunoAula.get_by(aluno=aluno, aula=self.aula)
            if aluno_aula:
                if aluno_aula.presente:
                    item.setCheckState(0, QtCore.Qt.Checked)
                    item.setText(0, "Presente")
                else:
                    item.setCheckState(0, QtCore.Qt.Unchecked)
            else:
                item.setCheckState(0, QtCore.Qt.Unchecked)
            self.alunosList.addTopLevelItem(item)

        serial = self.parent().ser
        self.thread = LerMultiplosCartoes(serial)
        self.connect(self.thread, QtCore.SIGNAL("card(QString)"), self.marcar)
        self.connect(self.thread, QtCore.SIGNAL("erro()"), self.erro_serial)
        self.thread.start()

            
    def on_alunosList_itemChanged(self, item, column):
        if item.checkState(0):
            item.setText(0, "Presente")
        else:
            item.setText(0, "Falta")
    
    def erro_serial(self):
        msg = u"""A chamada foi iniciada, mas a leitura de cartão não está funcionado.
        Verifique a configuração da plataforma Arduino®."""
        QtGui.QMessageBox.information(self, 'Iniciar Chamada', msg,
                                                QtGui.QMessageBox.Ok)
            
    def marcar(self, card):
        numItems = self.alunosList.topLevelItemCount()
        aluno = models.Aluno.get_by(rfid_card=unicode(card))
        if aluno:
            for i in range(numItems):
                item = self.alunosList.topLevelItem(i)
                if item.text(2) == aluno.matricula:
                    item.setCheckState(0, QtCore.Qt.Checked)
                    break
    
    def salvar(self):
        numItems = self.alunosList.topLevelItemCount()
        
        for i in range(numItems):
            item = self.alunosList.topLevelItem(i)
            aluno = models.Aluno.get_by(matricula=unicode(item.text(2)))
            aluno_aula = models.AlunoAula.get_by(aluno=aluno, aula=self.aula)
            
            if not aluno_aula:
                aluno_aula = models.AlunoAula()
                aluno_aula.aluno = aluno
                aluno_aula.aula = self.aula
            if item.checkState(0):
                aluno_aula.presente = True
            else:
                aluno_aula.presente = False
            models.saveData()
    