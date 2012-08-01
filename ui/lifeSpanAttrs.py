# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lifeSpanAttrs.ui'
#
# Created: Sun Mar 04 14:28:59 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_lifespanAttrWidget(object):
    def setupUi(self, lifespanAttrWidget):
        lifespanAttrWidget.setObjectName("lifespanAttrWidget")
        lifespanAttrWidget.resize(270, 224)
        self.gridLayout = QtGui.QGridLayout(lifespanAttrWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.maxCountLabel = QtGui.QLabel(lifespanAttrWidget)
        self.maxCountLabel.setObjectName("maxCountLabel")
        self.gridLayout.addWidget(self.maxCountLabel, 0, 0, 1, 1)
        self.lifeSpanMode = QtGui.QComboBox(lifespanAttrWidget)
        self.lifeSpanMode.setObjectName("lifeSpanMode")
        self.lifeSpanMode.addItem("")
        self.lifeSpanMode.addItem("")
        self.lifeSpanMode.addItem("")
        self.lifeSpanMode.addItem("")
        self.gridLayout.addWidget(self.lifeSpanMode, 0, 1, 1, 1)
        self.levelOfDetailLabel = QtGui.QLabel(lifespanAttrWidget)
        self.levelOfDetailLabel.setObjectName("levelOfDetailLabel")
        self.gridLayout.addWidget(self.levelOfDetailLabel, 1, 0, 1, 1)
        self.lifeSpan = QtGui.QDoubleSpinBox(lifespanAttrWidget)
        self.lifeSpan.setDecimals(3)
        self.lifeSpan.setMaximum(1000000.0)
        self.lifeSpan.setProperty("value", 1.0)
        self.lifeSpan.setObjectName("lifeSpan")
        self.gridLayout.addWidget(self.lifeSpan, 1, 1, 1, 1)
        self.inheritFactorLabel = QtGui.QLabel(lifespanAttrWidget)
        self.inheritFactorLabel.setObjectName("inheritFactorLabel")
        self.gridLayout.addWidget(self.inheritFactorLabel, 2, 0, 1, 1)
        self.lifeSpanRandom = QtGui.QDoubleSpinBox(lifespanAttrWidget)
        self.lifeSpanRandom.setDecimals(3)
        self.lifeSpanRandom.setMaximum(1000000.0)
        self.lifeSpanRandom.setProperty("value", 0.0)
        self.lifeSpanRandom.setObjectName("lifeSpanRandom")
        self.gridLayout.addWidget(self.lifeSpanRandom, 2, 1, 1, 1)
        self.inheritFactorLabel_2 = QtGui.QLabel(lifespanAttrWidget)
        self.inheritFactorLabel_2.setObjectName("inheritFactorLabel_2")
        self.gridLayout.addWidget(self.inheritFactorLabel_2, 3, 0, 1, 1)
        self.generalSeed = QtGui.QDoubleSpinBox(lifespanAttrWidget)
        self.generalSeed.setDecimals(3)
        self.generalSeed.setMaximum(1000000.0)
        self.generalSeed.setProperty("value", 0.0)
        self.generalSeed.setObjectName("generalSeed")
        self.gridLayout.addWidget(self.generalSeed, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)

        self.retranslateUi(lifespanAttrWidget)
        QtCore.QMetaObject.connectSlotsByName(lifespanAttrWidget)

    def retranslateUi(self, lifespanAttrWidget):
        lifespanAttrWidget.setWindowTitle(QtGui.QApplication.translate("lifespanAttrWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCountLabel.setText(QtGui.QApplication.translate("lifespanAttrWidget", "Lifespan Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.lifeSpanMode.setItemText(0, QtGui.QApplication.translate("lifespanAttrWidget", "Live Forever", None, QtGui.QApplication.UnicodeUTF8))
        self.lifeSpanMode.setItemText(1, QtGui.QApplication.translate("lifespanAttrWidget", "Constant", None, QtGui.QApplication.UnicodeUTF8))
        self.lifeSpanMode.setItemText(2, QtGui.QApplication.translate("lifespanAttrWidget", "Random Range", None, QtGui.QApplication.UnicodeUTF8))
        self.lifeSpanMode.setItemText(3, QtGui.QApplication.translate("lifespanAttrWidget", "lifespanPP only", None, QtGui.QApplication.UnicodeUTF8))
        self.levelOfDetailLabel.setText(QtGui.QApplication.translate("lifespanAttrWidget", "Lifespan", None, QtGui.QApplication.UnicodeUTF8))
        self.inheritFactorLabel.setText(QtGui.QApplication.translate("lifespanAttrWidget", "Lifespan Random", None, QtGui.QApplication.UnicodeUTF8))
        self.inheritFactorLabel_2.setText(QtGui.QApplication.translate("lifespanAttrWidget", "General Seed", None, QtGui.QApplication.UnicodeUTF8))

