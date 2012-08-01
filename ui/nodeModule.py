from PyQt4 import QtGui, QtCore, QtSvg
import maya.cmds as cmds

class NodeBase(object):

    def __init__(self, newNode = "", **kwargs):
        self.displayText = newNode.split(".")[0]
        self.imagePath =""
        self.description = "Foo"
        self.listWidgetName = ""
        self.mayaCMD = ""
        self.nodeType = ""
        self.dictKey = ""
        self.nodeColor = ""
        self.widgetMenu = None

        self._widgetMenuObj = None

        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def getWidgetMenu(self):
        if self._widgetMenuObj is None and self.widgetMenu:
            self._widgetMenuObj = self.widgetMenu()
        return self._widgetMenuObj

class NodeListItem(NodeBase, QtGui.QListWidgetItem):

    def __init__(self, *args, **kwargs):

        # Grab the args as a list so we can edit it
        args = list(args)
        otherNode = None
        # Check to see if the first argument is of type NodeBase
        if args and isinstance(args[0], NodeBase):
            otherNode = args.pop(0)

        # Separately initiate the inherited classes
        QtGui.QListWidgetItem.__init__(self, *args, **kwargs)
        NodeBase.__init__(self)

        # Set all necessary attributes that come from the base class if they're present
        self.displayText = otherNode.displayText if otherNode else ""
        self.dictKey = otherNode.dictKey if otherNode else ""
        self.imagePath = otherNode.imagePath if otherNode else ""
        self.description = otherNode.description if otherNode else ""
        self.nodeColor = otherNode.nodeColor if otherNode else ""
        self.listWidgetName = otherNode.listWidgetName if otherNode else None

        self.setIcon(QtGui.QIcon(self.imagePath))
        self.setText(self.displayText)

'''
************* CATEGORY NODE ***************
'''

