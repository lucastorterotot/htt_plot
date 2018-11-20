
import htt_plot.tools.config as config
config.parallel = True

from htt_plot.datasets.lucas_small import *

from htt_plot.tools.cut import Cut
from htt_plot.cuts.mt import *
from htt_plot.tools.plot import hist, add, scale

from htt_plot.cuts.generic import cuts_generic, cut_os, cut_ss
from htt_plot.cuts.mt import cuts_mt
from htt_plot.cuts.mt_triggers import triggers

from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=True)


import copy

cuts = cuts_generic + cuts_mt + triggers
var = 'mt_total'
cuts_os = copy.copy(cuts)
cuts_os['os'] = cut_os
cut = str(cuts_os)

weight='weight'

# adding weight
cut = '({cut})*({weight})'.format(cut=cut,weight=weight)

bins = 50, 0., 500.

lumi = 35900. * nevents_fraction

##############
# 
##############

mc_datasets = [DYJetsToLL_M10to50_LO, DYJetsToLL_M50_LO_ext, DYJetsToLL_M50_LO_ext2, TT_pow, WJetsToLNu_LO, WJetsToLNu_LO_ext]

for dataset in mc_datasets:
    dataset.compute_weight(lumi)

data_datasets = [data1, data2, data3, data4]

for dataset in data_datasets:
    dataset.compute_weight()

##############
# Data histo
##############

data1 = hist('data1', data1, var, cut, *bins)
data2 = hist('data2', data2, var, cut, *bins)
data3 = hist('data3', data3, var, cut, *bins)
data4 = hist('data4', data4, var, cut, *bins)

all_data = [data1, data2, data3, data4]
data = add('data', all_data)
if config.parallel:
    print 'running'
    # h_data = h_data.compute(scheduler='single-threaded')
    data = data.compute()
print data.GetEntries()
print data.Integral()
#data.Scale(1/nevents_fraction)
#h_data.Draw()

##############
# MC histos
##############
##

## DY

##DY_mlt50   = hist('DY_mlt50', DYJetsToLL_M10to50_LO, var, cut, *bins)
##DY_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

DY_mht50_1 = hist('DY_mht50_1', DYJetsToLL_M50_LO_ext, var, cut, *bins)
DY_mht50_2 = hist('DY_mht50_2', DYJetsToLL_M50_LO_ext2, var, cut, *bins)
DY = add('DY', [DY_mht50_1,DY_mht50_2])
lumi_eq = DYJetsToLL_M50_LO_ext.lumi_eq() + DYJetsToLL_M50_LO_ext2.lumi_eq()
print 'INTEGRAL BEFORE SCALE', DY.Integral()
DY = scale(DY, lumi/lumi_eq)
if config.parallel:
    DY = DY.compute()
print 'LUMI', lumi, lumi_eq,  DYJetsToLL_M50_LO_ext.lumi_eq(),  DYJetsToLL_M50_LO_ext2.lumi_eq()
##DY_mht50.Scale(sumMCweights([DYJetsToLL_M50_LO_ext,DYJetsToLL_M50_LO_ext2]))
print DY.GetEntries()
print DY.Integral()
#h_DY.Draw()

## TT
##
##TT = hist('TT', TT_pow, var, cut, *bins)
##TT.Scale(TT_pow.weight)
##
##print TT.GetEntries()
##print TT.Integral()
###TT_pow.Draw()
##
#### WJ
##
##WJ1 = hist('WJ1', WJetsToLNu_LO, var, cut, *bins)
##WJ2 = hist('WJ2', WJetsToLNu_LO_ext, var, cut, *bins)
##
##WJ = add('WJ', [WJ1, WJ2])
##WJ.Scale(sumMCweights([WJetsToLNu_LO,WJetsToLNu_LO_ext]))
##
##print WJ.GetEntries()
##print WJ.Integral()
##
##background = add('background',[DY,TT,WJ])
##if config.parallel:
##    DY = DY.compute()
##    TT = TT.compute()
##    WJ = WJ.compute()
##    background = background.compute()

data.stack = False
plotter = Plotter([data, DY], lumi)
plotter.draw(var, 'a.u.')

print plotter.plot
