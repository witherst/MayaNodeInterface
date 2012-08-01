# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genControlAttr.ui'
#
# Created: Fri Mar 09 19:16:40 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_genControlAttr(object):
    def setupUi(self, genControlAttr):
        genControlAttr.setObjectName("genControlAttr")
        genControlAttr.resize(251, 300)
        self.gridLayout = QtGui.QGridLayout(genControlAttr)
        self.gridLayout.setObjectName("gridLayout")
        self.isDynamic = QtGui.QCheckBox(genControlAttr)
        self.isDynamic.setChecked(True)
        self.isDynamic.setObjectName("isDynamic")
        self.gridLayout.addWidget(self.isDynamic, 0, 0, 1, 2)
        self.dynamicWeightsLabel = QtGui.QLabel(genControlAttr)
        self.dynamicWeightsLabel.setObjectName("dynamicWeightsLabel")
        self.gridLayout.addWidget(self.dynamicWeightsLabel, 1, 0, 1, 1)
        self.dynamicsWeight = QtGui.QDoubleSpinBox(genControlAttr)
        self.dynamicsWeight.setDecimals(3)
        self.dynamicsWeight.setMaximum(1.0)
        self.dynamicsWeight.setSingleStep(0.01)
        self.dynamicsWeight.setProperty("value", 1.0)
        self.dynamicsWeight.setObjectName("dynamicsWeight")
        self.gridLayout.addWidget(self.dynamicsWeight, 1, 1, 1, 1)
        self.conserveLabel = QtGui.QLabel(genControlAttr)
        self.conserveLabel.setObjectName("conserveLabel")
        self.gridLayout.addWidget(self.conserveLabel, 2, 0, 1, 1)
        self.conserve = QtGui.QDoubleSpinBox(genControlAttr)
        self.conserve.setDecimals(3)
        self.conserve.setMaximum(1.0)
        self.conserve.setSingleStep(0.01)
        self.conserve.setProperty("value", 1.0)
        self.conserve.setObjectName("conserve")
        self.gridLayout.addWidget(self.conserve, 2, 1, 1, 1)
        self.forcesInWorld = QtGui.QCheckBox(genControlAttr)
        self.forcesInWorld.setChecked(True)
        self.forcesInWorld.setObjectName("forcesInWorld")
        self.gridLayout.addWidget(self.forcesInWorld, 3, 0, 1, 2)
        self.countLabel = QtGui.QLabel(genControlAttr)
        self.countLabel.setObjectName("countLabel")
        self.gridLayout.addWidget(self.countLabel, 4, 0, 1, 1)
        self.count = QtGui.QLineEdit(genControlAttr)
        self.count.setObjectName("count")
        self.gridLayout.addWidget(self.count, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)

        self.retranslateUi(genControlAttr)
        QtCore.QMetaObject.connectSlotsByName(genControlAttr)

    def retranslateUi(self, genControlAttr):
        genControlAttr.setWindowTitle(QtGui.QApplication.translate("genControlAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.isDynamic.setText(QtGui.QApplication.translate("genControlAttr", "Is Dynamic", None, QtGui.QApplication.UnicodeUTF8))
        self.dynamicWeightsLabel.setText(QtGui.QApplication.translate("genControlAttr", "Dynamics Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.conserveLabel.setText(QtGui.QApplication.translate("genControlAttr", "Conserve", None, QtGui.QApplication.UnicodeUTF8))
        self.forcesInWorld.setText(QtGui.QApplication.translate("genControlAttr", "Forces in World", None, QtGui.QApplication.UnicodeUTF8))
        self.countLabel.setText(QtGui.QApplication.translate("genControlAttr", "Count", None, QtGui.QApplication.UnicodeUTF8))

