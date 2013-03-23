# -*- coding: utf-8 -*-
import os,sys, datetime
from uuid import uuid4
from serial import Serial
# Import Qt modules
from PyQt4 import QtCore,QtGui
# Importando módulos de Ui's
from interfaces.windowUi import Ui_MainWindow
from turma_dialog import TurmaDialog
from aula_dialog import AulaDialog
from arduino_dialog import ArduinoDialog
from chamada_dialog import ChamadaDialog
# Import do banco de dados
import models
# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Padrã em apps Qt
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.alunoEditorWidget.hide()
        
        self.ser = Serial()
        self.ser.port = "/dev/ttyUSB0"
        self.ser.baudrate = 19200
        
        self.ui.alunosList.clear()
        self.ui.aulasList.clear()
        
        self.popular_comboBox_Turmas()
        self.popular_alunosList(self.ui.alunosList2)
        
    def popular_comboBox_Turmas(self):
        """populando combobox de turmas"""
        self.ui.turmasComboBox.clear()
        self.ui.turmasComboBox2.clear()
        for turma in models.Turma.query.all():
            self.ui.turmasComboBox.addItem("%s"%(turma.__repr__()), turma.id)
            self.ui.turmasComboBox2.addItem("%s"%(turma.__repr__()), turma.id)
    
    def popular_alunosList(self, alunos_list, turma_id=None):
        """Preenche a lista de alunos em função da turma escolhida
        """
        if turma_id:
            turma = models.Turma.get_by(id=turma_id)
            if not turma:
                error = QtGui.QErrorMessage(parent=self)
                error.showMessage("""Não foi possível encontrar a 
                                    turma desejada.""")
                return 
            
            for aluno in turma.alunos:
                item = QtGui.QTreeWidgetItem([aluno.nome, aluno.matricula])
                alunos_list.addTopLevelItem(item)
        
        else:
            for aluno in models.Aluno.query.all():
                item = QtGui.QTreeWidgetItem([aluno.nome, aluno.matricula])
                alunos_list.addTopLevelItem(item)
            
    def popular_aulasList(self, turma_id):
        """Preenche a lista de aulas em função da turma escolhida
        """
        turma = models.Turma.get_by(id=turma_id)
        if not turma:
            return
        for aula in turma.aulas:
            item = QtGui.QTreeWidgetItem([aula.conteudo,
                                          aula.data.strftime("%d/%m/%Y")])
            item.aula_id = aula.id
            self.ui.aulasList.addTopLevelItem(item)
     
    @QtCore.pyqtSlot('int')    
    def on_turmasComboBox_currentIndexChanged(self, index = None):
        """
        Preenche a lista de alunos dinâmicamente toda vez que o valor do combo
        box de turmas for alterado.
        """
        value = self.ui.turmasComboBox.itemData(index).toInt()
        alunos_list = self.ui.alunosList
        if value[1]:
            turma_id = value[0]
            self.ui.alunosList.clear()
            self.popular_alunosList(alunos_list, turma_id)
            self.ui.aulasList.clear()
            self.popular_aulasList(turma_id)
        else:
            return
        
    @QtCore.pyqtSlot('int')    
    def on_turmasComboBox2_currentIndexChanged(self, index = None):
        """
        Preenche a lista de alunos dinâmicamente toda vez que o valor do combo
        box de turmas for alterado.
        """
        value = self.ui.turmasComboBox2.itemData(index).toInt()
        alunos_list = self.ui.alunosList3
        if value[1]:
            turma_id = value[0]
            self.ui.alunosList3.clear()
            self.popular_alunosList(alunos_list, turma_id)
        else:
            return
        
    @QtCore.pyqtSlot('bool')
    def on_actionNova_Aula_triggered(self, checked=None):
        cb_index = self.ui.turmasComboBox.currentIndex()
        aux = self.ui.turmasComboBox.itemData(cb_index).toInt()
        if aux[1]:
            turma_id = aux[0]
            turma = models.Turma.get_by(id=turma_id)
            dialog = AulaDialog(self)
            if dialog.exec_():
                values = dialog.get_values()
                if not values[0]:
                    error = QtGui.QErrorMessage(self)
                    error.showMessage(u'Não foi possível marcar a aula.')
                    return
                    
                aula = models.Aula(conteudo=unicode(values[0]), data=values[1])
                aula.turma = turma
            
                try:
                    models.saveData()
                except:
                    error = QtGui.QErrorMessage(self)
                    error.showMessage(u'Não foi possível marcar a aula.')
                    return
                
                item = QtGui.QTreeWidgetItem([aula.conteudo, str(aula.data)])
                item.aula_id = aula.id
                self.ui.aulasList.addTopLevelItem(item)
                self.ui.aulasList.setCurrentItem(item)
    
    @QtCore.pyqtSlot('bool')
    def on_actionEditar_Aula_triggered(self, checked=None):
        item = self.ui.aulasList.currentItem()
        aula_id = item.aula_id
        aula = models.Aula.get_by(id = aula_id)
        
        dialog = AulaDialog(self, aula)
        if dialog.exec_():
            values = dialog.get_values()
            if not values[0]:
                error = QtGui.QErrorMessage(self)
                error.showMessage('Não foi possível editar a aula.')
                return
            
            aula.conteudo = unicode(values[0])
            aula.data = values[1]
            try:
                models.saveData()
            except:
                error = QtGui.QErrorMessage(self)
                error.showMessage('Não foi possível editar a aula')
                return
            
            item.setText(0, aula.conteudo)
            item.setText(1, str(aula.data))
            
    @QtCore.pyqtSlot('bool')
    def on_actionExcluir_Aula_triggered(self, checked=None):
        item = self.ui.aulasList.currentItem()
        aula_id = item.aula_id
        aula = models.Aula.get_by(id = aula_id)
        
        reply = QtGui.QMessageBox.question(self, 'Excluir Aula',
                        "Tem certeza que deseja excluir esta aula: %s?"
                         %(unicode(aula)), QtGui.QMessageBox.Yes | 
                        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if not reply == QtGui.QMessageBox.Yes: return
        
        aula.delete()
        models.saveData()
        
        index = self.ui.aulasList.indexOfTopLevelItem(item)
        self.ui.aulasList.takeTopLevelItem(index)

    @QtCore.pyqtSlot('bool')
    def on_actionCadastrar_Aluno_triggered(self, checked=None):
        rfid = unicode(uuid4())
        matr = unicode(uuid4())
        aluno = models.Aluno(nome=u'Novo Aluno', matricula=matr,rfid_card=rfid)      
        
        try:
            models.saveData()
        except:
            error = QtGui.QErrorMessage(self)
            error.showMessage('Não foi possível cadastar o aluno.')
            return
            
        item = QtGui.QTreeWidgetItem([aluno.nome, aluno.matricula])
        self.ui.alunosList2.addTopLevelItem(item)
        self.ui.alunosList2.setCurrentItem(item)
    
    @QtCore.pyqtSlot('bool')
    def on_actionExcluir_Aluno_triggered(self, checked=None):
        item = self.ui.alunosList2.currentItem()
        matr = unicode(item.text(1))
        
        aluno = models.Aluno.get_by(matricula = matr)
        
        reply = QtGui.QMessageBox.question(self, 'Excluir Aluno',
                        "Tem certeza que deseja excluir este aluno: %s?"
                         %(unicode(aluno)), QtGui.QMessageBox.Yes | 
                        QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if not reply == QtGui.QMessageBox.Yes: return
        
        aluno.delete()
        models.saveData()
        
        index = self.ui.alunosList2.indexOfTopLevelItem(item)
        self.ui.alunosList2.takeTopLevelItem(index)
    
    @QtCore.pyqtSlot('bool')
    def on_actionAdicionar_Aluno_triggered(self, checked=None):
        item = self.ui.alunosList2.currentItem()
        matr = unicode(item.text(1))
        aluno = models.Aluno.get_by(matricula = matr)
        
        cb_index = self.ui.turmasComboBox2.currentIndex()
        aux = self.ui.turmasComboBox2.itemData(cb_index).toInt()
        
        if aux[1]:
            turma_id = aux[0]
            turma = models.Turma.get_by(id=turma_id)
            
            if not turma.alunos.count(aluno):
                turma.alunos.append(aluno)
            
                item2 = QtGui.QTreeWidgetItem([aluno.nome, aluno.matricula])
                self.ui.alunosList3.addTopLevelItem(item2)
                self.ui.alunosList3.setCurrentItem(item2)
                models.saveData()
            else:
                error = QtGui.QErrorMessage(parent=self)
                error.showMessage(u'Este aluno já pertence a esta turma.')
                
    @QtCore.pyqtSlot('bool')
    def on_actionRemover_Aluno_triggered(self, checked=None):
        item = self.ui.alunosList3.currentItem()
        matr = unicode(item.text(1))
        aluno = models.Aluno.get_by(matricula = matr)
        
        cb_index = self.ui.turmasComboBox2.currentIndex()
        aux = self.ui.turmasComboBox2.itemData(cb_index).toInt()
        
        if aux[1]:
            turma_id = aux[0]
            turma = models.Turma.get_by(id=turma_id)
            
            if turma.alunos.count(aluno):
                turma.alunos.remove(aluno)
            
                item_index = self.ui.alunosList3.indexOfTopLevelItem(item)
                self.ui.alunosList3.takeTopLevelItem(item_index)
                models.saveData()
            else:
                error = QtGui.QErrorMessage(parent=self)
                error.showMessage(u'Não foi possível remover o aluno.')
            
    @QtCore.pyqtSlot('bool')
    def on_actionCadastrar_Turma_triggered(self, checked=None):
        dialog = TurmaDialog(self)
        if dialog.exec_():
            values = dialog.get_values()
            try:
                if not values[0]: raise Exception()
                turma = models.Turma(disciplina=unicode(values[0]),
                                     ano=values[1], semestre=values[2])
                models.saveData()
                QtGui.QMessageBox.information(self, 'Cadastrar turma',
                                              'Turma cadastrada com sucesso.',
                                              QtGui.QMessageBox.Ok)
            except:
                error = QtGui.QErrorMessage(self)
                error.showMessage(u'Não foi possível cadastrar a nova turma.')
                return
            
            self.popular_comboBox_Turmas()
    
    @QtCore.pyqtSlot('bool')
    def on_actionEditar_Turma_triggered(self, checked=None):
        cb_index = self.ui.turmasComboBox2.currentIndex()
        aux = self.ui.turmasComboBox2.itemData(cb_index).toInt()
        
        if aux[1]:
            turma_id = aux[0]
            turma = models.Turma.get_by(id=turma_id)
            
            dialog = TurmaDialog(self, turma=turma)
            if dialog.exec_():
                values = dialog.get_values()
                if not values[0]:
                    error = QtGui.QErrorMessage(self)
                    error.setWindowTitle('Erro ao Editar a Turma')
                    error.showMessage(u"""Não foi possível editar a nova turma.
                                         Verifique os dados de entrada.""")
                    return
                    
                turma.disciplina = unicode(values[0])
                turma.ano = values[1]
                turma.semestre = values[2]
                
                try:
                    models.saveData()
                except:
                    error = QtGui.QErrorMessage(self)
                    error.showMessage(u"""Não foi possível cadastrar
                                         a nova turma.""")
                    return
                self.popular_comboBox_Turmas()
    
    @QtCore.pyqtSlot('bool')            
    def on_actionExcluir_Turma_triggered(self, checked=None):
        cb_index = self.ui.turmasComboBox2.currentIndex()
        aux = self.ui.turmasComboBox2.itemData(cb_index).toInt()
        if aux[1]:
            turma_id = aux[0]
            turma = models.Turma.get_by(id=turma_id)
            
            reply = QtGui.QMessageBox.question(self, 'Mensagem',
                        "Tem certeza que deseja excluir esta turma: %s?"
                         %(unicode(turma)), QtGui.QMessageBox.Yes | 
                        QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if not reply == QtGui.QMessageBox.Yes: return
         
            turma.delete()
            models.saveData()
            
            self.ui.turmasComboBox2.removeItem(cb_index)
            self.ui.turmasComboBox.removeItem(cb_index)
    
    @QtCore.pyqtSlot('bool')
    def on_actionConfiguracoes_Arduino_triggered(self, checked=None):
        dialog =  ArduinoDialog(self)
        if dialog.exec_():
            values = dialog.get_values()
            self.ser.port = values[0]
            self.ser.baudrate = values[1]
    
    @QtCore.pyqtSlot('bool')
    def on_actionIniciar_Chamada_triggered(self, checked=None):
        aula_id = self.ui.aulasList.currentItem().aula_id
        aula = models.Aula.get_by(id=aula_id)
        
        dialog = ChamadaDialog(self, aula)
        exe = dialog.exec_()
        dialog.thread.exiting=True
        if exe: dialog.salvar()
           
                
    @QtCore.pyqtSlot('int')
    def on_tabWidget_currentChanged(self, index=None):
        if index==0:
            #falses
            self.ui.actionNova_Aula.setEnabled(False)
            self.ui.actionEditar_Aula.setEnabled(False)
            self.ui.actionExcluir_Aula.setEnabled(False)
            self.ui.actionIniciar_Chamada.setEnabled(False)
            #trues
            self.ui.actionCadastrar_Aluno.setEnabled(True)
            if self.ui.alunosList2.currentItem():
                self.ui.actionAdicionar_Aluno.setEnabled(True)
                self.ui.actionExcluir_Aluno.setEnabled(True)
            if self.ui.alunosList3.currentItem():
                self.ui.actionRemover_Aluno.setEnabled(True)            
            self.ui.actionCadastrar_Turma.setEnabled(True)
            self.ui.actionEditar_Turma.setEnabled(True)
            self.ui.actionExcluir_Turma.setEnabled(True)
        elif index==1:
            #falses 
            self.ui.actionAdicionar_Aluno.setEnabled(False)
            self.ui.actionCadastrar_Aluno.setEnabled(False)
            self.ui.actionCadastrar_Turma.setEnabled(False)
            self.ui.actionEditar_Turma.setEnabled(False)
            self.ui.actionExcluir_Turma.setEnabled(False)
            self.ui.actionExcluir_Turma.setEnabled(False)
            self.ui.actionExcluir_Aluno.setEnabled(False)
            self.ui.actionRemover_Aluno.setEnabled(False)
            #trues
            self.ui.actionNova_Aula.setEnabled(True)
            if self.ui.aulasList.currentItem():
                self.ui.actionEditar_Aula.setEnabled(True)
                self.ui.actionExcluir_Aula.setEnabled(True)
                self.ui.actionIniciar_Chamada.setEnabled(True)
            
    def on_alunosList2_currentItemChanged(self, current=None, previous=None):
        if current:
            self.ui.addAlunoPushButton.setEnabled(True)
            self.ui.excluirAlunoPushButton.setEnabled(True)
            self.ui.actionExcluir_Aluno.setEnabled(True)
            self.ui.actionAdicionar_Aluno.setEnabled(True)
            self.ui.alunoEditorWidget.editar(current)
        else:
            self.ui.addAlunoPushButton.setEnabled(False)
            self.ui.actionExcluir_Aluno.setEnabled(False)
            self.ui.actionAdicionar_Aluno.setEnabled(False)
    
    def on_alunosList3_currentItemChanged(self, current=None, previous=None):
        if current:
            self.ui.removeAlunoPushButton.setEnabled(True)
            self.ui.actionRemover_Aluno.setEnabled(True)
        else:
            self.ui.removeAlunoPushButton.setEnabled(False)
            self.ui.actionRemover_Aluno.setEnabled(False)
    
    def on_aulasList_currentItemChanged(self, current=None, previous=None):
        if current:
            self.ui.actionEditar_Aula.setEnabled(True)
            self.ui.editarAulaPushButton.setEnabled(True)
            self.ui.actionExcluir_Aula.setEnabled(True)
            self.ui.excluirAulaPushButton.setEnabled(True)
            self.ui.iniciarChamadaPushButton.setEnabled(True)
            self.ui.actionIniciar_Chamada.setEnabled(True)
        else:
            self.ui.actionEditar_Aula.setEnabled(False)
            self.ui.editarAulaPushButton.setEnabled(False)
            self.ui.actionExcluir_Aula.setEnabled(False)
            self.ui.excluirAulaPushButton.setEnabled(False)
            self.ui.iniciarChamadaPushButton.setEnabled(False)
            self.ui.actionIniciar_Chamada.setEnabled(False)
    
def main():
    #inicializando banco de dados
    models.initDB()
    # Comandos padrão do pyqt
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.showMaximized()
    window.ui.actionConfiguracoes_Arduino.trigger()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()