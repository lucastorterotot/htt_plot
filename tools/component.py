from ROOT import TH1F
import copy

class Component(object):
     def __init__(self, component_cfg, init_TH1F=True):
          self.cfg = component_cfg
          self.name = self.cfg.name
          self.var = self.cfg.variable
          self.histogram = TH1F(self.name+'_'+self.var, self.name+'_'+self.var, *self.cfg.bins)
          
     def Clone(self, name):
          new = copy.copy(self)
          new.name = name
          new.histogram = self.histogram.Clone(new.name+'_'+new.var)
          new.histogram.SetTitle(new.name+'_'+new.var)
          return new
          
class Component_cfg(object):
     
     def __init__(self, name, dataset, variable, cut, bins):
          self.name = name
          self.variable = variable
          self.cut = str(cut)
          self.bins = bins
          self.stack = True
          self.dataset = dataset
          self.nevts = 0
          self.xsection = self.dataset.xsection
          self.scale = 1
