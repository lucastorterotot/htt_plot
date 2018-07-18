
import htt_plot.tools.config as config
config.parallel = False

from htt_plot.datasets.lucas_all import *

from htt_plot.tools.cut import Cut
from htt_plot.tools.plot import hist, add

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

weight='weight*weight_dy'

# adding weight
cut = '({cut})*({weight})'.format(cut=cut,weight=weight)

bins = 50, 0., 500.

lumi = 35900.

##############
# Declaring datasets to weight
##############

mc_datasets = [
    DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_LO_ext,
    DYJetsToLL_M50_LO_ext2,
    TT_pow,
    WJetsToLNu_LO,
    WJetsToLNu_LO_ext,
]

for dataset in mc_datasets:
    dataset.compute_weight(lumi)

data_datasets = [data1, data2, data3, data4]

for dataset in data_datasets:
    dataset.compute_weight()

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

def sumMCweights(datasets, lumi_data = lumi):
    lumi_eq_tot = 0.
    for dataset in datasets:
        lumi_eq_tot += dataset.nevts/(dataset.xsection*dataset.norm_factor)
    return lumi_data/lumi_eq_tot

## DY

h_DY_mlt50   = hist('DY_mlt50', DYJetsToLL_M10to50_LO, var, cut, *bins)
h_DY_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

#h_DY_mht50_1 = hist('DY_mht50_1', DYJetsToLL_M50_LO_ext, var, cut, *bins)
#h_DY_mht50_2 = hist('DY_mht50_2', DYJetsToLL_M50_LO_ext2, var, cut, *bins)

#h_DY_mht50 = add('DY_mht50', [h_DY_mht50_1,h_DY_mht50_2])
#h_DY_mht50.Scale(sumMCweights([DYJetsToLL_M50_LO_ext,DYJetsToLL_M50_LO_ext2]))

h_DY_mht50 = hist('DY_mht50', DYJetsToLL_M50_LO_ext, var, cut, *bins)
h_DY_mht50.Scale(DYJetsToLL_M50_LO_ext.weight)

h_DY = add('DY', [h_DY_mlt50, h_DY_mht50])
if config.parallel:
    h_DY = h_DY.compute()
print h_DY.GetEntries()
print h_DY.Integral()
#h_DY.Draw()

## TT

h_TT = hist('TT', TT_pow, var, cut, *bins)
h_TT.Scale(TT_pow.weight)
if config.parallel:
    h_TT = h_TT.compute()
print h_TT.GetEntries()
print h_TT.Integral()
#TT_pow.Draw()

## WJ

# h_WJ1 = hist('WJ1', WJetsToLNu_LO, var, cut, *bins)
# h_WJ2 = hist('WJ2', WJetsToLNu_LO_ext, var, cut, *bins)

# h_WJ = add('WJ', [h_WJ1, h_WJ2])
# h_WJ.Scale(sumMCweights([WJetsToLNu_LO,WJetsToLNu_LO_ext]))
h_WJ = hist('WJ', WJetsToLNu_LO_ext, var, cut, *bins)
h_WJ.Scale(WJetsToLNu_LO_ext.weight)
if config.parallel:
    h_WJ = h_WJ.compute()
print h_WJ.GetEntries()
print h_WJ.Integral()
#h_WJ.Draw()

##############
# WJ renormalization
##############

auto_WJ_SF = False

var_WJ_SF = 'mt'

cuts_WJ_SF = copy.copy(cuts)
cuts_WJ_SF['low_mt'] = 'mt>70'
cuts_WJ_SF['os'] = cut_os

cut_WJ_SF = str(cuts_WJ_SF)
cut_WJ_SF = '({cut})*({weight})'.format(cut=cut_WJ_SF,weight=weight)

h_data1_WJ_SF = hist('data1_WJ_SF', data1, var_WJ_SF, cut_WJ_SF, *bins)
h_data2_WJ_SF = hist('data2_WJ_SF', data2, var_WJ_SF, cut_WJ_SF, *bins)
h_data3_WJ_SF = hist('data3_WJ_SF', data3, var_WJ_SF, cut_WJ_SF, *bins)
h_data4_WJ_SF = hist('data4_WJ_SF', data4, var_WJ_SF, cut_WJ_SF, *bins)

all_data_WJ_SF = [h_data1_WJ_SF, h_data2_WJ_SF, h_data3_WJ_SF, h_data4_WJ_SF]

h_data_WJ_SF = add('data_WJ_SF', all_data_WJ_SF)
h_data_WJ_SF.Scale(1)

