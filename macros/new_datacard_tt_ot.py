channel = 'tt'
leg1 = channel[0] if not channel[0] == channel[1] else channel[0]+'1'
leg2 = channel[1] if not channel[0] == channel[1] else channel[1]+'2'

# datasets
import htt_plot.datasets.gael_all as datasets

# output
output_dir = 'delayed_plots_'+channel

# dask tools
from dask import delayed, compute, visualize

# binning
from htt_plot.binning import bins

# variables
variables = bins.keys()
variables = ['mt_tot'] # just for testing

# plotting tools
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)

# datacards tools
from htt_plot.tools.datacards import make_datacards

# cuts
from htt_plot.cuts.htt_cuts import cuts
cut_signal = cuts[channel]['signal']

from htt_plot.cuts.htt_triggers_ot import triggers_CutFlows
triggers = triggers_CutFlows[channel]['']
# as three states for triggers exists, take the one we want
# which is without suffix --> '' key

from htt_plot.cuts.htt_isolations import cuts_iso
cuts_iso = cuts_iso[channel]

from htt_plot.cuts.htt_flags import cuts_flags
from htt_plot.cuts.htt_vetoes import cuts_vetoes
from htt_plot.cuts.htt_generic import cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine

basic_cuts = cuts_flags + cuts_vetoes + triggers + cut_os

from htt_plot.tools.cut import Cut, CutFlow
cuts_against_leptons = CutFlow([
    ('l1_againstleptons','l1_againstElectronVLooseMVA6 > 0.5 && l1_againstMuonLoose3 > 0.5'),
    ('l2_againstleptons','l2_againstElectronVLooseMVA6 > 0.5 && l2_againstMuonLoose3 > 0.5')
])
basic_cuts += cuts_against_leptons

signal_region_cut = basic_cuts # + cut_signal
for leg in [leg1, leg2]:
    if 't' in leg:
        signal_region_cut += cuts_iso['Tight'][leg]

signal_region_MC = signal_region_cut
signal_region_MC_nofakes = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet
signal_region_MC_nofakes_DY = signal_region_MC_nofakes + cut_dy_promptfakeleptons
signal_region_MC_nofakes_TT = signal_region_MC_nofakes + cut_TT_nogenuine

l1_FakeFactorApplication_Region = basic_cuts + cuts_iso['VLoose'][leg1] + ~cuts_iso['Tight'][leg1] + cuts_iso['Tight'][leg2]
l1_FakeFactorApplication_Region_genuinetauMC = l1_FakeFactorApplication_Region + ~cut_l1_fakejet

l2_FakeFactorApplication_Region = basic_cuts + cuts_iso['VLoose'][leg2] + ~cuts_iso['Tight'][leg2] + cuts_iso['Tight'][leg1]
l2_FakeFactorApplication_Region_genuinetauMC = l2_FakeFactorApplication_Region + ~cut_l2_fakejet

from htt_plot.cuts.htt_datacards_cuts import cuts_datacards
cuts_datacards = cuts_datacards[channel]

#### cuts+weights
from htt_plot.cuts.htt_weights import weight, weight_MC, weight_MC_DY

signal_region = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight=weight)
signal_region_Embedded = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight='weight*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
signal_region_MC = '({cut})*({weight})'.format(cut=str(signal_region_MC),weight=weight_MC)
signal_region_MC_nofakes_DY = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_DY),weight=weight_MC_DY)
signal_region_MC_nofakes_TT = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_TT),weight=weight_MC)
signal_region_MC_nofakes = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes),weight=weight_MC)
l1_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region),weight='l1_fakeweight*0.5')
l2_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region),weight='l2_fakeweight*0.5')
l1_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l2_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l1_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5')
l2_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5')

#########
# Cfgs and components
#########

from htt_plot.tools.builder import build_cfgs, merge_cfgs, merge_components
from htt_plot.tools.builder import  merge_components as merge_comps

# MC
ZTT_cfgs = build_cfgs(
    [dataset.name+'_ZTT' for dataset in datasets.DY_datasets], 
    datasets.DY_datasets, variables,
    signal_region_MC_nofakes_DY+'*('+cuts_datacards['ZTT'].cutstr+')', bins)
ZTT_comp = merge_cfgs('ZTT', ZTT_cfgs)

ZL_cfgs = build_cfgs(
    [dataset.name+'_ZL' for dataset in datasets.DY_datasets], 
    datasets.DY_datasets, variables,
    signal_region_MC_nofakes_DY+'*('+cuts_datacards['ZL'].cutstr+')', bins)
ZL_comp = merge_cfgs('ZL', ZL_cfgs)

ZJ_cfgs = build_cfgs(
    [dataset.name+'_ZJ' for dataset in datasets.DY_datasets], 
    datasets.DY_datasets, variables,
    signal_region_MC_nofakes_DY+'*('+cuts_datacards['ZJ'].cutstr+')', bins)
ZJ_comp = merge_cfgs('ZJ', ZJ_cfgs)

ZLL_comp = merge_comps('ZLL', [ZL_comp, ZJ_comp])

TTT_cfgs = build_cfgs(
    [dataset.name+'_TTT' for dataset in datasets.TT_datasets], 
    datasets.TT_datasets, variables,
    signal_region_MC_nofakes_TT+'*('+cuts_datacards['TTT'].cutstr+')', bins)
TTT_comp = merge_cfgs('TTT', TTT_cfgs)

