# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeAttrs.ui'
#
# Created: Fri Mar 09 14:48:53 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_timeAttrs(object):
    def setupUi(self, timeAttrs):
        timeAttrs.setObjectName("timeAttrs")
        timeAttrs.resize(305, 201)
        self.gridLayout = QtGui.QGridLayout(timeAttrs)
        self.gridLayout.setObjectName("gridLayout")
        self.startFrameLabel = QtGui.QLabel(timeAttrs)
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.gridLayout.addWidget(self.startFrameLabel, 0, 0, 1, 1)
        self.startFrame = QtGui.QDoubleSpinBox(timeAttrs)
        self.startFrame.setDecimals(3)
        self.startFrame.setMinimum(-1000000000.0)
        self.startFrame.setMaximum(1000000000.0)
        self.startFrame.setProperty("value", 1.0)
        self.startFrame.setObjectName("startFrame")
        self.gridLayout.addWidget(self.startFrame, 0, 1, 2, 1)
        self.currentFrameLabel = QtGui.QLabel(timeAttrs)
        self.currentFrameLabel.setObjectName("currentFrameLabel")
        self.gridLayout.addWidget(self.currentFrameLabel, 1, 0, 2, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.currentFrame = QtGui.QLineEdit(timeAttrs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFrame.sizePolicy().hasHeightForWidth())
        self.currentFrame.setSizePolicy(sizePolicy)
        self.currentFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.currentFrame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentFrame.setReadOnly(True)
        self.currentFrame.setObjectName("currentFrame")
        self.gridLayout.addWidget(self.currentFrame, 2, 1, 1, 1)

        self.retranslateUi(timeAttrs)
        QtCore.QMetaObject.connectSlotsByName(timeAttrs)

    def retranslateUi(self, timeAttrs):
        timeAttrs.setWindowTitle(QtGui.QApplication.translate("timeAttrs", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.startFrameLabel.setText(QtGui.QApplication.translate("timeAttrs", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.currentFrameLabel.setText(QtGui.QApplication.translate("timeAttrs", "Current Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.currentFrame.setText(QtGui.QApplication.translate("timeAttrs", "1", None, QtGui.QApplication.UnicodeUTF8))

