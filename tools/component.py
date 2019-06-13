from ROOT import TH1F
import copy

class Component(object):
     
     def __init__(self, component_cfg, init_TH1F=True):
          self.cfg = component_cfg
          self.name = self.cfg['name']
          self.var = self.cfg['variable']
          self.histogram = TH1F(self.name+'_'+self.var, self.name+'_'+self.var, *self.cfg['bins'])
          
     def Clone(self, name):
          new = copy.copy(self)
          new.name = name
          new.histogram = self.histogram.Clone(new.name+'_'+new.var)
          new.histogram.SetTitle(new.name+'_'+new.var)
          return new
          
class Component_cfg(dict):

     defaults = {
          'cut' : '1',
          'bins' : (30, 0., 300.),
          'stack' : True,
          'nevts' : 0,
          'scale' : 1,
     }
     
     def __init__(self, **kwargs):
          super(Component_cfg, self).__init__(Component_cfg.defaults)
          super(Component_cfg, self).__init__(kwargs)
          if not 'xsection' in self:
               # as user must provide a dataset
               self['xsection'] = self['dataset'].xsection
