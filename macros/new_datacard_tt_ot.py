import htt_plot.channels_configs.tt as cfg

# dask tools
from dask import delayed, compute, visualize

# output
output_dir = '_'.join(['delayed_plots', cfg.channel])

# plotting tools
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.plotting.tdrstyle import setTDRStyle
setTDRStyle(square=False)

# datacards tools
from htt_plot.tools.datacards import make_datacards

# cuts
signal_region_MC = cfg.cut_signal
signal_region_MC_nofakes = signal_region_MC & ~cfg.cut_l1_fakejet & ~cfg.cut_l2_fakejet
signal_region_MC_nofakes_DY = signal_region_MC & ~cfg.cut_l1_fakejet & ~cfg.cut_l2_fakejet & cfg.cut_dy_promptfakeleptons

l1_FakeFactorApplication_Region_cut = cfg.basic_cuts & cfg.cuts_iso['l1_VLoose'] & ~cfg.cuts_iso['l1_Tight'] & cfg.cuts_iso['l2_Tight']
l1_FakeFactorApplication_Region_genuinetauMC_cut = l1_FakeFactorApplication_Region_cut & ~cfg.cut_l1_fakejet
l1_FakeFactorApplication_Region_genuinetauMC_cut_DY = l1_FakeFactorApplication_Region_cut & ~cfg.cut_l1_fakejet & cfg.cut_dy_promptfakeleptons

l2_FakeFactorApplication_Region_cut = cfg.basic_cuts & cfg.cuts_iso['l2_VLoose'] & ~cfg.cuts_iso['l2_Tight'] & cfg.cuts_iso['l1_Tight']
l2_FakeFactorApplication_Region_genuinetauMC_cut = l2_FakeFactorApplication_Region_cut & ~cfg.cut_l2_fakejet
l2_FakeFactorApplication_Region_genuinetauMC_cut_DY = l2_FakeFactorApplication_Region_cut & ~cfg.cut_l2_fakejet & cfg.cut_dy_promptfakeleptons

#### cuts+weights
signal_region = cfg.cut_signal * cfg.weights['weight']
signal_region_Embedded = signal_region * cfg.weights['embed']
signal_region_MC = signal_region_MC * cfg.weights['weight'] * cfg.weights['MC']
signal_region_MC_nofakes_DY = signal_region_MC_nofakes_DY * cfg.weights['weight'] * cfg.weights['MC']# * cfg.weights['DY'] weight already in base weight
signal_region_MC_nofakes_TT = signal_region_MC_nofakes * cfg.weights['weight'] * cfg.weights['MC']# * cfg.weights['TT'] same
signal_region_MC_nofakes_Embedded = signal_region_MC_nofakes * cfg.weights['weight'] * cfg.weights['MC'] * cfg.weights['embed']
signal_region_MC_nofakes = signal_region_MC_nofakes * cfg.weights['weight'] * cfg.weights['MC']
l1_FakeFactorApplication_Region = l1_FakeFactorApplication_Region_cut * cfg.weights['l1_fake'] * cfg.weights['weight']
l2_FakeFactorApplication_Region = l2_FakeFactorApplication_Region_cut * cfg.weights['l2_fake'] * cfg.weights['weight']
l1_FakeFactorApplication_Region_genuinetauMC_Embedded = l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['embed'] * cfg.weights['l1_fake']
l2_FakeFactorApplication_Region_genuinetauMC_Embedded = l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['embed'] * cfg.weights['l2_fake']
l1_FakeFactorApplication_Region_genuinetauMC = l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['l1_fake']
l2_FakeFactorApplication_Region_genuinetauMC = l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['l2_fake']
l1_FakeFactorApplication_Region_genuinetauMC_DY = l1_FakeFactorApplication_Region_genuinetauMC_cut_DY * cfg.weights['weight'] * cfg.weights['l1_fake']# * cfg.weights['DY'] 
l2_FakeFactorApplication_Region_genuinetauMC_DY = l2_FakeFactorApplication_Region_genuinetauMC_cut_DY * cfg.weights['weight'] * cfg.weights['l2_fake']# * cfg.weights['DY'] 
l1_FakeFactorApplication_Region_genuinetauMC_TT = l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['l1_fake']# * cfg.weights['TT']
l2_FakeFactorApplication_Region_genuinetauMC_TT = l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['l2_fake']# * cfg.weights['TT']

