__author__ = 'Sam Vitello'
import nimble
from nimble import cmds
import os

#Wood
def createWoodShader():
    #wood shader
    woodShader = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(woodShader+'.reflectivity', 0)

    #wood texture
    woodText = cmds.shadingNode('wood', asTexture=True)
    tdtext = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(tdtext+'.wim[0]', woodText+'.pm')
    cmds.connectAttr(woodText+'.outColor', woodShader+'.color', force=True)

    #wood rings
    stuccoText = cmds.shadingNode('stucco', asTexture=True)
    cmds.setAttr(stuccoText+'.channel1', 0.588235, 0.382247, 0.219146, type="double3")
    cmds.setAttr(stuccoText+'.channel2', 0.421, 0.18444, 0.045047, type="double3")
    cmds.setAttr(woodText+'.veinSpread', 1.601504)
    cmds.connectAttr(stuccoText+'.outColor', woodText+'.veinColor', force=True)

    return woodShader

#Plastic
def createPlasticShader():
    #plastic shader
    plasticShader = cmds.shadingNode('phongE', asShader=True)
    cmds.setAttr(plasticShader+'.color', 0.07,0.55,0.06459, type="double3")
    cmds.setAttr(plasticShader+'.reflectivity', 0.82)
    cmds.setAttr(plasticShader+'.diffuse', 0.854701)

    #specular noise
    plasticNoise = cmds.shadingNode('volumeNoise', asTexture=True)
    cmds.setAttr(plasticNoise+'.amplitude', 0.4)
    tdtext = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(tdtext+'.wim[0]', plasticNoise+'.pm')
    cmds.connectAttr(plasticNoise+'.outColor', plasticShader+'.specularColor', force=True)

    return plasticShader

def createDirtyMetal():
    metalShader = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(metalShader+'.diffuse', 0.3)
    cmds.setAttr(metalShader+'.reflectedColor', 1, 1, 1, type="double3")
    cmds.setAttr(metalShader+'.eccentricity', 0.3)

    #load base color image file
    baseColorFile = cmds.shadingNode('file', asTexture=True)
    baseFilePath = os.path.abspath("resources/metal1_color.jpg")
    cmds.setAttr(baseColorFile+'.fileTextureName', baseFilePath, type="string")

    #load specular color image file
    specColorFile = cmds.shadingNode('file', asTexture=True)
    specFilePath = os.path.abspath("resources/metal1_spec.jpg")
    cmds.setAttr(specColorFile+'.fileTextureName', specFilePath, type="string")

    #connect files to color and reflective properties
    cmds.defaultNavigation(connectToExisting=True, source=baseColorFile+'.outColor', destination=metalShader+'.color')
    cmds.defaultNavigation(connectToExisting=True, source=specColorFile+'.outColor', destination=metalShader+'.reflectivity')
    cmds.defaultNavigation(connectToExisting=True, source=specColorFile+'.outColor', destination=metalShader+'.specularColor')

    return metalShader

def createGold():
    #create gold blinn
    goldShader = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr(goldShader+'.color',0.75,0.75,0.13, type='double3')
    cmds.setAttr(goldShader+'.diffuse',0.4)
    cmds.setAttr(goldShader+'.translucence',0)
    cmds.setAttr(goldShader+'.translucenceDepth',0)
    cmds.setAttr(goldShader+'.translucenceFocus',0)
    cmds.setAttr(goldShader+'.eccentricity',0.5)
    cmds.setAttr(goldShader+'.specularRollOff',0.667)
    cmds.setAttr(goldShader+'.reflectivity',0.215)


    #create envBall for reflection
    reflectEnv = cmds.shadingNode('envBall', asTexture=True)
    tdtext = cmds.shadingNode('place3dTexture', asUtility=True)
    cmds.connectAttr(tdtext+'.wim[0]', reflectEnv+'.pm')
    cmds.connectAttr(reflectEnv+'.outColor', goldShader+'.reflectedColor', force=True)

    #get env file loaded
    baseReflectFile = cmds.shadingNode('file', asTexture=True)
    baseFilePath = os.path.abspath("resources/backgroundhdri.jpg")
    cmds.setAttr(baseReflectFile+'.fileTextureName', baseFilePath, type="string")
    cmds.setAttr(baseReflectFile+'.defaultColor', 1,1,0, type="double3")
    cmds.setAttr(baseReflectFile+'.colorGain', 1,1,0, type="double3")

    cmds.defaultNavigation(connectToExisting=True, source=baseReflectFile+'.outColor', destination=reflectEnv+'.image')

    return goldShader


def assignMaterial(object, shader):
    cmds.select(object)
    cmds.hyperShade(assign = shader)



