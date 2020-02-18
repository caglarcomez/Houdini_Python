nodeName = "poly"
counter = 0
selectedNodes = hou.selectedNodes()

if len(selectedNodes) > 0:
    for node in selectedNodes:
        for cnode in node.children():
            if nodeName in cnode.name():
                cnode.destroy()
                counter += 1
        print(str(counter) + " node(s) deleted containing " + nodeName + " in the name")
else:
    print("Please select nodes to continue!")