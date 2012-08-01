# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goalAttr.ui'
#
# Created: Sat Mar 17 14:00:31 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_goalAttr(object):
    def setupUi(self, goalAttr):
        goalAttr.setObjectName("goalAttr")
        goalAttr.resize(290, 362)
        self.gridLayout = QtGui.QGridLayout(goalAttr)
        self.gridLayout.setObjectName("gridLayout")
        self.goalSmoothnessLabel = QtGui.QLabel(goalAttr)
        self.goalSmoothnessLabel.setObjectName("goalSmoothnessLabel")
        self.gridLayout.addWidget(self.goalSmoothnessLabel, 0, 0, 1, 1)
        self.goalSmoothness = QtGui.QDoubleSpinBox(goalAttr)
        self.goalSmoothness.setDecimals(3)
        self.goalSmoothness.setMaximum(999999999.0)
        self.goalSmoothness.setProperty("value", 3.0)
        self.goalSmoothness.setObjectName("goalSmoothness")
        self.gridLayout.addWidget(self.goalSmoothness, 0, 1, 1, 1)
        self.goalObject = QtGui.QLabel(goalAttr)
        self.goalObject.setObjectName("goalObject")
        self.gridLayout.addWidget(self.goalObject, 1, 0, 1, 1)
        self.goalWeight = QtGui.QDoubleSpinBox(goalAttr)
        self.goalWeight.setDecimals(3)
        self.goalWeight.setMaximum(1.0)
        self.goalWeight.setSingleStep(0.01)
        self.goalWeight.setProperty("value", 0.5)
        self.goalWeight.setObjectName("goalWeight")
        self.gridLayout.addWidget(self.goalWeight, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)

        self.retranslateUi(goalAttr)
        QtCore.QMetaObject.connectSlotsByName(goalAttr)

    def retranslateUi(self, goalAttr):
        goalAttr.setWindowTitle(QtGui.QApplication.translate("goalAttr", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.goalSmoothnessLabel.setText(QtGui.QApplication.translate("goalAttr", "Goal Smoothness", None, QtGui.QApplication.UnicodeUTF8))
        self.goalObject.setText(QtGui.QApplication.translate("goalAttr", "Goal Weight", None, QtGui.QApplication.UnicodeUTF8))

