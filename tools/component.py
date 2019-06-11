from ROOT import TH1F

class Component(object):
     def __init__(self, component_cfg):
          self.histogram = {}
          self.cfg = component_cfg
          self.name = self.cfg.name
          for var in self.cfg.variables:
               self.histogram[var] = TH1F(self.name+'_'+var, self.name+'_'+var, *self.cfg.bins[var])
               
class Component_cfg(object):
     
     def __init__(self, name, dataset, variables, cut, bins):
          self.name = name
          self.variables = variables
          self.cut = cut
          self.bins = bins
          self.stack = True
          self.dataset = dataset
          self.nevts = 0
          self.xsection = self.dataset.xsection
          self.scale = 1
