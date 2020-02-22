# MoCap System and Data importer
# https://accad.osu.edu/research/motion-lab/mocap-system-and-data

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

file = node.evalParm('mocapFile')

if file[-4:] != ".txt":
    print "Please select .txt file"
    exit()

frameNo = hou.intFrame()
fileContent = open(file)

for line in fileContent:
    #print line.split()
    lineArray = line.split()
    if lineArray[0] == str(frameNo):
        #print lineArray
        del lineArray[0:2]
        for i in range(0,len(lineArray),3):
            pnt = geo.createPoint()
            pnt.setPosition(hou.Vector3((float(lineArray[i]),float(lineArray[i+1]),float(lineArray[i+2]))))
            #print i,len(lineArray),frameNo,lineArray[i],lineArray[i+1],lineArray[i+2]  
            
fileContent.close()

