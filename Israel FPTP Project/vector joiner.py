import os
import math

inputFilePath = "vectors_2412_final.kml"

outputFilePath = "C:\\Users\\Michal\\Documents\\My Documents\\amnon\\elections-vote-transfer-master\\rendered\\polys_2412_final.kml"

file = open(inputFilePath, "r", encoding="utf-8")
vectorstring = file.read()
file.close()

vectorlist = []
newstring = ""

i = 0
fullLen = len (vectorstring) - 17
while i < fullLen:
    j = i
    while j < fullLen-10 and vectorstring[j:j+10] != "LineString":
        j += 1
    if j >= fullLen-10:
        newstring = newstring + vectorstring[i:fullLen]
        i = fullLen
    else:
        newstring = newstring + vectorstring[i: j-1]
        i = j
        j = i+1
        while j < fullLen-10 and vectorstring[j:j+10] != "LineString":
            j += 1
        coordstring = vectorstring[i+24:j-16]
        i = j + 11

        pairstring = coordstring.split()
        pairlist = []

        for co in pairstring:
            numberstringlist = co.split(",")
            pairlist.append ( ( float(numberstringlist[0]) , float(numberstringlist[1]) ) )

##        if len(pairlist)<2:
##            print("remove vector: ", pairlist) #clean input
        vectorlist.append(pairlist)
        vectorlist.append(pairlist[::-1])

def nearby(a,b):
    return( 1.5e-07 > ((a[0]-b[0])**2) + ((a[1]-b[1])**2) )

def addloop(vector):
    global newstring
    polystring = ""
    for copair in vector:
        polystring = polystring + str(copair[0]) + "," + str(copair[1]) + " "
    polystring = polystring.rstrip()
    newstring = newstring + '<Placemark><ExtendedData><Data name="_umap_options"><value>[object Object]</value></Data></ExtendedData><Polygon><outerBoundaryIs><LinearRing><coordinates>' + polystring + '</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>'


continuelist = []
i = 0
while i < len(vectorlist):
    vector = vectorlist[i]
    potentials = []
    
    for continuation in vectorlist:
        if nearby(vector[-1],continuation[0]) and vectorlist.index(continuation) not in continuelist and vector[-2] != continuation[1]:
            potentials.append(vectorlist.index(continuation))

    if len(potentials) < 2:
        if len(potentials) == 0:
            if i % 2 == 0:
                potentials = [i+1]
            else:
                potentials = [i-1]
        continuelist.append(potentials[0])
    else:
        angle = math.atan2( (vector[-2][1]-vector[-1][1]) , (vector[-2][0]-vector[-1][0]) )
        continuelist.append(sorted(potentials, key= (
            lambda x: (math.atan2( (vectorlist[x][1][1]-vector[-1][1]) , (vectorlist[x][1][0]-vector[-1][0]) ) -angle)%(2*math.pi))
                                   ,reverse=True)[0])
    i += 1
        

for vector in vectorlist:
    if vector!= None:
        loop = vector
        nextindex = continuelist[vectorlist.index(vector)]
        
        while nextindex != vectorlist.index(vector):
            loop.extend(vectorlist[nextindex])
            vectorlist[nextindex] = None
            nextindex = continuelist[nextindex]
            
        vector = None
        addloop(loop)


newstring = newstring + vectorstring[fullLen:]
#print(newstring[-2000:])

file = open(outputFilePath, "w", encoding="utf-8")
file.write(newstring)
file.close()


####distance check
##distances = []
##for vector in vectorlist:
##    start = vector[0]
##    end = vector[-1]
##    distances.append(( (start[0]-end[0])**2 + (start[1]-end[1])**2 ))
##
##print(vectorlist[distances.index(min(distances))])
##print(sorted(distances)[:8])
