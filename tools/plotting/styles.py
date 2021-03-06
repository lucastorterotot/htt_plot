import fnmatch

from ROOT import TColor, kBlack

from cpyroot.tools.style import *

embedcol =  TColor.GetColor(248,206,104)
dycol = TColor.GetColor(0,150,255)
WJcol = TColor.GetColor(193,68,78)
EWKcol = TColor.GetColor(222,90,106)
dibosoncol = TColor.GetColor(146,12,23)
ttcol = TColor.GetColor(155,152,204)
stcol = TColor.GetColor(85,82,204)
zlcol = TColor.GetColor(100,182,232)
H125col = TColor.GetColor(100,100,100)

sdy = Style(markerColor=dycol, markerSize=1, lineColor=1, fillColor=dycol, fillStyle=1001)
sembed = Style(markerColor=embedcol, markerSize=1, lineColor=1, fillColor=embedcol, fillStyle=1001)
swj = Style(markerColor=WJcol, markerSize=1, lineColor=1, fillColor=WJcol, fillStyle=1001)
sEWK = Style(markerColor=EWKcol, markerSize=1, lineColor=1, fillColor=EWKcol, fillStyle=1001)
stt = Style(markerColor=ttcol, markerSize=1, lineColor=1, fillColor=ttcol, fillStyle=1001)
sDiboson = Style(markerColor=dibosoncol, markerSize=1, lineColor=1, fillColor=dibosoncol, fillStyle=1001)
ssingletop = Style(markerColor=stcol, markerSize=1, lineColor=1, fillColor=stcol, fillStyle=1001)
sfakes = Style(markerColor=5, markerSize=1, lineColor=1, fillColor=8, fillStyle=1001)
sH125 = Style(markerColor=H125col, markerSize=1, lineColor=1, fillColor=H125col, fillStyle=1001)
sdata = sData
sunc = Style(fillColor=17, fillStyle=3002)
ssig = Style(fillColor=0, fillStyle=0, lineColor=2)
ssig2 = Style(fillColor=0, fillStyle=0, lineColor=4)
ssig3 = Style(fillColor=0, fillStyle=0, lineColor=5)
ssig4 = Style(fillColor=0, fillStyle=0, lineColor=6)
ssig5 = Style(fillColor=0, fillStyle=0, lineColor=7)
ssig6 = Style(fillColor=0, fillStyle=0, lineColor=8)

histPref = {}

