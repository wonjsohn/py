# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Code\nerf_verilog\source\py\data_parse\display.ui'
#
# Created: Tue Apr 09 11:43:19 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1489, 587)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 281, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 200, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(300, 50, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 70, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(300, 90, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(300, 110, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(300, 130, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 162, 171, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 281, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 281, 261))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 260, 281, 261))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(600, 260, 281, 261))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(890, 260, 271, 261))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(1170, 260, 281, 261))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 40, 81, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget_2 = QtGui.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(520, 40, 281, 151))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(630, 200, 81, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 162, 181, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 10, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 40, 81, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "data glove files", None))
        self.checkBox.setText(_translate("Dialog", "thumb", None))
        self.checkBox_2.setText(_translate("Dialog", "index", None))
        self.checkBox_3.setText(_translate("Dialog", "middle", None))
        self.checkBox_4.setText(_translate("Dialog", "ring", None))
        self.checkBox_5.setText(_translate("Dialog", "pinky", None))
        self.pushButton.setText(_translate("Dialog", "plot", None))
        self.label_2.setText(_translate("Dialog", "project path", None))
        self.label_3.setText(_translate("Dialog", "THUMB", None))
        self.label_4.setText(_translate("Dialog", "INDEX", None))
        self.label_5.setText(_translate("Dialog", "MIDDLE", None))
        self.label_6.setText(_translate("Dialog", "RING", None))
        self.label_7.setText(_translate("Dialog", "PINKY", None))
        self.pushButton_2.setText(_translate("Dialog", "remove lastline", None))
        self.label_8.setText(_translate("Dialog", "emg files", None))
        self.pushButton_3.setText(_translate("Dialog", "plot", None))
        self.pushButton_4.setText(_translate("Dialog", "REFRESH", None))
        self.pushButton_5.setText(_translate("Dialog", "remove lastline", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