class CategoryNode(NodeBase, QtSvg.QGraphicsSvgItem):

    clickedSignal = QtCore.pyqtSignal(QtCore.QObject)
    nodeCreatedInScene = QtCore.pyqtSignal()
    
    def __init__(self, *args, **kwargs):

        # Grab the args as a list so we can edit it
        args = list(args)
        otherNode = None
        # Check to see if the first argument is of type NodeBase
        if args and isinstance(args[0], NodeBase):
            otherNode = args.pop(0)

        # Separately init the inherited class
        NodeBase.__init__(self)

        # Set all necessary attributes that come from the base class if they're present
        self.displayText = otherNode.displayText if otherNode else ""
        self.dictKey = otherNode.dictKey if otherNode else ""
        self.imagePath = otherNode.imagePath if otherNode else ""
        self.description = otherNode.description if otherNode else ""
        self.nodeType = otherNode.nodeType if otherNode else ""
        self.nodeColor = otherNode.nodeColor if otherNode else ""
        self.listWidgetName = otherNode.listWidgetName if otherNode else None

        # If the imagePath exists, insert it into args for QGraphicsSvgItem.__init__(QString filename)
        # This is where the base image (cat_node_base.svg or attr_base.svg) is actually being used
        if self.imagePath:
            args.insert(0, self.imagePath)
        QtSvg.QGraphicsSvgItem.__init__(self, *args, **kwargs)

        # Set the attributes and variables specific to the Category Node Item
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|QtGui.QGraphicsItem.ItemIsMovable|QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False) # This added to get correct drawing of selection box around icon in viewport
        self.setAcceptHoverEvents(True)
        self.connectionPoints = [] # This is the amount of connection points that are on the node. Making it so you can have an arbitrary amount. Just have to make sure to append the connections to this list

        self.addNodeComponents()
        self.addText()
        self.nodeCreatedInScene.connect(self.doInitialMenuWidgetSetup)

    def addAttrConnections(self):
        self.attributeConnection = ConnectAttributeNode(":/catAttrConnection.svg", self)
        self.attributeConnection.setPos(-self.attributeConnection.width()/2, self.attributeConnection.height()/2 + 9)
        self.attributeConnection.isInputConnection = True
        self.attributeConnection.nodeType = self.nodeType
        self.connectionPoints.append(self.attributeConnection)

    def addCatConnections(self):
        if self.dictKey is "emitterCat":
            self.behaviorConnection = ConnectCategoryNode(":/behaviorInputConnection.svg", self)
            self.behaviorConnection.setPos(self.width()/2 - self.behaviorConnection.width()/2 + 6, -self.behaviorConnection.height()+6.0)
            self.behaviorConnection.isInputConnection = True
            self.behaviorConnection.nodeType = self.nodeType
            self.behaviorConnection.connectionName = "behavior"
            self.lookConnection = ConnectCategoryNode(":/lookInputConnection.svg", self)
            self.lookConnection.setPos(self.width()/2 - self.lookConnection.width()/2 + 6, self.height()-6)
            self.lookConnection.nodeType = self.nodeType
            self.lookConnection.isInputConnection = True
            self.lookConnection.connectionName = "look"
            self.connectionPoints.append(self.behaviorConnection)
            self.connectionPoints.append(self.lookConnection)
        elif self.dictKey is "behaviorCat":
            self.outputConnection = ConnectCategoryNode(":/behaviorOutputConnection.svg", self)
            self.outputConnection.setPos(self.width()/2 - self.outputConnection.width()/2 + 6, self.height()-6)
            self.outputConnection.nodeType = self.nodeType
            self.outputConnection.connectionName = "behavior"
            self.connectionPoints.append(self.outputConnection)
        elif self.dictKey is "lookCat":
            self.outputConnection = ConnectCategoryNode(":/lookOutputConnection.svg", self)
            self.outputConnection.setPos(self.width()/2 - self.outputConnection.width()/2 + 6, -self.outputConnection.height()+6.0)
            self.outputConnection.nodeType = self.nodeType
            self.outputConnection.connectionName = "look"
            self.connectionPoints.append(self.outputConnection)

    def addNodeComponents(self):
        self.addAttrConnections()
        self.addCatConnections()
        #self.addX()

    def addText(self):
        font = QtGui.QFont("SansSerif", 14)
        font.setStyleHint(QtGui.QFont.Helvetica)
        font.setStretch(100)
        self.displayText = QtGui.QGraphicsTextItem(self.displayText, self)
        self.displayText.setFont(font)
        self.displayText.setDefaultTextColor(QtGui.QColor(QtCore.Qt.white))
        self.displayText.setPos(self.boundingRect().width() + 5, self.sceneBoundingRect().center().y()/2 + 5)
        self.displayText.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

    def addX(self):
        self.x = xClass(":/X.svg", self)
        self.x.setPos(self.width()-5, -self.x.height()+5)

    def connectSignals(self):
        for item in self.connectionPoints:
            item.lineConnected.connect(self.getWidgetMenu().setupWidget)

    def deleteNode(self):
        for connectionPoint in self.connectionPoints:
            if connectionPoint.connectedLine:
                if not connectionPoint.isInputConnection:
                    # This for loop is going through all of the connected lines in the OUTPUT connection. Also doing this in "deleteLine" in graphicsModule
                    for connectedLine in connectionPoint.connectedLine:
                        connectedLine.getEndItem().getWidgetMenu().receiveFrom(connectedLine.getStartItem(), delete=True)
                        connectedLine.getStartItem().getWidgetMenu().sendData(connectedLine.getStartItem().getWidgetMenu().packageData())
                connectionPoint.clearLine()
                del connectionPoint.connectedLine[:]
        try:
            if self.dictKey is "emitterCat":
                cmds.delete(self.getWidgetMenu().getEmitter(), self.getWidgetMenu().getParticle())
            if self.dictKey is "instancer":
                self.getWidgetMenu().deleteInstancer()
            if self.dictKey.count("force"):
                cmds.select(self.getWidgetMenu().getObject())
                cmds.delete()
        except TypeError:
            pass
        self.scene().removeItem(self)

    def doInitialMenuWidgetSetup(self):
        '''
        This function is to do whatever the node needs to do when the node is JUST CREATED
        '''
        self.getWidgetMenu().setupWidget()

    def height(self):
        return self.sceneBoundingRect().height()

    def mousePressEvent(self, event):
        super(CategoryNode, self).mousePressEvent(event)
        self.clickedSignal.emit(self)
        if self.dictKey is "emitterCat":
            cmds.select(self.getWidgetMenu().getEmitter())

