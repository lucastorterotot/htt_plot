from ROOT import TFile

class Component(object):
    
    def __init__(self, name, rootfname, nevts=None, xsection=None):
        self.name = name
        self.rootfname = rootfname
        self.nevts = nevts
        self.xsection = xsection
        self.tfile = TFile(rootfname)
        self.tree = self.tfile.Get('tree')
        if nevts is not None and xsection is not None:
            self.lumi_eq = nevts/xsection
        
    def compute_weight(self, lumi_data):
        self.weight = self.xsection*lumi_data