TTJ_cfgs = build_cfgs(
    [dataset.name+'_TTJ' for dataset in datasets.TT_datasets], 
    datasets.TT_datasets, variables,
    signal_region_MC_nofakes_TT+'*('+cuts_datacards['TTJ'].cutstr+')', bins)
TTJ_comp = merge_cfgs('TTJ', TTJ_cfgs)

TT_comp = merge_comps('TT', [TTT_comp, TTJ_comp])

Diboson_VVT_cfgs = build_cfgs(
    [dataset.name+'_VVT' for dataset in datasets.Diboson_datasets], 
    datasets.Diboson_datasets, variables,
    signal_region_MC_nofakes+'*('+cuts_datacards['VVT'].cutstr+')', bins)
Diboson_VVT_comp = merge_cfgs('Diboson_VVT', Diboson_VVT_cfgs)

Diboson_VVJ_cfgs = build_cfgs(
    [dataset.name+'_VVJ' for dataset in datasets.Diboson_datasets], 
    datasets.Diboson_datasets, variables,
    signal_region_MC_nofakes+'*('+cuts_datacards['VVJ'].cutstr+')', bins)
Diboson_VVJ_comp = merge_cfgs('Diboson_VVJ', Diboson_VVJ_cfgs)

singleTop_VVT_cfgs = build_cfgs(
    [dataset.name+'_VVT' for dataset in datasets.singleTop_datasets], 
    datasets.singleTop_datasets, variables,
    signal_region_MC_nofakes+'*('+cuts_datacards['VVT'].cutstr+')', bins)
singleTop_VVT_comp = merge_cfgs('singleTop_VVT', singleTop_VVT_cfgs)

singleTop_VVJ_cfgs = build_cfgs(
    [dataset.name+'_VVJ' for dataset in datasets.singleTop_datasets], 
    datasets.singleTop_datasets, variables,
    signal_region_MC_nofakes+'*('+cuts_datacards['VVJ'].cutstr+')', bins)
singleTop_VVJ_comp = merge_cfgs('singleTop_VVJ', singleTop_VVJ_cfgs)

VVT_comp = merge_comps('VVT', [singleTop_VVT_comp, Diboson_VVT_comp])
VVJ_comp = merge_comps('VVJ', [singleTop_VVJ_comp, Diboson_VVJ_comp])
VV_comp = merge_comps('VV', [VVT_comp, VVJ_comp])

Diboson_comp = merge_comps('Diboson', [Diboson_VVT_comp, Diboson_VVJ_comp])
singleTop_comp = merge_comps('singleTop', [singleTop_VVT_comp, singleTop_VVJ_comp])

W_cfgs = build_cfgs(
    [dataset.name+'_W' for dataset in datasets.WJ_datasets], 
    datasets.WJ_datasets, variables,
    signal_region_MC_nofakes+'*('+cuts_datacards['W'].cutstr+')', bins)
W_comp = merge_cfgs('W', W_cfgs)

MC_comps = [ZLL_comp, TT_comp, singleTop_comp, Diboson_comp, W_comp]

# data
data_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, signal_region, bins)
for cfg in data_cfgs:
    cfg.stack = False
data_comp = merge_cfgs('data', data_cfgs)

# Embedded
Embedded_cfgs = build_cfgs(
    [dataset.name for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, signal_region_Embedded, bins)
Embedded_comp = merge_cfgs('Embedded', Embedded_cfgs)

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

data_fakes_cfgs = fake_cfgs_1 + fake_cfgs_2
nondata_fakes_cfgs = fake_cfgs_Embedded_1 + fake_cfgs_Embedded_2 + fake_cfgs_MC_1 + fake_cfgs_MC_2

data_fakes_comp = merge_cfgs('jetFakes', data_fakes_cfgs)

for cfg in nondata_fakes_cfgs:
    cfg.scale = -1.
nondata_fakes_comp = merge_cfgs('fakes', nondata_fakes_cfgs)
    
fakes_comp = merge_comps('fakes', [data_fakes_comp, nondata_fakes_comp])

# Plotting & datacards

all_comp =  MC_comps + [data_comp, Embedded_comp, fakes_comp]

plotter = delayed(Plotter)(all_comp, datasets.data_lumi)

datacards = delayed(make_datacards)(output_dir, 'mt_tot',
                                    ZTT = ZTT_comp,
                                    ZL = ZL_comp,
                                    ZJ = ZJ_comp,
                                    ZLL = ZLL_comp,
                                    TTT = TTT_comp,
                                    TTJ = TTJ_comp,
                                    TT = TT_comp,
                                    VVT = VVT_comp,
                                    VVJ = VVJ_comp,
                                    VV = VV_comp,
                                    W = W_comp,
                                    jetFakes = data_fakes_comp,
                                    data_obs = data_comp,
                                    embedded = Embedded_comp
)

def write_plots(plotter, variables, output_dir):
    for var in variables:
        plotter.draw(var, 'Number of events')
        plotter.write('{}/{}.png'.format(output_dir,var))
        plotter.write('{}/{}.tex'.format(output_dir,var))
        print plotter.plot

writter = delayed(write_plots)(plotter, variables, output_dir)

import os
os.system('rm -rf {}'.format(output_dir))
os.system('mkdir {}'.format(output_dir))

def get_processes(processes_list):
    return processes_list

processes = delayed(get_processes)([writter, datacards])
        
visualize(processes)
#compute(process)
