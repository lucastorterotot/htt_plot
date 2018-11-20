from htt_plot.tools.dataset import Dataset

import os 

basedir = os.path.expandvars('${HTTPLOT}/lucas_small/')

nevents_fraction = 1./100

DYJetsToLL_M10to50_LO = Dataset(
    'DYJetsToLL_M10to50_LO',
    basedir+'DYJetsToLL_M10to50_LO.root',
    35291566*nevents_fraction, 18610
)
DYJetsToLL_M50_LO_ext = Dataset(
    'DYJetsToLL_M50_LO_ext',
    basedir+'DYJetsToLL_M50_LO_ext.root',
    94531994*nevents_fraction, 5765.4
)
DYJetsToLL_M50_LO_ext2 = Dataset(
    'DYJetsToLL_M50_LO_ext2',
    basedir+'DYJetsToLL_M50_LO_ext2.root', 
    65473457*nevents_fraction, 5765.4
)
# Colin put 49144274 evts ?

DY = DYJetsToLL_M50_LO_ext2
DY.name = 'DY'

TT_pow = Dataset(
    'TT_pow',
    basedir+'TT_pow.root',
    74644514*nevents_fraction, 831.76
)
WJetsToLNu_LO = Dataset(
    'WJetsToLNu_LO',
    basedir+'WJetsToLNu_LO.root',
    28427574*nevents_fraction, 61526.7
)
WJetsToLNu_LO_ext = Dataset(
    'WJetsToLNu_LO_ext',
    basedir+'WJetsToLNu_LO_ext.root',
    57026058*nevents_fraction, 61526.7
)
data1 = Dataset(
    'data1',
    basedir+'data_single_muon_1.root',
    norm_factor = 1.
)
data2 = Dataset(
    'data1',
    basedir+'data_single_muon_2.root',
    norm_factor = 1.
)
data3 = Dataset(
    'data1',
    basedir+'data_single_muon_3.root',
    norm_factor = 1.
)
data4 = Dataset(
    'data1',
    basedir+'data_single_muon_4.root',
    norm_factor = 1.
)