h_DY_mlt50_WJ_SF   = hist('DY_mlt50_WJ_SF', DYJetsToLL_M10to50_LO, var_WJ_SF, cut_WJ_SF, *bins)
h_DY_mlt50_WJ_SF.Scale(DYJetsToLL_M10to50_LO.weight)

h_DY_mht50_WJ_SF = hist('DY_mht50_WJ_SF', DYJetsToLL_M50_LO_ext, var_WJ_SF, cut_WJ_SF, *bins)
h_DY_mht50_WJ_SF.Scale(DYJetsToLL_M50_LO_ext.weight)

h_DY_WJ_SF = add('DY_WJ_SF', [h_DY_mlt50_WJ_SF, h_DY_mht50_WJ_SF])

h_TT_WJ_SF = hist('TT_WJ_SF', TT_pow, var_WJ_SF, cut_WJ_SF, *bins)
h_TT_WJ_SF.Scale(TT_pow.weight)

h_WJ_SF = hist('WJ_SF', WJetsToLNu_LO_ext, var_WJ_SF, cut_WJ_SF, *bins)
h_WJ_SF.Scale(WJetsToLNu_LO_ext.weight)

h_DY_WJ_SF.Scale(-1)
h_TT_WJ_SF.Scale(-1)
h_ref_WJ_SF = add('ref_WJ_SF', [h_data_WJ_SF,h_DY_WJ_SF,h_TT_WJ_SF])
    
if auto_WJ_SF:
    ratio_WJ_SF = h_ref_WJ_SF.histogram.Integral()/h_WJ_SF.histogram.Integral()
else:
    ratio_WJ_SF = 0.347231800378 # 0.469080403348 # .5

print 'ratio_WJ_SF = ', ratio_WJ_SF
h_WJ.Scale(ratio_WJ_SF)

##############
# QCD estimation
##############

auto_QCD = False

var_QCD = 'mt_total'

cuts_QCD_B = copy.copy(cuts)
cuts_QCD_C = copy.copy(cuts)
cuts_QCD_D = copy.copy(cuts)

cuts_QCD_B['sign'] = cut_ss
cuts_QCD_C['sign'] = cut_os
cuts_QCD_D['sign'] = cut_ss

cuts_QCD_B['tau_iso'] = 'l2_byTightIsolationMVArun2v1DBoldDMwLT > 0.5'
cuts_QCD_C['tau_iso'] = '!('+cuts_QCD_B['tau_iso']+')'
cuts_QCD_D['tau_iso'] = cuts_QCD_C['tau_iso']

cut_QCD_B = str(cuts_QCD_B)
cut_QCD_B = '({cut})*({weight})'.format(cut=cut_QCD_B,weight=weight)
cut_QCD_C = str(cuts_QCD_C)
cut_QCD_C = '({cut})*({weight})'.format(cut=cut_QCD_C,weight=weight)
cut_QCD_D = str(cuts_QCD_D)
cut_QCD_D = '({cut})*({weight})'.format(cut=cut_QCD_D,weight=weight)


h_data1_QCD_B = hist('data1_B', data1, var_QCD, cut_QCD_B, *bins)
h_data2_QCD_B = hist('data2_B', data2, var_QCD, cut_QCD_B, *bins)
h_data3_QCD_B = hist('data3_B', data3, var_QCD, cut_QCD_B, *bins)
h_data4_QCD_B = hist('data4_B', data4, var_QCD, cut_QCD_B, *bins)

all_data_QCD_B = [h_data1_QCD_B, h_data2_QCD_B, h_data3_QCD_B, h_data4_QCD_B]

h_data_QCD_B = add('data_QCD_B', all_data_QCD_B)
h_data_QCD_B.Scale(1)


h_DY_mlt50_QCD_B   = hist('DY_mlt50_QCD_B', DYJetsToLL_M10to50_LO, var_QCD, cut_QCD_B, *bins)
h_DY_mlt50_QCD_B.Scale(DYJetsToLL_M10to50_LO.weight)
    
h_DY_mht50_QCD_B = hist('DY_mht50_QCD_B', DYJetsToLL_M50_LO_ext, var_QCD, cut_QCD_B, *bins)
h_DY_mht50_QCD_B.Scale(DYJetsToLL_M50_LO_ext.weight)
    
h_DY_QCD_B = add('DY_QCD_B', [h_DY_mlt50_QCD_B, h_DY_mht50_QCD_B])

