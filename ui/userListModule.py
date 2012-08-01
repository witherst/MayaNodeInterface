from PyQt4.QtGui import *
from PyQt4.QtCore import *
import cPickle, weakref
from ui import nodeModule, mayaNodesModule

class ListBaseClass(QListWidget):

    d = weakref.WeakValueDictionary()

    def __init__(self, *args, **kwargs):
        super(ListBaseClass, self).__init__(*args, **kwargs)

        self.setLayout(QHBoxLayout())
        self.setWrapping(True)
        self.setLayoutMode(QListView.SinglePass)
        self.setDragEnabled(True)
        self.setSpacing(1.5)
        self.setGeometry(9, 9, 608, 193)

        self.listName = ""

    def populateListWidget(self, listItems):

        for key in sorted(listItems.iterkeys()):
            if listItems[key].nodeType == "category" and listItems[key].listWidgetName == self.listName:
                self.addItem(nodeModule.NodeListItem(listItems[key]))

        for key in sorted(listItems.iterkeys()):
            if listItems[key].nodeType == "attribute" and listItems[key].listWidgetName == self.listName:
                self.addItem(nodeModule.NodeListItem(listItems[key]))
            elif listItems[key].nodeType == "utility" and listItems[key].listWidgetName == self.listName:
                self.addItem(nodeModule.NodeListItem(listItems[key]))

    def startDrag(self, event):
        # item is of type NodeListItem
        item = self.currentItem()
        # nodeData is the data (NodeBase type) that item was created with
        nodeData = mayaNodesModule.MayaNodes[item.dictKey]

        i = id(nodeData)
        self.d[i] = nodeData
        pickleData = cPickle.dumps(i)
#        pickleData = cPickle.dumps(nodeData)
        data = QByteArray.fromRawData(pickleData)

        mimeData = QMimeData()
        mimeData.setData("application/x-imgname", data)

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        # Setting the icon that the mouse cursor displays
        icon = item.icon()
        pixmap = icon.pixmap(48, 48)
        drag.setPixmap(pixmap.scaled(pixmap.height()*.5, pixmap.width()*.5))
        # Actually starts the dragging
        drag.exec_()