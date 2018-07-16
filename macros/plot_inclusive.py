
import htt_plot.tools.config as config
<<<<<<< HEAD
config.parallel = False # True
=======
config.parallel = False
>>>>>>> colin/master

from htt_plot.components.lucas_small import *
from htt_plot.tools.cut import Cut
from htt_plot.components.cuts_mutau import *
from htt_plot.tools.plot import hist, add

from htt_plot.cuts.generic import cuts_generic
from htt_plot.cuts.mt import cuts_mt

cuts = cuts_generic + cuts_mt
var = 'mt_total'
<<<<<<< HEAD
cut = cut_plot_mutau
=======
cut = str(cuts)
>>>>>>> colin/master
bins = 50, 0., 500.

lumi = 35900.

##############
# 
##############

mc_components = [DYJetsToLL_M10to50_LO, DYJetsToLL_M50_LO_ext, DYJetsToLL_M50_LO_ext2, TT_pow, WJetsToLNu_LO, WJetsToLNu_LO_ext]

##############
# Data histo
##############

h_data1 = hist('data1', data1, var, cut, *bins)
h_data2 = hist('data2', data2, var, cut, *bins)
h_data3 = hist('data3', data3, var, cut, *bins)
h_data4 = hist('data4', data4, var, cut, *bins)

all_data = [h_data1, h_data2, h_data3, h_data4]

h_data = add('data', all_data)
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

## DY

h_DY_mlt50   = hist('DY_mlt50', DYJetsToLL_M10to50_LO, var, cut, *bins)
h_DY_mht50_1 = hist('DY_mht50_1', DYJetsToLL_M50_LO_ext, var, cut, *bins)
h_DY_mht50_2 = hist('DY_mht50_2', DYJetsToLL_M50_LO_ext2, var, cut, *bins)
h_DY_mht50 = add('DY_mht50', [h_DY_mht50_1,h_DY_mht50_2])

all_DY = [h_DY_mlt50, h_DY_mht50]
h_DY_mlt50.Scale(lumi/DYJetsToLL_M10to50_LO.lumi_eq)
h_DY_mht50.Scale(lumi/(DYJetsToLL_M50_LO_ext.lumi_eq+DYJetsToLL_M50_LO_ext2.lumi_eq))

h_DY = add('DY', all_DY)
print h_DY.GetEntries()
print h_DY.Integral()
#h_DY.Draw()

## TT

h_TT = hist('TT', TT_pow, var, cut, *bins)

all_TT = [h_TT]
h_TT.Scale(lumi/TT_pow.lumi_eq)

h_TT = add('TT', all_TT)
print h_TT.GetEntries()
print h_TT.Integral()
#TT_pow.Draw()

## WJ

h_WJ1 = hist('WJ1', WJetsToLNu_LO, var, cut, *bins)
h_WJ2 = hist('WJ2', WJetsToLNu_LO_ext, var, cut, *bins)
h_WJ = add('WJ', [h_WJ1, h_WJ2])

all_WJ = [h_WJ]
h_WJ.Scale(lumi/(WJetsToLNu_LO.lumi_eq+WJetsToLNu_LO_ext.lumi_eq))

h_WJ = add('WJ', all_WJ)
print h_WJ.GetEntries()
print h_WJ.Integral()
#h_WJ.Draw()

h_bg = add('bg',all_DY+all_TT+all_WJ)

##############
# WJ renormalization
##############

cut_total_high_mt = cut_high_mt & cut
