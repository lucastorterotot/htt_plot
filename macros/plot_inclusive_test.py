from dask import delayed
import htt_plot.tools.config as config
config.parallel = False

from ROOT import TCanvas

from htt_plot.datasets.gael_all import *

from htt_plot.tools.cut import Cut
from htt_plot.cuts.mt import *
from htt_plot.tools.plot import build_component, build_components, merge_components, scale_component

from htt_plot.cuts.generic import signal_region, signal_region_MC, signal_region_MC_nofakes, l1_FakeFactorApplication_Region, l2_FakeFactorApplication_Region
from htt_plot.cuts.mt import cuts_mt
from htt_plot.cuts.tt_triggers import triggers

from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=True)


import copy

var='mt_tot'
weight='weight'
signal_region = '({cut})*({weight})'.format(cut=str(signal_region),weight=weight)
signal_region_MC = '({cut})*({weight})'.format(cut=str(signal_region_MC),weight=weight)
signal_region_MC_nofakes = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes),weight=weight)
l1_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region),weight='weight*l1_fakeweight*0.5')
l2_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region),weight='weight*l2_fakeweight*0.5')


# adding weight
bins = 50, 0., 500.

lumi = 44980. * nevents_fraction

##############
# 
##############

mc_datasets = [DYJetsToLL_M50,WJetsToLNu_LO,TTHad_pow,TTLep_pow,TTSemi_pow]

for dataset in mc_datasets:
    dataset.compute_weight(lumi)

data_datasets = [dataB, dataC, dataD, dataE, dataF]

for dataset in data_datasets:
    dataset.compute_weight()


all_fakes = [fakedataB, fakedataC, fakedataD, fakedataE, fakedataF]
for dataset in all_fakes:
    dataset.compute_weight()

##############
# Data histo
##############

#dataB = build_component('dataB', dataB, var, cut, *bins)
#dataC = build_component('dataC', dataC, var, cut, *bins)
#dataD = build_component('dataD', dataD, var, cut, *bins)
#dataE = build_component('dataE', dataE, var, cut, *bins)
#dataF = build_component('dataF', dataF, var, cut, *bins)


#data = merge_components('data', all_data)

#data = build_component('data', all_data, var, cut, *bins)
#print data.GetEntries()
#print data.Integral()

##############
# MC histos
##############

## DY
fake_components_1 = build_components(['fakes1'], 
                                     [all_fakes],
                                     var, l1_FakeFactorApplication_Region, *bins)
fake_components_2 = build_components(['fakes2'], 
                                     [all_fakes],
                                     var, l2_FakeFactorApplication_Region, *bins)

MC_components = build_components(['DY','WJ','TTHad','TTLep','TTSemi'], 
                              [DYJetsToLL_M50,WJetsToLNu_LO,TTHad_pow,TTLep_pow,TTSemi_pow],
                              var, signal_region_MC, *bins)#signal_region_MC_nofakes

data_components = build_components(['data'],[data_datasets],var,signal_region,*bins)

data_components[0].stack = False
plotter = Plotter(MC_components+data_components, lumi)#+fake_components_1+fake_components_2
plotter.draw(var, 'a.u.')
print plotter.plot
