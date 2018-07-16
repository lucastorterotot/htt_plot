from ROOT import TH1F 

class Histogram(object):

    def __init__(self, *args):
        self.h = TH1F(*args)
        self.args = args
        
    def Clone(self, name):
        return Histogram(name, name, *self.args[2:])
    
    def Add(self, other):
        self.h.Add(other.h)
    
    def __getattr__(self, attr):
        return getattr(self.h, attr)


def hist(name, component, var, cut, *bins):
    histo = Histogram(name, name, *bins)
    component.tree.Project(histo.GetName(), var, cut)
    print 'histogramming', name, histo.GetEntries()
    return histo

def add(name, hists):
    print 'adding'
    histo = hists[0].Clone('name')
    histo.Reset()
    for other_hist in hists:
        histo.Add(other_hist)
    return histo
