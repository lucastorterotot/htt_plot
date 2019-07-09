from htt_plot.tools.builder import build_cfgs, merge

def add_processes_per_component(cfgs,component_name,baseprocesses,datasets,variable,basecut,process_cuts_dict,fake1_cut,fake2_cut,bins, mergedict={}):
    for process in baseprocesses:
        cfgs[process+'_cfgs'] = build_cfgs(
            [dataset.name+'_{}'.format(process) for dataset in datasets],
            datasets, variable,
            basecut & process_cuts_dict[process], bins)
        if component_name == 'data_obs':
            for cfg in cfgs[process+'_cfgs']:
                cfg.stack = False
        cfgs[process] = merge(process,cfgs[process+'_cfgs'])
    for mergedname, names_to_merge in mergedict.iteritems():        cfgs[mergedname] = merge(mergedname,[cfgs[name] for name in names_to_merge])
    cfgs['fakes{}1'.format(component_name)] = build_cfgs(['fakes{}1'.format(component_name)],
                                                         datasets, variable,
                                                         fake1_cut, bins)
    if component_name != 'data_obs':
        for cfg in cfgs['fakes{}1'.format(component_name)]:
            cfg['scale'] = -1.
    cfgs['fakes{}2'.format(component_name)] = build_cfgs(['fakes{}2'.format(component_name)],
                                                         datasets, variable,
                                                         fake2_cut, bins)
    if component_name != 'data_obs':
        for cfg in cfgs['fakes{}2'.format(component_name)]:
            cfg['scale'] = -1.
    cfgs['fakes_{}'.format(component_name)] = merge('fakes{}'.format(component_name),
                                                   cfgs['fakes{}1'.format(component_name)]+cfgs['fakes{}2'.format(component_name)])
