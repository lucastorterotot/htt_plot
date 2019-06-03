from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component, Component_cfg
from dask import delayed
import copy
from ROOT import TH1F

def build_cfg(name, datasets, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    cfg = Component_cfg(name, datasets, var, cut, *bins)
    return cfg

def build_cfgs(names, datasets, var, cut, *bins):
    cfgs = []
    for name, dataset in zip(names, datasets):
        cfgs.append(build_cfg(name,dataset,var,cut,*bins))
    return cfgs

def create_component(cfg):
    comp = Component(cfg)
    project(comp)
    return comp

create_component = delayed(create_component)

def merge_cfgs(name, cfgs):
    comps = [create_component(cfg) for cfg in cfgs]
    return merge_components(name, comps)

def merge_components(name, comps):
    merged = copy.copy(comps[0])
    merged.name = name
    comps.remove(comps[0])
    merge(merged, comps)
    return merged

merge_components = delayed(merge_components)

def project(comp, verbose=False):
    for dataset in comp.cfg.datasets:
        for var in comp.cfg.variables:
            histo = TH1F(comp.cfg.name+dataset.name+var, comp.cfg.name+dataset.name, *comp.cfg.bins[var])
            if not hasattr(dataset.tree,'Project'):
                import pdb;pdb.set_trace()
            dataset.tree.Project(comp.cfg.name+dataset.name+var, var, comp.cfg.cut)
            if histo.Integral() == 0 and 'fake' in comp.name:
                print '\n', 'component :',comp.cfg.name, 'dataset :',dataset.name
                print dataset
                print dataset.tree
            if verbose:
                print '\n', 'component :',comp.cfg.name, 'dataset :',dataset.name
                if not dataset.is_data:
                    print 'lumi prescale:', dataset.nevts/dataset.xsection
                    print 'lumiweight:', dataset.weight
                print 'integral prescale:', histo.Integral()
            histo.Scale(dataset.weight)
            histo.Scale(comp.cfg.scale)
            if verbose:
                print 'integral postscale:', histo.Integral()
            comp.histogram[var].Add(histo)

def merge(comp, others):
    for var in comp.cfg.variables:
        for other in others:
            comp.histogram[var].Add(other.histogram[var]) 