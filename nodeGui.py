import os, sip, sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from .ui.gui_from_designer import Ui_MainWindow
from .ui import graphicsModule, mayaNodesModule, userListModule, icons_rc

app = None

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Setting up variables and functions
        self._path = os.getcwd()

        # Get the user defined Maya Nodes
        mayaNodesModule.getMayaNodes()

        # Scene view
        self.scene = graphicsModule.SceneView()
        self.nodeDropGraphicsView.setScene(self.scene)
        self.nodeDropGraphicsView.setSceneRect(0, 0, 630, 555)

        # Graphics View
        self.nodeDropGraphicsView.wheelEvent = self.graphicsView_wheelEvent
        self.nodeDropGraphicsView.resizeEvent = self.graphicsView_resizeEvent
        self.nodeDropGraphicsView.setBackgroundBrush(QBrush(QColor(60, 60, 60, 255), Qt.SolidPattern))

        # Tabs
        self.addTabs()

        # Connections
        self.makeConnections()

    def changeDescription(self, listItem):
        self.descriptionLabel.setText(listItem.description)

    def addTabs(self):

        self.emitterList = userListModule.ListBaseClass()
        self.emitterList.listName = "emitterList"
        self.emitterList.populateListWidget(mayaNodesModule.MayaNodes)
        listIcon = QIcon(":/attrEmitter.svg")
        self.nodesWindow.insertTab(0, self.emitterList, listIcon, "Particle Emitter")

        self.behaviorList = userListModule.ListBaseClass()
        self.behaviorList.listName = "behaviorList"
        self.behaviorList.populateListWidget(mayaNodesModule.MayaNodes)
        listIcon = QIcon(":/attrBehavior.svg")
        self.nodesWindow.insertTab(1, self.behaviorList, listIcon, "Particle Behavior/Movement")

        self.lookList = userListModule.ListBaseClass()
        self.lookList.listName = "lookList"
        self.lookList.populateListWidget(mayaNodesModule.MayaNodes)
        listIcon = QIcon(":/attrLook.svg")
        self.nodesWindow.insertTab(2, self.lookList, listIcon, "Particle Look")

        self.lookList = userListModule.ListBaseClass()
        self.lookList.listName = "utilitiesList"
        self.lookList.populateListWidget(mayaNodesModule.MayaNodes)
        listIcon = QIcon(":/objectNode.svg")
        self.nodesWindow.insertTab(3, self.lookList, listIcon, "Utilities")

        self.nodesWindow.setCurrentIndex(0)

    def setWidgetMenu(self, item):
        self.nodeMenuArea.takeWidget()
        self.nodeMenuArea.setWidget(item.getWidgetMenu())
        self.nodeOptionsWindow.setTitle(item.displayText.toPlainText())

    def graphicsView_wheelEvent(self, event):
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.nodeDropGraphicsView.scale(factor, factor)

    def graphicsView_resizeEvent(self, event):
        self.scene.setSceneRect(0, 0, self.nodeDropGraphicsView.width(), self.nodeDropGraphicsView.height())

    def makeConnections(self):
        self.emitterList.itemClicked.connect(self.changeDescription)
        self.behaviorList.itemClicked.connect(self.changeDescription)
        self.lookList.itemClicked.connect(self.changeDescription)
        self.scene.categoryItemClicked.connect(self.setWidgetMenu)


def show():
    global app

    # Use a shared instance of QApplication
    import maya.OpenMayaUI as mui
    app = QApplication.instance()

    # Get a pointer to the maya main window
    ptr = mui.MQtUtil.mainWindow()
    # Use sip to wrap the pointer into a QObject
    win = sip.wrapinstance(long(ptr), QObject)
    form = MainWindow(win)
    form.show()

'''
Run App
'''

if __name__ == "__main__":
    print "Standalone"
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