#        print self.getWidgetMenu().getEmitter()
#        print self.getWidgetMenu().getParticleShape()
#        print self.getWidgetMenu().getParticle()

    def paint(self, painter, option, widget):

        selected = False

        # Bitwise operations. These 2 if statements are checking to see if the current state of the item is selected or has focus.
        # If it is either, it sets them to false. Then, we set OUR selected flag to True so we can make our own selection graphic.
        # In essence, this "catches" the selected state and turns it off so the default BAD dotted line doesn't appear around the icon.
        if option.state & QtGui.QStyle.State_HasFocus:
            option.state ^= QtGui.QStyle.State_HasFocus
            selected = True

        if option.state & QtGui.QStyle.State_Selected:
            option.state ^= QtGui.QStyle.State_Selected
            selected = True

        super(CategoryNode, self).paint(painter, option, widget)

        # Since we turned off the default selection state, below we will make our own "selection" graphic.
        if selected:
            # Do special painting for selected state
            self.setElementId("hover")

        else:
            self.setElementId("regular")

    def removeReferences(self):
        '''
        This function goes through the attribute nodes connected to the Category node and resets their
        emitter, particle, and particleShape to None
        '''
        self.getWidgetMenu().clearEmitter()
        if isinstance(self, CategoryNode):
            for connection in self.connectionPoints:
                if isinstance(connection, ConnectAttributeNode):
                    for line in connection.connectedLine:
                        line.getStartItem().getWidgetMenu().clearEmitter()


    def width(self):
        return self.sceneBoundingRect().width()

'''
************* ATTRIBUTE NODE ***************
'''

class AttrNode(CategoryNode):

    def __init__(self, *args, **kwargs):
        super(AttrNode, self).__init__(*args, **kwargs)
        self.scale(.75, .75)

    def addAttrConnections(self):
        self.inputConnection = ConnectAttributeNode(":/attrConnection.svg", self)
        self.inputConnection.setPos(-self.inputConnection.width()+10, self.inputConnection.height()/2)
        self.inputConnection.isInputConnection = True
        self.inputConnection.nodeType = self.nodeType
        self.outputConnection = ConnectAttributeNode(":/catAttrConnection.svg", self)
        self.outputConnection.scale(1.5, 1.5)
        self.outputConnection.setPos(self.outputConnection.width()+32, self.outputConnection.height()/2)
        self.outputConnection.nodeType = self.nodeType
        self.connectionPoints.append(self.inputConnection)
        self.connectionPoints.append(self.outputConnection)

    def addText(self):
        super(AttrNode, self).addText()
        self.displayText.setPos(self.sceneBoundingRect().width()/2-self.displayText.sceneBoundingRect().width()/2, self.height()-15)

    def addX(self):
        super(AttrNode, self).addX()
        self.x.setPos(self.width() - 20, -self.x.height()+10)

class UtilityNode(CategoryNode):

    def __init__(self, *args, **kwargs):
        super(UtilityNode, self).__init__(*args, **kwargs)
        self.scale(.7, .7)

    def addAttrConnections(self):
        self.inputConnection = ConnectUtilityNode(":/attrConnection.svg", self)
        self.inputConnection.setPos(-self.inputConnection.width()+5, self.inputConnection.height()/2+6)
        self.inputConnection.isInputConnection = True
        self.inputConnection.nodeType = self.nodeType
        self.outputConnection = ConnectUtilityNode(":/attrConnection.svg", self)
        self.outputConnection.setPos(self.outputConnection.width()+77, self.outputConnection.height()/2+6)
        self.outputConnection.nodeType = self.nodeType
        self.connectionPoints.append(self.inputConnection)
        self.connectionPoints.append(self.outputConnection)

    def addText(self):
        super(UtilityNode, self).addText()
        self.displayText.setPos(self.sceneBoundingRect().width()/2-self.displayText.sceneBoundingRect().width()/2, self.height()-10)

    def addX(self):
        super(UtilityNode, self).addX()
        self.x.setPos(self.width() - 10, -self.x.height()+5)

