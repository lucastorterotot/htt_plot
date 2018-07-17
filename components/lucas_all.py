from htt_plot.components.component import Component

import os 

basedir = os.getcwd()+'/lucas_all/'

Nevts_factor = 1.

DYJetsToLL_M10to50_LO = Component(
    'DYJetsToLL_M10to50_LO',
    basedir+'DYJetsToLL_M10to50_LO.root',
    35291566*Nevts_factor, 18610.
)
DYJetsToLL_M50_LO_ext = Component(
    'DYJetsToLL_M50_LO_ext',
    basedir+'DYJetsToLL_M50_LO_ext.root',
    104113466*Nevts_factor, 5765.4
)
DYJetsToLL_M50_LO_ext2 = Component(
    'DYJetsToLL_M50_LO_ext2',
    basedir+'DYJetsToLL_M50_LO_ext2.root', 
    49144274*Nevts_factor, 5765.4
)
# Colin put 49144274 evts ?

DY = DYJetsToLL_M50_LO_ext2
DY.name = 'DY'

TT_pow = Component(
    'TT_pow',
    basedir+'TT_pow.root',
    92925926*Nevts_factor, 831.76
)
WJetsToLNu_LO = Component(
    'WJetsToLNu_LO',
    basedir+'WJetsToLNu_LO.root',
    29705748*Nevts_factor, 61526.7
)
WJetsToLNu_LO_ext = Component(
    'WJetsToLNu_LO_ext',
    basedir+'WJetsToLNu_LO_ext.root',
    57026058*Nevts_factor, 61526.7
)
data1 = Component(
    'data1',
    basedir+'data_single_muon_1.root',
    norm_factor = 1/Nevts_factor
)
data2 = Component(
    'data1',
    basedir+'data_single_muon_2.root',
    norm_factor = 1/Nevts_factor
)
data3 = Component(
    'data1',
    basedir+'data_single_muon_3.root',
    norm_factor = 1/Nevts_factor
)
data4 = Component(
    'data1',
    basedir+'data_single_muon_4.root',
    norm_factor = 1/Nevts_factor
)

