from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component, Component_cfg
from dask import delayed
import copy

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
    merged = copy.copy(comps[0])
    merged.name = name
    comps.remove(comps[0])
    merged.merge(comps)
    return merged

merge_components = delayed(_merge_components)
