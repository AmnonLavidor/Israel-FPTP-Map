
def define_colours():
    
    Rainbow = dict() ## Turnout scale
    Rainbow.update( (n,"ff1e00") for n in range ( 0,25))
    Rainbow.update( (n,"ff4900") for n in range (25,40))
    Rainbow.update( (n,"ff7400") for n in range (40,45))
    Rainbow.update( (n,"ff9f00") for n in range (45,50))
    Rainbow.update( (n,"ffca00") for n in range (50,54))
    Rainbow.update( (n,"fff400") for n in range (54,57))
    Rainbow.update( (n,"e0ff00") for n in range (57,60))
    Rainbow.update( (n,"b5ff00") for n in range (60,63))
    Rainbow.update( (n,"8bff00") for n in range (63,65))
    Rainbow.update( (n,"60ff00") for n in range (65,67))
    Rainbow.update( (n,"02ff4b") for n in range (67,69))
    Rainbow.update( (n,"02ff75") for n in range (69,70))
    Rainbow.update( (n,"02ffa0") for n in range (70,71))
    Rainbow.update( (n,"02ffca") for n in range (71,73))
    Rainbow.update( (n,"02fff4") for n in range (73,75))
    Rainbow.update( (n,"00b6ff") for n in range (75,77))
    Rainbow.update( (n,"008cff") for n in range (77,80))
    Rainbow.update( (n,"0062ff") for n in range (80,83))
    Rainbow.update( (n,"0038ff") for n in range (83,86))
    Rainbow.update( (n,"000eff") for n in range (86,90))
    Rainbow.update( (n,"5900ff") for n in range (90,101))
    
    Violet = {    ## populist right: Likud, Bibi Bloc
        0 :           "ebe2f1",
        1 :           "cbb5fd"}
    Violet.update( (n,"b89afc") for n in range (2,5) )
    Violet.update( (n,"9e75fb") for n in range (5,10) )
    Violet.update( (n,"834efa") for n in range (10,15) )
    Violet.update( (n,"6d2ff9") for n in range (15,20) )
    Violet.update( (n,"4f12c7") for n in range (20,25) )
    Violet.update( (n,"400f9f") for n in range (25,30) )
    Violet.update( (n,"350d84") for n in range (30,40) )
    Violet.update( (n,"280a65") for n in range (40,50) )
    Violet.update( (n,"1e0749") for n in range (50,60) )
    Violet.update( (n,"12042b") for n in range (60,101))

    Teal = {    ## centre: Blue-White, Ganz Bloc
        0 :         "e3f7ef",
        1 :         "cdf2df"}
    Teal.update( (n,"a6e8c7") for n in range (2,5) )
    Teal.update( (n,"8cdebc") for n in range (5,10) )
    Teal.update( (n,"6ac5a1") for n in range (10,15) )
    Teal.update( (n,"5bb19e") for n in range (15,20) )
    Teal.update( (n,"4e9686") for n in range (20,25) )
    Teal.update( (n,"407b6f") for n in range (25,30) )
    Teal.update( (n,"386d61") for n in range (30,40) )
    Teal.update( (n,"315e54") for n in range (40,50) )
    Teal.update( (n,"24453e") for n in range (50,60) )
    Teal.update( (n,"182e29") for n in range (60,101))

    Pink = {    ## haredi: UTJ, Degel, Aguda
        0 :         "f0ceff",
        1 :         "f5a0ff"}
    Pink.update( (n,"ff56d7") for n in range (2,5) )
    Pink.update( (n,"ff2db9") for n in range (5,10) )
    Pink.update( (n,"ea0299") for n in range (10,15) )
    Pink.update( (n,"db0066") for n in range (15,20) )
    Pink.update( (n,"ba0056") for n in range (20,25) )
    Pink.update( (n,"990047") for n in range (25,30) )
    Pink.update( (n,"87003f") for n in range (30,40) )
    Pink.update( (n,"750036") for n in range (40,50) )
    Pink.update( (n,"560027") for n in range (50,60) )
    Pink.update( (n,"3e001c") for n in range (60,101))

    Green = {    ## arab: Joint List, Hadash-Taal
    0 :              "e6ffcc",
    1 :              "dcffa0"}
    Green.update( (n,"c1ff56") for n in range (2,5) )
    Green.update( (n,"9dff2d") for n in range (5,10) )
    Green.update( (n,"7aea02") for n in range (10,15) )
    Green.update( (n,"49db00") for n in range (15,20) )
    Green.update( (n,"3eba00") for n in range (20,25) )
    Green.update( (n,"329900") for n in range (25,30) )
    Green.update( (n,"2d8700") for n in range (30,40) )
    Green.update( (n,"277500") for n in range (40,50) )
    Green.update( (n,"1c5600") for n in range (50,60) )
    Green.update( (n,"143e00") for n in range (60,101))

    Brown = {    ## religious right: Yemina, Jewish Home, UTJ+Shas, Raam?
        0 :          "f7eae3",
        1 :          "f2d5cd"}
    Brown.update( (n,"e8b5a6") for n in range (2,5) )
    Brown.update( (n,"dea686") for n in range (5,10) )
    Brown.update( (n,"c5896a") for n in range (10,15) )
    Brown.update( (n,"b16f5b") for n in range (15,20) )
    Brown.update( (n,"965f4e") for n in range (20,25) )
    Brown.update( (n,"7b4e40") for n in range (25,30) )
    Brown.update( (n,"6d4438") for n in range (30,40) )
    Brown.update( (n,"5e3b31") for n in range (40,50) )
    Brown.update( (n,"452c24") for n in range (50,60) )
    Brown.update( (n,"2d1d18") for n in range (60,101))
    
    Red = {    ## centreleft: Labour, Labour-Meretz, Zionist Union, ZU+YA, BW+Lab
        0 :        "ffcaeb",
        1 :        "ff9fcb"}
    Red.update( (n,"ff5588") for n in range (2,5) )
    Red.update( (n,"ff2d57") for n in range (5,10) )
    Red.update( (n,"eb012b") for n in range (10,15) )
    Red.update( (n,"dd0000") for n in range (15,20) )
    Red.update( (n,"bb0000") for n in range (20,25) )
    Red.update( (n,"990000") for n in range (25,30) )
    Red.update( (n,"880000") for n in range (30,40) )
    Red.update( (n,"770000") for n in range (40,50) )
    Red.update( (n,"590000") for n in range (50,60) )
    Red.update( (n,"330000") for n in range (60,101))
    
    Blue = {    ## Ideological right, NDI, Likud+Yemina, Likud+JH
        0 :         "b0e1ff",
        1 :         "8ad3ff"}
    Blue.update( (n,"5498fe") for n in range (2,5) )
    Blue.update( (n,"1271fe") for n in range (5,10) )
    Blue.update( (n,"123cfe") for n in range (10,15) )
    Blue.update( (n,"0000dd") for n in range (15,20) )
    Blue.update( (n,"0000bb") for n in range (20,25) )
    Blue.update( (n,"000099") for n in range (25,30) )
    Blue.update( (n,"000088") for n in range (30,40) )
    Blue.update( (n,"000077") for n in range (40,50) )
    Blue.update( (n,"000059") for n in range (50,60) )
    Blue.update( (n,"000033") for n in range (60,101))
    
    Orange = {    ## mizrahi: Shas
        0 :           "fff7df",
        1 :           "ffe9b6"}
    Orange.update( (n,"ffe196") for n in range (2,5) )
    Orange.update( (n,"ffd26a") for n in range (5,10) )
    Orange.update( (n,"ffc343") for n in range (10,15) )
    Orange.update( (n,"f5a812") for n in range (15,20) )
    Orange.update( (n,"d78804") for n in range (20,25) )
    Orange.update( (n,"b27303") for n in range (25,30) )
    Orange.update( (n,"966203") for n in range (30,40) )
    Orange.update( (n,"744b03") for n in range (40,50) )
    Orange.update( (n,"523602") for n in range (50,60) )
    Orange.update( (n,"302001") for n in range (60,101))

    return (Rainbow,Violet,Teal,Pink,Green,Brown,Red,Blue,Orange)



##Generic = {    ## Usage
##    0 :           "",
##    1 :           ""}
##Generic.update( (n,"") for n in range (2,5) )
##Generic.update( (n,"") for n in range (5,10) )
##Generic.update( (n,"") for n in range (10,15) )
##Generic.update( (n,"") for n in range (15,20) )
##Generic.update( (n,"") for n in range (20,25) )
##Generic.update( (n,"") for n in range (25,30) )
##Generic.update( (n,"") for n in range (30,40) )
##Generic.update( (n,"") for n in range (40,50) )
##Generic.update( (n,"") for n in range (50,60) )
##Generic.update( (n,"") for n in range (60,101) )

##class ColorKey:
##
##    def __init__(self, name):
##        self.name = name
##        self.key = dict{}
##
##    def setKey(self, pctRange, shade): #Tuple, string of hex code
##        self.key[pctRange] = shade
##
#### Colour[(100*votes)//valids]
##def margin(pct):
##    if pct < 0.01:
##        return 0
##    if pct < 0.02:
##        return 1
##    if pct < 0.05:
##        return 2
##    if pct < 0.1:
##        return 5
##    if pct < 0.15:
##        return 10
##    
