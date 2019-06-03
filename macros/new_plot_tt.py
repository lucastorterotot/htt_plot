channel = 'tt'

# dask tools
from dask import delayed, compute

# datasets
import htt_plot.datasets.gael_all as datasets

# cuts
from htt_plot.cuts.mt import *
from htt_plot.cuts.generic import *
from htt_plot.cuts.tt_triggers import triggers

# binning
from htt_plot.binning import bins

# variables
variables = ['l1_eta', 'l1_pt','l2_eta','l2_pt','met','m_vis','mt_tot']
variables = [variables[0]]

# plotting tools
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)

# output
output_dir = 'delayed_plots_tt'

#########
# Cfgs and components
#########

import htt_plot.tools.builder as builder

# MC
singleTop_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.singleTop_datasets], 
    datasets.singleTop_datasets, variables, signal_region_MC_nofakes, bins)

WJ_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.WJ_datasets], 
    datasets.WJ_datasets, variables, signal_region_MC_nofakes, bins)

Diboson_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.Diboson_datasets], 
    datasets.Diboson_datasets, variables, signal_region_MC_nofakes, bins)

TT_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.TT_datasets], 
    datasets.TT_datasets, variables, signal_region_MC_nofakes_TT, bins)

DY_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.DY_datasets], 
    datasets.DY_datasets, variables, signal_region_MC_nofakes_DY, bins)

singleTop_comp = builder.merge_cfgs('singleTop',singleTop_cfgs)
WJ_comp = builder.merge_cfgs('WJ',WJ_cfgs)
Diboson_comp = builder.merge_cfgs('Diboson',Diboson_cfgs)
TT_comp = builder.merge_cfgs('TTBar',TT_cfgs)
DY_comp = builder.merge_cfgs('DY',DY_cfgs)

MC_components = [singleTop_comp, WJ_comp, Diboson_comp, TT_comp, DY_comp]

# data
data_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, signal_region, bins)
for cfg in data_cfgs:
    cfg.stack = False
data_component = builder.merge_cfgs('data', data_cfgs)

# Embedded
Embedded_cfgs = builder.build_cfgs(
    [dataset.name for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, signal_region_Embedded, bins)
Embedded_component = builder.merge_cfgs('Embedded', Embedded_cfgs)

# fakes
datasets_MC_fakes = datasets.WJ_datasets + datasets.Diboson_datasets + datasets.singleTop_datasets + datasets.DY_datasets + datasets.TT_datasets
fake_cfgs_MC_1 = builder.build_cfgs(['fakesMC1'], datasets_MC_fakes, variables, l1_FakeFactorApplication_Region_genuinetauMC, bins)
fake_cfgs_MC_2 = builder.build_cfgs(['fakesMC2'], datasets_MC_fakes, variables, l2_FakeFactorApplication_Region_genuinetauMC, bins)

fake_cfgs_1 = builder.build_cfgs(
    ['fakes'+dataset.name[-1]+'1' for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, l1_FakeFactorApplication_Region, bins)
fake_cfgs_2 = builder.build_cfgs(
    ['fakes'+dataset.name[-1]+'2' for dataset in datasets.data_datasets], 
    datasets.data_datasets, variables, l2_FakeFactorApplication_Region, bins)

fake_cfgs_Embedded_1 = builder.build_cfgs(
    ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
fake_cfgs_Embedded_2 = builder.build_cfgs(
    ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in datasets.Embedded_datasets], 
    datasets.Embedded_datasets, variables, l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)

for cfg in fake_cfgs_MC_1+fake_cfgs_MC_2+fake_cfgs_Embedded_1+fake_cfgs_Embedded_2:
    cfg.scale = -1.

fakes_cfgs = fake_cfgs_1+fake_cfgs_2+fake_cfgs_Embedded_1+fake_cfgs_Embedded_2+fake_cfgs_MC_1+fake_cfgs_MC_2
fakes_component = builder.merge_cfgs('fakes',fakes_cfgs)

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
compute(writter)
