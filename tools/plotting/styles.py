
import fnmatch

from cpyroot.tools.style import *

sdy = Style(markerColor=4, markerSize=1, lineColor=4, fillColor=kBlue-9, fillStyle=1001)
swj = Style(markerColor=2, markerSize=1, lineColor=2, fillColor=5, fillStyle=1001)
stt = Style(markerColor=8, markerSize=1, lineColor=8, fillColor=kViolet, fillStyle=1001)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':30, 'legend':'DY', 'stack': True},
    'WJ': {'style':swj, 'layer':9, 'legend':'WJ', 'stack': True},
    'TT': {'style':stt, 'layer':10, 'legend':'TT', 'stack': True},
    'data': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
}

def set_style(comp):
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
    
    
    
