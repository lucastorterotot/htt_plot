import fnmatch

from ROOT import TColor

from cpyroot.tools.style import *

qcdcol = TColor.GetColor(250,202,255)
embedcol =  TColor.GetColor(248,206,104)
dycol = TColor.GetColor(0,150,255)
wcol = TColor.GetColor(222,90,106)
ttcol = TColor.GetColor(155,152,204)
zlcol = TColor.GetColor(100,182,232)
dibosoncol = TColor.GetColor(222,90,106)

sdy = Style(markerColor=dycol, markerSize=1, lineColor=1, fillColor=dycol, fillStyle=1001)
sembed = Style(markerColor=embedcol, markerSize=1, lineColor=1, fillColor=embedcol, fillStyle=1001)
swj = Style(markerColor=wcol, markerSize=1, lineColor=1, fillColor=wcol, fillStyle=1001)
stt = Style(markerColor=ttcol, markerSize=1, lineColor=1, fillColor=ttcol, fillStyle=1001)
sDiboson = Style(markerColor=dibosoncol, markerSize=1, lineColor=1, fillColor=dibosoncol, fillStyle=1001)
ssingletop = Style(markerColor=ttcol, markerSize=1, lineColor=1, fillColor=ttcol, fillStyle=1001)
sfakes = Style(markerColor=5, markerSize=1, lineColor=1, fillColor=8, fillStyle=1001)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':12, 'legend':'Z #rightarrow ll (l #rightarrow #tau_{h})', 'stack': True},
    'Embedded': {'style':sembed, 'layer':35, 'legend':'#mu #rightarrow embedded', 'stack': True},
    'WJ': {'style':swj, 'layer':9, 'legend':'WJ', 'stack': True},
    'TTBar': {'style':stt, 'layer':2, 'legend':'TTBar', 'stack': True},
    'Diboson': {'style':sDiboson, 'layer':3, 'legend':'Diboson', 'stack': True},
    'singleTop': {'style':ssingletop, 'layer':4, 'legend':'singleTop', 'stack': True},
    'data': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
    'fakes': {'style':sfakes, 'layer':15, 'legend':'jet #rightarrow #tau_{h} fakes', 'stack': True},
    
}

def set_style(comp):
    found=False
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
