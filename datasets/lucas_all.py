from htt_plot.tools.dataset import Dataset

import os 

basedir = os.path.expandvars('${HTTPLOT}/lucas_all/')

Nevts_factor = 1.

DYJetsToLL_M10to50_LO = Dataset(
    'DYJetsToLL_M10to50_LO',
    basedir+'DYJetsToLL_M10to50_LO.root',
    35291566*Nevts_factor,
    18610. # 16270.0
)
DYJetsToLL_M50_LO_ext = Dataset(
    'DYJetsToLL_M50_LO_ext',
    basedir+'DYJetsToLL_M50_LO_ext.root',
    94531994*Nevts_factor, # 49144274 # 65473457
    4963.0 # 5765.4 # 
)
DYJetsToLL_M50_LO_ext2 = Dataset( ## watch out, no matching between twiki and DAS
    'DYJetsToLL_M50_LO_ext2',
    basedir+'DYJetsToLL_M50_LO_ext2.root', 
    104113466*Nevts_factor, # 94531994
    5765.4 # 4963.0 # 
)

TT_pow = Dataset(
    'TT_pow',
    basedir+'TT_pow.root',
    92925926*Nevts_factor, #74644514
    831.76 # 730.6
)
WJetsToLNu_LO = Dataset(
    'WJetsToLNu_LO',
    basedir+'WJetsToLNu_LO.root',
    29705748*Nevts_factor, #28427574
    61526.7 # 50260.0
)
WJetsToLNu_LO_ext = Dataset(
    'WJetsToLNu_LO_ext',
    basedir+'WJetsToLNu_LO_ext.root',
    57026058*Nevts_factor,
    61526.7 # 50260.0
)
data1 = Dataset(
    'data1',
    basedir+'data_single_muon_1.root',
    norm_factor = 1/Nevts_factor
)
data2 = Dataset(
    'data1',
    basedir+'data_single_muon_2.root',
    norm_factor = 1/Nevts_factor
)
data3 = Dataset(
    'data1',
    basedir+'data_single_muon_3.root',
    norm_factor = 1/Nevts_factor
)
data4 = Dataset(
    'data1',
    basedir+'data_single_muon_4.root',
    norm_factor = 1/Nevts_factor
)

