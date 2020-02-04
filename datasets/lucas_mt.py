from htt_plot.harvesting.dbtools import fetch_dataset

channel = 'mt'

prod_date = '190819'

data_lumi = 41529

##### Data

data_datasets = []
data_datasets.append(fetch_dataset('SingleMuon_Run2017B_31Mar2018', channel=channel, prod_date=prod_date))
data_datasets.append(fetch_dataset('SingleMuon_Run2017C_31Mar2018', channel=channel, prod_date=prod_date))
data_datasets.append(fetch_dataset('SingleMuon_Run2017D_31Mar2018', channel=channel, prod_date=prod_date))
data_datasets.append(fetch_dataset('SingleMuon_Run2017E_31Mar2018', channel=channel, prod_date=prod_date))
data_datasets.append(fetch_dataset('SingleMuon_Run2017F_31Mar2018', channel=channel, prod_date=prod_date))

##### MC

## DY

n_ev_dy_incl = 48675378. + 49125561.
n_ev_dy_1jet = 42331295. + 33669127.
n_ev_dy_2jet = 88895. + 9701595.
n_ev_dy_3jet = 5748466. + 1149467.
n_ev_dy_4jet = 4328648.

dy_lowmass_xsec_incl = 21658.0
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
DY_datasets['nominal'].append(fetch_dataset('DYJetsToLL_M10to50_LO',39521230.,dy_lowmass_xsec_incl, channel=channel, prod_date=prod_date))
DY_datasets['nominal'].append(fetch_dataset('DYJetsToLL_M50',48675378.,dy_xsec_incl, channel=channel, prod_date=prod_date))
DY_datasets['nominal'].append(fetch_dataset('DYJetsToLL_M50_ext',49125561.,dy_xsec_incl, channel=channel, prod_date=prod_date))
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
WJ_datasets['nominal'].append(fetch_dataset('WJetsToLNu_LO',33073306,61526.7, channel=channel, prod_date=prod_date))
WJ_datasets['nominal'].append(fetch_dataset('WJetsToLNu_LO_ext',44627200,61526.7, channel=channel, prod_date=prod_date))
renorm_nevts(WJ_datasets['nominal'])


TT_datasets = {'nominal':[]}
TT_datasets['nominal'].append(fetch_dataset('TTHad_pow',41729120,377.96, channel=channel, prod_date=prod_date))
TT_datasets['nominal'].append(fetch_dataset('TTLep_pow',9000000,88.29, channel=channel, prod_date=prod_date))
TT_datasets['nominal'].append(fetch_dataset('TTSemi_pow',43732445,365.35, channel=channel, prod_date=prod_date))

##### Single top

singleTop_datasets = {'nominal':[]}
singleTop_datasets['nominal'].append(fetch_dataset('TBar_tch',3652340,80.95, channel=channel, prod_date=prod_date))
singleTop_datasets['nominal'].append(fetch_dataset('TBar_tWch',7977430,35.85, channel=channel, prod_date=prod_date))
singleTop_datasets['nominal'].append(fetch_dataset('T_tch',5982064,136.02, channel=channel, prod_date=prod_date))
singleTop_datasets['nominal'].append(fetch_dataset('T_tWch',7794186,35.85, channel=channel, prod_date=prod_date))

##### DiBoson inclusive

# using inclusive WW and WZ datasets for now
Diboson_datasets = {'nominal':[]}
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo4L',6964071,1.325, channel=channel, prod_date=prod_date))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo4L_ext',6967853,1.325, channel=channel, prod_date=prod_date))
renorm_nevts(Diboson_datasets['nominal'])
Diboson_datasets['nominal'].append(fetch_dataset('WW',7791498,75.88, channel=channel, prod_date=prod_date))
Diboson_datasets['nominal'].append(fetch_dataset('WZ',3928630,27.57, channel=channel, prod_date=prod_date))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo2L2Nu',8744768,0.6008, channel=channel, prod_date=prod_date))
Diboson_datasets['nominal'].append(fetch_dataset('ZZTo2L2Q',27840918,3.688, channel=channel, prod_date=prod_date))

