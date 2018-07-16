
import htt_plot.tools.config as config
config.parallel = False

from htt_plot.components.lucas_all import *
from htt_plot.tools.cut import Cut
from htt_plot.cuts.mt import *
from htt_plot.tools.plot import hist, add

from htt_plot.cuts.generic import cuts_generic, cut_os, cut_ss
from htt_plot.cuts.mt import cuts_mt
from htt_plot.cuts.mt_triggers import triggers

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

lumi = 35900.

##############
# 
##############

mc_components = [DYJetsToLL_M10to50_LO, DYJetsToLL_M50_LO_ext, DYJetsToLL_M50_LO_ext2, TT_pow, WJetsToLNu_LO, WJetsToLNu_LO_ext]

for component in mc_components:
    component.compute_weight(lumi)

data_components = [data1, data2, data3, data4]

for component in data_components:
    component.compute_weight()

##############
# Data histo
##############

h_data1 = hist('data1', data1, var, cut, *bins)
h_data2 = hist('data2', data2, var, cut, *bins)
h_data3 = hist('data3', data3, var, cut, *bins)
h_data4 = hist('data4', data4, var, cut, *bins)

all_data = [h_data1, h_data2, h_data3, h_data4]

h_data = add('data', all_data)
h_data.Scale(1)
# h_data.visualize()
if config.parallel:
    print 'running'
    # h_data = h_data.compute(scheduler='single-threaded')
    h_data = h_data.compute()
print h_data.GetEntries()
print h_data.Integral()
#h_data.Draw()

##############
# MC histos
##############

def sumMCweights(components, lumi_data = lumi):
    lumi_eq_tot = 0.
    for component in components:
        lumi_eq_tot += component.nevts/(component.xsection*component.norm_factor)
    return lumi_data/lumi_eq_tot

## DY

h_DY_mlt50   = hist('DY_mlt50', DYJetsToLL_M10to50_LO, var, cut, *bins)
h_DY_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

h_DY_mht50_1 = hist('DY_mht50_1', DYJetsToLL_M50_LO_ext, var, cut, *bins)
h_DY_mht50_2 = hist('DY_mht50_2', DYJetsToLL_M50_LO_ext2, var, cut, *bins)

h_DY_mht50 = add('DY_mht50', [h_DY_mht50_1,h_DY_mht50_2])
h_DY_mht50.Scale(sumMCweights([DYJetsToLL_M50_LO_ext,DYJetsToLL_M50_LO_ext2]))

h_DY = add('DY', [h_DY_mlt50, h_DY_mht50])
print h_DY.GetEntries()
print h_DY.Integral()
#h_DY.Draw()

## TT

h_TT = hist('TT', TT_pow, var, cut, *bins)
h_TT.Scale(TT_pow.weight)

print h_TT.GetEntries()
print h_TT.Integral()
#TT_pow.Draw()

## WJ

h_WJ1 = hist('WJ1', WJetsToLNu_LO, var, cut, *bins)
h_WJ2 = hist('WJ2', WJetsToLNu_LO_ext, var, cut, *bins)

h_WJ = add('WJ', [h_WJ1, h_WJ2])
h_WJ.Scale(sumMCweights([WJetsToLNu_LO,WJetsToLNu_LO_ext]))

print h_WJ.GetEntries()
print h_WJ.Integral()
#h_WJ.Draw()

h_bg = add('bg',[h_DY,h_TT,h_WJ])

##############
# WJ renormalization
##############

