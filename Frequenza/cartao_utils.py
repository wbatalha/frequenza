# coding -*- utf-8 -*-
from PyQt4 import QtCore

class LerCartao(QtCore.QThread):
    def __init__(self, widget, serial):
        QtCore.QThread.__init__(self)
        self.widget = widget
        self.serial = serial
    
    def __del__(self):
        if self.serial.isOpen():
            self.serial.close()    
    
    def run(self):
        if not self.serial.isOpen():
            self.serial.setTimeout(10)
            try:
                self.serial.open()
            except:
                self.emit(QtCore.SIGNAL("erro()"))
                return

        res = self.serial.readline()
        self.serial.close()
        
        if res.startswith('\x00\xff'):
            res = res[2:]
        if res.endswith('\r\n'):
            res = res[:-2]
        
        #averiguar algum tratamento pra erros
        #if (not res) or (len(res) is not 24):
            
        self.widget.value = res

class LerMultiplosCartoes(QtCore.QThread):
    def __init__(self, serial):
        QtCore.QThread.__init__(self)
        # self.widget = widget
        self.serial = serial
        self.exiting = False
    
    def __del__(self):
        if self.serial.isOpen():
            self.serial.close()
            
    def run(self):
        if not self.serial.isOpen():
            self.serial.setTimeout(10)
            try:
                self.serial.open()
            except:
                self.emit(QtCore.SIGNAL("erro()"))
                return
            
        while not self.exiting:
            res = self.serial.readline()
            if res.startswith('\x00\xff'):
                res = res[2:]
            if res.endswith('\r\n'):
                res = res[:-2]
            if res:
                self.emit(QtCore.SIGNAL("card(QString)"), res)
        
        if self.exiting:
            self.serial.close()
            
        #if self.serial.isOpen():
        #    self.serial.close()
        
        #if self.exiting:
        #   print "Parou a Thread de leitura de cards"
        
        
        
    