# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectUtil.ui'
#
# Created: Tue Mar 13 17:01:06 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_objectUtil(object):
    def setupUi(self, objectUtil):
        objectUtil.setObjectName("objectUtil")
        objectUtil.resize(186, 298)
        self.gridLayout = QtGui.QGridLayout(objectUtil)
        self.gridLayout.setObjectName("gridLayout")
        self.objectNameLabel = QtGui.QLabel(objectUtil)
        self.objectNameLabel.setObjectName("objectNameLabel")
        self.gridLayout.addWidget(self.objectNameLabel, 0, 0, 1, 3)
        self.translateLabel = QtGui.QLabel(objectUtil)
        self.translateLabel.setObjectName("translateLabel")
        self.gridLayout.addWidget(self.translateLabel, 2, 0, 1, 1)
        self.rotateLabel = QtGui.QLabel(objectUtil)
        self.rotateLabel.setObjectName("rotateLabel")
        self.gridLayout.addWidget(self.rotateLabel, 4, 0, 1, 1)
        self.scaleLabel = QtGui.QLabel(objectUtil)
        self.scaleLabel.setObjectName("scaleLabel")
        self.gridLayout.addWidget(self.scaleLabel, 6, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 1, 1, 1)
        self.pickObject = QtGui.QPushButton(objectUtil)
        self.pickObject.setCheckable(True)
        self.pickObject.setFlat(False)
        self.pickObject.setObjectName("pickObject")
        self.gridLayout.addWidget(self.pickObject, 8, 0, 1, 3)
        self.waitingLabel = QtGui.QLabel(objectUtil)
        self.waitingLabel.setObjectName("waitingLabel")
        self.gridLayout.addWidget(self.waitingLabel, 10, 0, 1, 3)
        self.scaleZ = QtGui.QLineEdit(objectUtil)
        self.scaleZ.setObjectName("scaleZ")
        self.gridLayout.addWidget(self.scaleZ, 7, 2, 1, 1)
        self.scaleY = QtGui.QLineEdit(objectUtil)
        self.scaleY.setObjectName("scaleY")
        self.gridLayout.addWidget(self.scaleY, 7, 1, 1, 1)
        self.rotateZ = QtGui.QLineEdit(objectUtil)
        self.rotateZ.setObjectName("rotateZ")
        self.gridLayout.addWidget(self.rotateZ, 5, 2, 1, 1)
        self.translateX = QtGui.QLineEdit(objectUtil)
        self.translateX.setObjectName("translateX")
        self.gridLayout.addWidget(self.translateX, 3, 0, 1, 1)
        self.rotateX = QtGui.QLineEdit(objectUtil)
        self.rotateX.setObjectName("rotateX")
        self.gridLayout.addWidget(self.rotateX, 5, 0, 1, 1)
        self.scaleX = QtGui.QLineEdit(objectUtil)
        self.scaleX.setObjectName("scaleX")
        self.gridLayout.addWidget(self.scaleX, 7, 0, 1, 1)
        self.translateZ = QtGui.QLineEdit(objectUtil)
        self.translateZ.setObjectName("translateZ")
        self.gridLayout.addWidget(self.translateZ, 3, 2, 1, 1)
        self.rotateY = QtGui.QLineEdit(objectUtil)
        self.rotateY.setObjectName("rotateY")
        self.gridLayout.addWidget(self.rotateY, 5, 1, 1, 1)
        self.translateY = QtGui.QLineEdit(objectUtil)
        self.translateY.setObjectName("translateY")
        self.gridLayout.addWidget(self.translateY, 3, 1, 1, 1)
        self.objName = QtGui.QLineEdit(objectUtil)
        self.objName.setObjectName("objName")
        self.gridLayout.addWidget(self.objName, 1, 0, 1, 3)
        self.clearObject = QtGui.QPushButton(objectUtil)
        self.clearObject.setObjectName("clearObject")
        self.gridLayout.addWidget(self.clearObject, 9, 0, 1, 3)

        self.retranslateUi(objectUtil)
        QtCore.QMetaObject.connectSlotsByName(objectUtil)

    def retranslateUi(self, objectUtil):
        objectUtil.setWindowTitle(QtGui.QApplication.translate("objectUtil", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.objectNameLabel.setText(QtGui.QApplication.translate("objectUtil", "Object Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setText(QtGui.QApplication.translate("objectUtil", "Translate:", None, QtGui.QApplication.UnicodeUTF8))
        self.rotateLabel.setText(QtGui.QApplication.translate("objectUtil", "Rotate:", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleLabel.setText(QtGui.QApplication.translate("objectUtil", "Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.pickObject.setText(QtGui.QApplication.translate("objectUtil", "Pick Object", None, QtGui.QApplication.UnicodeUTF8))
        self.waitingLabel.setText(QtGui.QApplication.translate("objectUtil", "Awaiting selection from Maya...", None, QtGui.QApplication.UnicodeUTF8))
        self.clearObject.setText(QtGui.QApplication.translate("objectUtil", "Clear Object", None, QtGui.QApplication.UnicodeUTF8))

