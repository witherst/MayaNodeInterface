from PyQt4.QtGui import *
from PyQt4.QtCore import *
import cPickle, math, weakref, mayaNodesModule, nodeWidgetsModule, userListModule
import maya.cmds as cmds
import nodeModule

global i

class SceneView(QGraphicsScene):

    categoryItemClicked = pyqtSignal(QObject)

    def __init__(self, parent=None):
        super(SceneView, self).__init__(parent)

        # Setting up variables
        self.sceneNodes = weakref.WeakValueDictionary() # Dict of all SVG nodes in the scene
        self.line = None

    def createNewParticles(self, widgetMenu):
        """
        This function is ONLY for the "collisionEvent" attribute node.
        """
        newPos = QPointF(150, 150)
        newParticleSystem = self.createNode(mayaNodesModule.MayaNodes['emitterCat'], newPos)
        cmds.setAttr(newParticleSystem.getWidgetMenu().getEmitter()+".rate", 0.0)
        widgetMenu.setTargetParticles(newParticleSystem.getWidgetMenu().getParticleShape())
        widgetMenu.targetParticleSystem.setText(newParticleSystem.getWidgetMenu().getParticleShape())

    def connectionTest(self, startItems, endItems):
        '''
        This is the big if statement that is checking
        to make sure that whatever nodes the user is trying to
        make a connection between is allowable.
        '''
        if startItems[0].isInputConnection:
            temp = startItems[0]
            startItems[0] = endItems[0]
            endItems[0] = temp

        try:
            if len(startItems) is not 0 and len(endItems) is not 0:
                if startItems[0] is not endItems[0]:
                    if isinstance(startItems[0], nodeModule.ConnectAttributeNode) and not isinstance(endItems[0], nodeModule.ConnectCategoryNode) or\
                       isinstance(startItems[0], nodeModule.ConnectCategoryNode) and isinstance(endItems[0], nodeModule.ConnectCategoryNode) or\
                       isinstance(startItems[0], nodeModule.ConnectUtilityNode) and isinstance(endItems[0], nodeModule.ConnectAttributeNode) or\
                       isinstance(startItems[0], nodeModule.ConnectAttributeNode) and isinstance(endItems[0], nodeModule.ConnectUtilityNode):
                        if (startItems[0].isInputConnection and not endItems[0].isInputConnection) or\
                           (endItems[0].isInputConnection and not startItems[0].isInputConnection):
                            if (startItems[0].parentItem().listWidgetName is endItems[0].parentItem().listWidgetName) or\
                                (startItems[0].connectionName is endItems[0].connectionName):
                                if startItems[0].parentItem().dictKey is "objectUtil" and endItems[0].parentItem().dictKey is "colliderAttr":
                                    if not endItems[0].parentItem().getWidgetMenu().getParticle():
                                        QMessageBox.warning(QMessageBox(), "Connection Warning", "Please make sure the Behavior Node or Look Node is connected to an Emitter.")
                                        return False
                                if (startItems[0].parentItem().dictKey.count("force") or startItems[0].parentItem().dictKey.count("collision")) and endItems[0].parentItem().dictKey is "behaviorCat":
                                    if not endItems[0].parentItem().getWidgetMenu().getParticleShape():
                                        QMessageBox.warning(QMessageBox(), "Connection Warning", "Please make sure the Behavior Node is connected to an Emitter.")
                                        return False
                                if not startItems[0].parentItem().nodeType is endItems[0].parentItem().nodeType:
                                    if not startItems[0].parentItem().nodeType is "utility":
                                        if not startItems[0].parentItem().nodeColor is endItems[0].parentItem().nodeColor:
                                            QMessageBox.warning(QMessageBox(), "Connection Warning", "Only Nodes of the SAME color can connect to each other.")
                                            return False
                                return True
        except AttributeError:
            pass
        return False

    def createNode(self, nodeToCreate, pos):
        # If node is already present in the scene, rename it
        name = nodeToCreate.displayText
        i = 1
        while name in self.sceneNodes:
            name = "%s%d" %(nodeToCreate.displayText, i)
            i += 1

        # Now transfer the nodeToCreate (which is the base class Node) to a category or attribute node
        if nodeToCreate.nodeType is "attribute":
            sceneNode = nodeModule.AttrNode(nodeToCreate)
        elif nodeToCreate.nodeType is "category":
            sceneNode = nodeModule.CategoryNode(nodeToCreate)
        elif nodeToCreate.nodeType is "utility":
            sceneNode = nodeModule.UtilityNode(nodeToCreate)

        sceneNode.widgetMenu = nodeToCreate.widgetMenu
        sceneNode.displayText.setPlainText(name)
        sceneNode.connectSignals()

        # Adding all the components to the main node (Connection points, X, text, etc...)
        sceneNode.setPos(pos)
        # Here I am emitting a signal with another signal. The purpose is to get the category node into to my MainWindow "space" (So I can use the variable to change the QScrollArea)
        sceneNode.clickedSignal.connect(self.categoryItemClicked.emit)
        sceneNode.nodeCreatedInScene.emit()
        # Below is what creates a new particle system for the collision event node
        if sceneNode.dictKey is "collisionEvent":
            sceneNode.getWidgetMenu().createParticles.connect(self.createNewParticles)
        self.sceneNodes[name] = sceneNode
        self.addItem(sceneNode)

        return sceneNode

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-imgname"):
            event.accept()
            data = event.mimeData().data("application/x-imgname")
            data = data.data()
            unPickleData = cPickle.loads(data)
            unPickleData = userListModule.ListBaseClass.d[unPickleData]
            # Create the node in the scene
            self.createNode(unPickleData, event.scenePos())
            if unPickleData.dictKey is "emitterCat":
                newPos = event.scenePos()
                newPos.setY(newPos.y()-175)
                behaviorNode = mayaNodesModule.MayaNodes['behaviorCat']
                self.createNode(behaviorNode, newPos)

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-imgname"):
            event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            for item in self.selectedItems():
                if isinstance(item, nodeModule.CategoryNode) or isinstance(item, nodeModule.AttrNode) or\
                isinstance(item,nodeModule.UtilityNode):
                    item.deleteNode()
                else:
                    try:
                        item.deleteLine()
                    except AttributeError:
                        pass

        else:
            super(SceneView, self).keyPressEvent(event)

    def mousePressEvent(self, event):
        item = self.itemAt(event.scenePos())

        if event.button() == Qt.LeftButton and (isinstance(item, nodeModule.ConnectCategoryNode) or isinstance(item, nodeModule.ConnectAttributeNode) or isinstance(item, nodeModule.ConnectUtilityNode)):
            self.line = QGraphicsLineItem(QLineF(event.scenePos(), event.scenePos()))
            self.addItem(self.line)

        if item is None:
            cmds.select(clear=True)

        super(SceneView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.line:
            newLine = QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)

        super(SceneView, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):

        if self.line:
            startItems = self.items(self.line.line().p1())
            if len(startItems) and startItems[0] == self.line:
                startItems.pop(0)
            endItems = self.items(self.line.line().p2())
            if len(endItems) and endItems[0] == self.line:
                endItems.pop(0)

            self.removeItem(self.line)

            # If this is true a successful line was created
            if self.connectionTest(startItems, endItems):
                # Creates a line that is basically of 0 length, just to put a line into the scene
                connectionLine = LineClass(startItems[0], endItems[0], QLineF(startItems[0].scenePos(), endItems[0].scenePos()))
                self.addItem(connectionLine)
                # Now use that previous line created and update its position, giving it the proper length and etc...
                connectionLine.updatePosition()
                # Setting the emitter, particle, and particleShape on the node
                connectionLine.getStartItem().getWidgetMenu().emitter = connectionLine.getEndItem().getWidgetMenu().emitter
                connectionLine.getStartItem().getWidgetMenu().particle = connectionLine.getEndItem().getWidgetMenu().particle
                connectionLine.getStartItem().getWidgetMenu().particleShape = connectionLine.getEndItem().getWidgetMenu().particleShape
                # Sending the data downstream. The start item is the upstream node ALWAYS. The end item is the downstream node ALWAYS.
                connectionLine.getEndItem().getWidgetMenu().receiveFrom(connectionLine.getStartItem(), delete=False)
                connectionLine.getStartItem().getWidgetMenu().sendData(connectionLine.getStartItem().getWidgetMenu().packageData())
                # Emitting the "justConnected" signal (That is on all connection points)
                connectionLine.myEndItem.lineConnected.emit()
                connectionLine.myStartItem.lineConnected.emit()

        self.line = None

        super(SceneView, self).mouseReleaseEvent(event)

