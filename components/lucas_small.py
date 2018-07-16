from htt_plot.components.component import Component

import os 

basedir = os.getcwd()+'/lucas_small/'

DY = Component(
    'DY',
    basedir+'DYJetsToLL_M50_LO_ext2.root',
    49144274, 5765.4
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

