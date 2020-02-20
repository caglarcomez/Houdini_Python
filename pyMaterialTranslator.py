# Creates material network and shaders depending on material network selection
# Transfer principledshader::2.0 to classicshader
# Sets diffuse texture parameters
# And assign to selected material 

texture_path = "$HIP/tex/"

materials = hou.selectedNodes()

if len(materials) == 0:
    print("Please select a node")
    exit()    

if materials[0].type().name() != 'matnet':
    print("Please select a material network")
    exit()
    
#select first element of selection
print materials[0]
    
# get all shaders inside material node
shaders = materials[0].children()
    
# create new material network
# mantraShaders = hou.node('obj').createNode('matnet','mantraShaders')
#print materials[0].parent()
mantraShaders = materials[0].parent().createNode('matnet','mantraShaders')
mantraShaders.moveToGoodPosition()

for s in shaders:
    #print s.name(), s.type().name()
    if s.type().name() == 'principledshader::2.0':
        #create classicshader for each node
        classicshader = mantraShaders.createNode('classicshader', s.name())
        if s.evalParm('basecolor_useTexture') == 1:
            classicshader.parm('diff_colorUseTexture').set(True)
            #get textures file name
            texture = s.evalParm('basecolor_texture').split("\\")[-1]
            #print texture
            classicshader.parm('diff_colorTexture').set(texture_path + texture)
            
mantraShaders.layoutChildren()

selected_node_path = hou.ui.selectNode(initial_node=mantraShaders.parent())
if selected_node_path is not None:
    selected_node = hou.node(selected_node_path)
    #print selected_node.type().name() # material
    if selected_node.type().name() == 'material':
        for i in range(selected_node.evalParm('num_materials')):
            material_path = selected_node.evalParm('shop_materialpath' + str(i+1))
            new_material_path = material_path.replace("materials","mantraShaders")
            #print new_material_path
            selected_node.parm('shop_materialpath' + str(i+1)).set(new_material_path)
            
print ("Material transfer completed")