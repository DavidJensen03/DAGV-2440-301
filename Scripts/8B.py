import maya.cmds as cmd
all_joints = cmds.ls(type='joint')

cmds.select(all_joints)
test = cmds.ls( selection=True )
cmds.select( clear=True )

firstGo = True
for x in test:
    element = x
    index = test.index(element)
    object_name = test[index]
    object_nameFixName = object_name.split("_")
    object_nameFixName2 = str(object_nameFixName[-1])

    
    
    object_nameFixName3 = object_name.replace(object_nameFixName[-1], "")


    pivot_position = cmds.xform(object_name, query=True, worldSpace=True, rotatePivot=True)
    translation = cmds.xform(object_name, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(object_name, query=True, rotation=True, worldSpace=True)
    cmds.circle( nr=(0, 9, 1), c=(0, 0, 0),name=object_nameFixName3 + "Ctrl" )
    cmds.move( translation[0], translation[1], translation[2])
    cmds.rotate( pivot_position[0], pivot_position[1], rotation[2] + 90)
    cmds.makeIdentity(apply=True, translate=True, r=1,s=True)
    

    cmds.group( em=True,name=object_nameFixName3 + "Ctrl_group" )
    cmds.move( translation[0], translation[1], translation[2])
    cmds.rotate( pivot_position[0], pivot_position[1], rotation[2] + 90)
    
    cmds.parent(object_nameFixName3 + "Ctrl")
    cmds.select(hi=True)
    cmds.makeIdentity(apply=True, translate=True, r=1,s=True)

    #finds name, makes it into list slit by "_", creates a new name while deleteing the last portion.
    #makes curve, moves it, put in group, then zeros the curve. 


    

            
    




    
