# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces/window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(742, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/rfid-icon_2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.alunosList2 = QtGui.QTreeWidget(self.tab)
        self.alunosList2.setAcceptDrops(False)
        self.alunosList2.setAutoFillBackground(False)
        self.alunosList2.setAlternatingRowColors(True)
        self.alunosList2.setRootIsDecorated(False)
        self.alunosList2.setItemsExpandable(True)
        self.alunosList2.setAllColumnsShowFocus(True)
        self.alunosList2.setObjectName(_fromUtf8("alunosList2"))
        self.verticalLayout_3.addWidget(self.alunosList2)
        self.alunoEditorWidget = AlunoEditor(self.tab)
        self.alunoEditorWidget.setObjectName(_fromUtf8("alunoEditorWidget"))
        self.verticalLayout_3.addWidget(self.alunoEditorWidget)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.excluirAlunoPushButton = QtGui.QPushButton(self.tab)
        self.excluirAlunoPushButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/delete_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excluirAlunoPushButton.setIcon(icon1)
        self.excluirAlunoPushButton.setObjectName(_fromUtf8("excluirAlunoPushButton"))
        self.horizontalLayout_5.addWidget(self.excluirAlunoPushButton)
        self.novoAlunoPushButton = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/education_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.novoAlunoPushButton.setIcon(icon2)
        self.novoAlunoPushButton.setObjectName(_fromUtf8("novoAlunoPushButton"))
        self.horizontalLayout_5.addWidget(self.novoAlunoPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.addAlunoPushButton = QtGui.QPushButton(self.tab)
        self.addAlunoPushButton.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/right_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAlunoPushButton.setIcon(icon3)
        self.addAlunoPushButton.setObjectName(_fromUtf8("addAlunoPushButton"))
        self.verticalLayout_5.addWidget(self.addAlunoPushButton)
        self.removeAlunoPushButton = QtGui.QPushButton(self.tab)
        self.removeAlunoPushButton.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/left_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeAlunoPushButton.setIcon(icon4)
        self.removeAlunoPushButton.setObjectName(_fromUtf8("removeAlunoPushButton"))
        self.verticalLayout_5.addWidget(self.removeAlunoPushButton)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.turmasComboBox2 = QtGui.QComboBox(self.tab)
        self.turmasComboBox2.setObjectName(_fromUtf8("turmasComboBox2"))
        self.horizontalLayout_3.addWidget(self.turmasComboBox2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.alunosList3 = QtGui.QTreeWidget(self.tab)
        self.alunosList3.setAlternatingRowColors(True)
        self.alunosList3.setRootIsDecorated(False)
        self.alunosList3.setAllColumnsShowFocus(True)
        self.alunosList3.setObjectName(_fromUtf8("alunosList3"))
        self.verticalLayout_4.addWidget(self.alunosList3)
        self.novaTurmaPushButton = QtGui.QPushButton(self.tab)
        self.novaTurmaPushButton.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/user_group_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.novaTurmaPushButton.setIcon(icon5)
        self.novaTurmaPushButton.setObjectName(_fromUtf8("novaTurmaPushButton"))
        self.verticalLayout_4.addWidget(self.novaTurmaPushButton)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.excluirTurmaPushButton = QtGui.QPushButton(self.tab)
        self.excluirTurmaPushButton.setEnabled(True)
        self.excluirTurmaPushButton.setIcon(icon1)
        self.excluirTurmaPushButton.setObjectName(_fromUtf8("excluirTurmaPushButton"))
        self.horizontalLayout_4.addWidget(self.excluirTurmaPushButton)
        self.editarTurmaPushButton = QtGui.QPushButton(self.tab)
        self.editarTurmaPushButton.setEnabled(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/edit_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editarTurmaPushButton.setIcon(icon6)
        self.editarTurmaPushButton.setObjectName(_fromUtf8("editarTurmaPushButton"))
        self.horizontalLayout_4.addWidget(self.editarTurmaPushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, icon2, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.turmasComboBox = QtGui.QComboBox(self.tab_2)
        self.turmasComboBox.setObjectName(_fromUtf8("turmasComboBox"))
        self.horizontalLayout.addWidget(self.turmasComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.alunosList = QtGui.QTreeWidget(self.tab_2)
        self.alunosList.setAutoFillBackground(False)
        self.alunosList.setAlternatingRowColors(True)
        self.alunosList.setRootIsDecorated(False)
        self.alunosList.setUniformRowHeights(True)
        self.alunosList.setAllColumnsShowFocus(True)
        self.alunosList.setObjectName(_fromUtf8("alunosList"))
        item_0 = QtGui.QTreeWidgetItem(self.alunosList)
        item_0 = QtGui.QTreeWidgetItem(self.alunosList)
        item_0 = QtGui.QTreeWidgetItem(self.alunosList)
        item_0 = QtGui.QTreeWidgetItem(self.alunosList)
        self.verticalLayout.addWidget(self.alunosList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.aulasList = QtGui.QTreeWidget(self.tab_2)
        self.aulasList.setAlternatingRowColors(True)
        self.aulasList.setRootIsDecorated(False)
        self.aulasList.setUniformRowHeights(True)
        self.aulasList.setAnimated(False)
        self.aulasList.setAllColumnsShowFocus(True)
        self.aulasList.setObjectName(_fromUtf8("aulasList"))
        item_0 = QtGui.QTreeWidgetItem(self.aulasList)
        item_0 = QtGui.QTreeWidgetItem(self.aulasList)
        item_0 = QtGui.QTreeWidgetItem(self.aulasList)
        item_0 = QtGui.QTreeWidgetItem(self.aulasList)
        self.verticalLayout_2.addWidget(self.aulasList)
        self.novaAulaPushButton = QtGui.QPushButton(self.tab_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/lessons_48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.novaAulaPushButton.setIcon(icon7)
        self.novaAulaPushButton.setIconSize(QtCore.QSize(24, 24))
        self.novaAulaPushButton.setObjectName(_fromUtf8("novaAulaPushButton"))
        self.verticalLayout_2.addWidget(self.novaAulaPushButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.excluirAulaPushButton = QtGui.QPushButton(self.tab_2)
        self.excluirAulaPushButton.setEnabled(False)
        self.excluirAulaPushButton.setIcon(icon1)
        self.excluirAulaPushButton.setIconSize(QtCore.QSize(24, 24))
        self.excluirAulaPushButton.setObjectName(_fromUtf8("excluirAulaPushButton"))
        self.horizontalLayout_2.addWidget(self.excluirAulaPushButton)
        self.editarAulaPushButton = QtGui.QPushButton(self.tab_2)
        self.editarAulaPushButton.setEnabled(False)
        self.editarAulaPushButton.setIcon(icon6)
        self.editarAulaPushButton.setObjectName(_fromUtf8("editarAulaPushButton"))
        self.horizontalLayout_2.addWidget(self.editarAulaPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.iniciarChamadaPushButton = QtGui.QPushButton(self.tab_2)
        self.iniciarChamadaPushButton.setEnabled(False)
        self.iniciarChamadaPushButton.setIcon(icon)
        self.iniciarChamadaPushButton.setIconSize(QtCore.QSize(24, 24))
        self.iniciarChamadaPushButton.setObjectName(_fromUtf8("iniciarChamadaPushButton"))
        self.verticalLayout_2.addWidget(self.iniciarChamadaPushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, icon7, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTurma = QtGui.QMenu(self.menubar)
        self.menuTurma.setObjectName(_fromUtf8("menuTurma"))
        self.menuAluno = QtGui.QMenu(self.menubar)
        self.menuAluno.setObjectName(_fromUtf8("menuAluno"))
        self.menuAula = QtGui.QMenu(self.menubar)
        self.menuAula.setObjectName(_fromUtf8("menuAula"))
        self.menuConfigura_es = QtGui.QMenu(self.menubar)
        self.menuConfigura_es.setObjectName(_fromUtf8("menuConfigura_es"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExcluir_Turma = QtGui.QAction(MainWindow)
        self.actionExcluir_Turma.setCheckable(False)
        self.actionExcluir_Turma.setEnabled(True)
        self.actionExcluir_Turma.setIcon(icon1)
        self.actionExcluir_Turma.setObjectName(_fromUtf8("actionExcluir_Turma"))
        self.actionCadastrar_Turma = QtGui.QAction(MainWindow)
        self.actionCadastrar_Turma.setIcon(icon5)
        self.actionCadastrar_Turma.setObjectName(_fromUtf8("actionCadastrar_Turma"))
        self.actionCadastrar_Aluno = QtGui.QAction(MainWindow)
        self.actionCadastrar_Aluno.setIcon(icon2)
        self.actionCadastrar_Aluno.setObjectName(_fromUtf8("actionCadastrar_Aluno"))
        self.actionNova_Aula = QtGui.QAction(MainWindow)
        self.actionNova_Aula.setEnabled(False)
        self.actionNova_Aula.setIcon(icon7)
        self.actionNova_Aula.setObjectName(_fromUtf8("actionNova_Aula"))
        self.actionAdicionar_Aluno = QtGui.QAction(MainWindow)
        self.actionAdicionar_Aluno.setEnabled(False)
        self.actionAdicionar_Aluno.setIcon(icon3)
        self.actionAdicionar_Aluno.setObjectName(_fromUtf8("actionAdicionar_Aluno"))
        self.actionRemover_Aluno = QtGui.QAction(MainWindow)
        self.actionRemover_Aluno.setEnabled(False)
        self.actionRemover_Aluno.setIcon(icon4)
        self.actionRemover_Aluno.setObjectName(_fromUtf8("actionRemover_Aluno"))
        self.actionExcluir_Aluno = QtGui.QAction(MainWindow)
        self.actionExcluir_Aluno.setEnabled(False)
        self.actionExcluir_Aluno.setIcon(icon1)
        self.actionExcluir_Aluno.setObjectName(_fromUtf8("actionExcluir_Aluno"))
        self.actionEditar_Turma = QtGui.QAction(MainWindow)
        self.actionEditar_Turma.setEnabled(True)
        self.actionEditar_Turma.setIcon(icon6)
        self.actionEditar_Turma.setObjectName(_fromUtf8("actionEditar_Turma"))
        self.actionEditar_Aula = QtGui.QAction(MainWindow)
        self.actionEditar_Aula.setEnabled(False)
        self.actionEditar_Aula.setIcon(icon6)
        self.actionEditar_Aula.setObjectName(_fromUtf8("actionEditar_Aula"))
        self.actionExcluir_Aula = QtGui.QAction(MainWindow)
        self.actionExcluir_Aula.setEnabled(False)
        self.actionExcluir_Aula.setIcon(icon1)
        self.actionExcluir_Aula.setObjectName(_fromUtf8("actionExcluir_Aula"))
        self.actionConfiguracoes_Arduino = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguracoes_Arduino.setIcon(icon8)
        self.actionConfiguracoes_Arduino.setObjectName(_fromUtf8("actionConfiguracoes_Arduino"))
        self.actionIniciar_Chamada = QtGui.QAction(MainWindow)
        self.actionIniciar_Chamada.setEnabled(False)
        self.actionIniciar_Chamada.setIcon(icon)
        self.actionIniciar_Chamada.setObjectName(_fromUtf8("actionIniciar_Chamada"))
        self.menuTurma.addAction(self.actionCadastrar_Turma)
        self.menuTurma.addSeparator()
        self.menuTurma.addAction(self.actionEditar_Turma)
        self.menuTurma.addAction(self.actionExcluir_Turma)
        self.menuAluno.addAction(self.actionCadastrar_Aluno)
        self.menuAluno.addSeparator()
        self.menuAluno.addAction(self.actionExcluir_Aluno)
        self.menuAluno.addAction(self.actionAdicionar_Aluno)
        self.menuAluno.addAction(self.actionRemover_Aluno)
        self.menuAula.addAction(self.actionNova_Aula)
        self.menuAula.addSeparator()
        self.menuAula.addAction(self.actionIniciar_Chamada)
        self.menuAula.addSeparator()
        self.menuAula.addAction(self.actionEditar_Aula)
        self.menuAula.addAction(self.actionExcluir_Aula)
        self.menuConfigura_es.addAction(self.actionConfiguracoes_Arduino)
        self.menubar.addAction(self.menuAluno.menuAction())
        self.menubar.addAction(self.menuTurma.menuAction())
        self.menubar.addAction(self.menuAula.menuAction())
        self.menubar.addAction(self.menuConfigura_es.menuAction())
        self.toolBar.addAction(self.actionCadastrar_Aluno)
        self.toolBar.addAction(self.actionExcluir_Aluno)
        self.toolBar.addAction(self.actionAdicionar_Aluno)
        self.toolBar.addAction(self.actionRemover_Aluno)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCadastrar_Turma)
        self.toolBar.addAction(self.actionEditar_Turma)
        self.toolBar.addAction(self.actionExcluir_Turma)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNova_Aula)
        self.toolBar.addAction(self.actionIniciar_Chamada)
        self.toolBar.addAction(self.actionEditar_Aula)
        self.toolBar.addAction(self.actionExcluir_Aula)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfiguracoes_Arduino)
        self.label_4.setBuddy(self.alunosList2)
        self.label_5.setBuddy(self.turmasComboBox2)
        self.label.setBuddy(self.turmasComboBox)
        self.label_2.setBuddy(self.alunosList)
        self.label_3.setBuddy(self.aulasList)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.addAlunoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionAdicionar_Aluno.trigger)
        QtCore.QObject.connect(self.removeAlunoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionRemover_Aluno.trigger)
        QtCore.QObject.connect(self.novaTurmaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionCadastrar_Turma.trigger)
        QtCore.QObject.connect(self.novoAlunoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionCadastrar_Aluno.trigger)
        QtCore.QObject.connect(self.editarTurmaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionEditar_Turma.trigger)
        QtCore.QObject.connect(self.excluirTurmaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionExcluir_Turma.trigger)
        QtCore.QObject.connect(self.excluirAulaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionExcluir_Aula.trigger)
        QtCore.QObject.connect(self.editarAulaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionEditar_Aula.trigger)
        QtCore.QObject.connect(self.novaAulaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionNova_Aula.trigger)
        QtCore.QObject.connect(self.excluirAlunoPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionExcluir_Aluno.trigger)
        QtCore.QObject.connect(self.iniciarChamadaPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionIniciar_Chamada.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Frequenza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Alunos:", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList2.setSortingEnabled(True)
        self.alunosList2.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList2.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Matrícula", None, QtGui.QApplication.UnicodeUTF8))
        self.excluirAlunoPushButton.setText(QtGui.QApplication.translate("MainWindow", "Excluir Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.novoAlunoPushButton.setText(QtGui.QApplication.translate("MainWindow", "Novo Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.addAlunoPushButton.setText(QtGui.QApplication.translate("MainWindow", "Adicionar Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAlunoPushButton.setText(QtGui.QApplication.translate("MainWindow", "Remover Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Turmas:", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList3.setSortingEnabled(True)
        self.alunosList3.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList3.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Matrícula", None, QtGui.QApplication.UnicodeUTF8))
        self.novaTurmaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Nova Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.excluirTurmaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Excluir Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.editarTurmaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Editar Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Cadastros", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Turma:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Alunos:", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.setSortingEnabled(True)
        self.alunosList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Matrícula", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.alunosList.isSortingEnabled()
        self.alunosList.setSortingEnabled(False)
        self.alunosList.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.alunosList.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Aulas:", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.setSortingEnabled(True)
        self.aulasList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Conteúdo", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.aulasList.isSortingEnabled()
        self.aulasList.setSortingEnabled(False)
        self.aulasList.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.topLevelItem(2).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.topLevelItem(3).setText(0, QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.aulasList.setSortingEnabled(__sortingEnabled)
        self.novaAulaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Nova Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.excluirAulaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Excluir Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.editarAulaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Editar Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.iniciarChamadaPushButton.setText(QtGui.QApplication.translate("MainWindow", "Iniciar Chamada", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Chamadas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTurma.setTitle(QtGui.QApplication.translate("MainWindow", "Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAluno.setTitle(QtGui.QApplication.translate("MainWindow", "Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAula.setTitle(QtGui.QApplication.translate("MainWindow", "Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfigura_es.setTitle(QtGui.QApplication.translate("MainWindow", "Configurações", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Turma.setText(QtGui.QApplication.translate("MainWindow", "Excluir Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Turma.setToolTip(QtGui.QApplication.translate("MainWindow", "Exclui uma turma permanentemente", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Turma.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadastrar_Turma.setText(QtGui.QApplication.translate("MainWindow", "Cadastrar Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadastrar_Turma.setToolTip(QtGui.QApplication.translate("MainWindow", "Cria uma nova tuma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadastrar_Aluno.setText(QtGui.QApplication.translate("MainWindow", "Cadastrar Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCadastrar_Aluno.setToolTip(QtGui.QApplication.translate("MainWindow", "Cadastra um novo aluno no sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNova_Aula.setText(QtGui.QApplication.translate("MainWindow", "Nova Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNova_Aula.setToolTip(QtGui.QApplication.translate("MainWindow", "Cria uma nova aula para a turma selecionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdicionar_Aluno.setText(QtGui.QApplication.translate("MainWindow", "Adicionar Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdicionar_Aluno.setToolTip(QtGui.QApplication.translate("MainWindow", "Adiciona um aluno à turma selecionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemover_Aluno.setText(QtGui.QApplication.translate("MainWindow", "Remover_Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemover_Aluno.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove o aluno selecionado da turma selecionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Aluno.setText(QtGui.QApplication.translate("MainWindow", "Excluir Aluno", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Aluno.setToolTip(QtGui.QApplication.translate("MainWindow", "Exclui um aluno permanentemente", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Turma.setText(QtGui.QApplication.translate("MainWindow", "Editar Turma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Turma.setToolTip(QtGui.QApplication.translate("MainWindow", "Edita a turma selecionada", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Aula.setText(QtGui.QApplication.translate("MainWindow", "Editar Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Aula.setToolTip(QtGui.QApplication.translate("MainWindow", "Edita a aula selecionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Aula.setText(QtGui.QApplication.translate("MainWindow", "Excluir Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExcluir_Aula.setToolTip(QtGui.QApplication.translate("MainWindow", "Exclui pemanentemente a aula selecionada.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguracoes_Arduino.setText(QtGui.QApplication.translate("MainWindow", "Configurações do Arduino", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguracoes_Arduino.setToolTip(QtGui.QApplication.translate("MainWindow", "Configura a comunicação com a plataforma Arduino®.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIniciar_Chamada.setText(QtGui.QApplication.translate("MainWindow", "Iniciar Chamada", None, QtGui.QApplication.UnicodeUTF8))

from aluno_editor import AlunoEditor
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
