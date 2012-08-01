# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicEmSpeedAttr.ui'
#
# Created: Mon Mar 12 16:33:52 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_basicEmSpeedAttr(object):
    def setupUi(self, basicEmSpeedAttr):
        basicEmSpeedAttr.setObjectName("basicEmSpeedAttr")
        basicEmSpeedAttr.resize(305, 201)
        self.gridLayout = QtGui.QGridLayout(basicEmSpeedAttr)
        self.gridLayout.setObjectName("gridLayout")
        self.speedLabel = QtGui.QLabel(basicEmSpeedAttr)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 0, 0, 1, 1)
        self.speed = QtGui.QDoubleSpinBox(basicEmSpeedAttr)
        self.speed.setDecimals(3)
        self.speed.setMinimum(-1000000000.0)
        self.speed.setMaximum(1000000000.0)
        self.speed.setProperty("value", 1.0)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 0, 1, 1, 1)
        self.speedRandLabel = QtGui.QLabel(basicEmSpeedAttr)
        self.speedRandLabel.setObjectName("speedRandLabel")
        self.gridLayout.addWidget(self.speedRandLabel, 1, 0, 1, 1)
        self.speedRandom = QtGui.QDoubleSpinBox(basicEmSpeedAttr)
        self.speedRandom.setDecimals(3)
        self.speedRandom.setMinimum(-1000000000.0)
        self.speedRandom.setMaximum(1000000000.0)
        self.speedRandom.setProperty("value", 0.0)
        self.speedRandom.setObjectName("speedRandom")
        self.gridLayout.addWidget(self.speedRandom, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.tangentSpeedLabel = QtGui.QLabel(basicEmSpeedAttr)
        self.tangentSpeedLabel.setObjectName("tangentSpeedLabel")
        self.gridLayout.addWidget(self.tangentSpeedLabel, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.tangentSpeed = QtGui.QDoubleSpinBox(basicEmSpeedAttr)
        self.tangentSpeed.setDecimals(3)
        self.tangentSpeed.setMinimum(-1000000000.0)
        self.tangentSpeed.setMaximum(1000000000.0)
        self.tangentSpeed.setProperty("value", 0.0)
        self.tangentSpeed.setObjectName("tangentSpeed")
        self.gridLayout.addWidget(self.tangentSpeed, 2, 1, 1, 1)
        self.normalSpeed = QtGui.QDoubleSpinBox(basicEmSpeedAttr)
        self.normalSpeed.setDecimals(3)
        self.normalSpeed.setMinimum(-1000000000.0)
        self.normalSpeed.setMaximum(1000000000.0)
        self.normalSpeed.setProperty("value", 1.0)
        self.normalSpeed.setObjectName("normalSpeed")
        self.gridLayout.addWidget(self.normalSpeed, 3, 1, 1, 1)
        self.normalSpeedLabel = QtGui.QLabel(basicEmSpeedAttr)
        self.normalSpeedLabel.setObjectName("normalSpeedLabel")
        self.gridLayout.addWidget(self.normalSpeedLabel, 3, 0, 1, 1)

        self.retranslateUi(basicEmSpeedAttr)
        QtCore.QMetaObject.connectSlotsByName(basicEmSpeedAttr)

    def retranslateUi(self, basicEmSpeedAttr):
        basicEmSpeedAttr.setWindowTitle(QtGui.QApplication.translate("basicEmSpeedAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setText(QtGui.QApplication.translate("basicEmSpeedAttr", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.speedRandLabel.setText(QtGui.QApplication.translate("basicEmSpeedAttr", "Speed Random", None, QtGui.QApplication.UnicodeUTF8))
        self.tangentSpeedLabel.setText(QtGui.QApplication.translate("basicEmSpeedAttr", "Tangent Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.normalSpeedLabel.setText(QtGui.QApplication.translate("basicEmSpeedAttr", "Normal Speed", None, QtGui.QApplication.UnicodeUTF8))

