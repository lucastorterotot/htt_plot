from ROOT import TH1F

class Component(object):
     def __init__(self, component_cfg, init_TH1F=True):
          self.cfg = component_cfg
          self.name = self.cfg.name
          if init_TH1F:
               self.init_hists()

     def init_hists(self):
          self.histogram = {}
          for var in self.cfg.variables:
               self.histogram[var] = TH1F(self.name+'_'+var, self.name+'_'+var, *self.cfg.bins[var])
          
     def get_copy(self, name):
          new = Component(self.cfg, init_TH1F=False)
          new.name = name
          new.init_hists()
          return new
          
class Component_cfg(object):
     
     def __init__(self, name, dataset, variables, cut, bins):
          self.name = name
          self.variables = variables
          self.cut = str(cut)
          self.bins = bins
          self.stack = True
          self.dataset = dataset
          self.nevts = 0
          self.xsection = self.dataset.xsection
          self.scale = 1
