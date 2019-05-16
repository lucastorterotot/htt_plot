from dask import delayed

from ROOT import TCanvas

from htt_plot.datasets.gael_all import *

from htt_plot.tools.cut import Cut
from htt_plot.cuts.mt import *
from htt_plot.tools.plot import build_component, build_components, merge_components, scale_component

from htt_plot.cuts.generic import signal_region as signal_region_cutflow
from htt_plot.cuts.generic import *
from htt_plot.cuts.mt import cuts_mt
from htt_plot.cuts.tt_triggers import triggers

from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)


verbose=True

import copy

output_dir = 'plots_1912'
variables = ['l1_eta', 'l1_pt','l2_eta','l2_pt','met','m_vis','mt_tot']
weight='weight'
weight_MC = 'weight*l1_weight_mutotaufake_loose*l1_weight_etotaufake_vloose*l1_weight_tauid_vtight*l2_weight_mutotaufake_loose*l2_weight_etotaufake_vloose*l2_weight_tauid_vtight'
weight_MC_DY = 'weight*l1_weight_mutotaufake_loose*l1_weight_etotaufake_vloose*l1_weight_tauid_vtight*l2_weight_mutotaufake_loose*l2_weight_etotaufake_vloose*l2_weight_tauid_vtight*weight_dy*weight_generator'#*'+dy_stitching_weight
signal_region = '({cut})*({weight})'.format(cut=str(signal_region_cutflow),weight=weight)
signal_region_Embedded = '({cut})*({weight})'.format(cut=str(signal_region_cutflow),weight='weight*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')#
print 'signal region:', signal_region
signal_region_MC = '({cut})*({weight})'.format(cut=str(signal_region_MC),weight=weight_MC)
signal_region_MC_nofakes_DY = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_DY),weight=weight_MC_DY)
signal_region_MC_nofakes_TT = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_TT),weight=weight_MC)
signal_region_MC_nofakes = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes),weight=weight_MC)
l1_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region),weight='l1_fakeweight*0.5')
print 'l1 ASR:',l1_FakeFactorApplication_Region
l2_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region),weight='l2_fakeweight*0.5')
print 'l2 ASR:',l2_FakeFactorApplication_Region
l1_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l2_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l1_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5')
l2_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5')


# adding weight
from htt_plot.binning import bins
lumi = 41529

##############
# 
##############

mc_datasets = [WJetsToLNu,WJetsToLNu_ext,
               WW,WZ,
               ZZTo4L,ZZTo4L_ext,ZZTo2L2Nu,ZZTo2L2Q,
               TBar_tch,TBar_tWch,T_tch,T_tWch]

for dataset in mc_datasets:
    dataset.compute_weight(lumi)


TT_datasets = [TTHad_pow,TTLep_pow,TTSemi_pow]

for dataset in TT_datasets:
    dataset.compute_weight(lumi)

stitched_datasets = [DYJetsToLL_M50,DYJetsToLL_M50_ext,
                     DY1JetsToLL_M50,DY1JetsToLL_M50_ext,
                     DY2JetsToLL_M50,DY2JetsToLL_M50_ext,
                     DY3JetsToLL_M50,DY3JetsToLL_M50_ext,
                     DY4JetsToLL_M50]


for dataset in stitched_datasets:
    dataset.compute_weight(stitched=True)
    
data_datasets = [dataB, dataC, dataD, dataE, dataF]

for dataset in data_datasets:
    dataset.compute_weight()


Embedded_datasets = [EmbeddedB, EmbeddedC, EmbeddedD, EmbeddedE, EmbeddedF]

for dataset in Embedded_datasets:
    dataset.compute_weight()


# all_fakes = [fakedataB, fakedataC, fakedataD, fakedataE, fakedataF]
# for dataset in all_fakes:
#     dataset.compute_weight()

##############
# Data histo
##############

#dataB = build_component('dataB', dataB, var, cut, bins)
#dataC = build_component('dataC', dataC, var, cut, bins)
#dataD = build_component('dataD', dataD, var, cut, bins)
#dataE = build_component('dataE', dataE, var, cut, bins)
#dataF = build_component('dataF', dataF, var, cut, bins)


#data = merge_components('data', all_data)

#data = build_component('data', all_data, var, cut, bins)
#print data.GetEntries()
#print data.Integral()

##############
# MC histos
##############

## MC
fake_components_1 = build_components(['fakesB1','fakesC1','fakesD1','fakesE1','fakesF1'], 
                                     data_datasets,
                                     variables, l1_FakeFactorApplication_Region, bins)
fake_components_2 = build_components(['fakesB2','fakesC2','fakesD2','fakesE2','fakesF2'], 
                                     data_datasets,
                                     variables, l2_FakeFactorApplication_Region, bins)
fake_components_MC_1 = build_components(['fakesMC1'], 
                                     mc_datasets,
                                     variables, l1_FakeFactorApplication_Region_genuinetauMC, bins)
