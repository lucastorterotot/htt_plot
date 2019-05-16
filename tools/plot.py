from ROOT import TH1F 
from dask import delayed, compute
from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component, Component_cfg

def build_component(name, datasets, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    comp = Component_cfg(name, datasets, var, cut, *bins)
    # print 'histogramming', name, comp.GetEntries()
    return comp

def build_components(names, datasets, var, cut, *bins):
    components = []
    for name, dataset in zip(names, datasets):
        components.append(build_component(name,dataset,var,cut,*bins))
    return components

def merge_components(name, components, extension=False):
    print 'adding'
    comp = components[0].Clone(name)
    comp.reset()
    for other_hist in components:
        for var in comp.variables:
            comp.histogram[var].Add(other_hist.histogram[var])
    return comp

def scale_component(component, factor):
    print 'scaling'
    component.Scale(factor)
    return component

#build_component = delayed(build_component)
#merge_components = delayed(merge_components)
#scale_component = delayed(scale_component)
