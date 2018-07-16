from htt_plot.components.component import Component

import os 

basedir = os.getcwd()+'/lucas_small/'

Nevts_factor = 1./100

DYJetsToLL_M10to50_LO = Component(
    'DYJetsToLL_M10to50_LO',
    basedir+'DYJetsToLL_M10to50_LO.root',
    35291566/Nevts_factor, 16270.0
)
DYJetsToLL_M50_LO_ext = Component(
    'DYJetsToLL_M50_LO_ext',
    basedir+'DYJetsToLL_M50_LO_ext.root',
    94531994/Nevts_factor, 4963.0
)
DYJetsToLL_M50_LO_ext2 = Component(
    'DYJetsToLL_M50_LO_ext2',
    basedir+'DYJetsToLL_M50_LO_ext2.root', 
    65473457/Nevts_factor, 4963.0 # 5765.4
)
# Colin put 49144274 evts ?

DY = DYJetsToLL_M50_LO_ext2
DY.name = 'DY'

TT_pow = Component(
    'TT_pow',
    basedir+'TT_pow.root',
    74644514/Nevts_factor, 730.6
)
WJetsToLNu_LO = Component(
    'WJetsToLNu_LO',
    basedir+'WJetsToLNu_LO.root',
    28427574/Nevts_factor, 50260.0
)
WJetsToLNu_LO_ext = Component(
    'WJetsToLNu_LO_ext',
    basedir+'WJetsToLNu_LO_ext.root',
    57026058/Nevts_factor, 50260.0
)
data1 = Component(
    'data1',
    basedir+'data_single_muon_1.root'
)
data2 = Component(
    'data1',
    basedir+'data_single_muon_2.root'
)
data3 = Component(
    'data1',
    basedir+'data_single_muon_3.root'
)
data4 = Component(
    'data1',
    basedir+'data_single_muon_4.root'
)

