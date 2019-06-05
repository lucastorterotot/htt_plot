from htt_plot.tools.dataset import Dataset

import os 

basepath = os.path.expandvars('/data2/ltorterotot/MSSM_Samples_19-06-05/{}/tree_fakes.root')

treename = 'events'
data_lumi = 41529

##### MC

## DY

n_ev_dy_incl = 48675378. + 49125561.
n_ev_dy_1jet = 42331295. + 33669127.
n_ev_dy_2jet = 88895. + 9701595.
n_ev_dy_3jet = 5748466. + 1149467.
n_ev_dy_4jet = 4328648.

dy_xsec_incl = 5765.4
k_factor = dy_xsec_incl/5343.0
dy_xsec_1jet = 877.8 * k_factor
dy_xsec_2jet = 304.4 * k_factor
dy_xsec_3jet = 111.5 * k_factor
dy_xsec_4jet = 44.03 * k_factor

DYJetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_incl, 5765.4,
    treename = treename
)
DYJetsToLL_M50_ext = Dataset(
    'DYJetsToLL_M50_ext',
    basepath.format('DYJetsToLL_M50_ext'),
    n_ev_dy_incl, 5765.4,
    treename = treename
)
DY1JetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_1jet, 5765.4,
    treename = treename
)
DY1JetsToLL_M50_ext = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_1jet, 5765.4,
    treename = treename
)
DY2JetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_2jet, 5765.4,
    treename = treename
)
DY2JetsToLL_M50_ext = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_2jet, 5765.4,
    treename = treename
)
DY3JetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_3jet, 5765.4,
    treename = treename
)
DY3JetsToLL_M50_ext = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_3jet, 5765.4,
    treename = treename
)
DY4JetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basepath.format('DYJetsToLL_M50'),
    n_ev_dy_4jet, 5765.4,
    treename = treename
)

dy_weight_dict = {
    0:dy_xsec_incl/n_ev_dy_incl,
    1:dy_xsec_1jet/(n_ev_dy_incl*dy_xsec_1jet/dy_xsec_incl + n_ev_dy_1jet),
    2:dy_xsec_2jet/(n_ev_dy_incl*dy_xsec_2jet/dy_xsec_incl  + n_ev_dy_2jet),
    3:dy_xsec_3jet/(n_ev_dy_incl*dy_xsec_3jet/dy_xsec_incl  + n_ev_dy_3jet),
    4:dy_xsec_4jet/(n_ev_dy_incl*dy_xsec_4jet/dy_xsec_incl  + n_ev_dy_4jet),
}

dy_exps = []
for njet in range(0, 4):
    weight = dy_weight_dict[njet]
    dy_exps.append('(n_up == {njet})*{weight}'.format(njet=njet, weight=weight*data_lumi))
dy_stitching_weight = '({})'.format(' + '.join(dy_exps))

WJetsToLNu = Dataset(
    'WJetsToLNu',
    basepath.format('WJetsToLNu_LO'),
    33073306*(64./65.)+44627200, 61526.7,
    treename = treename
)
WJetsToLNu_ext = Dataset(
    'WJetsToLNu_ext',
    basepath.format('WJetsToLNu_LO_ext'),
    33073306*(64./65.)+44627200, 61526.7,
    treename = treename
)


TTHad_pow = Dataset(
    'TTHad_pow',
    basepath.format('TTHad_pow'),
    41729120, 377.96,
    treename = treename
)
TTLep_pow = Dataset(
    'TTLep_pow',
    basepath.format('TTLep_pow'),
    9000000*(7./17.), 88.29,
    treename = treename
)
TTSemi_pow = Dataset(
    'TTSemi_pow',
    basepath.format('TTSemi_pow'),
    43732445, 365.35,
    treename = treename
)

##### Single top

TBar_tch = Dataset(
    'TBar_tch',
    basepath.format('TBar_tch'),
    3652340, 80.95,
    treename = treename
)
TBar_tWch = Dataset(
    'TBar_tWch',
    basepath.format('TBar_tWch'),
    7977430*(14./15.), 35.85,
    treename = treename
)
T_tch = Dataset(
    'T_tch',
    basepath.format('T_tch'),
    5982064, 136.02,
    treename = treename
)
T_tWch = Dataset(
    'T_tWch',
    basepath.format('T_tWch'),
    7794186, 35.85,
    treename = treename
)

##### DiBoson inclusive

# using inclusive WW and WZ datasets for now
WW = Dataset(
    'WW',
    basepath.format('WW'),
    7791498, 75.88,
    treename = treename
)
WZ = Dataset(
    'WZ',
    basepath.format('WZ'),
    3928630, 27.57,
    treename = treename
)
# ZZ failed computing, going to exclusive datasets
# ZZ = Dataset(
#     'ZZ',
#     basepath.format('ZZ'),
#     1949768, 12.14,
#     treename = treename
# )

ZZTo4L = Dataset(
    'ZZTo4L',
    basepath.format('ZZTo4L'),
    6964071*(10./12.)+6967853, 1.325,
    treename = treename
)
ZZTo4L_ext = Dataset(
    'ZZTo4L_ext',
    basepath.format('ZZTo4L'),
    6964071+6967853, 1.325,
    treename = treename
)

ZZTo2L2Nu = Dataset(
    'ZZTo2L2Nu',
    basepath.format('ZZTo2L2Nu'),
    8744768, 0.6008,
    treename = treename
)

ZZTo2L2Q = Dataset(
    'ZZTo2L2Q',
    basepath.format('ZZTo2L2Q'),
    27840918, 3.688,
    treename = treename
)


##### Data

datapath = os.path.expandvars('/data2/gtouquet/MSSM_Samples_310119/{}/tree_fakes.root')

dataB = Dataset(
    'dataB',
    datapath.format('DYJetsToLL_M50'),
    norm_factor = 1.,
    treename = treename
)

##### Embedded

EmbeddedB = Dataset(
    'EmbeddedB',
    basepath.format('ZZTo4L'),
    norm_factor = 1.,
    treename = treename
)

## lumi weighting

singleTop_datasets = [TBar_tch,TBar_tWch,T_tch,T_tWch]
WJ_datasets = [WJetsToLNu,WJetsToLNu_ext]
Diboson_datasets = [WW,WZ,ZZTo4L,ZZTo4L_ext,ZZTo2L2Nu,ZZTo2L2Q]
TT_datasets = [TTHad_pow,TTLep_pow,TTSemi_pow]
DY_datasets = [DYJetsToLL_M50,DYJetsToLL_M50_ext,
               # DY1JetsToLL_M50,DY1JetsToLL_M50_ext,
               # DY2JetsToLL_M50,DY2JetsToLL_M50_ext,
               # DY3JetsToLL_M50,DY3JetsToLL_M50_ext,
               # DY4JetsToLL_M50
]

MC_datasets = singleTop_datasets + WJ_datasets + Diboson_datasets + TT_datasets + DY_datasets

data_datasets = [dataB]

Embedded_datasets = [EmbeddedB]

stitched_datasets = DY_datasets

for dataset in MC_datasets :
    dataset.compute_weight(data_lumi, stitched=(dataset in stitched_datasets))

for dataset in data_datasets + Embedded_datasets:
    dataset.compute_weight()