# ZZ failed computing, going to exclusive datasets
# ZZ = Dataset(
#     'ZZ',
#     basepath.format('ZZ'),
#     1949768, 12.14,
#     treename = treename
# )

##### EWK

EWK_datasets = {'nominal':[]}
EWK_datasets['nominal'].append(fetch_dataset('WToLNu_M50_Plus2J',4358697,29.59, channel=channel, prod_date=prod_date))
EWK_datasets['nominal'].append(fetch_dataset('WToLNu_M50_Minus2J',4385142,23.24, channel=channel, prod_date=prod_date))
EWK_datasets['nominal'].append(fetch_dataset('ZToLL_M50',952504,4.321, channel=channel, prod_date=prod_date))
EWK_datasets['nominal'].append(fetch_dataset('ZToNuNu',2949960,10.66, channel=channel, prod_date=prod_date))


##### Embedded

Embedded_datasets = {'nominal':[]}
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017B_{}'.format(channel), channel=channel, prod_date=prod_date))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017C_{}'.format(channel), channel=channel, prod_date=prod_date))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017D_{}'.format(channel), channel=channel, prod_date=prod_date))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017E_{}'.format(channel), channel=channel, prod_date=prod_date))
Embedded_datasets['nominal'].append(fetch_dataset('Embedded2017F_{}'.format(channel), channel=channel, prod_date=prod_date))


from htt_plot.systematics import sys_dict_samples # TODO put sys_dicts in their own modules

