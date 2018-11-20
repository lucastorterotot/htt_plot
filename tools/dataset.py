from ROOT import TFile

class Dataset(object):
    '''represents a dataset on disk
    
    attributes:
    tree
    norm_factor : additional normalization factor
    
    for MC components
    nevts : number of events generated
    xsection : xsection   
    '''
    
    def __init__(self, name, rootfname, nevts=None, xsection=None, norm_factor = 1.):
        self.name = name
        self.rootfname = rootfname
        self.nevts = nevts
        self.xsection = xsection
        self.norm_factor = norm_factor
        if xsection and nevts:
            self.is_data = False
        elif xsection or nevts:
            raise ValueError('provide both xsection and nevts, or neither')
        else:
            self.is_data = True
        self.tfile = TFile(rootfname)
        self.tree = self.tfile.Get('tree')
        
    def lumi_eq(self):
        return float(self.nevts) / self.xsection * self.norm_factor
        
    def compute_weight(self, lumi_data = None):
        if self.is_data:
            self.weight = self.norm_factor
        else:
            if not lumi_data:
                raise ValueError('provide lumi to weight MC component')
            self.weight = float(self.xsection)*lumi_data/self.nevts*self.norm_factor
        return self.weight

