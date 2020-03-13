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
    
    def __init__(self, name, rootfname, nevts=None, xsection=None, norm_factor = 1., treename='tree'):
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
        self.file = rootfname
        self.treename = treename
        
    def lumi_eq(self):
        return float(self.nevts) / self.xsection * self.norm_factor
        
    def compute_weight(self, lumi_data = None, stitched=False):
        if self.is_data or stitched:
            self.weight = self.norm_factor
        else:
            if not lumi_data:
                raise ValueError('provide lumi to weight MC component')
            self.weight = (float(self.xsection)*lumi_data)/(self.nevts*self.norm_factor)
        return self.weight

