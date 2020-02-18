import os

objDir = hou.ui.selectFile(title="Select OBJ file directory", file_type=hou.fileType.Directory)
objDirExpanded = hou.expandString(objDir)

objFiles = os.listdir(objDirExpanded)

node = hou.node('/obj').createNode('geo','OBJLoader')
mergeNode = node.createNode('merge','OBJ_Merge')

for f in objFiles:
    if f.endswith('.obj'):
        print(f)
        #remove the file extention to use in naming
        fNode = node.createNode('file', f[0:len(f)-4])
        fNode.parm('file').set(objDir + f)
        fNode.parm('missingframe').set(1)
        
        mergeNode.setNextInput(fNode)
        
node.layoutChildren()
mergeNode.setDisplayFlag(True)
mergeNode.setRenderFlag(True)
        
        
        
