from ROOT import TH1F

class Component(object):
     def __init__(self, component_cfg):
          self.histogram = {}
          self.cfg = component_cfg
          self.name = self.cfg.name
          for var in self.cfg.variables:
               self.histogram[var] = TH1F(self.name+var, self.name+var, *self.cfg.bins[var])
               
class Component_cfg(object):
     
     def __init__(self, name, datasets, variables, cut, bins):
          self.name = name
          self.variables = variables
          self.cut = cut
          self.bins = bins
          self.stack = True
          if not isinstance(datasets, list):
               self.datasets = [datasets]
          else:
               self.datasets = datasets
          self.nevts = 0
          if not all([ds.xsection==self.datasets[0].xsection for ds in self.datasets]):
               print '!!!xsection not same in all datasets!!!'
               import pdb;pdb.set_trace()
          self.xsection = self.datasets[0].xsection
          self.scale = 1
