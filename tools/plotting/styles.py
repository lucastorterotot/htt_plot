
import fnmatch

from cpyroot.tools.style import *

sdy = Style(markerColor=4, markerSize=1, lineColor=4, fillColor=kBlue-9, fillStyle=3344)
swj = Style(markerColor=2, markerSize=1, lineColor=2, fillColor=5, fillStyle=0)
stt = Style(markerColor=8, markerSize=1, lineColor=8, fillColor=5, fillStyle=0)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':30, 'legend':'DY'},
    'WJ': {'style':swj, 'layer':20, 'legend':'WJ'},
    'TT': {'style':stt, 'layer':10, 'legend':'TT'},
    'data': {'style':sdata, 'layer':0, 'legend':'data'},
}

def set_style(comp):
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
    
    
    
