import colour_key
(Rainbow, Violet,Teal,Pink,Green,Brown,Red,Blue,Orange) = colour_key.define_colours()


file = open("colour_ready_final.svg", "r")
global mapwriter
mapwriter = str.split(file.read(), "fb")
file.close()
##The map file is precoloured on a magenta key, encoding the seat ids in the green value.

csv = open("Mapped 2020 constituencies.csv", "r", encoding="utf-8")
data20 = []
for line in csv.readlines():
    data20.append(str.split(line,","))
csv.close()

    
def test_colour(output = "rendered\\test_colour.svg"):
    file = open(output, "w")

    for i in range(1,len(mapwriter),2):
        file.write(mapwriter[(i-1)])
        seat = int(mapwriter[i], 16)

        colour = "ffffff"
        pct = float(data20[seat][11])
        if pct > 0: #Ganz
            colour = str(995000 + 20*seat)
        if pct < 0: #Bibi
            colour = str(100000 + 20*seat)
        file.write(colour)

    file.write(mapwriter[-1])

    file.close()
    return


def blocs20_preset(output = "rendered\\blocs20_preset.svg"):
    file = open(output, "w")

    for i in range(1,len(mapwriter),2):
        file.write(mapwriter[(i-1)])
        seat = int(mapwriter[i], 16)
        
        colour = "ffffff"
        pct = float(data20[seat][11])
        if pct > 0: #Ganz
            colour = Teal[int(pct) ]
        if pct < 0: #Bibi
            colour = Violet[-1*int(pct) ]
        file.write(colour)

    file.write(mapwriter[-1])

    file.close()
    return

def partys20(output = "rendered\\partys20.svg"):
    file = open(output, "w")

    for i in range(1,len(mapwriter),2):
        file.write(mapwriter[(i-1)])
        seat = int(mapwriter[i], 16)
        
        colour = "ffffff"
        if data20[seat][10] == "מחל": #Likud
            pct = (100* (int(data20[seat][17]) - max({int(data20[seat][n]) for n in [12,13,14,15,16,18,19]})) ) // int(data20[seat][8])
            colour = Violet[pct]
        if data20[seat][10] == "פה": #Blue-White
            pct = (100* (int(data20[seat][18]) - max({int(data20[seat][n]) for n in [12,13,14,15,16,17,19]})) ) // int(data20[seat][8])
            colour = Teal[pct]
        if data20[seat][10] == "ודעם": #Joint List
            pct = (100* (int(data20[seat][14]) - max({int(data20[seat][n]) for n in [12,13,15,16,17,18,19]})) ) // int(data20[seat][8])
            colour = Green[pct]
        if data20[seat][10] == "ג": #UTJ
            pct = (100* (int(data20[seat][13]) - max({int(data20[seat][n]) for n in [12,14,15,16,17,18,19]})) ) // int(data20[seat][8])
            colour = Pink[pct]
        if data20[seat][10] == "שס": #Shas
            pct = (100* (int(data20[seat][19]) - max({int(data20[seat][n]) for n in [12,13,14,15,16,17,18]})) ) // int(data20[seat][8])
            colour = Orange[pct]
        if data20[seat][10] == "טב": #Yemina
            pct = (100* (int(data20[seat][15]) - max({int(data20[seat][n]) for n in [12,13,14,16,17,18,19]})) ) // int(data20[seat][8])
            colour = Brown[pct]            
        file.write(colour)

    file.write(mapwriter[-1])

    file.close()
    return

def voteshare(column, Colour, output="rendered\\_share20.svg", minrange=1):
    #increase minrange for smaller parties, up to 9
    file = open(output, "w")

    pctlist = [0]
    for i in range(1,200):
        pctlist.append( (100*int(data20[i][column])) // int(data20[i][8]) )
    pctrange = sorted(pctlist)
    i = 0
    while pctrange[i] == 0:
        i += 1
    pctrange = pctrange[i:]

    print(1)
    newcolour = {0: Colour[0]}
    a = max(1+minrange,pctrange[len(pctrange)//11])
    newcolour.update( (n,Colour[1]) for n in range (1,a) )
    print(a)
    b = max(a+minrange, pctrange[(len(pctrange)*2)//11])
    newcolour.update( (n,Colour[2]) for n in range (a,b) )
    print(b)
    c = max(b+minrange, pctrange[(len(pctrange)*3)//11])
    newcolour.update( (n,Colour[5]) for n in range (b,c) )
    print(c)
    d = max(c+minrange, pctrange[(len(pctrange)*4)//11])
    newcolour.update( (n,Colour[10]) for n in range (c,d) )
    print(d)
    e = max(d+minrange, pctrange[(len(pctrange)*5)//11])
    newcolour.update( (n,Colour[15]) for n in range (d,e) )
    print(e)
    f = max(e+minrange, pctrange[(len(pctrange)*6)//11])
    newcolour.update( (n,Colour[20]) for n in range (e,f) )
    print(f)
    g = max(f+minrange, pctrange[(len(pctrange)*7)//11])
    newcolour.update( (n,Colour[25]) for n in range (f,g) )
    print(g)
    h = max(g+minrange, pctrange[(len(pctrange)*8)//11])
    newcolour.update( (n,Colour[30]) for n in range (g,h) )
    print(h)
    i = max(h+minrange, pctrange[(len(pctrange)*9)//11])
    newcolour.update( (n,Colour[40]) for n in range (h,i) )
    print(i)
    j = max(i+minrange, pctrange[(len(pctrange)*10)//11])
    newcolour.update( (n,Colour[50]) for n in range (i,j) )
    print(j)
    newcolour.update( (n,Colour[60]) for n in range (j,101) )
    print("highest: ",pctrange[-1])

    for i in range(1,len(mapwriter),2):
        file.write(mapwriter[(i-1)])
        seat = int(mapwriter[i], 16)
        
        colour = newcolour[ pctlist[seat] ]
        file.write(colour)

    file.write(mapwriter[-1])

    file.close()
    return

def turnout20(output = "rendered\\turnout20.svg"):
    file = open(output, "w")

    for i in range(1,len(mapwriter),2):
        file.write(mapwriter[(i-1)])
        seat = int(mapwriter[i], 16)
        
        colour = Rainbow[ (100*int(data20[seat][6])) // int(data20[seat][4]) ]
        file.write(colour)

    file.write(mapwriter[-1])

    file.close()
    return

