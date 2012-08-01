# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emissionAttrs.ui'
#
# Created: Fri Mar 09 14:29:01 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_emissionAttrWidget(object):
    def setupUi(self, emissionAttrWidget):
        emissionAttrWidget.setObjectName("emissionAttrWidget")
        emissionAttrWidget.resize(270, 224)
        self.gridLayout = QtGui.QGridLayout(emissionAttrWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.maxCountLabel = QtGui.QLabel(emissionAttrWidget)
        self.maxCountLabel.setObjectName("maxCountLabel")
        self.gridLayout.addWidget(self.maxCountLabel, 0, 0, 1, 1)
        self.maxCount = QtGui.QSpinBox(emissionAttrWidget)
        self.maxCount.setMinimum(-1)
        self.maxCount.setMaximum(100000000)
        self.maxCount.setProperty("value", -1)
        self.maxCount.setObjectName("maxCount")
        self.gridLayout.addWidget(self.maxCount, 0, 1, 1, 1)
        self.levelOfDetailLabel = QtGui.QLabel(emissionAttrWidget)
        self.levelOfDetailLabel.setObjectName("levelOfDetailLabel")
        self.gridLayout.addWidget(self.levelOfDetailLabel, 1, 0, 1, 1)
        self.levelOfDetail = QtGui.QDoubleSpinBox(emissionAttrWidget)
        self.levelOfDetail.setDecimals(4)
        self.levelOfDetail.setMaximum(1.0)
        self.levelOfDetail.setSingleStep(0.01)
        self.levelOfDetail.setProperty("value", 1.0)
        self.levelOfDetail.setObjectName("levelOfDetail")
        self.gridLayout.addWidget(self.levelOfDetail, 1, 1, 1, 1)
        self.inheritFactorLabel = QtGui.QLabel(emissionAttrWidget)
        self.inheritFactorLabel.setObjectName("inheritFactorLabel")
        self.gridLayout.addWidget(self.inheritFactorLabel, 2, 0, 1, 1)
        self.inheritFactor = QtGui.QDoubleSpinBox(emissionAttrWidget)
        self.inheritFactor.setDecimals(4)
        self.inheritFactor.setMaximum(1.0)
        self.inheritFactor.setSingleStep(0.01)
        self.inheritFactor.setProperty("value", 0.0)
        self.inheritFactor.setObjectName("inheritFactor")
        self.gridLayout.addWidget(self.inheritFactor, 2, 1, 1, 1)
        self.emissionInWorld = QtGui.QCheckBox(emissionAttrWidget)
        self.emissionInWorld.setChecked(True)
        self.emissionInWorld.setObjectName("emissionInWorld")
        self.gridLayout.addWidget(self.emissionInWorld, 3, 0, 1, 2)
        self.dieOnEmissionVolExit = QtGui.QCheckBox(emissionAttrWidget)
        self.dieOnEmissionVolExit.setObjectName("dieOnEmissionVolExit")
        self.gridLayout.addWidget(self.dieOnEmissionVolExit, 4, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        self.retranslateUi(emissionAttrWidget)
        QtCore.QMetaObject.connectSlotsByName(emissionAttrWidget)

    def retranslateUi(self, emissionAttrWidget):
        emissionAttrWidget.setWindowTitle(QtGui.QApplication.translate("emissionAttrWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCountLabel.setText(QtGui.QApplication.translate("emissionAttrWidget", "Max Count", None, QtGui.QApplication.UnicodeUTF8))
        self.levelOfDetailLabel.setText(QtGui.QApplication.translate("emissionAttrWidget", "Level of Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.inheritFactorLabel.setText(QtGui.QApplication.translate("emissionAttrWidget", "Inherit Factor", None, QtGui.QApplication.UnicodeUTF8))
        self.emissionInWorld.setText(QtGui.QApplication.translate("emissionAttrWidget", "Emission In World", None, QtGui.QApplication.UnicodeUTF8))
        self.dieOnEmissionVolExit.setText(QtGui.QApplication.translate("emissionAttrWidget", "Die on Emission Volume Exit", None, QtGui.QApplication.UnicodeUTF8))

