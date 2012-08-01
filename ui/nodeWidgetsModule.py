from ui.basicEmitter import Ui_basicEmitterWidget
from ui.emissionAttrs import Ui_emissionAttrWidget
from ui.lifeSpanAttrs import Ui_lifespanAttrWidget
from ui.timeAttrs import Ui_timeAttrs
from ui.basicEmSpeedAttr import Ui_basicEmSpeedAttr
from ui.distDirAttr import Ui_distDirAttr
from ui.genControlAttr import Ui_genControlAttr
from ui.volSpeedAttr import Ui_volSpeedAttr
from ui.renderStats import Ui_renderStats
from ui.renderAttr import Ui_renderAttr
from ui.perParticleAttr import Ui_perParticleAttr
from ui.emitterCat import Ui_emitterCat
from ui.behaviorCat import Ui_behaviorCat
from ui.instancer import Ui_instancer
from ui.objectUtil import Ui_objectUtil
from ui.colliderUtil import Ui_colliderUtil
from ui.goalAttr import Ui_goalAttr
from ui.airForceAttr import Ui_airForceAttr
from ui.gravityForce import Ui_gravityForce
from ui.newtonForce import Ui_newtonForce
from ui.turbulenceForce import Ui_turbulenceForce
from ui.vortexForce import Ui_vortexForce
from ui.collisionEvent import Ui_collisionEvent
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import maya.cmds as cmds

class BaseAttrObject(object):

    def __init__(self):
        self.emitter = None
        self.particle = None
        self.particleShape = None
        self.dataToSend = {}
        self.receivedData = {}
        self.object = None

    def clearEmitter(self):
        self.emitter = None
        self.particle = None
        self.particleShape = None

    def connectSignals(self):
        pass

    def getEmitter(self):
        try:
            return self.emitter[0]
        except (TypeError, AttributeError), e:
            print "getEmitter() Error: %s" %str(e)

    def getObject(self):
        try:
            return self.object
        except (TypeError, AttributeError), e:
            print "getObject() Error: %s" %str(e)

    def getParticle(self):
        try:
            return self.particle[0]
        except (TypeError, AttributeError), e:
            print "getParticle() Error: %s" %str(e)

    def getParticleShape(self):
        try:
            return self.particle[1]
        except (TypeError, AttributeError), e:
            print "getParticleShape() Error: %s" %str(e)

    def setEmitter(self, emitter):
        self.emitter = emitter

    def setParticle(self, particle):
        self.particle = particle

    def setParticleShape(self, particle):
        self.particleShape = particle

    def setObject(self, object):
        if object is not None:
            self.object = object.replace(' ', '_')
            self.object = object.lstrip('1234567890')
        else:
            self.object = None

    def setScriptJobs(self):
        pass

    def setupVariables(self):
        pass

class AbstractAttrObject(QWidget, BaseAttrObject):

    dataReady = pyqtSignal(object)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        BaseAttrObject.__init__(self)
        self._connectedTo = None

    def deleteData(self, data):
        """
        Abstract. This is the exact opposite of receiveData(). When a node is deleted this function
          will be called. So whatever data was obtained needs to be cleaned up and deleted.

        IMPORTANT: MUST ADD "self._connectedTo.getWidgetMenu().dataReady.disconnect(self.deleteData)"
         TO THE END OF EACH OF THESE FUNCTIONS YOU OVERLOAD OR EVERYTHING WILL GO TO SHIT.
        """
        pass

    def justConnected(self):
        """
        Abstract. This function is called WHEN TWO NODES ARE CONNECTED TOGETHER.
        Example: When I connect an ObjectUtility node into my Instancer, I will use this function to
         call another function that adds that object to the instancer list.
        """
        pass

    def packageData(self):
        """
        Abstract. Use this function to put all variables in a dictionary that you want the downstream nodes
         to access. MUST be in a dictionary.
        """
        pass

    def receiveData(self, data):
        """
        Abstract. receivedData will have whatever data the upstreamNode sends it. Then it's
         up to the widget to process and do stuff with that data.
        """
        pass

    def receiveFrom(self, otherObject, delete):
        """
        Connect this object to an upstream object and receive data from its output. You can specify
         whether or not the item is being deleted or created with the "delete" flag. This is used in
         "deleteNode()" in nodeModule.py under CategoryNode.
        """

        # _connectedTo is the other node. UtilNode/AttrNode/CategoryNode
        if self._connectedTo:
            try:
                self._connectedTo.getWidgetMenu().dataReady.disconnect(self.receiveData)
            except Exception, e:
                print "Trying to disconnect from delete function ERROR: %s" %str(e)

        if delete:
            otherObject.getWidgetMenu().dataReady.connect(self.deleteData)
        else:
            otherObject.getWidgetMenu().dataReady.connect(self.receiveData)
        self._connectedTo = otherObject

    def sendData(self, data):
        print "sendData() function called by: ", self
        """ Send data to downstream objects """
        self.dataReady.emit(data)
        print "EMITTED DATA"

    def setupWidget(self):
        """
        Abstract. This function is called AS SOON AS THE NODE IS CREATED IN THE SCENE, regardless of
         if it is connected to another node.
        """
        pass

    def updateMayaValues(self):
        """
        Abstract. The purpose of this function is to update all the widget's values in Maya when a new particle emitter is connected.
        Basically, call all the changeFunctions() in this. If you need to do something else, like create a Instancer node
         (example the "instancer" node), call those functions here.
        This function is called in nodeModule.py in def updateAll() in class ConnectionsBase()
        """
        pass

class basicEmitterWidget(AbstractAttrObject, Ui_basicEmitterWidget):

    def __init__(self, parent = None):
        super(basicEmitterWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()
        self.setupVariables()

    def changeRate(self, num):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".rate", num)

    def changeRateObject(self, num):
        if self.emitter:
            # In PyQt, a checked box is = 2. In Maya a checked box is = 1
            if num > 1:
                num = 1
            cmds.setAttr(self.getEmitter()+".scaleRateByObjectSize", num)

    def changeRateSpeed(self, num):
        if self.emitter:
            # In PyQt, a checked box is = 2. In Maya a checked box is = 1
            if num > 1:
                num = 1
            cmds.setAttr(self.getEmitter()+".scaleRateBySpeed", num)

    def changeSectionRadius(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".sectionRadius", value)

    def changeVolumeShape(self, index):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".volumeShape", index)

    def changeVolumeSweep(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".volumeSweep", value)

    def connectSignals(self):
        """Gui Related"""
        self.emitterType.activated.connect(self.handleActivation)
        self.volumeShape.activated.connect(self.handleVolEmitAttr)
        """Maya Related"""
        self.rate.valueChanged.connect(self.changeRate)
        self.scaleRateSpeed.stateChanged.connect(self.changeRateSpeed)
        self.scaleRateObjectSize.stateChanged.connect(self.changeRateObject)
        self.volumeShape.activated.connect(self.changeVolumeShape)
        self.volumeSweep.valueChanged.connect(self.changeVolumeSweep)
        self.sectionRadius.valueChanged.connect(self.changeSectionRadius)


    def handleActivation(self, index):
        if index is 0 or index is 1:
            self.scaleRateObjectSize.setEnabled(False)
        elif index is 2 or index is 3 or index is 4:
            self.scaleRateObjectSize.setEnabled(True)

        if index is 4:
            self.volumeEmitAttr.setCurrentIndex(1)
        else:
            self.volumeEmitAttr.setCurrentIndex(0)

        if self.getEmitter():
            cmds.setAttr(self.getEmitter()+".emitterType", index)

    def handleVolEmitAttr(self, index):
        if index is 0:
            self.volumeOffset.setEnabled(True)
            self.volumeSweep.setEnabled(False)
            self.sectionRadius.setEnabled(False)
        elif index is 1 or index is 2 or index is 3:
            self.volumeOffset.setEnabled(True)
            self.volumeSweep.setEnabled(True)
            self.sectionRadius.setEnabled(False)
        elif index is 4:
            self.volumeOffset.setEnabled(True)
            self.volumeSweep.setEnabled(True)
            self.sectionRadius.setEnabled(True)

    def setupVariables(self):
        self.scaleRateObjectSize.setEnabled(False)
        self.volumeSweep.setEnabled(False)
        self.sectionRadius.setEnabled(False)
        self.scaleRateObjectSize.setChecked(True)
        self.volumeSweep.setValue(360.0)
        self.sectionRadius.setValue(0.5)
        self.emitterType.setCurrentIndex(1)

    def updateMayaValues(self):
        self.changeRate(self.rate.value())
        self.changeRateSpeed(self.scaleRateSpeed.checkState())
        self.changeRateObject(self.scaleRateObjectSize.checkState())
        self.changeVolumeShape(self.volumeShape.currentIndex())
        self.changeVolumeSweep(self.volumeSweep.value())
        self.changeSectionRadius(self.sectionRadius.value())
        self.handleActivation(self.emitterType.currentIndex())

