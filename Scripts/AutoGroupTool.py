
import maya.cmds as cmd
cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)
cmds.delete(constructionHistory = True)
test = cmds.ls( selection=True )
cmds.select( clear=True )
for x in test:
    element = x
    index = test.index(element)
    object_name = test[index]
    translation = cmds.xform(object_name, query=True, translation=True)
    print(translation[2])
    rotation = cmds.xform(object_name, query=True, rotation=True)
    print(rotation[2])
    cmds.group( em=True, name=object_name + "_Grp" )
    cmds.move( translation[0], translation[1], translation[2])
    cmds.rotate( rotation[0], rotation[1], rotation[2])
    cmds.parent(object_name, object_name + "_Grp", relative=True)
    cmds.makeIdentity( apply=False, t=True, r=True, s=True)