for sys in sys_dict_samples:
    
    ## DY
    if 'DY' in sys_dict_samples[sys]['processes']:
        DY_datasets[sys] = []
        DY_datasets[sys].append(fetch_dataset('DYJetsToLL_M10to50_LO',39521230.,dy_lowmass_xsec_incl, channel=channel, prod_date=prod_date))
        DY_datasets[sys].append(fetch_dataset('DYJetsToLL_M50',48675378,dy_xsec_incl,sys=sys, channel=channel, prod_date=prod_date))
        DY_datasets[sys].append(fetch_dataset('DYJetsToLL_M50_ext',49125561,dy_xsec_incl,sys=sys, channel=channel, prod_date=prod_date))
        renorm_nevts(DY_datasets[sys])

    # W+Jets
    if 'W' in sys_dict_samples[sys]['processes']:
        WJ_datasets[sys] = []
        WJ_datasets[sys].append(fetch_dataset('WJetsToLNu_LO',33073306,61526.7,sys=sys, channel=channel, prod_date=prod_date))
        WJ_datasets[sys].append(fetch_dataset('WJetsToLNu_LO_ext',44627200,61526.7,sys=sys, channel=channel, prod_date=prod_date))
        renorm_nevts(WJ_datasets[sys])
    
    # TTbar
    if 'TT' in sys_dict_samples[sys]['processes']:
        TT_datasets[sys] = []
        TT_datasets[sys].append(fetch_dataset('TTHad_pow',41729120,377.96,sys=sys, channel=channel, prod_date=prod_date))
        TT_datasets[sys].append(fetch_dataset('TTLep_pow',9000000,88.29,sys=sys, channel=channel, prod_date=prod_date))
        TT_datasets[sys].append(fetch_dataset('TTSemi_pow',43732445,365.35,sys=sys, channel=channel, prod_date=prod_date))

    # EWK
    if 'EWK' in sys_dict_samples[sys]['processes']:
        EWK_datasets[sys] = []
        EWK_datasets[sys].append(fetch_dataset('WToLNu_M50_Plus2J',4358697,29.59,sys=sys, channel=channel, prod_date=prod_date))
        EWK_datasets[sys].append(fetch_dataset('WToLNu_M50_Minus2J',4385142,23.24,sys=sys, channel=channel, prod_date=prod_date))
        EWK_datasets[sys].append(fetch_dataset('ZToLL_M50',952504,4.321,sys=sys, channel=channel, prod_date=prod_date))
        EWK_datasets[sys].append(fetch_dataset('ZToNuNu',2949960,10.66,sys=sys, channel=channel, prod_date=prod_date))
    
    ##### Single top
    if 'singleTop' in sys_dict_samples[sys]['processes']:
        singleTop_datasets[sys] = []
        singleTop_datasets[sys].append(fetch_dataset('TBar_tch',3652340,80.95,sys=sys, channel=channel, prod_date=prod_date))
        singleTop_datasets[sys].append(fetch_dataset('TBar_tWch',7977430,35.85,sys=sys, channel=channel, prod_date=prod_date))
        singleTop_datasets[sys].append(fetch_dataset('T_tch',5982064,136.02,sys=sys, channel=channel, prod_date=prod_date))
        singleTop_datasets[sys].append(fetch_dataset('T_tWch',7794186,35.85,sys=sys, channel=channel, prod_date=prod_date))
    
    ##### DiBoson inclusive
    if 'Diboson' in sys_dict_samples[sys]['processes']:
        Diboson_datasets[sys] = []
        Diboson_datasets[sys].append(fetch_dataset('ZZTo4L',6964071,1.325,sys=sys, channel=channel, prod_date=prod_date))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo4L_ext',6967853,1.325,sys=sys, channel=channel, prod_date=prod_date))
        renorm_nevts(Diboson_datasets[sys])
        Diboson_datasets[sys].append(fetch_dataset('WW',7791498,75.88,sys=sys, channel=channel, prod_date=prod_date))
        Diboson_datasets[sys].append(fetch_dataset('WZ',3928630,27.57,sys=sys, channel=channel, prod_date=prod_date))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo2L2Nu',8744768,0.6008,sys=sys, channel=channel, prod_date=prod_date))
        Diboson_datasets[sys].append(fetch_dataset('ZZTo2L2Q',27840918,3.688,sys=sys, channel=channel, prod_date=prod_date))
    
    ##### Embedded
    if 'Embedded' in sys_dict_samples[sys]['processes']:
        Embedded_datasets[sys] = []
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017B_{}'.format(channel),sys=sys, channel=channel, prod_date=prod_date))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017C_{}'.format(channel),sys=sys, channel=channel, prod_date=prod_date))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017D_{}'.format(channel),sys=sys, channel=channel, prod_date=prod_date))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017E_{}'.format(channel),sys=sys, channel=channel, prod_date=prod_date))
        Embedded_datasets[sys].append(fetch_dataset('Embedded2017F_{}'.format(channel),sys=sys, channel=channel, prod_date=prod_date))

nevents_dict = {
    'ggH80': 479614,
    'ggH90': 500000,
    'ggH100': 500000,
    'ggH110': 500000,
    'ggH120': 500000,
    'ggH130': 500000,
    'ggH140': 500000,
    'ggH180': 500000,
    'ggH200': 200000,
    'ggH250': 200000,
    'ggH300': 195159,
    'ggH350': 200000,
    'ggH400': 200000,
    'ggH450': 200000,
    'ggH500': 200000,
    'ggH600': 195350,
    'ggH700': 190896,
    'ggH800': 200000,
    'ggH900': 200000,
    'ggH1200': 200000,
    'ggH1400': 200000,
    'ggH1500': 200000,
    'ggH1600': 200000,
    'ggH1800': 200000,
    'ggH2000': 196915,
    'ggH2300': 194106,
    'ggH2600': 200000,
    'ggH2900': 190493,
    'ggH3200': 200000,
    'bbH80': 478796,
    'bbH90': 495914,
    'bbH100': 500000,
    'bbH110': 493035,
    'bbH120': 500000,
    'bbH130': 500000,
    'bbH140': 500000,
    'bbH180': 476584,
    'bbH200': 200000,
    'bbH250': 200000,
    'bbH300': 200000,
    'bbH350': 191582,
    'bbH400': 200000,
    'bbH450': 194897,
    'bbH500': 200000,
    'bbH600': 194825,
    'bbH700': 200000,
    'bbH800': 200000,
    'bbH900': 200000,
    'bbH1200': 200000,
    'bbH1400': 200000,
    'bbH1500': 200000,
    'bbH1600': 200000,
    'bbH1800': 193168,
    'bbH2000': 200000,
    'bbH2300': 200000,
    'bbH2600': 200000,
    'bbH2900': 200000,
    'bbH3200': 200000,
    }

