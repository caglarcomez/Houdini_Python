typeName = "null"
counter = 0
selectedNodes = hou.selectedNodes()

if len(selectedNodes) > 0:
    for node in selectedNodes:
        for cnode in node.children():
            if cnode.type().name() == typeName:
                cnode.destroy()
                counter += 1
        print(str(counter) + " type of " + typeName + " node(s) deleted")
else:
    print("Please select nodes to continue!")