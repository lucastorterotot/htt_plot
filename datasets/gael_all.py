from htt_plot.harvesting.dbtools import fetch_dataset

data_lumi = 41529

##### Data

data_datasets = []
data_datasets.append(fetch_dataset('Tau_Run2017B_31Mar2018'))
data_datasets.append(fetch_dataset('Tau_Run2017C_31Mar2018'))
data_datasets.append(fetch_dataset('Tau_Run2017D_31Mar2018'))
data_datasets.append(fetch_dataset('Tau_Run2017E_31Mar2018'))
data_datasets.append(fetch_dataset('Tau_Run2017F_31Mar2018'))

##### MC

## signal

signal_datasets = {'nominal':{}}
signal_datasets['nominal']['ggH200'] = fetch_dataset('HiggsSUSYGG200',200000,9.569511)
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG300',195159,1.169562))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG400',200000,0.248239))
signal_datasets['nominal']['ggH600'] = fetch_dataset('HiggsSUSYGG600',195350,0.016568)
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG700',190896,0.005497))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG800',200000,0.002045))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG900',200000,0.000831))
signal_datasets['nominal']['bbH200'] = fetch_dataset('HiggsSUSYBB200',200000,31.423088)
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB300',200000,6.820417))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB400',200000,2.097873))
signal_datasets['nominal']['bbH600'] = fetch_dataset('HiggsSUSYBB600',194825,0.342609)
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB700',200000,0.163232))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB800',200000,0.083649))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB900',200000,0.045345))
#for xs , tan beta set to 3 for now # watch out following xs are for ggH and not ggA # do tan beta 20 and ma=700GeV
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG80',479614,50.252373))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG90',500000,51.405460))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG100',500000,54.482143))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG110',500000,58.322144))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG120',500000,68.485321))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG130',500000,75.008011))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG140',500000,57.867386))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG180',500000,16.391922))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG200',200000,9.569511))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG250',200000,3.020394))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG300',195159,1.169562))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG350',200000,0.539824))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG400',200000,0.248239))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG450',200000,0.117098))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG600',195350,1.656800e-2))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG700',190896,5.496914e-3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG800',200000,2.045229e-3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG900',200000,8.306932e-4))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG1200',200000,7.921765e-5))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG1400',200000,1.983880e-5))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG1500',200000,1.022560e-5))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG1600',200000,5.327557e-6))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG1800',200000,1.462044e-6))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG2000',196915,3.986337e-7))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG2300',194106,1.522691e-7))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG2600',200000,4.000802e-7))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG2900',190493, 0 ))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYGG3200',200000, 0 ))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB80',478796,0.703451))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB90',495914,1.262232))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB100',500000,2.925667))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB110',493035,8.533750))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB120',500000,33.897850))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB130',500000,91.988472))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB140',500000,96.569893))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB160',500000,67.362778))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB180',476584,45.486023))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB200',200000,31.423088))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB250',200000,13.813787))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB300',200000,6.820417))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB350',191582,3.663028))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB400',200000,2.097873))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB450',194897,1.263573))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB600',194825,3.426089e-1))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB700',200000,1.632315e-1))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB800',200000,8.364933e-2))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB900',200000,4.534489e-2))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB1200',200000,9.192610e-3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB1400',200000,3.662792e-3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB1500',200000,2.384024e-3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB1600',200000,1.577887e3))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB1800',193168,7.209288e-4))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB2000',200000,3.471938e-4))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB2300',200000,1.245566e-4))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB2600',200000,4.776850e-5))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB2900',200000, 0 ))
# signal_datasets['nominal'].append(fetch_dataset('HiggsSUSYBB3200',200000, 0 ))

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

def renorm_nevts(dataset_list):
    ntot = 0.
    for dataset in dataset_list:
        ntot += dataset.nevts
    for dataset in dataset_list:
        dataset.nevts = ntot

DY_datasets = {'nominal':[]}
DY_datasets['nominal'].append(fetch_dataset('DYJetsToLL_M50',48675378.,dy_xsec_incl))
DY_datasets['nominal'].append(fetch_dataset('DYJetsToLL_M50_ext',49125561.,dy_xsec_incl))
renorm_nevts(DY_datasets['nominal'])


# DY1JetsToLL_M50 = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_1jet, 5765.4,
#     treename = treename
# )
# DY1JetsToLL_M50_ext = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_1jet, 5765.4,
#     treename = treename
# )
# DY2JetsToLL_M50 = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_2jet, 5765.4,
#     treename = treename
# )
# DY2JetsToLL_M50_ext = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_2jet, 5765.4,
#     treename = treename
# )
# DY3JetsToLL_M50 = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_3jet, 5765.4,
#     treename = treename
# )
# DY3JetsToLL_M50_ext = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_3jet, 5765.4,
#     treename = treename
# )
# DY4JetsToLL_M50 = Dataset(
#     'DYJetsToLL_M50',
#     basepath.format('DYJetsToLL_M50'),
#     n_ev_dy_4jet, 5765.4,
#     treename = treename
# )

