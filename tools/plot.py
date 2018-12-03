from ROOT import TH1F 
from dask import delayed, compute
from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component

import config

def build_component(name, datasets, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    comp = Component(name, datasets, var, cut, *bins)
    print 'histogramming', name, comp.GetEntries()
    return comp

def build_components(names, datasets, var, cut, *bins):
    components = []
    for name, dataset in zip(names, datasets):
        if config.parallel:
            components.append(delayed(build_component)(name,dataset,var,cut,*bins))
        else:
            components.append(build_component(name,dataset,var,cut,*bins))
    if config.parallel:
        components = list(compute(*components))
    return components

def merge_components(name, components):
    print 'adding'
    comp = components[0].Clone(name)
    comp.Reset()
    for other_hist in components:
        comp.Add(other_hist)
    return comp

def scale_component(component, factor):
    print 'scaling'
    component.Scale(factor)
    return component

#if config.parallel:
    #build_component = delayed(build_component)
    #merge_components = delayed(merge_components)
    #scale_component = delayed(scale_component)
