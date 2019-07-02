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
fake_comps = {}
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
    fake_comps[variable] = {}
    datasets_MC_fakes = cfg.datasets.WJ_datasets + cfg.datasets.Diboson_datasets + cfg.datasets.singleTop_datasets + cfg.datasets.DY_datasets + cfg.datasets.TT_datasets
    
    fake_cfgs_DY_1 = build_cfgs(['fakesDY1'], cfg.datasets.DY_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_DY_2 = build_cfgs(['fakesDY2'], cfg.datasets.DY_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_TT_1 = build_cfgs(['fakesTT1'], cfg.datasets.TT_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_TT_2 = build_cfgs(['fakesTT2'], cfg.datasets.TT_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_WJ_1 = build_cfgs(['fakesWJ1'], cfg.datasets.WJ_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_WJ_2 = build_cfgs(['fakesWJ2'], cfg.datasets.WJ_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_Diboson_1 = build_cfgs(['fakesDiboson1'], cfg.datasets.Diboson_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_Diboson_2 = build_cfgs(['fakesDiboson2'], cfg.datasets.Diboson_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_singleTop_1 = build_cfgs(['fakessingleTop1'], cfg.datasets.singleTop_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC, bins)
    fake_cfgs_singleTop_2 = build_cfgs(['fakessingleTop2'], cfg.datasets.singleTop_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC, bins)
    
    fake_cfgs_Embedded_1 = build_cfgs(
        ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in cfg.datasets.Embedded_datasets], 
        cfg.datasets.Embedded_datasets, variable, l1_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)
    fake_cfgs_Embedded_2 = build_cfgs(
        ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in cfg.datasets.Embedded_datasets], 
        cfg.datasets.Embedded_datasets, variable, l2_FakeFactorApplication_Region_genuinetauMC_Embedded, bins)

    for cfg in [fake_cfgs_DY_1,fake_cfgs_DY_2,fake_cfgs_TT_1,fake_cfgs_TT_2,fake_cfgs_WJ_1,fake_cfgs_WJ_2,fake_cfgs_Diboson_1,fake_cfgs_Diboson_2,fake_cfgs_singleTop_1,fake_cfgs_singleTop_2,fake_cfgs_Embedded_1,fake_cfgs_Embedded_2]:
        cfg['scale'] = -1.

    fake_cfgs_1 = build_cfgs(
        ['fakes'+dataset.name[-1]+'1' for dataset in cfg.datasets.data_datasets], 
        cfg.datasets.data_datasets, variable, l1_FakeFactorApplication_Region, bins)
    fake_cfgs_2 = build_cfgs(
        ['fakes'+dataset.name[-1]+'2' for dataset in cfg.datasets.data_datasets], 
        cfg.datasets.data_datasets, variable, l2_FakeFactorApplication_Region, bins)
    data_fakes_cfgs = fake_cfgs_1 + fake_cfgs_2
    data_fakes_comp = merge_cfgs('jetFakes', data_fakes_cfgs)

    
    fake_comps[variable] = {'DY': merge_cfgs('DY', [fake_cfgs_DY_1,fake_cfgs_DY_2]),
                            'TT': merge_cfgs('TT', [fake_cfgs_TT_1,fake_cfgs_TT_2]),
                            'std_bkg': merge_cfgs('std_bkg', [fake_cfgs_Diboson_1,fake_cfgs_Diboson_2,fake_cfgs_singleTop_1,fake_cfgs_singleTop_2,fake_cfgs_WJ_1,fake_cfgs_WJ_2]),
                            'Embedded': merge_cfgs('Embedded', [fake_cfgs_Embedded_1,fake_cfgs_Embedded_2]),
                            'data': data_fakes_comp
    }
    
    fakes_comp = merge_comps('fakes', [comp for name, comp in fake_comps[variable].iteritems()])

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
import copy
for variable in set(cfg.variables + cfg.datacards_variables):
    for sys in cfg.sys_dict:

        dc_comps[variable][sys] = copy.copy(dc_comps[variable]['nominal'])
        sys_fake_comp = copy.copy(fake_comps[variable])
        
        if 'ZTT' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes_DY
            else:
                datasets = cfg.datasets.DY_datasets
                cutstring = cfg.sys_dict[sys]['change']
            ZTT_cfgs = build_cfgs(
                [dataset.name+'_ZTT' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['ZTT'], bins)
            ZTT_comp = merge_cfgs('ZTT', ZTT_cfgs)
            dc_comps[variable][sys]['ZTT'] = ZTT_comp
            
        if 'ZL' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes_DY
            else:
                datasets = cfg.datasets.DY_datasets
                cutstring = cfg.sys_dict[sys]['change']
            ZL_cfgs = build_cfgs(
                [dataset.name+'_ZL' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['ZL'], bins)
            ZL_comp = merge_cfgs('ZL', ZL_cfgs)
            dc_comps[variable][sys]['ZL'] = ZL_comp

        if 'ZJ' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes_DY
            else:
                datasets = cfg.datasets.DY_datasets
                cutstring = cfg.sys_dict[sys]['change']
            ZJ_cfgs = build_cfgs(
                [dataset.name+'_ZJ' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['ZJ'], bins)
            ZJ_comp = merge_cfgs('ZJ', ZJ_cfgs)
            dc_comps[variable][sys]['ZJ'] = ZJ_comp

        if 'ZLL' in cfg.sys_dict[sys]['processes']:
            ZLL_comp = merge_comps('ZLL', [ZL_comp, ZJ_comp])
            dc_comps[variable][sys]['ZLL'] = ZLL_comp

        if 'DY' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring_l1 = signal_region_MC_nofakes_DY
                cutstring_l2 = signal_region_MC_nofakes_DY
            else:
                datasets = cfg.datasets.DY_datasets
                cutstring_l1 = cfg.sys_dict[sys]['fakecutstring_l1']
                cutstring_l2 = cfg.sys_dict[sys]['fakecutstring_l2']
            fake_cfgs_DY_1 = build_cfgs(['fakesDY1'], datasets, variable, cutstring_l1, bins)
            fake_cfgs_DY_2 = build_cfgs(['fakesDY2'], datasets, variable, cutstring_l2, bins)
            fake_cfgs_DY_1['scale'] = -1.
            fake_cfgs_DY_2['scale'] = -1.
            sys_fake_comp['DY'] = merge_cfgs('DY', [fake_cfgs_DY_1,fake_cfgs_DY_2])
            
        if 'TTT' in cfg.sys_dict[sys]['processes']:  
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes_TT
            else:
                datasets = cfg.datasets.TT_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            TTT_cfgs = build_cfgs(
                [dataset.name+'_TTT' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['TTT'], bins)
            TTT_comp = merge_cfgs('TTT', TTT_cfgs)
            dc_comps[variable][sys]['TTT'] = TTT_comp

        if 'TTJ' in cfg.sys_dict[sys]['processes']:    
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes_TT
            else:
                datasets = cfg.datasets.TT_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            TTJ_cfgs = build_cfgs(
                [dataset.name+'_TTJ' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['TTJ'], bins)
            TTJ_comp = merge_cfgs('TTJ', TTJ_cfgs)
            dc_comps[variable][sys]['TTJ'] = TTJ_comp

        if 'TT' in cfg.sys_dict[sys]['processes']:    
            TT_comp = merge_comps('TT', [TTT_comp, TTJ_comp])
            dc_comps[variable][sys]['TT'] = TT_comp

        if 'TT' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring_l1 = signal_region_MC_nofakes_TT
                cutstring_l2 = signal_region_MC_nofakes_TT
            else:
                datasets = cfg.datasets.TT_datasets
                cutstring_l1 = cfg.sys_dict[sys]['fakecutstring_l1']
                cutstring_l2 = cfg.sys_dict[sys]['fakecutstring_l2']
            fake_cfgs_TT_1 = build_cfgs(['fakesTT1'], datasets, variable, cutstring_l1, bins)
            fake_cfgs_TT_2 = build_cfgs(['fakesTT2'], datasets, variable, cutstring_l2, bins)
            fake_cfgs_TT_1['scale'] = -1.
            fake_cfgs_TT_2['scale'] = -1.
            sys_fake_comp['TT'] = merge_cfgs('TT', [fake_cfgs_TT_1,fake_cfgs_TT_2])

        if 'Diboson_VVT' in cfg.sys_dict[sys]['processes']:  
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.Diboson_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            Diboson_VVT_cfgs = build_cfgs(
                [dataset.name+'_VVT' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['VVT'], bins)
            Diboson_VVT_comp = merge_cfgs('Diboson_VVT', Diboson_VVT_cfgs)

        if 'Diboson_VVJ' in cfg.sys_dict[sys]['processes']:  
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.Diboson_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            Diboson_VVJ_cfgs = build_cfgs(
                [dataset.name+'_VVJ' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['VVJ'], bins)
            Diboson_VVJ_comp = merge_cfgs('Diboson_VVJ', Diboson_VVJ_cfgs)
    
        if 'singleTop_VVT' in cfg.sys_dict[sys]['processes']:  
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.singleTop_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            singleTop_VVT_cfgs = build_cfgs(
                [dataset.name+'_VVT' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['VVT'], bins)
            singleTop_VVT_comp = merge_cfgs('singleTop_VVT', singleTop_VVT_cfgs)
            
        if 'singleTop_VVJ' in cfg.sys_dict[sys]['processes']:   
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.singleTop_datasets
                cutstring = cfg.sys_dict[sys]['change']  
            singleTop_VVJ_cfgs = build_cfgs(
                [dataset.name+'_VVJ' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['VVJ'], bins)
            singleTop_VVJ_comp = merge_cfgs('singleTop_VVJ', singleTop_VVJ_cfgs)

        if 'VVT' in cfg.sys_dict[sys]['processes']: 
            VVT_comp = merge_comps('VVT', [singleTop_VVT_comp, Diboson_VVT_comp])
            dc_comps[variable][sys]['VVT'] = VVT_comp
        
        if 'VVJ' in cfg.sys_dict[sys]['processes']: 
            VVJ_comp = merge_comps('VVJ', [singleTop_VVJ_comp, Diboson_VVJ_comp])
            dc_comps[variable][sys]['VVJ'] = VVJ_comp
        
        if 'VV' in cfg.sys_dict[sys]['processes']: 
            VV_comp = merge_comps('VV', [VVT_comp, VVJ_comp])
            dc_comps[variable][sys]['VV'] = VV_comp

        if 'W' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.WJ_datasets
                cutstring = cfg.sys_dict[sys]['change'] 
            W_cfgs = build_cfgs(
                [dataset.name+'_W' for dataset in datasets], 
                datasets, variable,
                cutstring & cfg.cuts_datacards['W'], bins)
            W_comp = merge_cfgs('W', W_cfgs)
            dc_comps[variable][sys]['W'] = W_comp

        if 'std_bkg' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring_l1 = signal_region_MC_nofakes
                cutstring_l2 = signal_region_MC_nofakes
            else:
                datasets = cfg.datasets.WJ_datasets + cfg.datasets.Diboson_datasets + cfg.datasets.singleTop_datasets
                cutstring_l1 = cfg.sys_dict[sys]['fakecutstring_l1']
                cutstring_l2 = cfg.sys_dict[sys]['fakecutstring_l2']
            fake_cfgs_std_bkg_1 = build_cfgs(['fakes_std_bkg1'], datasets, variable, cutstring_l1, bins)
            fake_cfgs_std_bkg_2 = build_cfgs(['fakes_std_bkg2'], datasets, variable, cutstring_l2, bins)
            fake_cfgs_std_bkg_1['scale'] = -1.
            fake_cfgs_std_bkg_2['scale'] = -1.
            sys_fake_comp['std_bkg'] = merge_cfgs('std_bkg', [fake_cfgs_std_bkg_1,fake_cfgs_std_bkg_2])
            
        # data
        data_comp = dc_comps[variable]['nominal']['data']

        # Embedded
        if 'Embedded' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring = signal_region_Embedded
            else:
                datasets = cfg.datasets.Embedded_datasets
                cutstring = cfg.sys_dict[sys]['change'] 
            Embedded_cfgs = build_cfgs(
                [dataset.name for dataset in datasets], 
                datasets, variable, cutstring, bins)
            Embedded_cfgs['scale'] = -1.
            Embedded_comp = merge_cfgs('Embedded', Embedded_cfgs)
            dc_comps[variable][sys]['Embedded'] = Embedded_comp

        if 'Embedded' in cfg.sys_dict[sys]['processes']:
            if cfg.sys_dict[sys]['change'] == 'dataset':
                datasets = cfg.sys_datasets[sys]
                cutstring_l1 = l1_FakeFactorApplication_Region_genuinetauMC_Embedded
                cutstring_l2 = l2_FakeFactorApplication_Region_genuinetauMC_Embedded
            else:
                datasets = cfg.datasets.Embedded_datasets
                cutstring_l1 = cfg.sys_dict[sys]['fakecutstring_l1']
                cutstring_l2 = cfg.sys_dict[sys]['fakecutstring_l2']
            fake_cfgs_Embedded_1 = build_cfgs(['fakesEmbedded1'], datasets, variable, cutstring_l1, bins)
            fake_cfgs_Embedded_2 = build_cfgs(['fakesEmbedded2'], datasets, variable, cutstring_l2, bins)
            sys_fake_comp['Embedded'] = merge_cfgs('Embedded', [fake_cfgs_Embedded_1,fake_cfgs_Embedded_2])
            
        # propagation of systematics to fakes
        if sys != 'fakes':
            fakes_comp = merge_comps('fakes', [comp for name, comp in sys_fake_comp.iteritems()])
            dc_comps[variable][sys]['jetFakes'] = fakes_comp
            
        # fakes systematics
        if sys = 'fakes':
            #TODO sys here
            datasets_MC_fakes = cfg.datasets.WJ_datasets + cfg.datasets.Diboson_datasets + cfg.datasets.singleTop_datasets + cfg.datasets.DY_datasets + cfg.datasets.TT_datasets
            fake_cfgs_MC_1 = build_cfgs(['fakesMC1'], datasets_MC_fakes, variable, cfg.sys_dict[sys]['change']['l1MC'], bins)
            fake_cfgs_MC_2 = build_cfgs(['fakesMC2'], datasets_MC_fakes, variable, cfg.sys_dict[sys]['change']['l2MC'], bins)

            
            fake_cfgs_1 = build_cfgs(
                ['fakes'+dataset.name[-1]+'1' for dataset in cfg.datasets.data_datasets], 
                cfg.datasets.data_datasets, variable, cfg.sys_dict[sys]['change']['l1'], bins)
            fake_cfgs_2 = build_cfgs(
                ['fakes'+dataset.name[-1]+'2' for dataset in cfg.datasets.data_datasets], 
                cfg.datasets.data_datasets, variable, cfg.sys_dict[sys]['change']['l2'], bins)
    
            fake_cfgs_Embedded_1 = build_cfgs(
                ['fakesEmbedded'+dataset.name[-1]+'1' for dataset in cfg.datasets.Embedded_datasets], 
                cfg.datasets.Embedded_datasets, variable, cfg.sys_dict[sys]['change']['Embedded_l1'], bins)
            fake_cfgs_Embedded_2 = build_cfgs(
                ['fakesEmbedded'+dataset.name[-1]+'2' for dataset in cfg.datasets.Embedded_datasets], 
                cfg.datasets.Embedded_datasets, variable, cfg.sys_dict[sys]['change']['Embedded_l2'], bins)
    
            data_fakes_cfgs = fake_cfgs_1 + fake_cfgs_2
            nondata_fakes_cfgs = fake_cfgs_Embedded_1 + fake_cfgs_Embedded_2 + fake_cfgs_MC_1 + fake_cfgs_MC_2
    
            data_fakes_comp = merge_cfgs('jetFakes', data_fakes_cfgs)

            for nondata_fakes_cfg in nondata_fakes_cfgs:
                nondata_fakes_cfg['scale'] = -1.
            nondata_fakes_comp = merge_cfgs('fakes_nondata', nondata_fakes_cfgs)
    
            fakes_comp = merge_comps('fakes', [data_fakes_comp, nondata_fakes_comp])
            dc_comps[variable][sys]['JetFakes'] = fakes_comp

    
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
