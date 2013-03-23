# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from interfaces.turmaDialogUi import Ui_Dialog

class TurmaDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, turma=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        if turma:
            self.disciplinaLineEdit.setText(turma.disciplina)
            self.anoSpinBox.setValue(turma.ano)
            self.semestreComboBox.setCurrentIndex(turma.semestre-1)
    
    def get_values(self):
        values = []
        values.append(self.disciplinaLineEdit.text())
        values.append(self.anoSpinBox.value())
        values.append(self.semestreComboBox.currentIndex()+1)
        return values