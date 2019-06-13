from ROOT import TH1F
import copy

class Component(object):
     ''' Python wrapper for ROOT histograms. Based on a Component_cfg object,
     this gives access to a histogram. Shortcuts for the name and the variable
     are also available, yet all information can be found in the cfg attribute.'''
     
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
     ''' A configuration class for components. Gives a dict
     containing all key words passed at init. Some defaults are
     provided, yet some key words are necessary, such as
     - name : component name, used for histograms names
              so this is important to differenciate
              differents components
     - variable : the variable that will be used to plot
     - dataset : the python class wrapper for the root
              source file containing the root tree
     '''

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
