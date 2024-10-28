bodyScaling = .85
bodymove = 1
numberOfBodyParts = 2
whatPart = 1

import maya.cmds as cmd
cmds.select(all=True)
cmds.delete()

cmds.polyCube(d=2,h=2,w=2, n="body1") 
cmds.polySmooth(dv=2)




for x in range(numberOfBodyParts):
    cmds.duplicate(name="body1")
    cmds.scale( bodyScaling, bodyScaling, bodyScaling, relative=True)
    cmds.move( 0, bodymove, 0, relative=True)

    

cmds.polyCylinder(radius=.5, h= .8)
cmds.rotate(0,0,20, relative=True)
cmds.move( -0.22, 2.8, 0)
cmds.duplicate()
cmds.move(-0.127,2.5,0)
cmds.scale( 1.5, .2,  1.5, relative=True)

cmds.polyCone(sx=5,radius=.13,h=1.3)
cmds.rotate(90,0,0, relative=True)
cmds.move(0, 2, 1)

cmds.polyCube(d=.3,h=.3,w=.3, n="eyes") 
cmds.polySmooth(dv=1)
cmds.select('eyes')
cmds.move(0.153,2.259,0.486)
cmds.duplicate()
cmds.move(-0.225,2.142,0.486)

    
    