from htt_plot.systematics import sys_dict_samples


for key, item in sys_dict_samples.iteritems():
    if 'DY' in item['processes']:
        item['DY_cut'] = signal_region_MC_nofakes_DY 
        item['DY_l1fakecut'] = l1_FakeFactorApplication_Region_genuinetauMC_DY
        item['DY_l2fakecut'] = l2_FakeFactorApplication_Region_genuinetauMC_DY
    if 'TT' in item['processes']:
        item['TT_cut'] = signal_region_MC_nofakes_TT
        item['TT_l1fakecut'] = l1_FakeFactorApplication_Region_genuinetauMC_TT
        item['TT_l2fakecut'] = l2_FakeFactorApplication_Region_genuinetauMC_TT
    if 'all_MC' in item['processes']:
        item['bkg_cut'] = signal_region_MC_nofakes
        item['bkg_l1fakecut'] = l1_FakeFactorApplication_Region_genuinetauMC
        item['bkg_l2fakecut'] = l2_FakeFactorApplication_Region_genuinetauMC
    if 'Embedded' in item['processes']:
        item['Embedded_cut'] = signal_region_MC_nofakes_Embedded
        item['Embedded_l1fakecut'] = l1_FakeFactorApplication_Region_genuinetauMC_Embedded
        item['Embedded_l2fakecut'] = l2_FakeFactorApplication_Region_genuinetauMC_Embedded
sys_dict_weights = {}
from htt_plot.tools.cut import Cut
for up_down in ['up','down']:
    for syst in ['qcd_syst_{}','qcd_dm0_njet0_stat_{}','qcd_dm0_njet1_stat_{}','w_syst_{}','tt_syst_{}','w_frac_syst_{}','tt_frac_syst_{}']:
        sys_name = 'ff_{}'.format(syst.format(up_down))
        cfg.datasets.DY_datasets[sys_name] = cfg.datasets.DY_datasets['nominal']
        cfg.datasets.TT_datasets[sys_name] = cfg.datasets.TT_datasets['nominal']
        cfg.datasets.Diboson_datasets[sys_name] = cfg.datasets.Diboson_datasets['nominal']
        cfg.datasets.singleTop_datasets[sys_name] = cfg.datasets.singleTop_datasets['nominal']
        cfg.datasets.WJ_datasets[sys_name] = cfg.datasets.WJ_datasets['nominal']
        cfg.datasets.Embedded_datasets[sys_name] = cfg.datasets.Embedded_datasets['nominal']
        sys_dict_weights[sys_name] = {'processes': ['all_MC','Embedded','data'],
                                      'DY_cut': signal_region_MC_nofakes_DY,
                                      'DY_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_cut_DY * cfg.weights['weight'] * Cut('0.5*l1_fakeweight_{}'.format(syst.format(up_down))),
                                      'DY_l2fakecut': l1_FakeFactorApplication_Region_genuinetauMC_cut_DY * cfg.weights['weight'] * Cut('0.5*l2_fakeweight_{}'.format(syst.format(up_down))),
                                      'TT_cut': signal_region_MC_nofakes_TT,
                                      'TT_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * Cut('0.5*l1_fakeweight_{}'.format(syst.format(up_down))),
                                      'TT_l2fakecut': l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * Cut('0.5*l2_fakeweight_{}'.format(syst.format(up_down))),
                                      'bkg_cut': signal_region_MC_nofakes,
                                      'bkg_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * Cut('0.5*l1_fakeweight_{}'.format(syst.format(up_down))),
                                      'bkg_l2fakecut': l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * Cut('0.5*l2_fakeweight_{}'.format(syst.format(up_down))),
                                      'Embedded_cut': signal_region_MC_nofakes_Embedded,
                                      'Embedded_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['embed'] * Cut('0.5*l1_fakeweight_{}'.format(syst.format(up_down))),
                                      'Embedded_l2fakecut': l2_FakeFactorApplication_Region_genuinetauMC_cut * cfg.weights['weight'] * cfg.weights['embed'] * Cut('0.5*l2_fakeweight_{}'.format(syst.format(up_down))),
                                      'l1fakecut': l1_FakeFactorApplication_Region_cut * cfg.weights['weight'] * Cut('0.5*l1_fakeweight_{}'.format(syst.format(up_down))),
                                      'l2fakecut': l2_FakeFactorApplication_Region_cut * cfg.weights['weight'] * Cut('0.5*l2_fakeweight_{}'.format(syst.format(up_down)))}
    sys_dict_weights['top_pt_reweighting_{}'.format(up_down)] = {'processes':['TT'],
                                                                 'TT_cut': signal_region_MC_nofakes_TT, # here find a way to de-apply top pt reweighting and re-apply up or down shift
                                                                 'TT_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_TT,
                                                                 'TT_l2fakecut': l2_FakeFactorApplication_Region_genuinetauMC_TT}
    cfg.datasets.TT_datasets['top_pt_reweighting_{}'.format(up_down)] = cfg.datasets.TT_datasets['nominal']
    sys_dict_weights['dy_pt_reweighting_{}'.format(up_down)] = {'processes':['DY'],
                                                                 'DY_cut': signal_region_MC_nofakes_DY, # here find a way to de-apply dy pt reweighting and re-apply up or down shift
                                                                 'DY_l1fakecut': l1_FakeFactorApplication_Region_genuinetauMC_DY,
                                                                 'DY_l2fakecut': l2_FakeFactorApplication_Region_genuinetauMC_DY}
    cfg.datasets.DY_datasets['dy_pt_reweighting_{}'.format(up_down)] = cfg.datasets.DY_datasets['nominal']
    

