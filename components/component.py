from ROOT import TFile

class Component(object):
    
    def __init__(self, name, rootfname, nevts=None, xsection=None):
        self.name = name
        self.rootfname = rootfname
        self.nevts = nevts
        self.xsection = xsection
        self.tfile = TFile(rootfname)
        self.tree = self.tfile.Get('tree')
        
