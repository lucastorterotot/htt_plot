from ROOT import TH1F

class Component(object):
     def __init__(self, component_cfg, init_TH1F=True):
          self.cfg = component_cfg
          self.name = self.cfg.name
          if init_TH1F:
               self.init_hist()

     def init_hist(self):
          var = self.cfg.variable
          self.histogram = TH1F(self.name+'_'+var, self.name+'_'+var, *self.cfg.bins)
          
     def get_copy(self, name):
          new = Component(self.cfg, init_TH1F=False)
          new.name = name
          new.init_hist()
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