fake_components_MC_2 = build_components(['fakesMC2'], 
                                     mc_datasets,
                                     variables, l2_FakeFactorApplication_Region_genuinetauMC, bins)


MC_components = build_components(['WJetsToLNu','WJetsToLNu_ext',
                                  'WW','WZ',
                                  'ZZTo4L','ZZTo4L_ext','ZZTo2L2Nu','ZZTo2L2Q',
                                  'TBar_tch','TBar_tWch','T_tch','T_tWch'], 
                                 mc_datasets,
                                 variables, signal_region_MC_nofakes, bins)

TT = build_components(['TTHad_pow','TTLep_pow','TTSemi_pow'], 
                      TT_datasets,
                      variables, signal_region_MC_nofakes_TT, bins)

DY = build_components(['DYJetsToLL_M50','DYJetsToLL_M50_ext'],#,
                       # 'DY1JetsToLL_M50','DY1JetsToLL_M50_ext',
                       # 'DY2JetsToLL_M50','DY2JetsToLL_M50_ext',
                       # 'DY3JetsToLL_M50','DY3JetsToLL_M50_ext',
                       # 'DY4JetsToLL_M50'],
                      [DYJetsToLL_M50,DYJetsToLL_M50_ext],#,
                       # DY1JetsToLL_M50,DY1JetsToLL_M50_ext,
                       # DY2JetsToLL_M50,DY2JetsToLL_M50_ext,
                       # DY3JetsToLL_M50,DY3JetsToLL_M50_ext,
                       # DY4JetsToLL_M50],
                      variables, signal_region_MC_nofakes_DY, bins)

MC_components.extend(DY)
MC_components.extend(TT)

### Merging components
TTBar = []
singleTop = []
DY = []
WJ = []
Diboson = []
for component in MC_components:
    if component.name in ['TTHad_pow','TTLep_pow','TTSemi_pow']:
        TTBar.append(component)
    elif component.name in ['TBar_tch','TBar_tWch','T_tch','T_tWch']:
        singleTop.append(component)
    elif component.name in ['DYJetsToLL_M50','DYJetsToLL_M50_ext','DY1JetsToLL_M50','DY1JetsToLL_M50_ext','DY2JetsToLL_M50','DY2JetsToLL_M50_ext','DY3JetsToLL_M50','DY3JetsToLL_M50_ext','DY4JetsToLL_M50']:
        DY.append(component)
    elif component.name in ['WJetsToLNu','WJetsToLNu_ext']:
        WJ.append(component)
    elif component.name in ['WW','WZ','ZZTo4L','ZZTo4L_ext','ZZTo2L2Nu','ZZTo2L2Q']:
        Diboson.append(component)
    else:
        print component.name, component
        import pdb;pdb.set_trace()

TTBar = merge_components('TTBar',TTBar)
singleTop = merge_components('singleTop',singleTop)
DY = merge_components('DY',DY)
WJ = merge_components('WJ',WJ)
Diboson = merge_components('Diboson',Diboson)

MC_components = [TTBar,DY,singleTop,Diboson,WJ]

#### data

data_components = build_components(['data'],[data_datasets],variables,signal_region, bins)

#### Embedded

Embedded_components = build_components(['Embedded'],[Embedded_datasets],variables,signal_region_Embedded, bins)# embedded signal region

fake_component_Embedded_1 = build_components(['fakesEmbedded1'],[Embedded_datasets],variables,l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)# embedded signal region
fake_component_Embedded_2 = build_components(['fakesEmbedded2'],[Embedded_datasets],variables,l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)# embedded signal region

#### fakes

for component in fake_components_MC_1+fake_components_MC_2+fake_component_Embedded_1+fake_component_Embedded_2:
    for var in variables:
        component.histogram[var].Scale(-1.)

fakes = merge_components('fakes',fake_components_1+fake_components_2+fake_component_Embedded_1+fake_component_Embedded_2+fake_components_MC_1+fake_components_MC_2)#



# estimated_integral = 0.
# data_integral = 0.
# fakes_integral = 0.
# for component in MC_components:
#     estimated_integral += component.histogram.Integral()
# for component in data_components:
#     data_integral += component.histogram.Integral()
# for component in fake_components_1+fake_components_2:
#     fakes_integral += component.histogram.Integral()

# for component in MC_components:
#     component.histogram.Scale((data_integral-fakes_integral)/estimated_integral)

# print 'needed scale =', (data_integral-fakes_integral)/estimated_integral

data_components[0].stack = False
plotter = Plotter(MC_components+data_components+[fakes]+Embedded_components, lumi)
import os
os.system('rm -rf {}'.format(output_dir))
os.system('mkdir {}'.format(output_dir))
for var in variables:
    plotter.draw(var, 'Number of events')
    plotter.write('{}/{}.png'.format(output_dir,var))
    print plotter.plot
