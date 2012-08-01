# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtonForce.ui'
#
# Created: Sat Mar 17 16:21:54 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_newtonForce(object):
    def setupUi(self, newtonForce):
        newtonForce.setObjectName("newtonForce")
        newtonForce.resize(234, 181)
        self.gridLayout = QtGui.QGridLayout(newtonForce)
        self.gridLayout.setObjectName("gridLayout")
        self.magnitudeLabel = QtGui.QLabel(newtonForce)
        self.magnitudeLabel.setObjectName("magnitudeLabel")
        self.gridLayout.addWidget(self.magnitudeLabel, 0, 0, 1, 1)
        self.magnitude = QtGui.QDoubleSpinBox(newtonForce)
        self.magnitude.setMinimum(-999999999.0)
        self.magnitude.setMaximum(999999999.0)
        self.magnitude.setProperty("value", 5.0)
        self.magnitude.setObjectName("magnitude")
        self.gridLayout.addWidget(self.magnitude, 0, 1, 1, 1)
        self.attenuationLabel = QtGui.QLabel(newtonForce)
        self.attenuationLabel.setObjectName("attenuationLabel")
        self.gridLayout.addWidget(self.attenuationLabel, 1, 0, 1, 1)
        self.minDistance = QtGui.QDoubleSpinBox(newtonForce)
        self.minDistance.setMinimum(-999999999.0)
        self.minDistance.setMaximum(999999999.0)
        self.minDistance.setProperty("value", 1.0)
        self.minDistance.setObjectName("minDistance")
        self.gridLayout.addWidget(self.minDistance, 1, 1, 1, 1)
        self.minDistanceLabel = QtGui.QLabel(newtonForce)
        self.minDistanceLabel.setObjectName("minDistanceLabel")
        self.gridLayout.addWidget(self.minDistanceLabel, 2, 0, 1, 1)
        self.attenuation = QtGui.QDoubleSpinBox(newtonForce)
        self.attenuation.setMinimum(-999999999.0)
        self.attenuation.setMaximum(999999999.0)
        self.attenuation.setProperty("value", 0.2)
        self.attenuation.setObjectName("attenuation")
        self.gridLayout.addWidget(self.attenuation, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)

        self.retranslateUi(newtonForce)
        QtCore.QMetaObject.connectSlotsByName(newtonForce)

    def retranslateUi(self, newtonForce):
        newtonForce.setWindowTitle(QtGui.QApplication.translate("newtonForce", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.magnitudeLabel.setText(QtGui.QApplication.translate("newtonForce", "Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.attenuationLabel.setText(QtGui.QApplication.translate("newtonForce", "Attenuation", None, QtGui.QApplication.UnicodeUTF8))
        self.minDistanceLabel.setText(QtGui.QApplication.translate("newtonForce", "Min Distance", None, QtGui.QApplication.UnicodeUTF8))

