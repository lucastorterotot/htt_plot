from ROOT import TH1F
import copy
from itertools import count


class Component(object):
     ''' Python wrapper for ROOT histograms. Based on a Component_cfg object,
     this gives access to a histogram. Shortcuts for the name and the variable
     are also available, yet all information can be found in the cfg attribute.'''
     _ids = count(0)
     
     def __init__(self, component_cfg):
          '''Init with a Component_cfg object, which must have at least a name and
          a variable'''
          self.id = next(self._ids)
          self.cfg = component_cfg
          self.name = self.cfg['name']
          self.var = self.cfg['variable']
          TH1F_str = '_'.join([self.name, str(self.id)])
          self.histogram = TH1F(TH1F_str, TH1F_str, *self.cfg['bins'])
          
     def Clone(self, name):
          '''Get a new component wich only differs from the previous by its name and id'''
          new = copy.copy(self)
          new.name = name
          new.id = next(self._ids)
          TH1F_str = '_'.join([new.name, str(new.id)])
          new.histogram = self.histogram.Clone(TH1F_str)
          new.histogram.SetTitle(TH1F_str)
          return new

class Hist_Component(Component):
     
     def __init__(self,hist):
          self.id = next(self._ids)
          self.name = hist.GetName()
          self.histogram = hist
          
          
     
class Component_cfg(dict):
     defaults = {
          'cut' : '1',
          'bins' : (30, 0., 300.),
          'stack' : True,
          'nevts' : 0,
          'scale' : 1,
     }
     
     def __init__(self, **kwargs):
          ''' A configuration class for components. Gives a dict
          containing all key words passed at init. Some defaults are
          provided, yet some keywords are necessary, such as
          - name : component name, used for histograms names
              so this is important to differenciate
              differents components
          - variable : the variable that will be used to plot
          - dataset : the python class wrapper for the root
              source file containing the root tree
          - xsection : if not provided, dataset.xsection will be used
          '''
          init_dict = copy.copy(self.defaults)
          init_dict.update(kwargs)
          super(Component_cfg, self).__init__(init_dict)
          if not 'xsection' in self:
               # as user must provide a dataset
               self['xsection'] = self['dataset'].xsection
