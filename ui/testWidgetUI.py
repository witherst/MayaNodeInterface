# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWidget.ui'
#
# Created: Wed Feb 29 16:50:14 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 347)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 1, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 3, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Text Label:         ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Form", "RadioButton", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