h_TT_QCD_B = hist('TT_QCD_B', TT_pow, var_QCD, cut_QCD_B, *bins)
h_TT_QCD_B.Scale(TT_pow.weight)

h_WJ_QCD_B = hist('WJ_QCD_B', WJetsToLNu_LO_ext, var_QCD, cut_QCD_B, *bins)
h_WJ_QCD_B.Scale(WJetsToLNu_LO_ext.weight*ratio_WJ_SF)

h_DY_QCD_B.Scale(-1)
h_TT_QCD_B.Scale(-1)
h_WJ_QCD_B.Scale(-1)

h_QCD = add('QCD', [h_data_QCD_B,h_DY_QCD_B,h_TT_QCD_B])

if auto_QCD:
    h_data1_QCD_C = hist('data1_C', data1, var_QCD, cut_QCD_C, *bins)
    h_data2_QCD_C = hist('data2_C', data2, var_QCD, cut_QCD_C, *bins)
    h_data3_QCD_C = hist('data3_C', data3, var_QCD, cut_QCD_C, *bins)
    h_data4_QCD_C = hist('data4_C', data4, var_QCD, cut_QCD_C, *bins)
    
    all_data_QCD_C = [h_data1_QCD_C, h_data2_QCD_C, h_data3_QCD_C, h_data4_QCD_C]
    
    h_data_QCD_C = add('data_QCD_C', all_data_QCD_C)
    h_data_QCD_C.Scale(1)
    
    h_data1_QCD_D = hist('data1_D', data1, var_QCD, cut_QCD_D, *bins)
    h_data2_QCD_D = hist('data2_D', data2, var_QCD, cut_QCD_D, *bins)
    h_data3_QCD_D = hist('data3_D', data3, var_QCD, cut_QCD_D, *bins)
    h_data4_QCD_D = hist('data4_D', data4, var_QCD, cut_QCD_D, *bins)
    
    all_data_QCD_D = [h_data1_QCD_D, h_data2_QCD_D, h_data3_QCD_D, h_data4_QCD_D]
    
    h_data_QCD_D = add('data_QCD_D', all_data_QCD_D)
    h_data_QCD_D.Scale(1)
    
    
    h_DY_mlt50_QCD_C   = hist('DY_mlt50_QCD_C', DYJetsToLL_M10to50_LO, var_QCD, cut_QCD_C, *bins)
    h_DY_mlt50_QCD_C.Scale(DYJetsToLL_M10to50_LO.weight)
    
    h_DY_mht50_QCD_C = hist('DY_mht50_QCD_C', DYJetsToLL_M50_LO_ext, var_QCD, cut_QCD_C, *bins)
    h_DY_mht50_QCD_C.Scale(DYJetsToLL_M50_LO_ext.weight)
    
    h_DY_QCD_C = add('DY_QCD_C', [h_DY_mlt50_QCD_C, h_DY_mht50_QCD_C])
    
    h_TT_QCD_C = hist('TT_QCD_C', TT_pow, var_QCD, cut_QCD_C, *bins)
    h_TT_QCD_C.Scale(TT_pow.weight)
    
    h_WJ_QCD_C = hist('WJ_QCD_C', WJetsToLNu_LO_ext, var_QCD, cut_QCD_C, *bins)
    h_WJ_QCD_C.Scale(WJetsToLNu_LO_ext.weight*ratio_WJ_SF)
    
    h_DY_QCD_C.Scale(-1)
    h_TT_QCD_C.Scale(-1)
    h_WJ_QCD_C.Scale(-1)
    
    h_ref_QCD_C = add('ref_QCD_C', [h_data_QCD_C,h_DY_QCD_C,h_TT_QCD_C])
    
    
    h_DY_mlt50_QCD_D   = hist('DY_mlt50_QCD_D', DYJetsToLL_M10to50_LO, var_QCD, cut_QCD_D, *bins)
    h_DY_mlt50_QCD_D.Scale(DYJetsToLL_M10to50_LO.weight)
    
    h_DY_mht50_QCD_D = hist('DY_mht50_QCD_D', DYJetsToLL_M50_LO_ext, var_QCD, cut_QCD_D, *bins)
    h_DY_mht50_QCD_D.Scale(DYJetsToLL_M50_LO_ext.weight)
    
    h_DY_QCD_D = add('DY_QCD_D', [h_DY_mlt50_QCD_D, h_DY_mht50_QCD_D])
    
    h_TT_QCD_D = hist('TT_QCD_D', TT_pow, var_QCD, cut_QCD_D, *bins)
    h_TT_QCD_D.Scale(TT_pow.weight)
    
    h_WJ_QCD_D = hist('WJ_QCD_D', WJetsToLNu_LO_ext, var_QCD, cut_QCD_D, *bins)
    h_WJ_QCD_D.Scale(WJetsToLNu_LO_ext.weight*ratio_WJ_SF)
    
    h_DY_QCD_D.Scale(-1)
    h_TT_QCD_D.Scale(-1)
    h_WJ_QCD_D.Scale(-1)
    
    h_ref_QCD_D = add('ref_QCD_D', [h_data_QCD_D,h_DY_QCD_D,h_TT_QCD_D])
    
    ratio_QCD = h_ref_QCD_C.histogram.Integral()/h_ref_QCD_D.histogram.Integral()
