from htt_plot.tools.cut import Cuts
from htt_plot.tools.component import Component, Component_cfg
from dask import delayed
import copy
from ROOT import TH1F

def build_cfg(name, dataset, variable, cut, *bins):
    '''Allows to pass non-str cuts'''
    if not isinstance(cut, str):
        cut = str(cut)
    cfg = Component_cfg(name, dataset, variable, cut, *bins)
    return cfg

def build_cfgs(names, datasets, variable, cut, *bins):
    cfgs = []
    for name, dataset in zip(names, datasets):
        cfgs.append(build_cfg(name,dataset,variable,cut,*bins))
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
    merged = comps[0].Clone(name)
    comps.remove(comps[0])
    merge(merged, comps)
    return merged

merge_components = delayed(merge_components)

def project(comp):
    dataset = comp.cfg.dataset
    var = comp.cfg.variable
    histo = TH1F(comp.name+dataset.name+var, comp.name+dataset.name, *comp.cfg.bins)
    dataset.tree.Project(comp.name+dataset.name+var, var, comp.cfg.cut)
    histo.Scale(dataset.weight * comp.cfg.scale)
    comp.histogram.Add(histo)

def merge(comp, others):
    var = comp.cfg.variable
    for other in others:
        comp.histogram.Add(other.histogram)
