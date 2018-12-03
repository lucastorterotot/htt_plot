
import fnmatch

from cpyroot.tools.style import *

sdy = Style(markerColor=4, markerSize=1, lineColor=4, fillColor=kBlue-9, fillStyle=1001)
swj = Style(markerColor=2, markerSize=1, lineColor=2, fillColor=2, fillStyle=1001)
stt = Style(markerColor=8, markerSize=1, lineColor=kViolet, fillColor=kViolet, fillStyle=1001)
sfakes = Style(markerColor=5, markerSize=1, lineColor=1, fillColor=8, fillStyle=1001)
sdata = sData

histPref = {
    'DY': {'style':sdy, 'layer':30, 'legend':'DY', 'stack': True},
    'WJ': {'style':swj, 'layer':9, 'legend':'WJ', 'stack': True},
    'TT*': {'style':stt, 'layer':10, 'legend':'TT', 'stack': True},
    'data': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
    'fakes1': {'style':sfakes, 'layer':15, 'legend':'fakes', 'stack': True},
    'fakes2': {'style':sfakes, 'layer':15, 'legend':'fakes', 'stack': True}
}

def set_style(comp):
    found=False
    for key, pref in histPref.iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
    
    
    