for key, item in sys_dict_weights.iteritems():
    if 'all_MC' in item['processes']:
        item['processes'].extend(['DY','TT','Diboson','singleTop','W'])
        
sys_dict = sys_dict_samples.copy()
sys_dict.update(sys_dict_weights)
    

#########
# Cfgs and components
#########

from htt_plot.tools.builder import build_cfgs, merge
from htt_plot.tools.builder import  merge_components as merge_comps
from htt_plot.tools.utils import add_processes_per_component

cfg_dict = {}
dc_comps = {}
components = {}
for variable in set(cfg.variables + cfg.datacards_variables):
    bins = cfg.bins[variable]
    cfg_dict[variable] = {}
    dc_comps[variable] = {}
    cfg_dict[variable]['nominal'] = {}
    cfgs = cfg_dict[variable]['nominal'] # for lighter syntax
    
    #DY
    add_processes_per_component(cfgs,
                                'DY',
                                ['ZTT','ZL','ZJ'],
                                cfg.datasets.DY_datasets['nominal'],
                                variable,
                                signal_region_MC_nofakes_DY,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC_DY,
                                l2_FakeFactorApplication_Region_genuinetauMC_DY,
                                bins,
                                mergedict = {'ZLL':['ZL','ZJ'],
                                             'DY':['ZLL','ZTT']})

    #TT
    add_processes_per_component(cfgs,
                                'TT',
                                ['TTT','TTJ'],
                                cfg.datasets.TT_datasets['nominal'],
                                variable,
                                signal_region_MC_nofakes_TT,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC_TT,
                                l2_FakeFactorApplication_Region_genuinetauMC_TT,
                                bins,
                                mergedict = {'TT':['TTT','TTJ']})

    #Diboson
    add_processes_per_component(cfgs,
                                'Diboson',
                                ['Diboson_VVT','Diboson_VVJ'],
                                cfg.datasets.Diboson_datasets['nominal'],
                                variable,
                                signal_region_MC_nofakes,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'Diboson':['Diboson_VVT','Diboson_VVJ']})

    #singleTop
    add_processes_per_component(cfgs,
                                'singleTop',
                                ['singleTop_VVT','singleTop_VVJ'],
                                cfg.datasets.singleTop_datasets['nominal'],
                                variable,
                                signal_region_MC_nofakes,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'singleTop':['singleTop_VVT','singleTop_VVJ']})
    
    #VV
    cfgs['VVT'] = merge('VVT', [cfgs['Diboson_VVT'],cfgs['singleTop_VVT']])
    cfgs['VVJ'] = merge('VVJ', [cfgs['Diboson_VVJ'],cfgs['singleTop_VVT']])
    cfgs['VV'] = merge('VV', [cfgs['VVJ'],cfgs['VVT']])
    
    #W
    add_processes_per_component(cfgs,
                                'W',
                                ['WJ'],
                                cfg.datasets.WJ_datasets['nominal'],
                                variable,
                                signal_region_MC_nofakes,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'W':['WJ']})
    
    # data
    add_processes_per_component(cfgs,
                                'data_obs',
                                ['data'],
                                cfg.datasets.data_datasets,
                                variable,
                                signal_region,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region,
                                l2_FakeFactorApplication_Region,
                                bins,
                                mergedict = {'data_obs':['data']})
        
    # Embedded
    add_processes_per_component(cfgs,
                                'Embedded',
                                ['embed'],
                                cfg.datasets.Embedded_datasets['nominal'],
                                variable,
                                signal_region_Embedded,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC_Embedded,
                                l2_FakeFactorApplication_Region_genuinetauMC_Embedded,
                                bins,
                                mergedict = {'Embedded':['embed']})

    # fakes
    cfgs['fakes'] = merge('fakes', [cfgs['fakes_data_obs'],
                                    cfgs['fakes_DY'],
                                    cfgs['fakes_TT'],
                                    cfgs['fakes_Diboson'],
                                    cfgs['fakes_singleTop'],
                                    cfgs['fakes_W'],
                                    cfgs['fakes_Embedded']])

    components[variable] = [cfgs['DY'],
                            cfgs['TT'],
                            cfgs['singleTop'],
                            cfgs['Diboson'],
                            cfgs['W'],
                            cfgs['data_obs'],
                            cfgs['Embedded'],
                            cfgs['fakes']]

    dc_comps[variable]['nominal'] = {
        'ZTT' : cfgs['ZTT'],
        'ZL' : cfgs['ZL'],
        'ZJ' : cfgs['ZJ'],
        'ZLL' : cfgs['ZLL'],
        'TTT' : cfgs['TTT'],
        'TTJ' : cfgs['TTJ'],
        'TT' : cfgs['TT'],
        'VVT' : cfgs['VVT'],
        'VVJ' : cfgs['VVJ'],
        'VV' : cfgs['VV'],
        'W' : cfgs['W'],
        'jetFakes' : cfgs['fakes'],
        'data_obs' : cfgs['data_obs'],
        'Embedded' : cfgs['Embedded'],
    }


