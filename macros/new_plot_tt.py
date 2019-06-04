channel = 'tt'
leg1 = channel[0] if not channel[0] == channel[1] else channel[0]+'1'
leg2 = channel[1] if not channel[0] == channel[1] else channel[1]+'2'

# dask tools
from dask import delayed, compute

# binning
from htt_plot.binning import bins

# variables
variables = bins.keys()
variables = [variables[0]]

# plotting tools
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)

# output
output_dir = 'delayed_plots_'+channel

# cuts
from htt_plot.cuts.htt_cuts import cuts
cut_signal = cuts[channel]['signal']

from htt_plot.cuts.htt_triggers import triggers_CutFlows
triggers = triggers_CutFlows[channel]['']

from htt_plot.cuts.htt_isolations import cuts_iso
cuts_iso = cuts_iso[channel]

from htt_plot.cuts.htt_flags import cuts_flags
from htt_plot.cuts.htt_vetoes import cuts_vetoes
from htt_plot.cuts.htt_generic import cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine

signal_region_cut = cut_signal + cuts_flags + cuts_vetoes + triggers + cut_os
for leg in [leg1, leg2]:
    if 't' in leg:
        signal_region_cut += cuts_iso['Tight'][leg]

signal_region_MC = signal_region_cut
signal_region_MC_nofakes = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet
signal_region_MC_nofakes_DY = signal_region_MC_nofakes + cut_dy_promptfakeleptons
signal_region_MC_nofakes_TT = signal_region_MC_nofakes + cut_TT_nogenuine

l1_FakeFactorApplication_Region = cuts_flags + cuts_vetoes + triggers + cut_os + cuts_iso['VLoose'][leg1] + ~cuts_iso['Tight'][leg1] + cuts_iso['Tight'][leg2]
l1_FakeFactorApplication_Region_genuinetauMC = l1_FakeFactorApplication_Region + ~cut_l1_fakejet

l2_FakeFactorApplication_Region = cuts_flags + cuts_vetoes + triggers + cut_os + cuts_iso['VLoose'][leg2] + ~cuts_iso['Tight'][leg2]  + cuts_iso['Tight'][leg1]
l2_FakeFactorApplication_Region_genuinetauMC = l2_FakeFactorApplication_Region + ~cut_l2_fakejet

from htt_plot.tools.cut import Cut
import pprint
pprint.pprint(Cut.available_cuts())

#### cuts+weights
from htt_plot.cuts.htt_weights import weight, weight_MC, weight_MC_DY

signal_region = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight=weight)
signal_region_Embedded = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight='weight*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
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

#########
# Cfgs and components
#########

# datasets
import htt_plot.datasets.gael_all as datasets

# from htt_plot.datasets.htt import datasets
# datasets = datasets[channel]

from htt_plot.tools.builder import build_cfgs, merge_cfgs

# MC
singleTop_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.singleTop_datasets], 
    datasets.singleTop_datasets, variables, signal_region_MC_nofakes, bins)

WJ_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.WJ_datasets], 
    datasets.WJ_datasets, variables, signal_region_MC_nofakes, bins)

Diboson_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.Diboson_datasets], 
    datasets.Diboson_datasets, variables, signal_region_MC_nofakes, bins)

TT_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.TT_datasets], 
    datasets.TT_datasets, variables, signal_region_MC_nofakes_TT, bins)

DY_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.DY_datasets], 
    datasets.DY_datasets, variables, signal_region_MC_nofakes_DY, bins)

singleTop_comp = merge_cfgs('singleTop',singleTop_cfgs)
WJ_comp = merge_cfgs('WJ',WJ_cfgs)
Diboson_comp = merge_cfgs('Diboson',Diboson_cfgs)
TT_comp = merge_cfgs('TTBar',TT_cfgs)
DY_comp = merge_cfgs('DY',DY_cfgs)

MC_components = [singleTop_comp, WJ_comp, Diboson_comp, TT_comp, DY_comp]

# data
data_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, signal_region, bins)
for cfg in data_cfgs:
    cfg.stack = False
data_component = merge_cfgs('data', data_cfgs)

# Embedded
Embedded_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, signal_region_Embedded, bins)
Embedded_component = merge_cfgs('Embedded', Embedded_cfgs)

# fakes
datasets_MC_fakes = datasets.WJ_datasets + datasets.Diboson_datasets + datasets.singleTop_datasets + datasets.DY_datasets + datasets.TT_datasets
fake_cfgs_MC_1 = build_cfgs(['fakesMC1'], datasets_MC_fakes, variables, l1_FakeFactorApplication_Region_genuinetauMC, bins)
fake_cfgs_MC_2 = build_cfgs(['fakesMC2'], datasets_MC_fakes, variables, l2_FakeFactorApplication_Region_genuinetauMC, bins)

fake_cfgs_1 = build_cfgs(
    ['fakes'+dataset.name[-1]+'1' for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, l1_FakeFactorApplication_Region, bins)
fake_cfgs_2 = build_cfgs(
    ['fakes'+dataset.name[-1]+'2' for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, l2_FakeFactorApplication_Region, bins)

fake_cfgs_Embedded_1 = build_cfgs(
    ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
fake_cfgs_Embedded_2 = build_cfgs(
    ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)

for cfg in fake_cfgs_MC_1+fake_cfgs_MC_2+fake_cfgs_Embedded_1+fake_cfgs_Embedded_2:
    cfg.scale = -1.

fakes_cfgs = fake_cfgs_1+fake_cfgs_2+fake_cfgs_Embedded_1+fake_cfgs_Embedded_2+fake_cfgs_MC_1+fake_cfgs_MC_2
fakes_component = merge_cfgs('fakes',fakes_cfgs)

all_comp =  MC_components+[data_component]+[Embedded_component]+[fakes_component]

plotter = delayed(Plotter)(all_comp, datasets.data_lumi)

def write_plots(plotter, variables, output_dir):
    import os
    os.system('rm -rf {}'.format(output_dir))
    os.system('mkdir {}'.format(output_dir))
    for var in variables:
        plotter.draw(var, 'Number of events')
        plotter.write('{}/{}.png'.format(output_dir,var))
        plotter.write('{}/{}.tex'.format(output_dir,var))
        print plotter.plot

writter = delayed(write_plots)(plotter, variables, output_dir)

writter.visualize()
#compute(writter)