class emissionAttrWidget(AbstractAttrObject, Ui_emissionAttrWidget):

    def __init__(self, parent = None):
        super(emissionAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def mousePressEvent(self, event):
        super(emissionAttrWidget, self).mousePressEvent(event)
        self.maxCount.valueChanged.emit(self.maxCount.value())

    def changeMaxCount(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".maxCount", value)

    def changeLevelOfDetail(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".levelOfDetail", value)

    def changeInheritFactor(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".inheritFactor", value)

    def changeEmissionInWorld(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".emissionInWorld", num)

    def changeVolumeExit(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".dieOnEmissionVolumeExit", num)

    def connectSignals(self):
        self.maxCount.valueChanged.connect(self.changeMaxCount)
        self.levelOfDetail.valueChanged.connect(self.changeLevelOfDetail)
        self.inheritFactor.valueChanged.connect(self.changeInheritFactor)
        self.emissionInWorld.stateChanged.connect(self.changeEmissionInWorld)
        self.dieOnEmissionVolExit.stateChanged.connect(self.changeVolumeExit)

    def updateMayaValues(self):
        self.changeMaxCount(self.maxCount.value())
        self.changeLevelOfDetail(self.levelOfDetail.value())
        self.changeInheritFactor(self.inheritFactor.value())
        self.changeEmissionInWorld(self.emissionInWorld.checkState())
        self.changeVolumeExit(self.dieOnEmissionVolExit.checkState())

class lifespanAttrWidget(AbstractAttrObject, Ui_lifespanAttrWidget):

    def __init__(self, parent = None):
        super(lifespanAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()
        self.setupVariables()

    def changeLifespan(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".lifespan", value)

    def changeLifespanRandom(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".lifespanRandom", value)

    def changeGeneralSeed(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".generalSeed", value)

    def connectSignals(self):
        self.lifeSpanMode.activated.connect(self.handleActivation)
        self.lifeSpan.valueChanged.connect(self.changeLifespan)
        self.lifeSpanRandom.valueChanged.connect(self.changeLifespanRandom)
        self.generalSeed.valueChanged.connect(self.changeGeneralSeed)

    def handleActivation(self, index):
        if index is 0:
            self.lifeSpan.setEnabled(False)
            self.lifeSpanRandom.setEnabled(False)
            self.generalSeed.setEnabled(False)
        elif index is 1:
            self.lifeSpan.setEnabled(True)
            self.lifeSpanRandom.setEnabled(False)
            self.generalSeed.setEnabled(False)
        elif index is 2:
            self.lifeSpan.setEnabled(True)
            self.lifeSpanRandom.setEnabled(True)
            self.generalSeed.setEnabled(True)
        elif index is 3:
            self.lifeSpan.setEnabled(False)
            self.lifeSpanRandom.setEnabled(False)
            self.generalSeed.setEnabled(False)

        if self.particle:
            cmds.setAttr(self.getParticle()+".lifespanMode", index)

    def setupVariables(self):
        self.lifeSpan.setEnabled(False)
        self.lifeSpanRandom.setEnabled(False)
        self.generalSeed.setEnabled(False)

    def updateMayaValues(self):
        self.changeLifespan(self.lifeSpan.value())
        self.changeLifespanRandom(self.lifeSpanRandom.value())
        self.changeGeneralSeed(self.generalSeed.value())

class timeAttrWidget(AbstractAttrObject, Ui_timeAttrs):

    def __init__(self, parent = None):
        super(timeAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()
        self.changeCurrentTime()
        self.setScriptJobs()

    def changeCurrentTime(self):
        self.currentFrame.setText("%.2f" %cmds.currentTime(query=True))

    def changeStartFrame(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".startFrame", value)

    def connectSignals(self):
        self.startFrame.valueChanged.connect(self.changeStartFrame)

    def setScriptJobs(self):
        self.timeChanged = cmds.scriptJob(event=['timeChanged', self.changeCurrentTime])

    def updateMayaValues(self):
        self.changeStartFrame(self.startFrame.value())

class basicEmSpeedAttrWidget(AbstractAttrObject, Ui_basicEmSpeedAttr):

    def __init__(self, parent = None):
        super(basicEmSpeedAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def changeSpeed(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".speed", value)

    def changeSpeedRandom(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".speedRandom", value)

    def changeNormalSpeed(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".normalSpeed", value)

    def changeTangentSpeed(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".tangentSpeed", value)

    def connectSignals(self):
        self.speed.valueChanged.connect(self.changeSpeed)
        self.speedRandom.valueChanged.connect(self.changeSpeedRandom)
        self.tangentSpeed.valueChanged.connect(self.changeTangentSpeed)
        self.normalSpeed.valueChanged.connect(self.changeNormalSpeed)

    def updateMayaValues(self):
        self.changeSpeed(self.speed.value())
        self.changeSpeedRandom(self.speedRandom.value())
        self.changeTangentSpeed(self.tangentSpeed.value())
        self.changeNormalSpeed(self.normalSpeed.value())

class distDirWidget(AbstractAttrObject, Ui_distDirAttr):

    def __init__(self, parent = None):
        super(distDirWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def changeDirX(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".directionX", value)

    def changeDirY(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".directionY", value)

    def changeDirZ(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".directionZ", value)

    def changeMaxDist(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".maxDistance", value)

    def changeMinDist(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".minDistance", value)

    def changeSpread(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".spread", value)

    def connectSignals(self):
        self.minDist.valueChanged.connect(self.changeMinDist)
        self.maxDist.valueChanged.connect(self.changeMaxDist)
        self.dirX.valueChanged.connect(self.changeDirX)
        self.dirY.valueChanged.connect(self.changeDirY)
        self.dirZ.valueChanged.connect(self.changeDirZ)
        self.spread.valueChanged.connect(self.changeSpread)

    def updateMayaValues(self):
        self.changeMinDist(self.minDist.value())
        self.changeMaxDist(self.maxDist.value())
        self.changeDirX(self.dirX.value())
        self.changeDirY(self.dirY.value())
        self.changeDirZ(self.dirZ.value())
        self.changeSpread(self.spread.value())

class genControlAttrWidget(AbstractAttrObject, Ui_genControlAttr):

    def __init__(self, parent = None):
        super(genControlAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()
        self.setupScriptJob()

    def changeConserve(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".conserve", value)

    def changeCount(self):
        if self.particle:
            self.count.setText(str(cmds.particle(self.getParticle(), q=True, count=True)))

    def changeDynamicsWeight(self, value):
        if self.particle:
            cmds.setAttr(self.getParticle()+".dynamicsWeight", value)

    def changeForcesInWorld(self, num):
        if num > 1:
            num = 1
        if self.particle:
            cmds.setAttr(self.getParticle()+".forcesInWorld", num)

    def changeIsDynamic(self, num):
        if num > 1:
            num = 1
        if self.particle:
            cmds.setAttr(self.getParticle()+".isDynamic", num)

    def connectSignals(self):
        self.isDynamic.stateChanged.connect(self.changeIsDynamic)
        self.dynamicsWeight.valueChanged.connect(self.changeDynamicsWeight)
        self.conserve.valueChanged.connect(self.changeConserve)
        self.forcesInWorld.stateChanged.connect(self.changeForcesInWorld)

    def setupScriptJob(self):
        self.particleCount = cmds.scriptJob(event=['timeChanged', self.changeCount])

    def updateMayaValues(self):
        self.changeIsDynamic(self.isDynamic.checkState())
        self.changeDynamicsWeight(self.dynamicsWeight.value())
        self.changeConserve(self.conserve.value())
        self.changeForcesInWorld(self.forcesInWorld.checkState())

class volSpeedAttrWidget(AbstractAttrObject, Ui_volSpeedAttr):

    def __init__(self, parent = None):
        super(volSpeedAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def changeAlongAxis(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".alongAxis", value)

    def changeAroundAxis(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".aroundAxis", value)

    def changeAwayFromAxis(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".awayFromAxis", value)

    def changeAwayFromCenter(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".awayFromCenter", value)

    def changeDirectionalSpeed(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".directionalSpeed", value)

    def changeDisplaySpeed(self, num):
        if num > 1:
            num = 1
        if self.particle:
            cmds.setAttr(self.getEmitter()+".displaySpeed", num)

    def changeRandomDirection(self, value):
        if self.emitter:
            cmds.setAttr(self.getEmitter()+".randomDirection", value)

    def changeScaleSpeedBySize(self, num):
        if num > 1:
            num = 1
        if self.emitter:
            print num
            cmds.setAttr(self.getEmitter()+".scaleSpeedBySize", num)

    def connectSignals(self):
        self.awayFromCenter.valueChanged.connect(self.changeAwayFromCenter)
        self.awayFromAxis.valueChanged.connect(self.changeAwayFromAxis)
        self.alongAxis.valueChanged.connect(self.changeAlongAxis)
        self.aroundAxis.valueChanged.connect(self.changeAroundAxis)
        self.randomDirection.valueChanged.connect(self.changeRandomDirection)
        self.directionalSpeed.valueChanged.connect(self.changeDirectionalSpeed)
        self.scaleSpeedBySize.stateChanged.connect(self.changeScaleSpeedBySize)
        self.displaySpeed.stateChanged.connect(self.changeDisplaySpeed)

    def updateMayaValues(self):
        self.changeAwayFromCenter(self.awayFromCenter.value())
        self.changeAwayFromAxis(self.awayFromAxis.value())
        self.changeAlongAxis(self.alongAxis.value())
        self.changeAroundAxis(self.aroundAxis.value())
        self.changeRandomDirection(self.randomDirection.value())
        self.changeDirectionalSpeed(self.directionalSpeed.value())
        self.changeScaleSpeedBySize(self.scaleSpeedBySize.checkState())
        self.changeDisplaySpeed(self.displaySpeed.checkState())

class renderStatsWidget(AbstractAttrObject, Ui_renderStats):

    def __init__(self, parent = None):
        super(renderStatsWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def changeCastShadows(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".castsShadows", num)

    def changeReceiveShadows(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".receiveShadows", num)

    def changeRefl(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".visibleInReflections", num)

    def changeRefr(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".visibleInRefractions", num)

    def changeMotionBlur(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".motionBlur", num)

    def changeVisibility(self, num):
        if self.particle:
            if num > 1:
                num = 1
            cmds.setAttr(self.getParticle()+".primaryVisibility", num)

    def connectSignals(self):
        self.visibleInReflections.stateChanged.connect(self.changeRefl)
        self.visibleInRefractions.stateChanged.connect(self.changeRefr)
        self.castsShadows.stateChanged.connect(self.changeCastShadows)
        self.receiveShadows.stateChanged.connect(self.changeReceiveShadows)
        self.motionBlur.stateChanged.connect(self.changeMotionBlur)
        self.primaryVisibility.stateChanged.connect(self.changeVisibility)

    def updateMayaValues(self):
        self.changeRefl(self.visibleInReflections.checkState())
        self.changeRefr(self.visibleInRefractions.checkState())
        self.changeCastShadows(self.castsShadows.checkState())
        self.changeReceiveShadows(self.receiveShadows.checkState())
        self.changeMotionBlur(self.motionBlur.checkState())
        self.changeVisibility(self.primaryVisibility.checkState())

class renderAttrWidget(AbstractAttrObject, Ui_renderAttr):

    def __init__(self, parent = None):
        super(renderAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def changeDepthSort(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".depthSort", num)

    def changeLighting(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".useLighting", num)

    def changeColorAccumMP(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".colorAccum", num)

    def changeMultiCountMP(self, value):
        cmds.setAttr(self.getParticleShape()+".multiCount", value)

    def changeMultiRadiusMP(self, value):
        cmds.setAttr(self.getParticleShape()+".multiRadius", value)

    def changeNormalDirMP(self, value):
        cmds.setAttr(self.getParticleShape()+".normalDir", value)

    def changePointSizeMP(self, value):
        cmds.setAttr(self.getParticleShape()+".pointSize", value)

    def changeColorAccumMS(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".colorAccum", num)

    def changeLineWidthMS(self, value):
        cmds.setAttr(self.getParticleShape()+".lineWidth", value)

    def changeMultiCountMS(self, value):
        cmds.setAttr(self.getParticleShape()+".multiCount", value)

    def changeMultiRadiusMS(self, value):
        cmds.setAttr(self.getParticleShape()+".multiRadius", value)

    def changeNormalDirMS(self, value):
        cmds.setAttr(self.getParticleShape()+".normalDir", value)

    def changeTailFadeMS(self, value):
        cmds.setAttr(self.getParticleShape()+".tailFade", value)

    def changeTailSizeMS(self, value):
        cmds.setAttr(self.getParticleShape()+".tailSize", value)

    def changeAttrNameNum(self):
        cmds.setAttr(self.getParticleShape()+".attributeName", self.attributeNameNum.text(), type='string')

    def changePointSizeNum(self, value):
        cmds.setAttr(self.getParticleShape()+".pointSize", value)

    def changeSelectedOnlyNum(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".selectedOnly", num)

    def changeColorAccumPoints(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getParticleShape()+".colorAccum", num)

    def changeNormalDirPoints(self, value):
        cmds.setAttr(self.getParticleShape()+".normalDir", value)

    def changePointSizePoints(self, value):
        cmds.setAttr(self.getParticleShape()+".pointSize", value)

    def changeRadiusSphere(self, value):
        cmds.setAttr(self.getParticleShape()+".radius", value)

    def changeSpriteNum(self, value):
        cmds.setAttr(self.getParticleShape()+".spriteNum", value)

    def changeSSX(self, value):
        cmds.setAttr(self.getParticleShape()+".spriteScaleX", value)

    def changeSSY(self, value):
        cmds.setAttr(self.getParticleShape()+".spriteScaleY", value)

    def changeSpriteTwist(self, value):
        cmds.setAttr(self.getParticleShape()+".spriteTwist", value)

    def changeLineWidthStreak(self, value):
        cmds.setAttr(self.getParticleShape()+".lineWidth", value)

    def changeNormalDirStreak(self, value):
        cmds.setAttr(self.getParticleShape()+".normalDir", value)

    def changeTailFadeStreak(self, value):
        cmds.setAttr(self.getParticleShape()+".tailFade", value)

    def changeTailSizeStreak(self, value):
        cmds.setAttr(self.getParticleShape()+".tailSize", value)

    def changeRadiusBlobby(self, value):
        cmds.setAttr(self.getParticleShape()+".radius", value)

    def changeThresholdBlobby(self, value):
        cmds.setAttr(self.getParticleShape()+".threshold", value)

    def changeRadiusCloud(self, value):
        cmds.setAttr(self.getParticleShape()+".radius", value)

    def changeSurfShadCloud(self, value):
        cmds.setAttr(self.getParticleShape()+".surfaceShading", value)

    def changeThresholdCloud(self, value):
        cmds.setAttr(self.getParticleShape()+".threshold", value)

    def changeRadius0(self, value):
        cmds.setAttr(self.getParticleShape()+".radius0", value)

    def changeRadius1(self, value):
        cmds.setAttr(self.getParticleShape()+".radius1", value)

    def changeTailSizeTube(self, value):
        cmds.setAttr(self.getParticleShape()+".tailSize", value)

    def changeRenderType(self, index):
        cmds.setAttr(self.getParticleShape()+".particleRenderType", index)
        print self.getParticleShape()+".particleRenderType"

    def connectSignals(self):
        self.depthSort.stateChanged.connect(self.changeDepthSort)
        self.useLighting.stateChanged.connect(self.changeLighting)
        self.particleRenderType.currentIndexChanged.connect(self.changeRenderType)
        """MultiPoint"""
        self.colorAccumulationMP.stateChanged.connect(self.changeColorAccumMP)
        self.multiCountMP.valueChanged.connect(self.changeMultiCountMP)
        self.multiRadiusMP.valueChanged.connect(self.changeMultiRadiusMP)
        self.normalDirMP.valueChanged.connect(self.changeNormalDirMP)
        self.pointSizeMP.valueChanged.connect(self.changePointSizeMP)
        """MultiStreak"""
        self.colorAccumulationMS.stateChanged.connect(self.changeColorAccumMS)
        self.lineWidthMS.valueChanged.connect(self.changeLineWidthMS)
        self.multiCountMS.valueChanged.connect(self.changeMultiCountMS)
        self.multiRadiusMS.valueChanged.connect(self.changeMultiRadiusMS)
        self.normalDirMS.valueChanged.connect(self.changeNormalDirMS)
        self.tailFadeMS.valueChanged.connect(self.changeTailFadeMS)
        self.tailSizeMS.valueChanged.connect(self.changeTailSizeMS)
        """Numeric"""
        self.attributeNameNum.editingFinished.connect(self.changeAttrNameNum)
        self.pointSizeNum.valueChanged.connect(self.changePointSizeNum)
        self.selectedOnlyNum.stateChanged.connect(self.changeSelectedOnlyNum)
        """Points"""
        self.colorAccumulationPoints.stateChanged.connect(self.changeColorAccumPoints)
        self.normalDirPoints.valueChanged.connect(self.changeNormalDirPoints)
        self.pointSizePoints.valueChanged.connect(self.changePointSizePoints)
        """Spheres"""
        self.radiusSphere.valueChanged.connect(self.changeRadiusSphere)
        """Sprites"""
        self.spriteNum.valueChanged.connect(self.changeSpriteNum)
        self.spriteScaleX.valueChanged.connect(self.changeSSX)
        self.spriteScaleY.valueChanged.connect(self.changeSSY)
        self.spriteTwist.valueChanged.connect(self.changeSpriteTwist)
        """Streak"""
        self.lineWidthStreak.valueChanged.connect(self.changeLineWidthStreak)
        self.normalDirStreak.valueChanged.connect(self.changeNormalDirStreak)
        self.tailFadeStreak.valueChanged.connect(self.changeTailFadeStreak)
        self.tailSizeStreak.valueChanged.connect(self.changeTailSizeStreak)
        """Blobby Surface"""
        self.radiusBlobby.valueChanged.connect(self.changeRadiusBlobby)
        self.thresholdBlobby.valueChanged.connect(self.changeThresholdBlobby)
        """Cloud"""
        self.radiusCloud.valueChanged.connect(self.changeRadiusCloud)
        self.surfaceShadingCloud.valueChanged.connect(self.changeSurfShadCloud)
        self.thresholdCloud.valueChanged.connect(self.changeThresholdCloud)
        """Tube"""
        self.radius0Tube.valueChanged.connect(self.changeRadius0)
        self.radius1Tube.valueChanged.connect(self.changeRadius1)
        self.tailSizeTube.valueChanged.connect(self.changeTailSizeTube)

class ppTextEdit(QTextEdit):

    def __init__(self, parent=None):
        super(ppTextEdit, self).__init__(parent)
        self.setPlainText("//Example:\n//particleShape.attribute = yourExpression;\n\n")

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-text"):
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-text"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-text"):
            data = event.mimeData().data("application/x-text")
            stream = QDataStream(data, QIODevice.ReadOnly)
            text = stream.readQString()
            self.append(text)
            event.accept()
        else:
            event.ignore()

class perParticleAttrWidget(AbstractAttrObject, Ui_perParticleAttr):

    def __init__(self, parent = None):
        super(perParticleAttrWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()
        self.attrList.startDrag = self.listStartDrag
        self.addMenus()

    def addMenus(self):
        self.creationExp = ppTextEdit()
        self.beforeDynExp = ppTextEdit()
        self.afterDynExp = ppTextEdit()
        self.particleAttrExpressions.insertWidget(0, self.creationExp)
        self.particleAttrExpressions.insertWidget(1, self.beforeDynExp)
        self.particleAttrExpressions.insertWidget(2, self.afterDynExp)
        self.particleAttrExpressions.setCurrentIndex(0)

    def connectSignals(self):
        self.updateExpressionButton.clicked.connect(self.updateExpression)

    def listStartDrag(self, dropActions):
        item = self.attrList.currentItem()
        data = QByteArray()
        stream = QDataStream(data, QIODevice.WriteOnly)
        if self.getParticleShape():
            textString = self.getParticleShape() + '.' + item.text()
        else:
            textString = item.text()
        stream.writeQString(textString)
        mimeData = QMimeData()
        mimeData.setData("application/x-text",data)
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_()

    def setupWidget(self):
        if self.getParticleShape():
            self.currentParticleShape.setText(self.getParticleShape())

    def updateMayaValues(self):
        self.currentParticleShape.setText(self.getParticleShape())

    def updateExpression(self):
        print str(self.creationExp.toPlainText())
        if self.runExpression.currentIndex() is 0:
            cmds.dynExpression(self.getParticleShape(), string=str(self.creationExp.toPlainText()), c = True)
        elif self.runExpression.currentIndex() is 1:
            cmds.dynExpression(self.getParticleShape(), string=str(self.beforeDynExp.toPlainText()), rbd = True)
        elif self.runExpression.currentIndex() is 2:
            cmds.dynExpression(self.getParticleShape(), string=str(self.afterDynExp.toPlainText()), rad = True)

class emitterCatWidget(AbstractAttrObject, Ui_emitterCat):

    def __init__(self, parent = None):
        super(emitterCatWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def addParticleAttributes(self):
        cmds.select(self.getParticleShape())
        cmds.addAttr(attributeType='bool', longName='useLighting')
        cmds.addAttr(attributeType='bool', longName='colorAccum')
        cmds.addAttr(attributeType='long', longName='multiCount')
        cmds.addAttr(attributeType='float', longName='multiRadius')
        cmds.addAttr(attributeType='long', longName='normalDir')
        cmds.addAttr(attributeType='long', longName='pointSize')
        cmds.addAttr(attributeType='long', longName='lineWidth')
        cmds.addAttr(attributeType='float', longName='tailFade')
        cmds.addAttr(attributeType='float', longName='tailSize')
        cmds.addAttr(dataType='string', longName='attributeName')
        cmds.addAttr(attributeType='bool', longName='selectedOnly')
        cmds.addAttr(attributeType='float', longName='radius')
        cmds.addAttr(attributeType='long', longName='spriteNum')
        cmds.addAttr(attributeType='float', longName='spriteScaleX')
        cmds.addAttr(attributeType='float', longName='spriteScaleY')
        cmds.addAttr(attributeType='float', longName='spriteTwist')
        cmds.addAttr(attributeType='float', longName='threshold')
        cmds.addAttr(attributeType='bool', longName='betterIllumination')
        cmds.addAttr(attributeType='float', longName='surfaceShading')
        cmds.addAttr(attributeType='float', longName='radius0')
        cmds.addAttr(attributeType='float', longName='radius1')
        cmds.addAttr(dataType='vectorArray', longName='rgbPP')
        cmds.addAttr(dataType='doubleArray', longName='opacityPP')

    def connectSignals(self):
        self.emitterName.editingFinished.connect(self.renameEmitter)
        self.tx.editingFinished.connect(self.setTranslate)
        self.ty.editingFinished.connect(self.setTranslate)
        self.tz.editingFinished.connect(self.setTranslate)
        self.rx.editingFinished.connect(self.setRotate)
        self.ry.editingFinished.connect(self.setRotate)
        self.rz.editingFinished.connect(self.setRotate)

    def createParticleSystem(self):
        cmds.select(deselect=True)
        self.setEmitter(cmds.emitter())
        self.setParticle(cmds.particle())
        cmds.connectDynamic(self.getParticleShape(), emitters=self.getEmitter())
        self.emitterName.setText(self.getEmitter())
        self.setScriptJobs()
        self.addParticleAttributes()

    def mousePressEvent(self, event):
        super(emitterCatWidget, self).mousePressEvent(event)

    def renameEmitter(self):
        cmds.rename(self.getEmitter(), str(self.emitterName.text()))
        self.emitter[0] = str(self.emitterName.text())
        self.emitter[0] = self.emitter[0].replace(' ', '_')
        self.emitterName.setText(self.emitter[0])

    def rotateX(self):
        self.rx.setText("%.2f" %cmds.getAttr(self.getEmitter()+".rotateX"))

    def rotateY(self):
        self.ry.setText("%.2f" %cmds.getAttr(self.getEmitter()+".rotateY"))

    def rotateZ(self):
        self.rz.setText("%.2f" %cmds.getAttr(self.getEmitter()+".rotateZ"))

    def setEmitterName(self, text):
        self.emitter[0] = text

    def setRotate(self):
        cmds.setAttr(self.getEmitter()+".rotateX", float(self.rx.text()))
        cmds.setAttr(self.getEmitter()+".rotateY", float(self.ry.text()))
        cmds.setAttr(self.getEmitter()+".rotateZ", float(self.rz.text()))

    def setScriptJobs(self):
        """
        If a property is changed in Maya, the changes will be reflected in the GUI
        with these functions.
        """
        self.jobNumTx = cmds.scriptJob(attributeChange=[self.getEmitter()+".translateX", self.translateX])
        self.jobNumTy = cmds.scriptJob(attributeChange=[self.getEmitter()+".translateY", self.translateY])
        self.jobNumTz = cmds.scriptJob(attributeChange=[self.getEmitter()+".translateZ", self.translateZ])
        self.jobNumRx = cmds.scriptJob(attributeChange=[self.getEmitter()+".rotateX", self.rotateX])
        self.jobNumRy = cmds.scriptJob(attributeChange=[self.getEmitter()+".rotateY", self.rotateY])
        self.jobNumRz = cmds.scriptJob(attributeChange=[self.getEmitter()+".rotateZ", self.rotateZ])

    def setTranslate(self):
        cmds.setAttr(self.getEmitter()+".translateX",float(self.tx.text()))
        cmds.setAttr(self.getEmitter()+".translateY",float(self.ty.text()))
        cmds.setAttr(self.getEmitter()+".translateZ",float(self.tz.text()))

    def setupWidget(self):
        if not self.getEmitter():
            self.createParticleSystem()
        self.setScriptJobs()

    def translateX(self):
        self.tx.setText("%.2f" %cmds.getAttr(self.getEmitter()+".translateX"))

    def translateY(self):
        self.ty.setText("%.2f" %cmds.getAttr(self.getEmitter()+".translateY"))

    def translateZ(self):
        self.tz.setText("%.2f" %cmds.getAttr(self.getEmitter()+".translateZ"))

class behaviorCatWidget(AbstractAttrObject, Ui_behaviorCat):

    def __init__(self, parent = None):
        super(behaviorCatWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)

    def justConnected(self):
        if self.getParticleShape():
            self.particleName.setText(self.getParticleShape())

class lookCatWidget(AbstractAttrObject, Ui_behaviorCat):

    def __init__(self, parent = None):
        super(lookCatWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)

    def justConnected(self):
        self.particleName.setText(self.getParticleShape())

class instancerWidget(AbstractAttrObject, Ui_instancer):

    def __init__(self, parent = None):
        super(instancerWidget, self).__init__(parent)
        BaseAttrObject.__init__(self)
        self.setupUi(self)
        self.instancerName = None
        self.instancedItems = {}

    def changeInstancerNameLabel(self, name):
        self.instancerNameLabel.setText(name)

    def changeRotationAngleUnits(self, index):
        if self.instancerName:
            cmds.setAttr(self.getInstancer()+".rotationAngleUnits", index)

    def changeLevelOfDetail(self, index):
        if self.instancerName:
            cmds.setAttr(self.getInstancer()+".levelOfDetail", index)

    def changeCycle(self, index):
        if self.instancerName:
            cmds.setAttr(self.getInstancer()+".cycle", index)

    def changeCycleStepUnit(self, index):
        if self.instancerName:
            cmds.setAttr(self.getInstancer()+".cycleStepUnit", index)

    def changeCycleStep(self, value):
        if self.instancerName:
            cmds.setAttr(self.getInstancer()+".cycleStep", value)

    def connectSignals(self):
        self.rotationAngleUnits.currentIndexChanged.connect(self.changeRotationAngleUnits)
        self.levelOfDetail.currentIndexChanged.connect(self.changeLevelOfDetail)
        self.cycle.currentIndexChanged.connect(self.changeCycle)
        self.cycleStepUnit.currentIndexChanged.connect(self.changeCycleStepUnit)
        self.cycleStep.valueChanged.connect(self.changeCycleStep)

    def deleteData(self, data):
        print "ATTEMPTING TO DELETE DATA FROM THE PARTICLE INSTANCER"
        cmds.particleInstancer(self.getParticleShape(),edit=True,removeObject=True,object=data['objName'], name=self.getInstancer())
        itemToRemove = self.instancedObjects.findItems(str(data['objName']), Qt.MatchContains)[0]
        print "itemToRemove: ", itemToRemove
        self.instancedObjects.takeItem(self.instancedObjects.row(itemToRemove))
        del itemToRemove
        self._connectedTo.getWidgetMenu().dataReady.disconnect(self.deleteData)

    def deleteInstancer(self):
        if self.getInstancer():
            cmds.select(self.getInstancer())
            cmds.delete()

    def getInstancer(self):
        return self.instancerName

    def receiveData(self, data):
        print "ATTEMPTING TO ADD OBJECT TO PARTICLE INSTANCER"
        cmds.particleInstancer(self.getParticleShape(),edit=True,addObject=True,object=data['objName'], name=self.getInstancer())
        self.instancedObjects.addItem(str(self.instancedObjects.count())+" : "+data['objName'])

    def setInstancer(self, name):
        self.instancerName = name

    def setupWidget(self):
        """
        Create the instancer when the nodeCreatedInScene signal is emitted
        """
        if self.getParticleShape() and not self.getInstancer():
            cmds.particleInstancer(self.getParticleShape())
            self.setInstancer(cmds.particleInstancer(self.getParticleShape(), query=True,name=True)[0])
            self.changeInstancerNameLabel(self.getInstancer())
            self.connectSignals()

    def updateMayaValues(self):
        self.setupWidget()
        self.changeRotationAngleUnits(self.rotationAngleUnits.currentIndex())
        self.changeLevelOfDetail(self.levelOfDetail.currentIndex())
        self.changeCycle(self.cycle.currentIndex())
        self.changeCycleStepUnit(self.cycleStepUnit.currentIndex())
        self.changeCycleStep(self.cycleStep.value())

class objectUtilWidget(AbstractAttrObject, Ui_objectUtil):
    def __init__(self, parent = None):
        super(objectUtilWidget, self).__init__(parent)
        self.setupUi(self)
        self.connectSignals()
        self.waitingLabel.hide()
        self.object = None
        self.pickObject.setChecked(False)
        # This script job is to be executed immediately. Waiting for the user to pick an object.
        selectionJob = cmds.scriptJob(event=['SelectionChanged', self.handleSelection])

    def changeObjName(self):
        if self.getObject():
            cmds.rename(self.getObject(), str(self.objName.text()))
            self.setObject(str(self.objName.text()))
            self.objName.setText(self.getObject())

    def changeRX(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".rotateX", float(self.rotateX.text()))

    def changeRY(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".rotateY", float(self.rotateY.text()))

    def changeRZ(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".rotateZ", float(self.rotateZ.text()))

    def changeSX(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".scaleX", float(self.scaleX.text()))

    def changeSY(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".scaleY", float(self.scaleY.text()))

    def changeSZ(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".scaleZ", float(self.scaleZ.text()))

    def changeTX(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".translateX", float(self.translateX.text()))

    def changeTY(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".translateY", float(self.translateY.text()))

    def changeTZ(self):
        if self.getObject():
            cmds.setAttr(self.getObject()+".translateZ", float(self.translateZ.text()))

    def connectSignals(self):
        self.pickObject.toggled.connect(self.handlePickToggle)
        self.clearObject.pressed.connect(self.handleClearPress)

        self.objName.editingFinished.connect(self.changeObjName)
        self.translateX.editingFinished.connect(self.changeTX)
        self.translateY.editingFinished.connect(self.changeTY)
        self.translateZ.editingFinished.connect(self.changeTZ)
        self.rotateX.editingFinished.connect(self.changeRX)
        self.rotateY.editingFinished.connect(self.changeRY)
        self.rotateZ.editingFinished.connect(self.changeRZ)
        self.scaleX.editingFinished.connect(self.changeSX)
        self.scaleY.editingFinished.connect(self.changeSY)
        self.scaleZ.editingFinished.connect(self.changeSZ)

    def getObject(self):
        return self.object

    def handleClearPress(self):
        self.setObject(None)
        # Name
        self.objName.setText("")
        # Translate
        self.translateX.setText("")
        self.translateY.setText("")
        self.translateZ.setText("")
        # Rotate
        self.rotateX.setText("")
        self.rotateY.setText("")
        self.rotateZ.setText("")
        # Scale
        self.scaleX.setText("")
        self.scaleY.setText("")
        self.scaleZ.setText("")

    def handleSelection(self):
        if self.pickObject.isChecked():
            self.pickObject.setChecked(False)
            self.setObject(cmds.ls(selection=True)[0])
            if self.object is not None:
                self.setWidgetVariables()
                self.setScriptJobs()

    def handlePickToggle(self, checked):
        if checked is True:
            self.waitingLabel.show()
        else:
            self.waitingLabel.hide()

    def packageData(self):
        if self.getObject():
            tempDict = {'objName':self.getObject(),
                        'translate':[float(self.translateX.text()), float(self.translateY.text()), float(self.translateY.text())],
                        'rotate':[float(self.rotateX.text()), float(self.rotateY.text()), float(self.rotateZ.text())],
                        'scale':[float(self.scaleX.text()), float(self.scaleY.text()), float(self.scaleZ.text())]}
        else:
            tempDict = None
        return tempDict

    def RX(self):
        self.rotateX.setText("%.2f" %cmds.getAttr(self.getObject()+".rotateX"))

    def RY(self):
        self.rotateY.setText("%.2f" %cmds.getAttr(self.getObject()+".rotateY"))

    def RZ(self):
        self.rotateZ.setText("%.2f" %cmds.getAttr(self.getObject()+".rotateZ"))

    def setObject(self, object):
        if object is not None:
            self.object = object.replace(' ', '_')
            self.object = object.lstrip('1234567890')
        else:
            self.object = None

    def setScriptJobs(self):
        self.jobNumRx = cmds.scriptJob(attributeChange=[self.getObject()+".rotateX", self.RX])
        self.jobNumRy = cmds.scriptJob(attributeChange=[self.getObject()+".rotateY", self.RY])
        self.jobNumRz = cmds.scriptJob(attributeChange=[self.getObject()+".rotateZ", self.RZ])
        self.jobNumSx = cmds.scriptJob(attributeChange=[self.getObject()+".scaleX", self.SX])
        self.jobNumSy = cmds.scriptJob(attributeChange=[self.getObject()+".scaleY", self.SY])
        self.jobNumSz = cmds.scriptJob(attributeChange=[self.getObject()+".scaleZ", self.SZ])
        self.jobNumTx = cmds.scriptJob(attributeChange=[self.getObject()+".translateX", self.TX])
        self.jobNumTy = cmds.scriptJob(attributeChange=[self.getObject()+".translateY", self.TY])
        self.jobNumTz = cmds.scriptJob(attributeChange=[self.getObject()+".translateZ", self.TZ])

    def setWidgetVariables(self):
        # Name
        self.objName.setText(self.getObject())
        # Translate
        self.translateX.setText("%.2f" %float(cmds.getAttr(self.getObject()+".translateX")))
        self.translateY.setText("%.2f" %float(cmds.getAttr(self.getObject()+".translateY")))
        self.translateZ.setText("%.2f" %float(cmds.getAttr(self.getObject()+".translateZ")))
        # Rotate
        self.rotateX.setText("%.2f" %float(cmds.getAttr(self.getObject()+".rotateX")))
        self.rotateY.setText("%.2f" %float(cmds.getAttr(self.getObject()+".rotateY")))
        self.rotateZ.setText("%.2f" %float(cmds.getAttr(self.getObject()+".rotateZ")))
        # Scale
        self.scaleX.setText("%.2f" %float(cmds.getAttr(self.getObject()+".scaleX")))
        self.scaleY.setText("%.2f" %float(cmds.getAttr(self.getObject()+".scaleY")))
        self.scaleZ.setText("%.2f" %float(cmds.getAttr(self.getObject()+".scaleZ")))

    def SX(self):
        self.scaleX.setText("%.2f" %cmds.getAttr(self.getObject()+".scaleX"))

    def SY(self):
        self.scaleY.setText("%.2f" %cmds.getAttr(self.getObject()+".scaleY"))

    def SZ(self):
        self.scaleZ.setText("%.2f" %cmds.getAttr(self.getObject()+".scaleZ"))

    def TX(self):
        self.translateX.setText("%.2f" %cmds.getAttr(self.getObject()+".translateX"))

    def TY(self):
        self.translateY.setText("%.2f" %cmds.getAttr(self.getObject()+".translateY"))

    def TZ(self):
        self.translateZ.setText("%.2f" %cmds.getAttr(self.getObject()+".translateZ"))

class colliderUtilWidget(AbstractAttrObject, Ui_colliderUtil):
    def __init__(self, parent = None):
        super(colliderUtilWidget, self).__init__(parent)
        self.setupUi(self)
        self.colliderObjects = []

    def changeFriction(self, value):
        if self.colliderObjects:
            for object in self.colliderObjects:
                cmds.collision(object, edit=True, friction=value)

    def changeOffset(self, value):
        if self.colliderObjects:
            for object in self.colliderObjects:
                cmds.collision(object, edit=True, offset=value)

    def changeResilience(self, value):
        if self.colliderObjects:
            for object in self.colliderObjects:
                cmds.collision(object, edit=True, resilience=value)

    def changeTessellation(self, value):
        if self.colliderObjects:
            for object in self.colliderObjects:
                cmds.collision(object, tessellationFactor=value)

    def connectSignals(self):
        self.resilience.valueChanged.connect(self.changeResilience)
        self.friction.valueChanged.connect(self.changeFriction)
        self.offset.valueChanged.connect(self.changeOffset)

    def deleteData(self, data):
        object = data['objName']
#        self.colliderObjects.remove(object)
        if object and self.getParticle():
            cmds.connectDynamic(self.getParticle(), delete=True, collisions=object)
        self._connectedTo.getWidgetMenu().dataReady.disconnect(self.deleteData)

    def receiveData(self, data):
        print "Collider node is receiving data."
        object = data['objName']
        self.colliderObjects.append(object)
        if object and self.getParticle():
            cmds.collision(object, self.getParticle())
        self.connectSignals()

class goalAttrWidget(AbstractAttrObject, Ui_goalAttr):
    def __init__(self, parent = None):
        super(goalAttrWidget, self).__init__(parent)
        self.setupUi(self)
        self.object = None

    def changeGoalSmoothness(self, value):
        if self.getParticleShape():
            cmds.setAttr(self.getParticleShape()+'.goalSmoothness', value)

    def changeGoalWeight(self, value):
        if self.getParticleShape():
            cmds.setAttr(self.getParticleShape()+'.goalWeight[0]', value)

    def connectSignals(self):
        self.goalSmoothness.valueChanged.connect(self.changeGoalSmoothness)
        self.goalWeight.valueChanged.connect(self.changeGoalWeight)

    def deleteData(self, data):
        if self.getObject():
            cmds.setAttr(self.getParticleShape()+'.goalWeight[0]', 0)
        self._connectedTo.getWidgetMenu().dataReady.disconnect(self.deleteData)

    def receiveData(self, data):
        print "Goal node is receiving data."
        # Since there's no way to DELETE A GOAL OBJECT (YES MAYA YOU ARE SHITTY), I have to set
        #  the previous goal object weight to 0 so it doesn't affect the particles.
        object = data['objName']
        self.setObject(object)
        if self.getObject() and self.getParticle():
            cmds.goal(self.getParticle(), goal=self.getObject())
        self.connectSignals()

class airForceWidget(AbstractAttrObject, Ui_airForceAttr):
    def __init__(self, parent = None):
        super(airForceWidget, self).__init__(parent)
        self.setupUi(self)

    def changeAttenuation(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".attenuation", value)

    def changeDirectionX(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionX", value)

    def changeDirectionY(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionY", value)

    def changeDirectionZ(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionZ", value)

    def changeInheritRotation(self, num):
        if num > 1:
            num = 1
        cmds.setAttr(self.getObject()+".inheritRotation", num)

    def changeInheritVelocity(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".inheritVelocity", value)

    def changeMagnitude(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".magnitude", value)

    def changeSpeed(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".speed", value)

    def connectSignals(self):
        self.magnitude.valueChanged.connect(self.changeMagnitude)
        self.attenuation.valueChanged.connect(self.changeAttenuation)
        self.directionX.valueChanged.connect(self.changeDirectionX)
        self.directionY.valueChanged.connect(self.changeDirectionY)
        self.directionZ.valueChanged.connect(self.changeDirectionZ)
        self.speed.valueChanged.connect(self.changeSpeed)
        self.inheritVelocity.valueChanged.connect(self.changeInheritVelocity)
        self.inheritRotation.stateChanged.connect(self.changeInheritRotation)

    def justConnected(self):
        if self.getParticleShape():
            if not self.getObject():
                cmds.select(deselect=True)
                cmds.air()
                self.setObject(cmds.air(q=True, name=True))
            cmds.connectDynamic(self.getParticleShape(), fields=self.getObject())
            self. connectSignals()

    def updateMayaValues(self):
        self.justConnected()
        self.changeMagnitude(self.magnitude.value())
        self.changeAttenuation(self.attenuation.value())
        self.changeDirectionX(self.directionX.value())
        self.changeDirectionY(self.directionY.value())
        self.changeDirectionZ(self.directionZ.value())
        self.changeSpeed(self.speed.value())
        self.changeInheritVelocity(self.inheritVelocity.value())
        self.changeInheritRotation(self.inheritRotation.checkState())

class gravityForceWidget(AbstractAttrObject, Ui_gravityForce):
    def __init__(self, parent = None):
        super(gravityForceWidget, self).__init__(parent)
        self.setupUi(self)

    def changeAttenuation(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".attenuation", value)

    def changeDirectionX(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionX", value)

    def changeDirectionY(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionY", value)

    def changeDirectionZ(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".directionZ", value)

    def changeMagnitude(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".magnitude", value)

    def connectSignals(self):
        self.magnitude.valueChanged.connect(self.changeMagnitude)
        self.attenuation.valueChanged.connect(self.changeAttenuation)
        self.directionX.valueChanged.connect(self.changeDirectionX)
        self.directionY.valueChanged.connect(self.changeDirectionY)
        self.directionZ.valueChanged.connect(self.changeDirectionZ)

    def justConnected(self):
        if self.getParticleShape():
            if not self.getObject():
                cmds.select(deselect=True)
                cmds.gravity()
                self.setObject(cmds.gravity(q=True, name=True))
            cmds.connectDynamic(self.getParticleShape(), fields=self.getObject())
            self.connectSignals()

    def updateMayaValues(self):
        self.justConnected()
        self.changeAttenuation(self.attenuation.value())
        self.changeDirectionX(self.directionX.value())
        self.changeDirectionY(self.directionY.value())
        self.changeDirectionZ(self.directionZ.value())
        self.changeMagnitude(self.magnitude.value())

class newtonForceWidget(AbstractAttrObject, Ui_newtonForce):
    def __init__(self, parent = None):
        super(newtonForceWidget, self).__init__(parent)
        self.setupUi(self)

    def changeAttenuation(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".attenuation", value)

    def changeMagnitude(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".magnitude", value)

    def changeMinDistance(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".minDistance", value)

    def connectSignals(self):
        self.magnitude.valueChanged.connect(self.changeMagnitude)
        self.attenuation.valueChanged.connect(self.changeAttenuation)
        self.minDistance.valueChanged.connect(self.changeMinDistance)

    def justConnected(self):
        if self.getParticleShape():
            if not self.getObject():
                cmds.select(deselect=True)
                cmds.newton()
                self.setObject(cmds.newton(q=True, name=True))
            cmds.connectDynamic(self.getParticleShape(), fields=self.getObject())
            self.connectSignals()

    def updateMayaValues(self):
        self.justConnected()
        self.changeAttenuation(self.attenuation.value())
        self.changeMagnitude(self.magnitude.value())
        self.changeMinDistance(self.minDistance.value())

class turbulenceForceWidget(AbstractAttrObject, Ui_turbulenceForce):
    def __init__(self, parent = None):
        super(turbulenceForceWidget, self).__init__(parent)
        self.setupUi(self)

    def changeMagnitude(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".magnitude", value)

    def changeAttenuation(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".attenuation", value)

    def changeFrequency(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".frequency", value)

    def changePhaseX(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".phaseX", value)

    def changePhaseY(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".phaseY", value)

    def changePhaseZ(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".phaseZ", value)

    def changeInterpolationType(self, index):
        if self.getObject():
            cmds.setAttr(self.getObject()+".interpolationType", index)

    def changeNoiseLevel(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".noiseLevel", value)

    def changeNoiseRatio(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".noiseRatio", value)

    def connectSignals(self):
        self.magnitude.valueChanged.connect(self.changeMagnitude)
        self.attenuation.valueChanged.connect(self.changeAttenuation)
        self.frequency.valueChanged.connect(self.changeFrequency)
        self.phaseX.valueChanged.connect(self.changePhaseX)
        self.phaseY.valueChanged.connect(self.changePhaseY)
        self.phaseZ.valueChanged.connect(self.changePhaseZ)
        self.interpolationType.activated.connect(self.changeInterpolationType)
        self.noiseLevel.valueChanged.connect(self.changeNoiseLevel)
        self.noiseRatio.valueChanged.connect(self.changeNoiseRatio)

    def justConnected(self):
        if self.getParticleShape():
            if not self.getObject():
                cmds.select(deselect=True)
                cmds.turbulence()
                self.setObject(cmds.turbulence(q=True, name=True))
            cmds.connectDynamic(self.getParticleShape(), fields=self.getObject())
            self.connectSignals()

    def updateMayaValues(self):
        self.justConnected()
        self.changeMagnitude(self.magnitude.value())
        self.changeAttenuation(self.attenuation.value())
        self.changeFrequency(self.frequency.value())
        self.changePhaseX(self.phaseX.value())
        self.changePhaseY(self.phaseY.value())
        self.changePhaseZ(self.phaseZ.value())
        self.changeInterpolationType(self.interpolationType.currentIndex())
        self.changeNoiseLevel(self.noiseLevel.value())
        self.changeNoiseRatio(self.noiseRatio.value())

class vortexForceWidget(AbstractAttrObject, Ui_vortexForce):
    def __init__(self, parent = None):
        super(vortexForceWidget, self).__init__(parent)
        self.setupUi(self)

    def changeMagnitude(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".magnitude", value)

    def changeAttenuation(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".attenuation", value)

    def changeAxisX(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".axisX", value)

    def changeAxisY(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".axisY", value)

    def changeAxisZ(self, value):
        if self.getObject():
            cmds.setAttr(self.getObject()+".axisZ", value)

    def connectSignals(self):
        self.magnitude.valueChanged.connect(self.changeMagnitude)
        self.attenuation.valueChanged.connect(self.changeAttenuation)
        self.axisX.valueChanged.connect(self.changeAxisX)
        self.axisY.valueChanged.connect(self.changeAxisY)
        self.axisZ.valueChanged.connect(self.changeAxisZ)

    def justConnected(self):
        if self.getParticleShape():
            if not self.getObject():
                cmds.select(deselect=True)
                cmds.vortex()
                self.setObject(cmds.vortex(q=True, name=True))
            cmds.connectDynamic(self.getParticleShape(), fields=self.getObject())
            self.connectSignals()

    def updateMayaValues(self):
        self.justConnected()
        self.changeMagnitude(self.magnitude.value())
        self.changeAttenuation(self.attenuation.value())
        self.changeAxisX(self.axisX.value())
        self.changeAxisY(self.axisY.value())
        self.changeAxisZ(self.axisZ.value())

class collisionEventWidget(AbstractAttrObject, Ui_collisionEvent):

    createParticles = pyqtSignal(object)

    def __init__(self, parent = None):
        super(collisionEventWidget, self).__init__(parent)
        self.setupUi(self)
        self._event = None
        self._targetParticles = None
        self.particleMsgBox = QMessageBox()
        self.particleMsgBox.setText("Select whether or not the new particles created should be from a new system\
                                    or the existing one.")
        self.particleMsgBox.addButton("Create new particles", QMessageBox.AcceptRole)
        self.particleMsgBox.addButton("Use existing particles", QMessageBox.AcceptRole)

    def changeAllCollisions(self, num):
        if self.getParticle() and self.getEvent():
            if num > 1:
                cmds.event(self.getParticle(), edit=True, name=self.getEvent(), count=0)
            else:
                cmds.event(self.getParticle(), edit=True, name=self.getEvent(), count=self.collisionNumber.value())

    def changeCollisionNumber(self, value):
        if self.getParticle() and self.getEvent():
            cmds.event(self.getParticle(), edit=True, name=self.getEvent(), count=0)

    def changeEmit(self, checked):
        if self.getParticle() and self.getEvent():
            if checked:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, emit=self.numParticles.value(), split=0)

    def changeSplit(self, checked):
        if self.getParticle() and self.getEvent():
            if checked:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, split=self.numParticles.value(), emit=0)

    def changeEmitRandomParticles(self, num):
        if self.getParticle() and self.getEvent():
            if num > 1:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, random=True)
            else:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, random=False)

    def changeOriginalParticleDies(self, num):
        if self.getParticle() and self.getEvent():
            if num > 1:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, dieAtCollision=True)
            else:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, dieAtCollision=False)

    def changeNumParticles(self, value):
        if self.getParticle() and self.getEvent():
            if self.emit.isChecked():
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, emit=value, split=0)
            else:
                cmds.event(self.getParticle(), name=self.getEvent(), edit=True, split=value, emit=0)

    def changeSpread(self, value):
        if self.getParticle() and self.getEvent():
            cmds.event(self.getParticle(), name=self.getEvent(), edit=True, spread=value)

    def changeInheritVelocity(self, value):
        if self.getTargetParticles() and self.getEvent():
            cmds.setAttr(self.getTargetParticles()+".inheritFactor", value)
        elif self.getParticleShape() and self.getEvent():
            cmds.setAttr(self.getParticleShape()+".inheritFactor", value)

    def connectSignals(self):
        self.allCollisions.stateChanged.connect(self.changeAllCollisions)
        self.collisionNumber.valueChanged.connect(self.changeCollisionNumber)
        self.emit.toggled.connect(self.changeEmit)
        self.split.toggled.connect(self.changeSplit)
        self.emitRandomParticles.stateChanged.connect(self.changeEmitRandomParticles)
        self.originalParticleDies.stateChanged.connect(self.changeOriginalParticleDies)
        self.numParticles.valueChanged.connect(self.changeNumParticles)
        self.spread.valueChanged.connect(self.changeSpread)
        self.inheritVelocity.valueChanged.connect(self.changeInheritVelocity)

    def deleteEvent(self):
        if self.getEvent():
            cmds.event(self.getParticleShape(), name = self.getEvent(), delete=True)
            self.setEvent(None)

    def getEvent(self):
        try:
            return self._event
        except (TypeError, AttributeError), e:
            print "Getting Event error: %s" %str(e)

    def getTargetParticles(self):
        try:
            return self._targetParticles
        except (TypeError, AttributeError), e:
            print "Getting _targetParticles error: %s" %str(e)

    def justConnected(self):
        if self.getParticleShape():
            test = self.particleMsgBox.exec_()
            if test is 0:
                print "Creating new particle system."
                self.createParticles.emit(self)
                event = cmds.event(self.getParticleShape(), target=self.getTargetParticles(), emit=True)
            else:
                # Create the event and then set the name of it
                event = cmds.event(self.getParticleShape(), target=self.getParticle(), emit=True)
                self.targetParticleSystem.setText(self.getParticleShape())
            self.setEvent(event)
            self.eventIsAffecting.setText("Particles: "+self.getParticle()+" and particleShape: "+self.getParticleShape())
            self.eventName.setText(self.getEvent())
            self.connectSignals()
            self.updateMayaValues()

    def setEvent(self, event):
        if event is not None:
            self._event = event.replace(' ', '_')
            self._event = event.lstrip('1234567890')
        else:
            self._event = None

    def setTargetParticles(self, targetParticles):
        if targetParticles is not None:
            self._targetParticles = targetParticles.replace(' ', '_')
            self._targetParticles = targetParticles.lstrip('1234567890')
        else:
            self._event = None

    def updateMayaValues(self):
        self.changeAllCollisions(self.allCollisions.isChecked())
        self.changeCollisionNumber(self.collisionNumber.value())
        self.changeEmit(self.emit.isChecked())
        self.changeSplit(self.split.isChecked())
        self.changeEmitRandomParticles(self.emitRandomParticles.isChecked())
        self.changeOriginalParticleDies(self.originalParticleDies.isChecked())
        self.changeNumParticles(self.numParticles.value())
        self.changeSpread(self.spread.value())
        self.changeInheritVelocity(self.inheritVelocity.value())