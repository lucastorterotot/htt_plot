from dask import delayed, compute

from htt_plot.datasets.gael_all import *

from htt_plot.cuts.mt import *
from htt_plot.cuts.generic import *
from htt_plot.cuts.tt_triggers import triggers

from htt_plot.binning import bins

variables = ['l1_eta', 'l1_pt','l2_eta','l2_pt','met','m_vis','mt_tot']
variables = [variables[0]]

from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)

output_dir = 'delayed_plots_tt'

from htt_plot.tools.delayed_plot import build_component, build_components

from htt_plot.tools.delayed_component import Component, Component_cfg

def _create_component(cfg):
    comp = Component(cfg)
    comp.project()
    return comp

create_component = delayed(_create_component)

def _merge_cfgs(name, cfgs):
    comps = [create_component(cfg) for cfg in cfgs]
    return merge_components(name, comps)

merge_cfgs = _merge_cfgs

def _merge_components(name, comps):
    datasets = comps[0].cfg.datasets
    variables = comps[0].cfg.variables
    cut = comps[0].cfg.cut
    bins = comps[0].cfg.bins
    cfg0 = Component_cfg(name, datasets, variables, cut, bins)
    cfg0.datasets = []
    merged = create_component(cfg0)
    merged.merge(comps)
    return merged

merge_components = delayed(_merge_components)

## MC
fake_components_MC_1 = build_components(['fakesMC1'], 
                                        mc_datasets,
                                        variables,
                                        l1_FakeFactorApplication_Region_genuinetauMC,
                                        bins)

fake_components_MC_2 = build_components(['fakesMC2'], 
                                        mc_datasets,
                                        variables,
                                        l2_FakeFactorApplication_Region_genuinetauMC,
                                        bins)

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

TTBar = merge_cfgs('TTBar',TTBar)
singleTop = merge_cfgs('singleTop',singleTop)
DY = merge_cfgs('DY',DY)
WJ = merge_cfgs('WJ',WJ)
Diboson = merge_cfgs('Diboson',Diboson)

MC_components = [TTBar,DY,singleTop,Diboson,WJ]

#### data

data_cfgs = build_components(['data'],[data_datasets],variables,signal_region, bins)
data_cfgs[0].stack = False
data_components = [create_component(cfg) for cfg in data_cfgs]
#### Embedded

Embedded_cfgs = build_components(['Embedded'],[Embedded_datasets],variables,signal_region_Embedded, bins)# embedded signal region
Embedded_components = [create_component(cfg) for cfg in Embedded_cfgs]

fake_component_Embedded_1 = build_components(['fakesEmbedded1'],[Embedded_datasets],variables,l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)# embedded signal region
fake_component_Embedded_2 = build_components(['fakesEmbedded2'],[Embedded_datasets],variables,l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)# embedded signal region

#### fakes

fake_components_1 = build_components(['fakesB1','fakesC1','fakesD1','fakesE1','fakesF1'], 
                                     data_datasets,
                                     variables, l1_FakeFactorApplication_Region, bins)
fake_components_2 = build_components(['fakesB2','fakesC2','fakesD2','fakesE2','fakesF2'], 
                                     data_datasets,
                                     variables, l2_FakeFactorApplication_Region, bins)

for component in fake_components_MC_1+fake_components_MC_2+fake_component_Embedded_1+fake_component_Embedded_2:
    component.scale = -1.

fakes = fake_components_1+fake_components_2+fake_component_Embedded_1+fake_component_Embedded_2+fake_components_MC_1+fake_components_MC_2
fakes = [merge_cfgs('fakes',fakes)]

all_comp =  MC_components+data_components+Embedded_components#+fakes

plotter = delayed(Plotter)(all_comp, data_lumi)

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

from dask import compute
writter.visualize()
#compute(writter)
