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

sqcd = Style(markerColor=qcdcol, markerSize=1, lineColor=1, fillColor=qcdcol, fillStyle=1001)
sdy = Style(markerColor=dycol, markerSize=1, lineColor=1, fillColor=dycol, fillStyle=1001)
sZll = Style(markerColor=kAzure+9, markerSize=1, lineColor=1, fillColor=kAzure+8, fillStyle=1001)
sembed = Style(markerColor=embedcol, markerSize=1, lineColor=1, fillColor=embedcol, fillStyle=1001)
swj = Style(markerColor=wcol, markerSize=1, lineColor=1, fillColor=wcol, fillStyle=1001)
stt = Style(markerColor=ttcol, markerSize=1, lineColor=1, fillColor=ttcol, fillStyle=1001)
sDiboson = Style(markerColor=dibosoncol, markerSize=1, lineColor=1, fillColor=dibosoncol, fillStyle=1001)
ssingletop = Style(markerColor=ttcol, markerSize=1, lineColor=1, fillColor=ttcol, fillStyle=1001)
sfakes = Style(markerColor=5, markerSize=1, lineColor=1, fillColor=8, fillStyle=1001)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':40, 'legend':'DY', 'stack': True},
    'QCD': {'style':sqcd, 'layer':30, 'legend':'QCD', 'stack': True},
    'WJ': {'style':swj, 'layer':20, 'legend':'W+Jets', 'stack': True},
    'TT': {'style':stt, 'layer':10, 'legend':'t#bar{t}', 'stack': True},
    'data': {'style':sdata, 'layer':100, 'legend':'Observation', 'stack': False},
    'Ztt': {'style':sdy, 'layer':45, 'legend':'Z#rightarrow #tau#tau', 'stack': True},
    'Jtf': {'style':sfakes, 'layer':35, 'legend':'jet#rightarrow #tau_{h} fakes', 'stack': True},
    'Zll': {'style':sZll, 'layer':34, 'legend':'Z#rightarrow ll', 'stack': True},
    'ew': {'style':swj, 'layer':25, 'legend':'Electroweak', 'stack': True},
    'DY_WJ_plot': {'style':sdy, 'layer':40, 'legend':'DY', 'stack': True},
    'QCD_WJ_plot': {'style':sqcd, 'layer':30, 'legend':'QCD', 'stack': True},
    'WJ_plot': {'style':swj, 'layer':20, 'legend':'W+Jets', 'stack': True},
    'TT_WJ_plot': {'style':stt, 'layer':10, 'legend':'t#bar{t}', 'stack': True},
    'data_WJ_plot': {'style':sdata, 'layer':100, 'legend':'Observation', 'stack': False},
    'DY_TT_plot': {'style':sdy, 'layer':40, 'legend':'DY', 'stack': True},
    'QCD_TT_plot': {'style':sqcd, 'layer':30, 'legend':'QCD', 'stack': True},
    'WJ_TT_plot': {'style':swj, 'layer':20, 'legend':'W+Jets', 'stack': True},
    'TT_plot': {'style':stt, 'layer':41, 'legend':'t#bar{t}', 'stack': True},
    'data_TT_plot': {'style':sdata, 'layer':100, 'legend':'Observation', 'stack': False},
    'Embedded': {'style':sembed, 'layer':35, 'legend':'#mu #rightarrow embedded', 'stack': True},
    'Diboson': {'style':sDiboson, 'layer':3, 'legend':'Diboson', 'stack': True},
    'singleTop': {'style':ssingletop, 'layer':4, 'legend':'singleTop', 'stack': True},
    'data': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
    'fakes': {'style':sfakes, 'layer':15, 'legend':'jet #rightarrow #tau_{h} fakes', 'stack': True},
}

histPref['TTBar']=histPref['TT']
histPref['WJ']=histPref['WJ_plot']

def set_style(comp):
    found=False
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
