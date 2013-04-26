# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4 import QtCore, QtGui
#from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QTimer,  SIGNAL, SLOT, Qt,  QRect
from PyQt4.QtGui import QPainter, QRegion, QPen
import sys, random
from struct import unpack
from functools import partial
from math import floor
from gloveDataParser import ParseGloveData 
from glob import glob
import os
from ampDetection import AmpAnalysis

PIXEL_OFFSET = 200 # pixels offsets
 
from Ui_display import Ui_Dialog


class View(QMainWindow, Ui_Dialog):
    """
    Class View inherits the GUI generated by QtDesigner, and add customized actions
    """
    def __init__(self, projectPath,  parent = None):
        """
        Constructor
        """
#        QMainWindow.__init__(self, parent, Qt.FramelessWindowHint)
        QMainWindow.__init__(self, parent)
        self.setStyleSheet("background-color:  rgb(240, 235, 235); margin: 2px;")
        self.setWindowOpacity(0.95)
                                                            
#                                    "QLineEdit { border-width: 20px;border-style: solid; border-color: darkblue; };")
        self.setupUi(self)
        
        self.move(10,  100)
        
        self.x = 200
        self.pen = QPen()

        self.numPt = PIXEL_OFFSET
        self.isPause = False
        self.projectPath = projectPath
        self.setWindowTitle(projectPath)
        
        # Search all .bit files, make them selectable 
        sys.path.append(projectPath)
        self.gloveDataPath = projectPath + "\\glove_data\\"
        self.emgDataPath = projectPath + "\\emg_data\\"
        
        
        
        print projectPath
        self.lineEdit.setText(str(projectPath))
        self.lineEdit.setStyleSheet("background-color:  rgb(220, 235, 235); margin: 2px;")
        
        for eachTxtFile in glob(projectPath+"/glove_data/*.txt"): 
            (filepath, filename) = os.path.split(eachTxtFile) 
            self.listWidget.addItem(filename)
        self.listWidget.setCurrentRow(0)
        self.listWidget.setStyleSheet("background-color:  rgb(220, 235, 235); margin: 2px;")
        
        
     
        ## initialization 
        self.digit1=0
        self.digit2=0
        self.digit3=0
        self.digit4=0
        self.digit5=0
        
       
        if (self.isPause):
            return
        size = self.size()
        self.update(QRect(self.x+ 1, 0,size.width() - self.x,size.height()))
        
        if (self.x < size.width() *0.7):  # display line width adjustment
            self.x = self.x + 1  
        else:
            self.x = PIXEL_OFFSET 
            
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        self.glove_item = item
        


    @pyqtSignature("bool")
    def on_checkBox_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit1 = checked

    
    @pyqtSignature("bool")
    def on_checkBox_2_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit2 = checked
    
    @pyqtSignature("bool")
    def on_checkBox_3_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit3 = checked
        
    @pyqtSignature("bool")
    def on_checkBox_4_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit4 = checked
        
    @pyqtSignature("bool")
    def on_checkBox_5_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.digit5 = checked
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.digit2: 
            ParseGloveData(str(self.glove_item.text()), 3, self.gloveDataPath,  self.pivot,  self.startTimeIndex )
#            self.label_4.setPixmap((QPixmap(str("glove_figures\\"+self.glove_item.text())+"_index.png")))
#            self.label_4.setScaledContents(True)
#            self.label_4.show()
        if self.digit3: 
            ParseGloveData(str(self.glove_item.text()), 4,  self.gloveDataPath,  self.pivot,  self.startTimeIndex )
#            self.label_5.setPixmap((QPixmap(str("glove_figures\\"+self.glove_item.text())+"_middle.png")))
#            self.label_5.setScaledContents(True)
#            self.label_5.show()
       
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        just show the plot
        """
        self.label_4.hide()
        self.label_5.hide()
        
        if self.digit2: 
            self.label_4.setPixmap((QPixmap(self.projectPath+str("\\glove_figures\\"+self.glove_item.text())+"_index.png")))
            print self.projectPath+str("\\glove_figures\\"+self.glove_item.text())+"_index.png"
            self.label_4.setScaledContents(True)
            self.label_4.show()
        if self.digit3: 
            self.label_5.setPixmap((QPixmap(self.projectPath+str("\\glove_figures\\"+self.glove_item.text())+"_middle.png")))
            self.label_5.setScaledContents(True)
            self.label_5.show()

    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.listWidget.clear()
        self.listWidget_2.clear()
        for eachTxtFile in glob(self.projectPath+"/glove_data/*.txt"): 
            (filepath, filename) = os.path.split(eachTxtFile) 
            self.listWidget.addItem(filename)
#        self.listWidget.setCurrentRow(0)
#        self.listWidget.setStyleSheet("background-color:  rgb(220, 235, 235); margin: 2px;")
        
    
    @pyqtSignature("double")
    def on_doubleSpinBox_valueChanged(self, p0):
        """
        pivot value input
        """
        self.pivot = p0
    
    @pyqtSignature("int")
    def on_spinBox_valueChanged(self, t0):
        """
        starting time index input
        """
        self.startTimeIndex = t0