# Line class for connecting the nodes together
class LineClass(QGraphicsLineItem):

    def __init__(self, startItem, endItem, *args, **kwargs):
        super(LineClass, self).__init__(*args, **kwargs)

        # The arrow that's drawn in the center of the line
        self.arrowHead = QPolygonF()
        self.myColor = Qt.black
        self.myStartItem = startItem
        self.myEndItem = endItem
        self.setZValue(-1.0)
        self.setFlags(QGraphicsItem.ItemIsSelectable|QGraphicsItem.ItemIsFocusable)
        self.setPen(QPen(self.myColor, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        '''
        This if statement is making all of the connections consistent. The startItem will always be the
        beginning of the line. The arrow will always point to the end item, no matter which way the user
        connects the line.
        '''
        try:
            if self.myStartItem.isInputConnection:
                temp = self.myStartItem
                self.myStartItem = self.myEndItem
                self.myEndItem = temp
        except AttributeError, e:
            print "Error checking isInputConnection on node %s" %str(e)

    def deleteLine(self):
        # For whatever the shit reason, I have to have this check. If I don't, I get an error in rare cases.
        if self:
            if self.getStartItem().dictKey.count("force"):
                cmds.connectDynamic(self.getStartItem().getWidgetMenu().getParticleShape(), delete=True, fields=self.getStartItem().getWidgetMenu().getObject())
            if self.getStartItem().dictKey is "behaviorCat" or self.getStartItem().dictKey is "lookCat":
                self.getStartItem().getWidgetMenu().particleName.setText(" ")
            if self.getStartItem().dictKey is "collisionEvent":
                self.getStartItem().getWidgetMenu().deleteEvent()
            self.getEndItem().getWidgetMenu().receiveFrom(self.getStartItem(), delete=True)
            self.getStartItem().getWidgetMenu().sendData(self.getStartItem().getWidgetMenu().packageData())
            self.getStartItem().removeReferences()
            self.scene().removeItem(self)
            self.myStartItem.connectedLine.remove(self)
            self.myEndItem.connectedLine.remove(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.deleteLine()
            self.update()
        else:
            super(LineClass, self).keyPressEvent(event)

    def getCenterPoint(self):
        line = self.getLine()
        centerX = (line.p1().x() + line.p2().x())/2
        centerY = (line.p1().y() + line.p2().y())/2
        return QPointF(centerX, centerY)

    def getLine(self):
        p1 = self.myStartItem.sceneBoundingRect().center()
        p2 = self.myEndItem.sceneBoundingRect().center()
        return QLineF(self.mapFromScene(p1), self.mapFromScene(p2))


    def getEndItem(self):
        return self.myEndItem.parentItem()

    def getStartItem(self):
        return self.myStartItem.parentItem()

    def updatePosition(self):
        self.setLine(self.getLine())
        self.myStartItem.connectedLine.append(self)
        self.myEndItem.connectedLine.append(self)

    def boundingRect(self):
        extra = (self.pen().width() + 100)  / 2.0
        line = self.getLine()
        p1 = line.p1()
        p2 = line.p2()
        return QRectF(p1, QSizeF(p2.x() - p1.x(), p2.y() - p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

    def shape(self):
        path = super(LineClass, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    def paint(self, painter, option, widget=None):
        arrowSize = 20.0
        line = self.getLine()
        painter.setBrush(self.myColor)
        myPen = self.pen()
        myPen.setColor(self.myColor)
        painter.setPen(myPen)

        if self.isSelected():
            painter.setBrush(Qt.yellow)
            myPen.setColor(Qt.yellow)
            myPen.setStyle(Qt.DashLine)
            painter.setPen(myPen)


        ####################################
        # This is Calculating the angle between the x-axis and the line of the arrow.
        # Then turning the arrow head to this angle so that it follows the direction of the arrow
        # If the angle is negative, turn the direction of the arrow
        ####################################

        if line.length() > 0.0:

            try:
                angle = math.acos(line.dx() / line.length())
            except ZeroDivisionError:
                angle = 0

            if line.dy() >= 0:
                angle = (math.pi * 2.0) - angle

            # Making sure that no matter which connectionCircle (output or input) is selected first, the arrow always points at the next input connection
            if self.myStartItem.isInputConnection:
                revArrow = 1
            else:
                revArrow = -1

            # Get the center point of the line
            centerPoint = self.getCenterPoint()

            # The head of the arrows tip is the centerPoint, so now calculate the other 2 arrow points
            arrowP1 = centerPoint + QPointF(math.sin(angle + math.pi / 3.0) * arrowSize * revArrow,
                                        math.cos(angle + math.pi / 3) * arrowSize * revArrow)
            arrowP2 = centerPoint + QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize * revArrow,
                                        math.cos(angle + math.pi - math.pi / 3.0) * arrowSize * revArrow)

            # Clear anything in the arrowHead polygon
            self.arrowHead.clear()

            # Set the points of the arrowHead polygon
            for point in [centerPoint, arrowP1, arrowP2]:
                self.arrowHead.append(point)

            if line:
                painter.drawPolygon(self.arrowHead)
                painter.drawLine(line)