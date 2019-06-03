from htt_plot.tools.cut import Cut
from htt_plot.tools.delayed_component import Component_cfg
import copy

def build_component(name, datasets, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    comp = Component_cfg(name, datasets, var, cut, *bins)
    return comp

def build_components(names, datasets, var, cut, *bins):
    components = []
    for name, dataset in zip(names, datasets):
        components.append(build_component(name,dataset,var,cut,*bins))
    return components
