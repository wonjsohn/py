# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Code\nerf_verilog\source\py\multC_tester\V_Display.ui'
#
# Created: Wed Mar 20 17:01:11 2013
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
        Dialog.resize(895, 669)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.comboBox.setStyleSheet(_fromUtf8("border-color: rgb(0, 98, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(150, 20, 97, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(680, 10, 201, 111))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(750, 120, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 20, 151, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.comboBox.setItemText(0, _translate("Dialog", "waveform 1", None))
        self.comboBox.setItemText(1, _translate("Dialog", "waveform 2", None))
        self.comboBox.setItemText(2, _translate("Dialog", "waveform 3", None))
        self.checkBox.setText(_translate("Dialog", "auto scale", None))
        self.label.setText(_translate("Dialog", ".bit files", None))
        self.checkBox_2.setText(_translate("Dialog", "input from wave", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

