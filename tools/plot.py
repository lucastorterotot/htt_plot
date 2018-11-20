from ROOT import TH1F 
from dask import delayed
from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component

import config

def hist(name, dataset, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    comp = Component(name, *bins)
    dataset.tree.Project(comp.GetName(), var, cut)
    print 'histogramming', name, comp.GetEntries()
    return comp

def add(name, components):
    print 'adding'
    comp = components[0].Clone(name)
    comp.Reset()
    for other_hist in components:
        comp.Add(other_hist)
    return comp

def scale(component, factor):
    print 'scaling'
    component.Scale(factor)
    return component

if config.parallel:
    hist = delayed(hist)
    add = delayed(add)
    scale = delayed(scale)