histPref['default'] = {
    'data_obs': {'style':sdata, 'layer':0, 'legend':'data', 'stack': False},
    'Embedded': {'style':sembed, 'layer':90, 'legend':'#mu #rightarrow #text{embedded}', 'stack': True},
    'jetFakes': {'style':sfakes, 'layer':80, 'legend':'#text{jet} #rightarrow #tauh #text{ fakes}', 'stack': True},
    'H125': {'style':sH125, 'layer':1, 'legend':'#higgs #text{ (#SI{125}{#GeV})}', 'stack': True},
    
    'Zll': {'style':sdy, 'layer':70, 'legend':'Z #rightarrow #ell#ell', 'stack': True},
    'ZL': {'style':sdy, 'layer':70, 'legend':'Z #rightarrow #ell#ell (#ell #rightarrow #tauh)', 'stack': True},
    'ZTT': {'style':sdy, 'layer':71, 'legend':'Z #rightarrow #tauh#tauh', 'stack': True},
    'ZLL': {'style':sdy, 'layer':69, 'legend':'Z #rightarrow qq, #ell#ell', 'stack': True},

    'TTL': {'style':stt, 'layer':40, 'legend':'#quarkt#antiquarkt #rightarrow #ell#ell (#ell #rightarrow #tauh)', 'stack': True},
    'TTT': {'style':stt, 'layer':41, 'legend':'#quarkt#antiquarkt #rightarrow #tau#tau', 'stack': True},
    'TTJ': {'style':stt, 'layer':39, 'legend':'#quarkt#antiquarkt #rightarrow qq, #ell#ell', 'stack': True},

    'VVL': {'style':sDiboson, 'layer':60, 'legend':'Diboson-singleTop #rightarrow #ell#ell (#ell #rightarrow #tauh)', 'stack': True},
    'VVT': {'style':sDiboson, 'layer':61, 'legend':'Diboson-singleTop #rightarrow #tau#tau', 'stack': True},
    'VVJ': {'style':sDiboson, 'layer':59, 'legend':'Diboson-singleTop #rightarrow qq, #ell#ell', 'stack': True},

    'WJ': {'style':swj, 'layer':58, 'legend':'#Wboson+#text{jets}', 'stack': True},
    
    'DY': {'style':sdy, 'layer':70, 'legend':'DY', 'stack': True},
    'TTBar': {'style':stt, 'layer':40, 'legend':'#quarkt#antiquarkt', 'stack': True},
    'EWK': {'style':sEWK, 'layer':60, 'legend':'Electroweak', 'stack': True},
    'Diboson': {'style':sDiboson, 'layer':61, 'legend':'Diboson', 'stack': True},
    'singleTop': {'style':ssingletop, 'layer':59, 'legend':'singleTop', 'stack': True},
    
    'VV': {'style':sDiboson, 'layer':62, 'legend':'VV', 'stack': True},

    'total_background': {'style':sunc, 'layer':1, 'legend':'systematic uncertainties', 'stack': False},
    'signal_H600': {'style':ssig, 'layer':0, 'legend':'#phi #rightarrow #tau#tau (m_{#phi}=600 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH600': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=600 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_ggH600': {'style':ssig, 'layer':0, 'legend':'gg#phi (m_{#phi}=600 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH800': {'style':ssig3, 'layer':0, 'legend':'bb#phi (m_{#phi}=800 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_ggH800': {'style':ssig4, 'layer':0, 'legend':'gg#phi (m_{#phi}=800 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH900': {'style':ssig5, 'layer':0, 'legend':'bb#phi (m_{#phi}=900 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_ggH900': {'style':ssig6, 'layer':0, 'legend':'gg#phi (m_{#phi}=900 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH400': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=400 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH450': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=450 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH1400': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=1400 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH1800': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=1800 GeV, #sigma#timesBR=1 pb)', 'stack': False},
    'signal_bbH2000': {'style':ssig2, 'layer':0, 'legend':'bb#phi (m_{#phi}=2000 GeV, #sigma#timesBR=1 pb)', 'stack': False},
}

import copy
def make_histPref_copy(key, origkey='default'):
    histPref[key] = copy.deepcopy(histPref[origkey])

for channel in ["tt", "mt", "et"]:
    make_histPref_copy(channel)

histPref['tt']['ZTT']['legend'] = 'Z #rightarrow #tauh#tauh'
histPref['mt']['ZTT']['legend'] = 'Z #rightarrow #tauh#tauh  (#tauh #rightarrow #mu)'
histPref['et']['ZTT']['legend'] = 'Z #rightarrow #tauh#tauh  (#tauh #rightarrow #ele)'

histPref['tt']['TTT']['legend'] = '#quarkt#antiquarkt #rightarrow #tauh#tauh'
histPref['mt']['TTT']['legend'] = '#quarkt#antiquarkt #rightarrow #ell#tauh'
histPref['et']['TTT']['legend'] = '#quarkt#antiquarkt #rightarrow #ell#tauh'

histPref['tt']['VVT']['legend'] = 'Diboson-singleTop #rightarrow #tauh#tauh'
histPref['mt']['VVT']['legend'] = 'Diboson-singleTop #rightarrow #ell#tauh'
histPref['et']['VVT']['legend'] = 'Diboson-singleTop #rightarrow #ell#tauh'

    
for key in histPref:
    histPref[key]['data_hist'] = histPref[key]['data_obs']
    histPref[key]['EMB'] = histPref[key]['Embedded']
    histPref[key]['fakes'] = histPref[key]['jetFakes']
    histPref[key]['ZJ'] = histPref[key]['jetFakes']
    histPref[key]['W'] = histPref[key]['WJ']
    histPref[key]['TT'] = histPref[key]['TTBar']

def set_style(comp, channel='default'):
    found=False
    for key, pref in histPref[channel].iteritems():
        if fnmatch.fnmatch(comp.name, key):
            comp.style = pref['style']
            found = True
    if not found:
        comp.style = sData
