# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emitterCat.ui'
#
# Created: Thu Mar 08 14:40:26 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_emitterCat(object):
    def setupUi(self, emitterCat):
        emitterCat.setObjectName("emitterCat")
        emitterCat.resize(206, 270)
        self.gridLayout = QtGui.QGridLayout(emitterCat)
        self.gridLayout.setObjectName("gridLayout")
        self.emitterNameLabel = QtGui.QLabel(emitterCat)
        self.emitterNameLabel.setObjectName("emitterNameLabel")
        self.gridLayout.addWidget(self.emitterNameLabel, 0, 0, 1, 1)
        self.translateLabel = QtGui.QLabel(emitterCat)
        self.translateLabel.setObjectName("translateLabel")
        self.gridLayout.addWidget(self.translateLabel, 2, 0, 1, 1)
        self.rotateLabel = QtGui.QLabel(emitterCat)
        self.rotateLabel.setObjectName("rotateLabel")
        self.gridLayout.addWidget(self.rotateLabel, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        self.tx = QtGui.QLineEdit(emitterCat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tx.sizePolicy().hasHeightForWidth())
        self.tx.setSizePolicy(sizePolicy)
        self.tx.setMinimumSize(QtCore.QSize(0, 0))
        self.tx.setObjectName("tx")
        self.gridLayout.addWidget(self.tx, 3, 0, 1, 1)
        self.ty = QtGui.QLineEdit(emitterCat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ty.sizePolicy().hasHeightForWidth())
        self.ty.setSizePolicy(sizePolicy)
        self.ty.setObjectName("ty")
        self.gridLayout.addWidget(self.ty, 3, 1, 1, 1)
        self.tz = QtGui.QLineEdit(emitterCat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tz.sizePolicy().hasHeightForWidth())
        self.tz.setSizePolicy(sizePolicy)
        self.tz.setObjectName("tz")
        self.gridLayout.addWidget(self.tz, 3, 2, 1, 1)
        self.rx = QtGui.QLineEdit(emitterCat)
        self.rx.setObjectName("rx")
        self.gridLayout.addWidget(self.rx, 5, 0, 1, 1)
        self.ry = QtGui.QLineEdit(emitterCat)
        self.ry.setObjectName("ry")
        self.gridLayout.addWidget(self.ry, 5, 1, 1, 1)
        self.rz = QtGui.QLineEdit(emitterCat)
        self.rz.setObjectName("rz")
        self.gridLayout.addWidget(self.rz, 5, 2, 1, 1)
        self.emitterName = QtGui.QLineEdit(emitterCat)
        self.emitterName.setObjectName("emitterName")
        self.gridLayout.addWidget(self.emitterName, 1, 0, 1, 2)

        self.retranslateUi(emitterCat)
        QtCore.QMetaObject.connectSlotsByName(emitterCat)

    def retranslateUi(self, emitterCat):
        emitterCat.setWindowTitle(QtGui.QApplication.translate("emitterCat", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.emitterNameLabel.setText(QtGui.QApplication.translate("emitterCat", "Emitter name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setText(QtGui.QApplication.translate("emitterCat", "Translate:", None, QtGui.QApplication.UnicodeUTF8))
        self.rotateLabel.setText(QtGui.QApplication.translate("emitterCat", "Rotate:", None, QtGui.QApplication.UnicodeUTF8))
        self.tx.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ty.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.tz.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.rx.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ry.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.rz.setText(QtGui.QApplication.translate("emitterCat", "0.0", None, QtGui.QApplication.UnicodeUTF8))

