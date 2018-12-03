from htt_plot.tools.dataset import Dataset

import os 

basedir = os.path.expandvars('/data2/gtouquet/MSSM_Samples_201118/')

treename = 'events'

nevents_fraction = 1.

DYJetsToLL_M50 = Dataset(
    'DYJetsToLL_M50',
    basedir+'DYJetsToLL_M50/NtupleProducer/tree.root',
    48675378*nevents_fraction, 6225.42,
    treename = treename
)


WJetsToLNu_LO = Dataset(
    'WJetsToLNu',
    basedir+'WJetsToLNu_LO/NtupleProducer/tree.root',
    33073306*nevents_fraction, 61526.7,
    treename = treename
)

TTHad_pow = Dataset(
    'TTHad_pow',
    basedir+'TTHad_pow/NtupleProducer/tree.root',
    41729120*nevents_fraction, 377.96,
    treename = treename
)
TTLep_pow = Dataset(
    'TTLep_pow',
    basedir+'TTLep_pow/NtupleProducer/tree.root',
    9000000*nevents_fraction, 88.29,
    treename = treename
)
TTSemi_pow = Dataset(
    'TTSemi_pow',
    basedir+'TTSemi_pow/NtupleProducer/tree.root',
    43732445*nevents_fraction, 365.35,
    treename = treename
)

#data

dataB = Dataset(
    'dataB',
    basedir+'Tau_Run2017B_31Mar2018/NtupleProducer/tree.root',
    norm_factor = 1.,
    treename = treename
)
dataC = Dataset(
    'dataC',
    basedir+'Tau_Run2017C_31Mar2018/NtupleProducer/tree.root',
    norm_factor = 1.,
    treename = treename
)
dataD = Dataset(
    'dataD',
    basedir+'Tau_Run2017D_31Mar2018/NtupleProducer/tree.root',
    norm_factor = 1.,
    treename = treename
)
dataE = Dataset(
    'dataE',
    basedir+'Tau_Run2017E_31Mar2018/NtupleProducer/tree.root',
    norm_factor = 1.,
    treename = treename
)
dataF = Dataset(
    'dataF',
    basedir+'Tau_Run2017F_31Mar2018/NtupleProducer/tree.root',
    norm_factor = 1.,
    treename = treename
)

#fakefactored data

fakedataB = Dataset(
    'fakedataB',
    basedir+'Tau_Run2017B_31Mar2018/NtupleProducer/tree_fakesB.root',
    norm_factor = 1.,
    treename = treename
)
fakedataC = Dataset(
    'fakedataC',
    basedir+'Tau_Run2017C_31Mar2018/NtupleProducer/tree_fakesC.root',
    norm_factor = 1.,
    treename = treename
)
fakedataD = Dataset(
    'fakedataD',
    basedir+'Tau_Run2017D_31Mar2018/NtupleProducer/tree_fakesD.root',
    norm_factor = 1.,
    treename = treename
)
fakedataE = Dataset(
    'fakedataE',
    basedir+'Tau_Run2017E_31Mar2018/NtupleProducer/tree_fakesE.root',
    norm_factor = 1.,
    treename = treename
)
fakedataF = Dataset(
    'fakedataF',
    basedir+'Tau_Run2017F_31Mar2018/NtupleProducer/tree_fakesF.root',
    norm_factor = 1.,
    treename = treename
)
