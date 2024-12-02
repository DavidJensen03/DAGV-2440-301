import maya.cmds as cmd
def rename(newname):
    input = newname
    selected_objects = cmds.ls(selection=True)

    numberOfPound = input.count('#')
    namelist = input.split("_")
    if len(namelist) == 4:
        nameSuffix = namelist[-1]
        mainName = namelist[0] + "_" + namelist[1]
    else:
        nameSuffix = namelist[-1]
        mainName = namelist[0]


    for x in selected_objects:
        element = x
        index = selected_objects.index(element)
        
        newIndex1 = str(int(index) + 1)
        newIndex2 = newIndex1.zfill(numberOfPound)
        finshedName = mainName + "_" + newIndex2 +'_'+ nameSuffix

        cmds.select( element, r=True )
        cmds.rename( finshedName )
    
    
    
    
    

#rename('Arm_#######_joint')

    






    
