#!/bin/sh

pyrcc4 icons.qrc -o icons_rc.py
pyuic4 interfaces/window.ui -o interfaces/windowUi.py -x
pyuic4 interfaces/aluno_editor.ui -o interfaces/alunoEditorUi.py -x
pyuic4 interfaces/turma_dialog.ui -o interfaces/turmaDialogUi.py -x
pyuic4 interfaces/aula_dialog.ui -o interfaces/aulaDialogUi.py -x
pyuic4 interfaces/cartao_dialog.ui -o interfaces/cartaoDialogUi.py -x
pyuic4 interfaces/arduino_dialog.ui -o interfaces/arduinoDialogUi.py -x
pyuic4 interfaces/chamada_dialog.ui -o interfaces/chamadaDialogUi.py -x