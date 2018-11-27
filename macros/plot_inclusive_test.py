from dask import delayed
import htt_plot.tools.config as config
config.parallel = True

from htt_plot.datasets.gael_all import *

from htt_plot.tools.cut import Cut
from htt_plot.cuts.mt import *
from htt_plot.tools.plot import hist, add, scale

from htt_plot.cuts.generic import cuts_generic, cut_os, cut_ss
from htt_plot.cuts.mt import cuts_mt
from htt_plot.cuts.tt_triggers import triggers

from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=True)


import copy

cuts = cuts_generic + triggers
var = 'mt_tot'
cuts_os = copy.copy(cuts)
cuts_os['os'] = cut_os
cut = str(cuts_os)

weight='weight'

# adding weight
cut = '({cut})*({weight})'.format(cut=cut,weight=weight)

bins = 50, 0., 500.

lumi = 44980. * nevents_fraction

##############
# 
##############

mc_datasets = [DYJetsToLL_M50,WJetsToLNu_LO,TTHad_pow,TTLep_pow,TTSemi_pow,]

for dataset in mc_datasets:
    dataset.compute_weight(lumi)

data_datasets = [dataB, dataC, dataD, dataE, dataF]

for dataset in data_datasets:
    dataset.compute_weight()

##############
# Data histo
##############

dataB = hist('dataB', dataB, var, cut, *bins)
dataC = hist('dataC', dataC, var, cut, *bins)
dataD = hist('dataD', dataD, var, cut, *bins)
dataE = hist('dataE', dataE, var, cut, *bins)
dataF = hist('dataF', dataF, var, cut, *bins)

all_data = [dataB, dataC, dataD, dataE, dataF]
data = add('data', all_data)
if config.parallel:
    print 'running'
    data = data.compute()
print data.GetEntries()
print data.Integral()

##############
# MC histos
##############

## DY

DY = hist('DY', DYJetsToLL_M50, var, cut, *bins)
WJ = hist('WJ', WJetsToLNu_LO, var, cut, *bins)
TTHad = hist('TTHad', TTHad_pow, var, cut, *bins)
TTLep = hist('TTLep', TTLep_pow, var, cut, *bins)
TTSemi = hist('TTSemi', TTSemi_pow, var, cut, *bins)

if config.parallel:
    DY = DY.compute()
    WJ = WJ.compute()
    TTHad = TTHad.compute()
    TTLep = TTLep.compute()
    TTSemi = TTSemi.compute()
# DY.scale(lumi/lumi_eq)
# DY = scale(DY, lumi/DYJetsToLL_M50.lumi_eq())
# WJ = scale(WJ, lumi/WJetsToLNu_LO.lumi_eq())
# TTHad = scale(TTHad, lumi/TTHad_pow.lumi_eq())
# TTLep = scale(TTLep, lumi/TTLep_pow.lumi_eq())
# TTSemi = scale(TTSemi, lumi/TTSemi_pow.lumi_eq())

data.stack = False
plotter = Plotter([data, DY, WJ, TTHad, TTLep, TTSemi], lumi)
plotter.draw(var, 'a.u.')

print plotter.plot
