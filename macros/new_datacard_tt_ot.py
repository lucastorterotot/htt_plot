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
signal_region_MC_nofakes_DY = signal_region_MC_nofakes & cfg.cut_dy_promptfakeleptons
signal_region_MC_nofakes_TT = signal_region_MC_nofakes & cfg.cut_TT_nogenuine

l1_FakeFactorApplication_Region = cfg.basic_cuts & cfg.cuts_iso['l1_VLoose'] & ~cfg.cuts_iso['l1_Tight'] & cfg.cuts_iso['l2_Tight']
l1_FakeFactorApplication_Region_genuinetauMC = l1_FakeFactorApplication_Region & ~cfg.cut_l1_fakejet

l2_FakeFactorApplication_Region = cfg.basic_cuts & cfg.cuts_iso['l2_VLoose'] & ~cfg.cuts_iso['l2_Tight'] & cfg.cuts_iso['l1_Tight']
l2_FakeFactorApplication_Region_genuinetauMC = l2_FakeFactorApplication_Region & ~cfg.cut_l2_fakejet

#### cuts+weights
signal_region = cfg.cut_signal * cfg.weights['weight']
signal_region_Embedded = signal_region * cfg.weights['embed']
signal_region_MC = signal_region_MC * cfg.weights['weight'] * cfg.weights['MC']
signal_region_MC_nofakes_DY = signal_region_MC_nofakes_DY * cfg.weights['weight'] * cfg.weights['MC'] * cfg.weights['DY'] 
signal_region_MC_nofakes_TT = signal_region_MC_nofakes_TT * cfg.weights['weight'] * cfg.weights['MC']
signal_region_MC_nofakes = signal_region_MC_nofakes * cfg.weights['weight'] * cfg.weights['MC']
l1_FakeFactorApplication_Region = l1_FakeFactorApplication_Region * cfg.weights['l1_fake']
l2_FakeFactorApplication_Region = l2_FakeFactorApplication_Region * cfg.weights['l2_fake']
l1_FakeFactorApplication_Region_genuinetauMC_Embedded = l1_FakeFactorApplication_Region_genuinetauMC * cfg.weights['weight'] * cfg.weights['embed'] * cfg.weights['l1_fake']
l2_FakeFactorApplication_Region_genuinetauMC_Embedded = l2_FakeFactorApplication_Region_genuinetauMC * cfg.weights['weight'] * cfg.weights['embed'] * cfg.weights['l2_fake']
l1_FakeFactorApplication_Region_genuinetauMC = l1_FakeFactorApplication_Region_genuinetauMC * cfg.weights['weight'] * cfg.weights['l1_fake']
l2_FakeFactorApplication_Region_genuinetauMC = l2_FakeFactorApplication_Region_genuinetauMC * cfg.weights['weight'] * cfg.weights['l2_fake']

#########
# Cfgs and components
#########

from htt_plot.tools.builder import build_cfgs, merge
from htt_plot.tools.builder import  merge_components as merge_comps
from htt_plot.tools.utils import add_processes_per_component