else:
    ratio_QCD = 1.06 # Twiki
    # ratio_QCD = 1.36950307892 # computed
    
print 'ratio_QCD C/D = ', ratio_QCD

h_QCD.Scale(ratio_QCD)
if config.parallel:
    h_QCD = h_QCD.compute()

    
h_bg = add('bg',[h_DY,h_TT,h_WJ,h_QCD])
h_DYTT = add('dytt',[h_DY,h_TT])

##############
# Categories
##############

from htt_plot.cuts.generic import cut_dy_ztt, cut_dy_zl, cut_dy_zj

# Z tt

cuts_ztt = copy.copy(cuts)
cuts_ztt['DY_cat'] = cut_dy_ztt.cutstr
cuts_ztt['os'] = cut_os

cut_ztt = str(cuts_ztt)
cut_ztt = '({cut})*({weight})'.format(cut=cut_ztt,weight=weight)

h_Ztt_mlt50   = hist('Ztt_mlt50', DYJetsToLL_M10to50_LO, var, cut_ztt, *bins)
h_Ztt_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

h_Ztt_mht50 = hist('Ztt_mht50', DYJetsToLL_M50_LO_ext, var, cut_ztt, *bins)
h_Ztt_mht50.Scale(DYJetsToLL_M50_LO_ext.weight)

h_Ztt = add('Ztt', [h_Ztt_mlt50, h_Ztt_mht50])
if config.parallel:
    h_Ztt = h_Ztt.compute()
print h_Ztt.GetEntries()
print h_Ztt.Integral()

# Z ll

cut_zll = '('+cut+') && ('+cut_dy_zl.cutstr+')'

h_Zll_mlt50   = hist('Zll_mlt50', DYJetsToLL_M10to50_LO, var, cut_zll, *bins)
h_Zll_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

h_Zll_mht50 = hist('Zll_mht50', DYJetsToLL_M50_LO_ext, var, cut_zll, *bins)
h_Zll_mht50.Scale(DYJetsToLL_M50_LO_ext.weight)

h_Zll = add('Zll', [h_Zll_mlt50, h_Zll_mht50])
if config.parallel:
    h_Zll = h_Zll.compute()
print h_Zll.GetEntries()
print h_Zll.Integral()

# Z j

cut_zj = '('+cut+') && ('+cut_dy_zj.cutstr+')'

h_Zj_mlt50   = hist('Zj_mlt50', DYJetsToLL_M10to50_LO, var, cut_zj, *bins)
h_Zj_mlt50.Scale(DYJetsToLL_M10to50_LO.weight)

h_Zj_mht50 = hist('Zj_mht50', DYJetsToLL_M50_LO_ext, var, cut_zj, *bins)
h_Zj_mht50.Scale(DYJetsToLL_M50_LO_ext.weight)

h_Zj = add('Zj', [h_Zj_mlt50, h_Zj_mht50])
if config.parallel:
    h_Zj = h_Zj.compute()
print h_Zj.GetEntries()
print h_Zj.Integral()

h_Jtf = add('Jtf',[h_QCD,h_Zj])

##############
# Print plots
##############

lumi_in_barn = lumi*1e12

from ROOT import gPad

h_data.stack = False
plotter = Plotter([h_data, h_DY, h_WJ, h_TT, h_QCD], lumi_in_barn)
#plotter = Plotter([h_data, h_Ztt, h_Zll, h_WJ, h_TT, h_Jtf], lumi_in_barn)
plotter.draw('m_{T}^{total}', 'Nevts')
plotter.print_info('CMS',xmin=.175, ymin=.8)

gPad.SaveAs("plot_inclusive.png")