# systematics
import copy
for variable in cfg.datacards_variables:
    for sys in sys_dict:
        cfg_dict[variable][sys] = copy.copy(cfg_dict[variable]['nominal'])
        cfgs = cfg_dict[variable][sys] # for lighter syntax

        #DY
        if 'DY' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'DY',
                                        ['ZTT','ZL','ZJ'],
                                        cfg.datasets.DY_datasets[sys],
                                        variable,
                                        sys_dict[sys]['DY_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['DY_l1fakecut'],
                                        sys_dict[sys]['DY_l2fakecut'],
                                        bins,
                                        mergedict = {'ZLL':['ZL','ZJ'],
                                                     'DY':['ZLL','ZTT']})
        
        #TT
        if 'TT' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'TT',
                                        ['TTT','TTJ'],
                                        cfg.datasets.TT_datasets[sys],
                                        variable,
                                        sys_dict[sys]['TT_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['TT_l1fakecut'],
                                        sys_dict[sys]['TT_l2fakecut'],
                                        bins,
                                        mergedict = {'TT':['TTT','TTJ']})
        
        #Diboson
        if 'Diboson' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'Diboson',
                                        ['Diboson_VVT','Diboson_VVJ'],
                                        cfg.datasets.Diboson_datasets[sys],
                                        variable,
                                        sys_dict[sys]['bkg_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['bkg_l1fakecut'],
                                        sys_dict[sys]['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'Diboson':['Diboson_VVT','Diboson_VVJ']})

        #singleTop
        if 'singleTop' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'singleTop',
                                        ['singleTop_VVT','singleTop_VVJ'],
                                        cfg.datasets.singleTop_datasets[sys],
                                        variable,
                                        sys_dict[sys]['bkg_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['bkg_l1fakecut'],
                                        sys_dict[sys]['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'singleTop':['singleTop_VVT','singleTop_VVJ']})
    
        #VV
        if any([name in sys_dict[sys]['processes'] for name in ['Diboson','singleTop']]):
            cfgs['VVT'] = merge('VVT', [cfgs['Diboson_VVT'],cfgs['singleTop_VVT']])
            cfgs['VVJ'] = merge('VVJ', [cfgs['Diboson_VVJ'],cfgs['singleTop_VVT']])
            cfgs['VV'] = merge('VV', [cfgs['VVJ'],cfgs['VVT']])
    
        #W
        if 'W' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'W',
                                        ['WJ'],
                                        cfg.datasets.WJ_datasets[sys],
                                        variable,
                                        sys_dict[sys]['bkg_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['bkg_l1fakecut'],
                                        sys_dict[sys]['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'W':['WJ']})
    
        # data
        if 'data' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'data_obs',
                                        ['data'],
                                        cfg.datasets.data_datasets,
                                        variable,
                                        signal_region,
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['l1fakecut'],
                                        sys_dict[sys]['l2fakecut'],
                                        bins,
                                        mergedict = {'data_obs':['data']})
        
        # Embedded
        if 'Embedded' in sys_dict[sys]['processes']:
            add_processes_per_component(cfgs,
                                        'Embedded',
                                        ['embed'],
                                        cfg.datasets.Embedded_datasets[sys],
                                        variable,
                                        sys_dict[sys]['Embedded_cut'],
                                        cfg.cuts_datacards,
                                        sys_dict[sys]['Embedded_l1fakecut'],
                                        sys_dict[sys]['Embedded_l2fakecut'],
                                        bins,
                                        mergedict = {'Embedded':['embed']})

        # fakes
        if any([name in sys_dict[sys]['processes'] for name in ['data_obs','DY','TT','Diboson','singleTop','W','Embedded']]):
            cfgs['fakes'] = merge('fakes', [cfgs['fakes_data_obs'],
                                            cfgs['fakes_DY'],
                                            cfgs['fakes_TT'],
                                            cfgs['fakes_Diboson'],
                                            cfgs['fakes_singleTop'],
                                            cfgs['fakes_W'],
                                            cfgs['fakes_Embedded']])

        dc_comps[variable][sys] = {
            'ZTT' : cfgs['ZTT'],
            'ZL' : cfgs['ZL'],
            'ZJ' : cfgs['ZJ'],
            'ZLL' : cfgs['ZLL'],
            'TTT' : cfgs['TTT'],
            'TTJ' : cfgs['TTJ'],
            'TT' : cfgs['TT'],
            'VVT' : cfgs['VVT'],
            'VVJ' : cfgs['VVJ'],
            'VV' : cfgs['VV'],
            'W' : cfgs['W'],
            'jetFakes' : cfgs['fakes'],
            'data_obs' : cfgs['data_obs'],
            'Embedded' : cfgs['Embedded'],
        }
    
processes = []

def write_plots(plotter, variable, output_dir):
    plotter.draw(variable, 'Number of events')
    plotter.write('{}/{}.png'.format(output_dir, variable))
    plotter.write('{}/{}.tex'.format(output_dir, variable))
    print plotter.plot
    
for variable in cfg.variables:
    processes.append(
        delayed(write_plots)(
            delayed(Plotter)(components[variable], cfg.datasets.data_lumi),
            variable,
            output_dir
            )
        )
    
for variable in cfg.datacards_variables:
    processes.append(
        delayed(make_datacards)(
            output_dir,
            cfg.channel,
            variable,
            dc_comps[variable],
            category = 'inclusive',
            systematics = ['nominal']+sys_dict.keys()
        )
    )

import os
os.system('rm -rf {}'.format(output_dir))
os.system('mkdir -p {}'.format(output_dir))
        
visualize(*processes)
#compute(*processes)
