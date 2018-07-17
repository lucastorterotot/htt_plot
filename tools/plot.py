from ROOT import TH1F 
from dask import delayed
from htt_plot.tools.cut import Cut
from htt_plot.tools.component import Component

import config

def hist(name, dataset, var, cut, *bins):
    if isinstance(cut,Cut):
        cut = cut.cutstr
    histo = Component(name, *bins)
    dataset.tree.Project(histo.GetName(), var, cut)
    print 'histogramming', name, histo.GetEntries()
    return histo

def add(name, components):
    print 'adding'
    histo = components[0].Clone(name)
    histo.Reset()
    for other_hist in components:
        histo.Add(other_hist)
    return histo

if config.parallel:
    hist = delayed(hist)
    add = delayed(add)
