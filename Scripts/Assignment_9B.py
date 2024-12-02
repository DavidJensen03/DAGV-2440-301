
def changeAllObjectsColor(givenColor):
    import maya.cmds as cmd
    cmds.select(adn=False, ado=True)

    ListOfObjects = cmds.ls( selection=True )
    cmds.select( clear=True )

        

    print(ListOfObjects)
    for x in ListOfObjects:
        element = x
        index = ListOfObjects.index(element)


        test2 = element + ".overrideEnabled"
        test3 = element + ".overrideColor"

        cmds.setAttr(test2, 1)
        cmds.setAttr(test3, givenColor)

changeAllObjectsColor(30)
        
    





    