'''
************ CONNECTION POINTS ON THE MAIN NODE ***********
'''

class ConnectionsBase(QtSvg.QGraphicsSvgItem):

    lineConnected = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ConnectionsBase, self).__init__(*args, **kwargs)
        self.setAcceptHoverEvents(True)
        self.isInputConnection = False
        self.connectedLine = []
        self.setElementId("regular")
        self.nodeType = ""
        self.connectionName = "" # connectionName is solely used for creating a line between a Behavior/Look Category node TO a Particle Emitter Category node
        self.lineConnected.connect(self.updateAll)
        self.lineConnected.connect(self.lineJustConnected)

    def clearLine(self):
        '''
        The purpose of this function is to graphically clear all a line and destroy references to it from other objects
        '''
        # The [:] denotes a copy of the connectedLine list. Because within deleteLine() I'm removing elements from connectedLine. Without [:] everything goes to shit.
        for line in self.connectedLine[:]:
            line.deleteLine()

    def lineJustConnected(self):
        '''
        This signal is being emitted in the mouseReleaseEvent() in graphicsModule.py
        '''
        self.parentItem().getWidgetMenu().justConnected()

    def width(self):
        return self.sceneBoundingRect().width()

    def height(self):
        return self.sceneBoundingRect().height()

    def hoverMoveEvent(self,event):
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        self.setElementId("regular")

    def mouseReleaseEvent(self, event):
        self.setElementId("regular")

    def updateAll(self):
        '''
        This is a function meant to update all attribute nodes when a new line is connected to a look or behavior category node.
        Example: Say a user hooks up 3 attributes nodes to a lookCat node before the lookCat is hooked into a particleEmitter node.
            Those attribute nodes won't receive the correct emitter and particleShape variables.
        It goes through each attribute connected and calls their setupWidget function which updates the emitter/particleShape variables
         and then gets the variables from the widgetMenu and sets them in Maya.
        '''
        # Updating
        if self.connectedLine:
            self.connectedLine[0].getStartItem().getWidgetMenu().updateMayaValues()
            for connection in self.connectedLine[0].getStartItem().connectionPoints:
                if isinstance(connection, ConnectAttributeNode) and connection.isInputConnection:
                    for line in connection.connectedLine:
                        line.getStartItem().getWidgetMenu().setEmitter(self.connectedLine[0].getStartItem().getWidgetMenu().emitter)
                        line.getStartItem().getWidgetMenu().setParticleShape(self.connectedLine[0].getStartItem().getWidgetMenu().particleShape)
                        line.getStartItem().getWidgetMenu().setParticle(self.connectedLine[0].getStartItem().getWidgetMenu().particle)
                        line.getStartItem().getWidgetMenu().updateMayaValues()
        
class ConnectCategoryNode(ConnectionsBase):

    def __init__(self, *args, **kwargs):
        super(ConnectCategoryNode, self).__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        print self.connectedLine

class ConnectAttributeNode(ConnectionsBase):

    def __init__(self, *args, **kwargs):
        super(ConnectAttributeNode, self).__init__(*args, **kwargs)
        self.setFlags(QtGui.QGraphicsItem.ItemStacksBehindParent)

    def mousePressEvent(self, event):
        print self.connectedLine

class ConnectUtilityNode(ConnectionsBase):

    def __init__(self, *args, **kwargs):
        super(ConnectUtilityNode, self).__init__(*args, **kwargs)
        self.setFlags(QtGui.QGraphicsItem.ItemStacksBehindParent)

    def mousePressEvent(self, event):
        print "Print: connected Line on Utility Connect Node: ", self.connectedLine

'''
************ THE 'X' GRAPHIC ON  THE MAIN NODE ***********
'''

class xClass(ConnectionsBase):

    def __init__(self, *args, **kwargs):
        super(xClass, self).__init__(*args, **kwargs)
        self.setZValue(1.0)

    def mousePressEvent(self, event):
        self.setElementId("down")