for variable in set(cfg.variables + cfg.datacards_variables):
    
    bins = cfg.bins[variable]

    cfg_dict[variable]['nominal'] = {}
    cfgs = cfg_dict[variable]['nominal'] # for lighter syntax
    
    #DY
    add_processes_per_component(cfgs,
                                'DY',
                                ['ZTT','ZL','ZJ'],
                                cfg.datasets.DY_datasets,
                                variable,
                                signal_region_MC_nofakes_DY,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,#here add DY reweighting in fakes
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'ZLL':['ZL','ZJ'],
                                             'DY':['ZLL','ZTT']})

    #TT
    add_processes_per_component(cfgs,
                                'TT',
                                ['TTT','TTJ'],
                                cfg.datasets.TT_datasets,
                                variable,
                                signal_region_MC_nofakes_TT,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,#here add TT reweighting in fakes
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'TT':['TTT','TTJ']})

    #Diboson
    add_processes_per_component(cfgs,
                                'Diboson',
                                ['Diboson_VVT','Diboson_VVJ'],
                                cfg.datasets.Diboson_datasets,
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
                                cfg.datasets.singleTop_datasets,
                                variable,
                                signal_region_MC_nofakes,
                                cfg.cuts_datacards,
                                l1_FakeFactorApplication_Region_genuinetauMC,
                                l2_FakeFactorApplication_Region_genuinetauMC,
                                bins,
                                mergedict = {'singleTop':['singleTop_VVT','singleTop_VVJ']})
    
    #VV
    cfgs['VVT'] = merge('VVT', [cfgs['Diboson_VVT'],cfgs['singleTop_VVT']])
    cfgs['VVJ'] = merge('VVJ', [cfgs['Diboson_VVJ'],cfgs['singleJop_VVT']])
    cfgs['VV'] = merge('VV', [cfgs['VVJ'],cfgs['VVT']])
    
    #W
    add_processes_per_component(cfgs,
                                'W',
                                ['WJ'],
                                cfg.datasets.WJ_datasets,
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
                                cfg.datasets.Embedded_datasets,
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
    for sys in cfg.sys_dict:
        cfg_dict[variable][sys] = copy.copy(cfg_dict[variable]['nominal'])
        cfgs = cfg_dict[variable][sys] # for lighter syntax

        #DY
        if 'DY' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('DY',sys)
            add_processes_per_component(cfgs,
                                        'DY',
                                        ['ZTT','ZL','ZJ'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['DY_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['DY_l1fakecut'],
                                        cfg.sys_dict['DY_l2fakecut'],
                                        bins,
                                        mergedict = {'ZLL':['ZL','ZJ'],
                                                     'DY':['ZLL','ZTT']})
        
        #TT
        if 'TT' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('TT',sys)
            add_processes_per_component(cfgs,
                                        'TT',
                                        ['TTT','TTJ'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['TT_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['TT_l1fakecut'],
                                        cfg.sys_dict['TT_l2fakecut'],
                                        bins,
                                        mergedict = {'TT':['TTT','TTJ']})
        
        #Diboson
        if 'Diboson' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('Diboson',sys)
            add_processes_per_component(cfgs,
                                        'Diboson',
                                        ['Diboson_VVT','Diboson_VVJ'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['bkg_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['bkg_l1fakecut'],
                                        cfg.sys_dict['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'Diboson':['Diboson_VVT','Diboson_VVJ']})

        #singleTop
        if 'singleTop' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('singleTop',sys)
            add_processes_per_component(cfgs,
                                        'singleTop',
                                        ['singleTop_VVT','singleTop_VVJ'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['bkg_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['bkg_l1fakecut'],
                                        cfg.sys_dict['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'singleTop':['singleTop_VVT','singleTop_VVJ']})
    
        #VV
        if any([name in cfg.sys_dict['process'] for name in ['Diboson','singleTop']]):
            cfgs['VVT'] = merge('VVT', [cfgs['Diboson_VVT'],cfgs['singleTop_VVT']])
            cfgs['VVJ'] = merge('VVJ', [cfgs['Diboson_VVJ'],cfgs['singleJop_VVT']])
            cfgs['VV'] = merge('VV', [cfgs['VVJ'],cfgs['VVT']])
    
        #W
        if 'W' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('W',sys)
            add_processes_per_component(cfgs,
                                        'W',
                                        ['WJ'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['bkg_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['bkg_l1fakecut'],
                                        cfg.sys_dict['bkg_l2fakecut'],
                                        bins,
                                        mergedict = {'W':['WJ']})
    
        # data
        if 'data' in cfg.sys_dict['process']:
            add_processes_per_component(cfgs,
                                        'data_obs',
                                        ['data'],
                                        cfg.datasets.data_datasets,
                                        variable,
                                        signal_region,
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['l1fakecut'],
                                        cfg.sys_dict['l2fakecut'],
                                        bins,
                                        mergedict = {'data_obs':['data']})
        
        # Embedded
        if 'Embedded' in cfg.sys_dict['process']:
            datasets = find_sys_dataset('Embedded',sys)
            add_processes_per_component(cfgs,
                                        'Embedded',
                                        ['embed'],
                                        datasets,
                                        variable,
                                        cfg.sys_dict['Embedded_cut'],
                                        cfg.cuts_datacards,
                                        cfg.sys_dict['Embedded_l1fakecut'],
                                        cfg.sys_dict['Embedded_l2fakecut'],
                                        bins,
                                        mergedict = {'Embedded':['embed']})

        # fakes
        if any([name in cfg.sys_dict['process'] for name in ['data_obs','DY','TT','Diboson','singleTop','W','Embedded']]):
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
            variable,
            dc_comps[variable]['nominal']
        )
    )
    for sys in cfg.sys_dict:
        processes.append(
            delayed(make_datacards)(
                output_dir,
                variable,
                dc_comps[variable][sys]
            )
        )

import os
os.system('rm -rf {}'.format(output_dir))
os.system('mkdir -p {}'.format(output_dir))
        
visualize(*processes)
#compute(*processes)
