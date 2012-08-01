# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renderStats.ui'
#
# Created: Sun Mar 04 14:38:51 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_renderStats(object):
    def setupUi(self, renderStats):
        renderStats.setObjectName("renderStats")
        renderStats.resize(251, 300)
        self.gridLayout = QtGui.QGridLayout(renderStats)
        self.gridLayout.setObjectName("gridLayout")
        self.visibleInReflections = QtGui.QCheckBox(renderStats)
        self.visibleInReflections.setObjectName("visibleInReflections")
        self.gridLayout.addWidget(self.visibleInReflections, 0, 0, 1, 1)
        self.visibleInRefractions = QtGui.QCheckBox(renderStats)
        self.visibleInRefractions.setObjectName("visibleInRefractions")
        self.gridLayout.addWidget(self.visibleInRefractions, 1, 0, 1, 1)
        self.castsShadows = QtGui.QCheckBox(renderStats)
        self.castsShadows.setChecked(True)
        self.castsShadows.setObjectName("castsShadows")
        self.gridLayout.addWidget(self.castsShadows, 2, 0, 1, 1)
        self.receiveShadows = QtGui.QCheckBox(renderStats)
        self.receiveShadows.setChecked(True)
        self.receiveShadows.setObjectName("receiveShadows")
        self.gridLayout.addWidget(self.receiveShadows, 3, 0, 1, 1)
        self.primaryVisibility = QtGui.QCheckBox(renderStats)
        self.primaryVisibility.setChecked(True)
        self.primaryVisibility.setObjectName("primaryVisibility")
        self.gridLayout.addWidget(self.primaryVisibility, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.motionBlur = QtGui.QCheckBox(renderStats)
        self.motionBlur.setChecked(True)
        self.motionBlur.setObjectName("motionBlur")
        self.gridLayout.addWidget(self.motionBlur, 4, 0, 1, 1)

        self.retranslateUi(renderStats)
        QtCore.QMetaObject.connectSlotsByName(renderStats)

    def retranslateUi(self, renderStats):
        renderStats.setWindowTitle(QtGui.QApplication.translate("renderStats", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.visibleInReflections.setText(QtGui.QApplication.translate("renderStats", "Visible in Reflections", None, QtGui.QApplication.UnicodeUTF8))
        self.visibleInRefractions.setText(QtGui.QApplication.translate("renderStats", "Visible in Refractions", None, QtGui.QApplication.UnicodeUTF8))
        self.castsShadows.setText(QtGui.QApplication.translate("renderStats", "Casts Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.receiveShadows.setText(QtGui.QApplication.translate("renderStats", "Receive Shadows", None, QtGui.QApplication.UnicodeUTF8))
        self.primaryVisibility.setText(QtGui.QApplication.translate("renderStats", "Primary Visibility", None, QtGui.QApplication.UnicodeUTF8))
        self.motionBlur.setText(QtGui.QApplication.translate("renderStats", "Motion Blur", None, QtGui.QApplication.UnicodeUTF8))