nevents_dict_amcatnlobbH = {
    'bbH80': 2476000,
    'bbH90': 2464000,
    'bbH110': 2220000,
    'bbH120': 2488000,
    'bbH130': 2450000,
    'bbH140': 2374000,
    'bbH180': 2449000,
    'bbH200': 990000,
    'bbH250': 960000,
    'bbH300': 995000,
    'bbH350': 875000,
    'bbH400': 500000,
    'bbH450': 491000,
    'bbH500': 491126,
    'bbH600': 492000,
    'bbH700': 485000,
    'bbH800': 483408,
    'bbH900': 485000,
    'bbH1200': 496000,
    'bbH1400': 500000,
    'bbH1600': 468000,
    'bbH1800': 486000,
    'bbH2000': 476000,
    'bbH2300': 494928,
    'bbH2600': 476000,
    'bbH2900': 500000,
    'bbH3200': 500000
    }

def build_signals(mass_points):
                          
    signal_datasets = {'nominal':{}}

    for mass in mass_points:
        print mass
        signal_datasets['nominal']['ggH{}'.format(mass)] = fetch_dataset('HiggsSUSYGG{}'.format(mass),nevents_dict['ggH{}'.format(mass)],1., channel=channel, prod_date=prod_date)
        signal_datasets['nominal']['bbH{}'.format(mass)] = fetch_dataset('HiggsSUSYBB{}'.format(mass),nevents_dict['bbH{}'.format(mass)],1., channel=channel, prod_date=prod_date)
        # signal_datasets['nominal']['bbH{}'.format(mass)] = fetch_dataset('HiggsSUSYBB{}_amcatnlo'.format(mass),nevents_dict_amcatnlobbH['bbH{}'.format(mass)],1., channel=channel, prod_date=prod_date)

        
    for sys in sys_dict_samples:
        signal_datasets[sys] = {}
        for mass in mass_points:
            if 'signal' in sys_dict_samples[sys]['processes']:
                signal_datasets[sys]['ggH{}'.format(mass)] = fetch_dataset('HiggsSUSYGG{}'.format(mass),nevents_dict['ggH{}'.format(mass)],1.,sys=sys, channel=channel, prod_date=prod_date)
                signal_datasets[sys]['bbH{}'.format(mass)] = fetch_dataset('HiggsSUSYBB{}'.format(mass),nevents_dict['bbH{}'.format(mass)],1.,sys=sys, channel=channel, prod_date=prod_date)
                # signal_datasets[sys]['bbH{}'.format(mass)] = fetch_dataset('HiggsSUSYBB{}_amcatnlo'.format(mass),nevents_dict_amcatnlobbH['bbH{}'.format(mass)],1.,sys=sys, channel=channel, prod_date=prod_date)

    return signal_datasets

## lumi weighting

for ds_type in [singleTop_datasets, WJ_datasets, Diboson_datasets, TT_datasets, DY_datasets, EWK_datasets]:
    for sys, dataset_list in ds_type.iteritems() :
        for dataset in dataset_list:
            dataset.compute_weight(data_lumi)

# for ds_type in [signal_datasets]:
#     for sys, dataset_list in ds_type.iteritems() :
#         for name, dataset in dataset_list.iteritems():
#             dataset.compute_weight(data_lumi)
            
for dataset in data_datasets:
    dataset.compute_weight()
for sys, dataset_list in Embedded_datasets.iteritems():
    for dataset in dataset_list:
        dataset.compute_weight()
