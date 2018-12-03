import copy 
import config
from dask import delayed, compute
from ROOT import TH1F

class Component(object):
     
     def __init__(self, name, datasets, var, cut, *args):
          self.name = name
          self.var = var
          self.cut = cut
          self.args = args
          self.stack = True
          if not isinstance(datasets, list):
               self.datasets = [datasets]
          else:
               self.datasets = datasets
          self.histogram = TH1F(name, name, *args)
          if config.parallel:
               self.delayed_objs = []
               for dataset in self.datasets:
                    self.delayed_objs.append(delayed(self._add_dataset)(dataset))
               compute(*self.delayed_objs)
               for dataset in self.datasets:
                    self.histogram.Add(dataset.histogram)
          else:
               for dataset in self.datasets:
                    self._add_dataset(dataset)
                    self.histogram.Add(dataset.histogram)
               
     def _add_dataset(self, dataset):
          if not isinstance(dataset, Component):
               dataset.histogram = TH1F(self.name+dataset.name, self.name+dataset.name, *self.args)
               dataset.tree.Project(self.name+dataset.name, self.var, self.cut)
          
     def Clone(self, name):
          new = Component(name, self.datasets, self.var, self.cut,*self.args)
          new.histogram = self.histogram.Clone(name)
          return new

     def Add(self, other):
          self.histogram.Add(other.histogram)
     
     def __getattr__(self, attr):
          return getattr(self.histogram, attr)
 
