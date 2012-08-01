# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'behaviorCat.ui'
#
# Created: Fri Mar 09 15:11:30 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_behaviorCat(object):
    def setupUi(self, behaviorCat):
        behaviorCat.setObjectName("behaviorCat")
        behaviorCat.resize(336, 344)
        self.gridLayout = QtGui.QGridLayout(behaviorCat)
        self.gridLayout.setObjectName("gridLayout")
        self.particleNameLabel = QtGui.QLabel(behaviorCat)
        self.particleNameLabel.setObjectName("particleNameLabel")
        self.gridLayout.addWidget(self.particleNameLabel, 0, 0, 1, 1)
        self.particleName = QtGui.QLineEdit(behaviorCat)
        self.particleName.setObjectName("particleName")
        self.gridLayout.addWidget(self.particleName, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(behaviorCat)
        QtCore.QMetaObject.connectSlotsByName(behaviorCat)

    def retranslateUi(self, behaviorCat):
        behaviorCat.setWindowTitle(QtGui.QApplication.translate("behaviorCat", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.particleNameLabel.setText(QtGui.QApplication.translate("behaviorCat", "ParticleShape name:", None, QtGui.QApplication.UnicodeUTF8))