# dy_weight_dict = {
#     0:dy_xsec_incl/n_ev_dy_incl,
#     1:dy_xsec_1jet/(n_ev_dy_incl*dy_xsec_1jet/dy_xsec_incl + n_ev_dy_1jet),
#     2:dy_xsec_2jet/(n_ev_dy_incl*dy_xsec_2jet/dy_xsec_incl  + n_ev_dy_2jet),
#     3:dy_xsec_3jet/(n_ev_dy_incl*dy_xsec_3jet/dy_xsec_incl  + n_ev_dy_3jet),
#     4:dy_xsec_4jet/(n_ev_dy_incl*dy_xsec_4jet/dy_xsec_incl  + n_ev_dy_4jet),
# }

# dy_exps = []
# for njet in range(0, 4):
#     weight = dy_weight_dict[njet]
#     dy_exps.append('(n_up == {njet})*{weight}'.format(njet=njet, weight=weight*data_lumi))
# dy_stitching_weight = '({})'.format(' + '.join(dy_exps))

WJ_datasets = {'nominal':[]}
WJ_datasets['nominal'].append(fetch_dataset('WJetsToLNu_LO',33073306,61526.7))
WJ_datasets['nominal'].append(fetch_dataset('WJetsToLNu_LO_ext',44627200,61526.7))
renorm_nevts(WJ_datasets['nominal'])


TT_datasets = {'nominal':[]}
TT_datasets['nominal'].append(fetch_dataset('TTHad_pow',41729120,377.96))
TT_datasets['nominal'].append(fetch_dataset('TTLep_pow',9000000,88.29))
TT_datasets['nominal'].append(fetch_dataset('TTSemi_pow',43732445,365.35))

##### Single top

singleTop_datasets = {'nominal':[]}
singleTop_datasets['nominal'].append(fetch_dataset('TBar_tch',3652340,80.95))
singleTop_datasets['nominal'].append(fetch_dataset('TBar_tWch',7977430,35.85))
singleTop_datasets['nominal'].append(fetch_dataset('T_tch',5982064,136.02))
singleTop_datasets['nominal'].append(fetch_dataset('T_tWch',7794186,35.85))

##### DiBoson inclusive

# using inclusive WW and WZ datasets for now
Diboson_datasets = {'nominal':[]}
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo4L',6964071,1.325))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo4L_ext',6967853,1.325))
renorm_nevts(Diboson_datasets['nominal'])
Diboson_datasets['nominal'].append(fetch_dataset('WW',7791498,75.88))
Diboson_datasets['nominal'].append(fetch_dataset('WZ',3928630,27.57))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo2L2Nu',8744768,0.6008))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo2L2Q',27840918,3.688))

# ZZ failed computing, going to exclusive datasets
# ZZ = Dataset(
#     'ZZ',
#     basepath.format('ZZ'),
#     1949768, 12.14,
#     treename = treename
# )


##### Embedded

Embedded_datasets = {'nominal':[]}
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017B_tt'))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017C_tt'))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017D_tt'))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017E_tt'))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017F_tt'))


from htt_plot.systematics import sys_dict_samples # TODO put sys_dicts in their own modules

