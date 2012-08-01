from ui import nodeModule, nodeWidgetsModule
import maya.cmds as cmds
import ui.icons_rc

MayaNodes = {}

def getMayaNodes(force=False):
    """
    All nodes will go into MayaNodes
    Make sure to add least one category node for each list.
    """

    if MayaNodes and not force:
        return MayaNodes

    """
     *************              PARTICLE EMITTER TAB            *************

        Fill these in as necessary:
            self.dictKey = The dictionary key that you give it
            self.displayText = The text that is displayed in the GUI
            self.imagePath = The Image Path to the node icon
            self.description = Node description to show up in lower right of GUI
            self.listWidgetName = The name of the list widget this attribute belongs to
            self.nodeType = The type of node: Category, Attribute, Conditional, etc...
            self.widgetMenu = The menu that is displayed with this node. maya.cmds are integrated into those menus

    """

    """Particle Emitter Category Node"""


    MayaNodes["emitterCat"] = nodeModule.NodeBase(
        dictKey = "emitterCat",
        displayText = "Particle Emitter",
        imagePath = ":/emitterBase.svg",
        description = "This is the Category node that all Emitter attributes will hook into."\
                      " Without this node nothing will happen.",
        listWidgetName = "emitterList",
        nodeType = "category",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.emitterCatWidget,
    )

    """Basic Emitter"""

    MayaNodes["basicEmitter"] = nodeModule.NodeBase(
        dictKey = "basicEmitter",
        displayText = "Basic Emitter",
        imagePath = ":/attrEmitter.svg",
        description = "Creates a point particle emitter by default. "\
                  "You can create: Point emitters, Surface emitters, "\
                  "Curve emitters, or Volume emitters.",
        listWidgetName = "emitterList",
        nodeType = "attribute",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.basicEmitterWidget
    )

    """Object Emitter"""

    MayaNodes["objectEmitter"] = nodeModule.NodeBase(
        dictKey = "objectEmitter",
        displayText = "Object Emitter",
        imagePath = ":/attrEmitter.svg",
        description = "Emit particles from a selected Polygon "\
                      "or NURBS object.\nNOTE: Make 'Emitter Type' = "\
                      "'Surface' to get particles emitting from the surface "\
                      "and NOT from the individual points in the object.",
        listWidgetName = "emitterList",
        nodeType = "attribute",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.basicEmitterWidget
    )

    """Emission Attributes"""

    MayaNodes["emissionAttr"] = nodeModule.NodeBase(
        dictKey = "emissionAttr",
        displayText = "Emission Attributes",
        imagePath = ":/attrEmitter.svg",
        description = "Basic emission attributes to "\
                      "control the amount and the rate "\
                      "of particle emission.",
        listWidgetName = "emitterList",
        nodeType = "attribute",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.emissionAttrWidget
    )

    """Life Span Attributes"""

    MayaNodes["lifeSpanAttr"] = nodeModule.NodeBase(
        dictKey = "lifeSpanAttr",
        displayText = "Lifespan Attributes",
        imagePath = ":/attrEmitter.svg",
        description = "Controls the lifespan of the particles.",
        listWidgetName = "emitterList",
        nodeType = "attribute",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.lifespanAttrWidget
    )

    """Time Attributes"""

    MayaNodes["timeAttr"] = nodeModule.NodeBase(
        dictKey = "timeAttr",
        displayText = "Time Attributes",
        imagePath = ":/attrEmitter.svg",
        description = "Controls WHEN the particles start being emitted.",
        listWidgetName = "emitterList",
        nodeType = "attribute",
        nodeColor = "green",
        widgetMenu = nodeWidgetsModule.timeAttrWidget
    )

    """

     *************              MOVEMENT/BEHAVIOR TAB            *************

    """

    """Particle Behavior/Movement Category Node"""

    MayaNodes["behaviorCat"] = nodeModule.NodeBase(
        dictKey = "behaviorCat",
        displayText = "Particle Behavior/Movement",
        imagePath = ":/behaviorBase.svg",
        description = "This is the Category node that all Emitter attributes will hook into."\
                      " Without this node nothing will happen.",
        listWidgetName = "behaviorList",
        nodeType = "category",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.behaviorCatWidget,
    )


    """
    Distance/Direction Attribute
    """

    MayaNodes["distDirAttr"] = nodeModule.NodeBase(
        dictKey = "distDirAttr",
        displayText = "Distance/Direction Attribute",
        imagePath = ":/attrBehavior.svg",
        description = "Allows you to control the Min/Max distance the particle travels. Depending on"\
                      "the emitter type, you can also control the X,Y,Z direction.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.distDirWidget
    )

    """
    Basic Emission Attribute
    """

    MayaNodes["basicEmSpeedAttr"] = nodeModule.NodeBase(
        dictKey = "basicEmSpeedAttr",
        displayText = "Basic Emission Speed",
        imagePath = ":/attrBehavior.svg",
        description = "Allows you to control the BASIC emission speed of the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.basicEmSpeedAttrWidget
    )

    """
    General Control Attribute
    """

    MayaNodes["genControlAttr"] = nodeModule.NodeBase(
        dictKey = "genControlAttr",
        displayText = "General Control",
        imagePath = ":/attrBehavior.svg",
        description = "Allows you to control the Dynamics Weight and Conserve attributes along with "\
                      "specifying that there is or isn't Cache Data.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.genControlAttrWidget
    )

    """
    Volume Speed Attribute
    """

    MayaNodes["volSpeedAttr"] = nodeModule.NodeBase(
        dictKey = "volSpeedAttr",
        displayText = "Volume Speed Attributes",
        imagePath = ":/attrBehavior.svg",
        description = "Allows you to control the VOLUME emission speed of the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.volSpeedAttrWidget
    )

    """
    General Control Attribute
    """

    MayaNodes["perParticleAttr"] = nodeModule.NodeBase(
        dictKey = "perParticleAttr",
        displayText = "Per Particle Attributes",
        imagePath = ":/attrBehavior.svg",
        description = "Allows you to control the attributes of individual particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.perParticleAttrWidget
    )
    
    """
    Collider Node
    """

    MayaNodes["colliderAttr"] = nodeModule.NodeBase(
        dictKey = "colliderAttr",
        displayText = "Collider",
        imagePath = ":/attrBehavior.svg",
        description = "This node allows you to plug in an OBJECT UTILITY to create a collision object that\
                        will interact with the particle system.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.colliderUtilWidget,
    )

    """
    Goal Node
    """

    MayaNodes["goalAttr"] = nodeModule.NodeBase(
        dictKey = "goalAttr",
        displayText = "Particle Goal",
        imagePath = ":/attrBehavior.svg",
        description = "This node allows you to plug in a SINGLE OBJECT UTILITY node into it. \
                        The particles will then move towards that goal object. You can affect \
                        the behavior of the particles by adjusting the Goal Smoothness and \
                        Goal Weight attributes.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.goalAttrWidget,
    )

    """
    Air Force Node
    """

    MayaNodes["forceAir"] = nodeModule.NodeBase(
        dictKey = "forceAir",
        displayText = "Force: Air",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds an AIR force to affect the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.airForceWidget,
    )

    """
    Gravity Force Node
    """

    MayaNodes["forceGravity"] = nodeModule.NodeBase(
        dictKey = "forceGravity",
        displayText = "Force: Gravity",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds a GRAVITY force to affect the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.gravityForceWidget,
    )

    """
    Newton Force Node
    """

    MayaNodes["forceNewton"] = nodeModule.NodeBase(
        dictKey = "forceNewton",
        displayText = "Force: Newton",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds a NEWTON force to affect the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.newtonForceWidget,
    )

    """
    Turbulence Force Node
    """

    MayaNodes["forceTurbulence"] = nodeModule.NodeBase(
        dictKey = "forceTurbulence",
        displayText = "Force: Turbulence",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds a TURBULENCE force to affect the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.turbulenceForceWidget,
    )

    """
    Vortex Force Node
    """

    MayaNodes["forceVortex"] = nodeModule.NodeBase(
        dictKey = "forceVortex",
        displayText = "Force: Vortex",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds a VORTEX force to affect the particles.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.vortexForceWidget,
    )

    """
    Collision Event
    """

    MayaNodes["collisionEvent"] = nodeModule.NodeBase(
        dictKey = "collisionEvent",
        displayText = "Collision Event",
        imagePath = ":/attrBehavior.svg",
        description = "This node adds a Collision Event to the particle system. \
                        **IMPORTANT** The particles that are SPAWNED from a collision \
                        take on the characteristics of the defined particle system in the Menu.",
        listWidgetName = "behaviorList",
        nodeType = "attribute",
        nodeColor = "blue",
        widgetMenu = nodeWidgetsModule.collisionEventWidget,
    )


    """

     *************              PARTICLE LOOK TAB            *************

    """

    """Particle Look Category Node"""

    MayaNodes["lookCat"] = nodeModule.NodeBase(
        dictKey = "lookCat",
        displayText = "Particle Look",
        imagePath = ":/lookBase.svg",
        description = "This is the Category node that all Emitter attributes will hook into."\
                      " Without this node nothing will happen.",
        listWidgetName = "lookList",
        nodeType = "category",
        nodeColor = "orange",
        widgetMenu = nodeWidgetsModule.lookCatWidget,
    )

    """
    Instancer
    """

    MayaNodes["instancer"] = nodeModule.NodeBase(
        dictKey = "instancer",
        displayText = "Instancer",
        imagePath = ":/attrLook.svg",
        description = "Allows you to instance objects onto each individual particle.",
        listWidgetName = "lookList",
        nodeType = "attribute",
        nodeColor = "orange",
        widgetMenu = nodeWidgetsModule.instancerWidget,
    )


    """
    Render Attributes
    """

    MayaNodes["renderAttr"] = nodeModule.NodeBase(
        dictKey = "renderAttr",
        displayText = "Render Attributes",
        imagePath = ":/attrLook.svg",
        description = "Allows you to change the particle render type to: MultiPoint, MultiStreak, Numeric" \
                        "Points, Spheres, Sprites, Streak, Blobby Surface, Cloud, and Tube. "\
                        "Also allows modifying the attributes for specific render types.",
        listWidgetName = "lookList",
        nodeType = "attribute",
        nodeColor = "orange",
        widgetMenu = nodeWidgetsModule.renderAttrWidget
    )


    """
    Render Stats
    """

    MayaNodes["renderStats"] = nodeModule.NodeBase(
        dictKey = "renderStats",
        displayText = "Render Stats",
        imagePath = ":/attrLook.svg",
        description = "Allows turning off and on the various render stats: Visible in Reflections/Refractions, "\
                       "Casts Shadows, Receive Shadows, Motion Blur, Primary Visibility.",
        listWidgetName = "lookList",
        nodeType = "attribute",
        nodeColor = "orange",
        widgetMenu = nodeWidgetsModule.renderStatsWidget
    )

    """

     *************              Utilities TAB            *************

    """

    """Object Utility"""

    MayaNodes["objectUtil"] = nodeModule.NodeBase(
        dictKey = "objectUtil",
        displayText = "Object",
        imagePath = ":/objectNode.svg",
        description = "Allows you to pick a SINGLE object and represent them with this Node.",
        listWidgetName = "utilitiesList",
        nodeType = "utility",
        widgetMenu = nodeWidgetsModule.objectUtilWidget,
    )

    return MayaNodes