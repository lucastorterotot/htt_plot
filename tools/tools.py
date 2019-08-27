from htt_plot.tools.builder import build_cfgs, merge

def add_processes_per_component(cfgs,component_name,processes,datasets,variable,basecut,process_cuts_dict,fake1_cut,fake2_cut,bins, mergedict={}):
    for process in processes:
        cfgs[process] = build_cfgs(
            [dataset.name+'_{}'.format(process) for dataset in datasets],
            datasets, variable,
            basecut & process_cuts_dict[process], bins)
    for mergedname, names_to_merge in mergedict:
        cfgs[mergedname] = merge(mergedname,names_to_merge)
    cfgs['fakes{}1'.format(component_name)] = build_cfgs(['fakes{}1'.format(component_name)],
                                                         datasets, variable,
                                                         fake1_cut, bins)
    cfgs['fakes{}2'.format(component_name)] = build_cfgs(['fakes{}2'.format(component_name)],
                                                         datasets, variable,
                                                         fake2_cut, bins)
    cfgs['fakes{}'.format(component_name)] = merge('fakes{}'.format(component_name),
                                                   [cfgs['fakes{}1'.format(component_name)],
                                                    cfgs['fakes{}2'.format(component_name)]])