for sys in sys_dict_samples:

    ## signal
    if 'signal' in sys_dict_samples[sys]['processes']:
        signal_datasets[sys] = {}
        signal_datasets[sys]['ggH200'] = fetch_dataset('HiggsSUSYGG200',200000,4.9964523,sys=sys)
        # signal_datasets[sys]['ggH300'] = fetch_dataset('HiggsSUSYGG300',195159,2.0481775,sys=sys)
        # signal_datasets[sys]['ggH400'] = fetch_dataset('HiggsSUSYGG400',200000,1.4211406,sys=sys)
        signal_datasets[sys]['ggH600'] = fetch_dataset('HiggsSUSYGG600',195350,0.24884269,sys=sys)
        # signal_datasets[sys]['ggH700'] = fetch_dataset('HiggsSUSYGG700',190896,0.11233324,sys=sys)
        # signal_datasets[sys]['ggH800'] = fetch_dataset('HiggsSUSYGG800',200000,0.054282725,sys=sys)
        # signal_datasets[sys]['ggH900'] = fetch_dataset('HiggsSUSYGG900',200000,0.027804535,sys=sys)
        signal_datasets[sys]['bbH200'] = fetch_dataset('HiggsSUSYBB200',200000,0.75723660,sys=sys)
        # signal_datasets[sys]['bbH300'] = fetch_dataset('HiggsSUSYBB300',200000,0.20989677,sys=sys)
        # signal_datasets[sys]['bbH400'] = fetch_dataset('HiggsSUSYBB400',200000,0.069850326,sys=sys)
        signal_datasets[sys]['bbH600'] = fetch_dataset('HiggsSUSYBB600',194825,0.012318182,sys=sys)
        # signal_datasets[sys]['bbH700'] = fetch_dataset('HiggsSUSYBB700',200000,0.0060249786,sys=sys)
        # signal_datasets[sys]['bbH800'] = fetch_dataset('HiggsSUSYBB800',200000,0.0031533239,sys=sys)
        # signal_datasets[sys]['bbH900'] = fetch_dataset('HiggsSUSYBB900',200000,0.0017401302,sys=sys)
    
    ## DY
    if 'DY' in sys_dict_samples[sys]['processes']:
        DY_datasets[sys] = []
        DY_datasets[sys].append(fetch_dataset('DYJetsToLL_M50',48675378,dy_xsec_incl,sys=sys))
        DY_datasets[sys].append(fetch_dataset('DYJetsToLL_M50_ext',49125561,dy_xsec_incl,sys=sys))
        renorm_nevts(DY_datasets[sys])

    # W+Jets
    if 'W' in sys_dict_samples[sys]['processes']:
        WJ_datasets[sys] = []
        WJ_datasets[sys].append(fetch_dataset('WJetsToLNu_LO',33073306,61526.7,sys=sys))
        WJ_datasets[sys].append(fetch_dataset('WJetsToLNu_LO_ext',44627200,61526.7,sys=sys))
        renorm_nevts(WJ_datasets[sys])
    
    # TTbar
    if 'TT' in sys_dict_samples[sys]['processes']:
        TT_datasets[sys] = []
        TT_datasets[sys].append(fetch_dataset('TTHad_pow',41729120,377.96,sys=sys))
        TT_datasets[sys].append(fetch_dataset('TTLep_pow',9000000,88.29,sys=sys))
        TT_datasets[sys].append(fetch_dataset('TTSemi_pow',43732445,365.35,sys=sys))
    
    ##### Single top
    if 'singleTop' in sys_dict_samples[sys]['processes']:
        singleTop_datasets[sys] = []
        singleTop_datasets[sys].append(fetch_dataset('TBar_tch',3652340,80.95,sys=sys))
        singleTop_datasets[sys].append(fetch_dataset('TBar_tWch',7977430,35.85,sys=sys))
        singleTop_datasets[sys].append(fetch_dataset('T_tch',5982064,136.02,sys=sys))
        singleTop_datasets[sys].append(fetch_dataset('T_tWch',7794186,35.85,sys=sys))
    
    ##### DiBoson inclusive
    if 'Diboson' in sys_dict_samples[sys]['processes']:
        Diboson_datasets[sys] = []
        Diboson_datasets[sys].append(fetch_dataset('ZZTo4L',6964071,1.325,sys=sys))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo4L_ext',6967853,1.325,sys=sys))
        renorm_nevts(Diboson_datasets[sys])
        Diboson_datasets[sys].append(fetch_dataset('WW',7791498,75.88,sys=sys))
        Diboson_datasets[sys].append(fetch_dataset('WZ',3928630,27.57,sys=sys))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo2L2Nu',8744768,0.6008,sys=sys))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo2L2Q',27840918,3.688,sys=sys))
    
    ##### Embedded
    if 'Embedded' in sys_dict_samples[sys]['processes']:
        Embedded_datasets[sys] = []
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017B_tt',sys=sys))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017C_tt',sys=sys))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017D_tt',sys=sys))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017E_tt',sys=sys))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017F_tt',sys=sys))
    


## lumi weighting

for ds_type in [singleTop_datasets, WJ_datasets, Diboson_datasets, TT_datasets, DY_datasets]:
    for sys, dataset_list in ds_type.iteritems() :
        for dataset in dataset_list:
            dataset.compute_weight(data_lumi)

for ds_type in [signal_datasets]:
    for sys, dataset_list in ds_type.iteritems() :
        for name, dataset in dataset_list.iteritems():
            dataset.compute_weight(data_lumi)
            
for dataset in data_datasets:
    dataset.compute_weight()
for sys, dataset_list in Embedded_datasets.iteritems():
    for dataset in dataset_list:
        dataset.compute_weight()
