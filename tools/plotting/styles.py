
import fnmatch

from cpyroot.tools.style import *

sZtt = Style(markerColor=kOrange-3,
             markerSize=1,
             lineColor=1,
             lineWidth=1,
             fillColor=kOrange-4,
             fillStyle=1001)

sJtf = Style(markerColor=kSpring+7,
             markerSize=1,
             lineColor=1,
             lineWidth=1,
             fillColor=kSpring+5,
             fillStyle=1001)

sZmm = Style(markerColor=kAzure+9,
             markerSize=1,
             lineColor=1,
             lineWidth=1,
             fillColor=kAzure+8,
             fillStyle=1001)

sew  = Style(markerColor=kRed-3,
             markerSize=1,
             lineColor=1,
             lineWidth=1,
             fillColor=kRed-6,
             fillStyle=1001)

stt = Style(markerColor=kBlue-6,
            markerSize=1,
            lineColor=1,
            lineWidth=1,
            fillColor=kBlue-8,
            fillStyle=1001)

sqcd = sJtf # Style(markerColor=3, markerSize=1, lineColor=3, fillColor=3, fillStyle=0)
sdy = sZtt # Style(markerColor=4, markerSize=1, lineColor=4, fillColor=kBlue-9, fillStyle=3344)
swj = sew # Style(markerColor=2, markerSize=1, lineColor=2, fillColor=5, fillStyle=0)
#stt = Style(markerColor=8, markerSize=1, lineColor=8, fillColor=5, fillStyle=0)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':40, 'legend':'DY', 'stack': True},
    'QCD': {'style':sqcd, 'layer':30, 'legend':'QCD', 'stack': True},
    'WJ': {'style':swj, 'layer':20, 'legend':'WJ', 'stack': True},
    'TT': {'style':stt, 'layer':10, 'legend':'TT', 'stack': True},
    'data': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
    'Ztt': {'style':sZtt, 'layer':45, 'legend':'Z to tautau', 'stack': True},
    'Jtf': {'style':sJtf, 'layer':35, 'legend':'jet to tauh', 'stack': True},
    'Zmm': {'style':sZmm, 'layer':34, 'legend':'Z to mumu', 'stack': True},
    'ew': {'style':sew, 'layer':25, 'legend':'electroweak', 'stack': True},
}

def set_style(comp):
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
    
    
    
