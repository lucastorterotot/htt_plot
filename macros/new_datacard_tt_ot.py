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

from htt_plot.tools.builder import build_cfgs, merge_cfgs, merge_components
from htt_plot.tools.builder import  merge_components as merge_comps

components = {}
dc_comps = {}
for variable in set(cfg.variables + cfg.datacards_variables):
    dc_comps[variable] = {}
    
    bins = cfg.bins[variable]

    # MC
    ZTT_cfgs = build_cfgs(
        [dataset.name+'_ZTT' for dataset in cfg.datasets.DY_datasets], 
        cfg.datasets.DY_datasets, variable,
        signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZTT'], bins)
    ZTT_comp = merge_cfgs('ZTT', ZTT_cfgs)
    
    ZL_cfgs = build_cfgs(
        [dataset.name+'_ZL' for dataset in cfg.datasets.DY_datasets], 
        cfg.datasets.DY_datasets, variable,
        signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZL'], bins)
    ZL_comp = merge_cfgs('ZL', ZL_cfgs)

    ZJ_cfgs = build_cfgs(
        [dataset.name+'_ZJ' for dataset in cfg.datasets.DY_datasets], 
        cfg.datasets.DY_datasets, variable,
        signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZJ'], bins)
    ZJ_comp = merge_cfgs('ZJ', ZJ_cfgs)
    
    ZLL_comp = merge_comps('ZLL', [ZL_comp, ZJ_comp])
    DY_comp = merge_comps('DY', [ZLL_comp, ZTT_comp])
    
    TTT_cfgs = build_cfgs(
        [dataset.name+'_TTT' for dataset in cfg.datasets.TT_datasets], 
        cfg.datasets.TT_datasets, variable,
        signal_region_MC_nofakes_TT & cfg.cuts_datacards['TTT'], bins)
    TTT_comp = merge_cfgs('TTT', TTT_cfgs)
    
    TTJ_cfgs = build_cfgs(
        [dataset.name+'_TTJ' for dataset in cfg.datasets.TT_datasets], 
        cfg.datasets.TT_datasets, variable,
        signal_region_MC_nofakes_TT & cfg.cuts_datacards['TTJ'], bins)
    TTJ_comp = merge_cfgs('TTJ', TTJ_cfgs)
    
    TT_comp = merge_comps('TT', [TTT_comp, TTJ_comp])
    
    Diboson_VVT_cfgs = build_cfgs(
        [dataset.name+'_VVT' for dataset in cfg.datasets.Diboson_datasets], 
        cfg.datasets.Diboson_datasets, variable,
        signal_region_MC_nofakes & cfg.cuts_datacards['VVT'], bins)
    Diboson_VVT_comp = merge_cfgs('Diboson_VVT', Diboson_VVT_cfgs)
    
    Diboson_VVJ_cfgs = build_cfgs(
        [dataset.name+'_VVJ' for dataset in cfg.datasets.Diboson_datasets], 
        cfg.datasets.Diboson_datasets, variable,
        signal_region_MC_nofakes & cfg.cuts_datacards['VVJ'], bins)
    Diboson_VVJ_comp = merge_cfgs('Diboson_VVJ', Diboson_VVJ_cfgs)
    
    singleTop_VVT_cfgs = build_cfgs(
        [dataset.name+'_VVT' for dataset in cfg.datasets.singleTop_datasets], 
        cfg.datasets.singleTop_datasets, variable,
        signal_region_MC_nofakes & cfg.cuts_datacards['VVT'], bins)
    singleTop_VVT_comp = merge_cfgs('singleTop_VVT', singleTop_VVT_cfgs)
    
    singleTop_VVJ_cfgs = build_cfgs(
        [dataset.name+'_VVJ' for dataset in cfg.datasets.singleTop_datasets], 
        cfg.datasets.singleTop_datasets, variable,
        signal_region_MC_nofakes & cfg.cuts_datacards['VVJ'], bins)
    singleTop_VVJ_comp = merge_cfgs('singleTop_VVJ', singleTop_VVJ_cfgs)
    
    VVT_comp = merge_comps('VVT', [singleTop_VVT_comp, Diboson_VVT_comp])
    VVJ_comp = merge_comps('VVJ', [singleTop_VVJ_comp, Diboson_VVJ_comp])
    VV_comp = merge_comps('VV', [VVT_comp, VVJ_comp])
    
    Diboson_comp = merge_comps('Diboson', [Diboson_VVT_comp, Diboson_VVJ_comp])
    singleTop_comp = merge_comps('singleTop', [singleTop_VVT_comp, singleTop_VVJ_comp])
    
    W_cfgs = build_cfgs(
        [dataset.name+'_W' for dataset in cfg.datasets.WJ_datasets], 
        cfg.datasets.WJ_datasets, variable,
        signal_region_MC_nofakes & cfg.cuts_datacards['W'], bins)
    W_comp = merge_cfgs('W', W_cfgs)
    
    MC_comps = [DY_comp, TT_comp, singleTop_comp, Diboson_comp, W_comp]
    
    # data
    data_cfgs = build_cfgs(
        [dataset.name for dataset in cfg.datasets.data_datasets], 
        cfg.datasets.data_datasets, variable, signal_region, bins)
    for data_cfg in data_cfgs:
        data_cfg.stack = False
    data_comp = merge_cfgs('data', data_cfgs)
        
    # Embedded
    Embedded_cfgs = build_cfgs(
        [dataset.name for dataset in cfg.datasets.Embedded_datasets], 
        cfg.datasets.Embedded_datasets, variable, signal_region_Embedded, bins)
    Embedded_comp = merge_cfgs('Embedded', Embedded_cfgs)

    # fakes
    datasets_MC_fakes = cfg.datasets.WJ_datasets + cfg.datasets.Diboson_datasets + cfg.datasets.singleTop_datasets + cfg.datasets.DY_datasets + cfg.datasets.TT_datasets
    fake_cfgs_MC_1 = build_cfgs(['fakesMC1'], datasets_MC_fakes, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_MC_2 = build_cfgs(['fakesMC2'], datasets_MC_fakes, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    
    fake_cfgs_1 = build_cfgs(
        ['fakes'+dataset.name[-1]+'1' for dataset in cfg.datasets.data_datasets], 
        cfg.datasets.data_datasets, variable, l1_FakeFactorApplication_Region, bins)
    fake_cfgs_2 = build_cfgs(
        ['fakes'+dataset.name[-1]+'2' for dataset in cfg.datasets.data_datasets], 
        cfg.datasets.data_datasets, variable, l2_FakeFactorApplication_Region, bins)
    
    fake_cfgs_Embedded_1 = build_cfgs(
        ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in cfg.datasets.Embedded_datasets], 
        cfg.datasets.Embedded_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
    fake_cfgs_Embedded_2 = build_cfgs(
        ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in cfg.datasets.Embedded_datasets], 
        cfg.datasets.Embedded_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
    
    data_fakes_cfgs = fake_cfgs_1 + fake_cfgs_2
    nondata_fakes_cfgs = fake_cfgs_Embedded_1 + fake_cfgs_Embedded_2 + fake_cfgs_MC_1 + fake_cfgs_MC_2
    
    data_fakes_comp = merge_cfgs('jetFakes', data_fakes_cfgs)

    for nondata_fakes_cfg in nondata_fakes_cfgs:
        nondata_fakes_cfg['scale'] = -1.
    nondata_fakes_comp = merge_cfgs('fakes_nondata', nondata_fakes_cfgs)
    
    fakes_comp = merge_comps('fakes', [data_fakes_comp, nondata_fakes_comp])

    components[variable] =  MC_comps + [data_comp, Embedded_comp, fakes_comp]

    dc_comps[variable]['nominal'] = {
        'ZTT' : ZTT_comp,
        'ZL' : ZL_comp,
        'ZJ' : ZJ_comp,
        'ZLL' : ZLL_comp,
        'TTT' : TTT_comp,
        'TTJ' : TTJ_comp,
        'TT' : TT_comp,
        'VVT' : VVT_comp,
        'VVJ' : VVJ_comp,
        'VV' : VV_comp,
        'W' : W_comp,
        'jetFakes' : data_fakes_comp,
        'data_obs' : data_comp,
        'embedded' : Embedded_comp,
    }


# systematics
#cfg.sys_dict
for variable in set(cfg.variables + cfg.datacards_variables):
    for sys in cfg.sys_dict:
        
        if 'ZTT' in cfg.sys_dict[sys]:
            ZTT_cfgs = build_cfgs(
                [dataset.name+'_ZTT' for dataset in cfg.datasets.DY_datasets], 
                cfg.datasets.DY_datasets, variable,
                signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZTT'], bins)
            ZTT_comp = merge_cfgs('ZTT', ZTT_cfgs)
        else:
            ZTT_comp = dc_comps[variable]['nominal']['ZTT']
            
        if 'ZL' in cfg.sys_dict[sys]:
            ZL_cfgs = build_cfgs(
                [dataset.name+'_ZL' for dataset in cfg.datasets.DY_datasets], 
                cfg.datasets.DY_datasets, variable,
                signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZL'], bins)
            ZL_comp = merge_cfgs('ZL', ZL_cfgs)
        else:
            ZL_comp = dc_comps[variable]['nominal']['ZL']

        if 'ZJ' in cfg.sys_dict[sys]:
            ZJ_cfgs = build_cfgs(
                [dataset.name+'_ZJ' for dataset in cfg.datasets.DY_datasets], 
                cfg.datasets.DY_datasets, variable,
                signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZJ'], bins)
            ZJ_comp = merge_cfgs('ZJ', ZJ_cfgs)
        else:
            ZJ_comp = dc_comps[variable]['nominal']['ZJ']

        if 'ZLL' in cfg.sys_dict[sys]:
            ZLL_comp = merge_comps('ZLL', [ZL_comp, ZJ_comp])
        else:
            ZLL_comp = dc_comps[variable]['nominal']['ZLL']

            
        if 'TTT' in cfg.sys_dict[sys]:    
            TTT_cfgs = build_cfgs(
                [dataset.name+'_TTT' for dataset in cfg.datasets.TT_datasets], 
                cfg.datasets.TT_datasets, variable,
                signal_region_MC_nofakes_TT & cfg.cuts_datacards['TTT'], bins)
            TTT_comp = merge_cfgs('TTT', TTT_cfgs)
        else:
            TTT_comp = dc_comps[variable]['nominal']['TTT']

        if 'TTJ' in cfg.sys_dict[sys]:    
            TTJ_cfgs = build_cfgs(
                [dataset.name+'_TTJ' for dataset in cfg.datasets.TT_datasets], 
                cfg.datasets.TT_datasets, variable,
                signal_region_MC_nofakes_TT & cfg.cuts_datacards['TTJ'], bins)
            TTJ_comp = merge_cfgs('TTJ', TTJ_cfgs)
        else:
            TTJ_comp = dc_comps[variable]['nominal']['TTJ']

        if 'TT' in cfg.sys_dict[sys]:    
            TT_comp = merge_comps('TT', [TTT_comp, TTJ_comp])
        else:
            TT_comp = dc_comps[variable]['nominal']['TT']


        if 'Diboson_VVT' in cfg.sys_dict[sys]:  
            Diboson_VVT_cfgs = build_cfgs(
                [dataset.name+'_VVT' for dataset in cfg.datasets.Diboson_datasets], 
                cfg.datasets.Diboson_datasets, variable,
                signal_region_MC_nofakes & cfg.cuts_datacards['VVT'], bins)
            Diboson_VVT_comp = merge_cfgs('Diboson_VVT', Diboson_VVT_cfgs)
        else:
            Diboson_VVT_comp = dc_comps[variable]['nominal']['Diboson_VVT']

        if 'Diboson_VVJ' in cfg.sys_dict[sys]:  
            Diboson_VVJ_cfgs = build_cfgs(
                [dataset.name+'_VVJ' for dataset in cfg.datasets.Diboson_datasets], 
                cfg.datasets.Diboson_datasets, variable,
                signal_region_MC_nofakes & cfg.cuts_datacards['VVJ'], bins)
            Diboson_VVJ_comp = merge_cfgs('Diboson_VVJ', Diboson_VVJ_cfgs)
        else:
            Diboson_VVJ_comp = dc_comps[variable]['nominal']['Diboson_VVJ']
    
        if 'singleTop_VVT' in cfg.sys_dict[sys]:  
            singleTop_VVT_cfgs = build_cfgs(
                [dataset.name+'_VVT' for dataset in cfg.datasets.singleTop_datasets], 
                cfg.datasets.singleTop_datasets, variable,
                signal_region_MC_nofakes & cfg.cuts_datacards['VVT'], bins)
            singleTop_VVT_comp = merge_cfgs('singleTop_VVT', singleTop_VVT_cfgs)
        else:
            singleTop_VVT_comp = dc_comps[variable]['nominal']['singleTop_VVT']
            
        if 'singleTop_VVJ' in cfg.sys_dict[sys]:  
            singleTop_VVJ_cfgs = build_cfgs(
                [dataset.name+'_VVJ' for dataset in cfg.datasets.singleTop_datasets], 
                cfg.datasets.singleTop_datasets, variable,
                signal_region_MC_nofakes & cfg.cuts_datacards['VVJ'], bins)
            singleTop_VVJ_comp = merge_cfgs('singleTop_VVJ', singleTop_VVJ_cfgs)
        else:
            singleTop_VVJ_comp = dc_comps[variable]['nominal']['singleTop_VVJ']

        if 'VVT' in cfg.sys_dict[sys]: 
            VVT_comp = merge_comps('VVT', [singleTop_VVT_comp, Diboson_VVT_comp])
        else:
            VVT_comp = dc_comps[variable]['nominal']['VVT']
        
        if 'VVJ' in cfg.sys_dict[sys]: 
            VVJ_comp = merge_comps('VVJ', [singleTop_VVJ_comp, Diboson_VVJ_comp])
        else:
            VVJ_comp = dc_comps[variable]['nominal']['VVJ']
        
        if 'VV' in cfg.sys_dict[sys]: 
            VV_comp = merge_comps('VV', [VVT_comp, VVJ_comp])
        else:
            VV_comp = dc_comps[variable]['nominal']['VV']

        if 'W' in cfg.sys_dict[sys]:
            W_cfgs = build_cfgs(
                [dataset.name+'_W' for dataset in cfg.datasets.WJ_datasets], 
                cfg.datasets.WJ_datasets, variable,
                signal_region_MC_nofakes & cfg.cuts_datacards['W'], bins)
            W_comp = merge_cfgs('W', W_cfgs)
        else:
            W_comp = dc_comps[variable]['nominal']['W']

        # data
        data_comp = dc_comps[variable]['nominal']['data']

        # Embedded
        if 'Embedded' in cfg.sys_dict[sys]:
            Embedded_cfgs = build_cfgs(
                [dataset.name for dataset in cfg.datasets.Embedded_datasets], 
                cfg.datasets.Embedded_datasets, variable, signal_region_Embedded, bins)
            Embedded_comp = merge_cfgs('Embedded', Embedded_cfgs)
        else:
            Embedded_comp = dc_comps[variable]['nominal']['Embedded']
        
        # fakes
        if 'fakes' in cfg.sys_dict[sys]:
            datasets_MC_fakes = cfg.datasets.WJ_datasets + cfg.datasets.Diboson_datasets + cfg.datasets.singleTop_datasets + cfg.datasets.DY_datasets + cfg.datasets.TT_datasets
            fake_cfgs_MC_1 = build_cfgs(['fakesMC1'], datasets_MC_fakes, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
            fake_cfgs_MC_2 = build_cfgs(['fakesMC2'], datasets_MC_fakes, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    
            fake_cfgs_1 = build_cfgs(
                ['fakes'+dataset.name[-1]+'1' for dataset in cfg.datasets.data_datasets], 
                cfg.datasets.data_datasets, variable, l1_FakeFactorApplication_Region, bins)
            fake_cfgs_2 = build_cfgs(
                ['fakes'+dataset.name[-1]+'2' for dataset in cfg.datasets.data_datasets], 
                cfg.datasets.data_datasets, variable, l2_FakeFactorApplication_Region, bins)
    
            fake_cfgs_Embedded_1 = build_cfgs(
                ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in cfg.datasets.Embedded_datasets], 
                cfg.datasets.Embedded_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
            fake_cfgs_Embedded_2 = build_cfgs(
                ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in cfg.datasets.Embedded_datasets], 
                cfg.datasets.Embedded_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
    
            data_fakes_cfgs = fake_cfgs_1 + fake_cfgs_2
            nondata_fakes_cfgs = fake_cfgs_Embedded_1 + fake_cfgs_Embedded_2 + fake_cfgs_MC_1 + fake_cfgs_MC_2
    
            data_fakes_comp = merge_cfgs('jetFakes', data_fakes_cfgs)

            for nondata_fakes_cfg in nondata_fakes_cfgs:
                nondata_fakes_cfg['scale'] = -1.
            nondata_fakes_comp = merge_cfgs('fakes_nondata', nondata_fakes_cfgs)
    
            fakes_comp = merge_comps('fakes', [data_fakes_comp, nondata_fakes_comp])
        else:
            data_fakes_comp = dc_comps[variable]['nominal']['jetFakes']

        dc_comps[variable][sys] = {
            'ZTT' : ZTT_comp,
            'ZL' : ZL_comp,
            'ZJ' : ZJ_comp,
            'ZLL' : ZLL_comp,
            'TTT' : TTT_comp,
            'TTJ' : TTJ_comp,
            'TT' : TT_comp,
            'VVT' : VVT_comp,
            'VVJ' : VVJ_comp,
            'VV' : VV_comp,
            'W' : W_comp,
            'jetFakes' : data_fakes_comp,
            'data_obs' : data_comp,
            'embedded' : Embedded_comp,
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
