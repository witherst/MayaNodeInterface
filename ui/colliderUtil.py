# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colliderUtil.ui'
#
# Created: Mon Mar 19 15:08:23 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_colliderUtil(object):
    def setupUi(self, colliderUtil):
        colliderUtil.setObjectName("colliderUtil")
        colliderUtil.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(colliderUtil)
        self.gridLayout.setObjectName("gridLayout")
        self.resilienceLabel = QtGui.QLabel(colliderUtil)
        self.resilienceLabel.setObjectName("resilienceLabel")
        self.gridLayout.addWidget(self.resilienceLabel, 0, 0, 1, 1)
        self.resilience = QtGui.QDoubleSpinBox(colliderUtil)
        self.resilience.setDecimals(3)
        self.resilience.setMaximum(1.0)
        self.resilience.setSingleStep(0.01)
        self.resilience.setProperty("value", 1.0)
        self.resilience.setObjectName("resilience")
        self.gridLayout.addWidget(self.resilience, 0, 1, 1, 1)
        self.frictionLabel = QtGui.QLabel(colliderUtil)
        self.frictionLabel.setObjectName("frictionLabel")
        self.gridLayout.addWidget(self.frictionLabel, 1, 0, 1, 1)
        self.friction = QtGui.QDoubleSpinBox(colliderUtil)
        self.friction.setDecimals(3)
        self.friction.setMaximum(1.0)
        self.friction.setSingleStep(0.01)
        self.friction.setProperty("value", 0.0)
        self.friction.setObjectName("friction")
        self.gridLayout.addWidget(self.friction, 1, 1, 1, 1)
        self.offsetLabel = QtGui.QLabel(colliderUtil)
        self.offsetLabel.setObjectName("offsetLabel")
        self.gridLayout.addWidget(self.offsetLabel, 2, 0, 1, 1)
        self.offset = QtGui.QDoubleSpinBox(colliderUtil)
        self.offset.setDecimals(3)
        self.offset.setMinimum(0.001)
        self.offset.setMaximum(1.0)
        self.offset.setSingleStep(0.01)
        self.offset.setProperty("value", 0.01)
        self.offset.setObjectName("offset")
        self.gridLayout.addWidget(self.offset, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(colliderUtil)
        QtCore.QMetaObject.connectSlotsByName(colliderUtil)

    def retranslateUi(self, colliderUtil):
        colliderUtil.setWindowTitle(QtGui.QApplication.translate("colliderUtil", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.resilienceLabel.setText(QtGui.QApplication.translate("colliderUtil", "Bounciness", None, QtGui.QApplication.UnicodeUTF8))
        self.frictionLabel.setText(QtGui.QApplication.translate("colliderUtil", "Friction", None, QtGui.QApplication.UnicodeUTF8))
        self.offsetLabel.setText(QtGui.QApplication.translate("colliderUtil", "Offset", None, QtGui.QApplication.UnicodeUTF8))

