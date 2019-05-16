import copy 
from dask import delayed, compute
from ROOT import TH1F

class Component(object):
     
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
          self.histogram = {}
          for var in self.variables:
               import locale; locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
               self.histogram[var] = TH1F(name+var, name+var, *self.bins[var])
               self.histogram[var].Draw()
          self.delayed_objs = []
          for dataset in self.datasets:
               self.delayed_objs.append(delayed(self._add_dataset)(dataset))
          compute(*self.delayed_objs)
          for dataset in self.datasets:
               for var in self.variables:
                    self.histogram[var].Add(dataset.histogram[var])
                    
     def _add_dataset(self, dataset, verbose=True):
          for var in self.variables:
               if not isinstance(dataset, Component):
                    if not hasattr(dataset,'histogram'):
                         dataset.histogram = {}
                    dataset.histogram[var] = TH1F(self.name+dataset.name+var, self.name+dataset.name, *self.bins[var])
                    if not hasattr(dataset.tree,'Project'):
                         import pdb;pdb.set_trace()
                    dataset.tree.Project(self.name+dataset.name+var, var, self.cut)
                    if verbose:
                         print '\n', 'component :',self.name, 'dataset :',dataset.name
                         if not dataset.is_data:
                              print 'lumi prescale:', dataset.nevts/dataset.xsection
                              print 'lumiweight:', dataset.weight
                         print 'integral prescale:', dataset.histogram[var].Integral()
                    dataset.histogram[var].Scale(dataset.weight)
                    if verbose:
                         print 'integral postscale:', dataset.histogram[var].Integral()
                    
     def Clone(self, name):
          new = Component(name, self.datasets, self.variables, self.cut,self.bins)
          for var in self.variables:
               new.histogram[var] = self.histogram[var].Clone(name)
          return new

     def Add(self, other, weight=1.):
          self.datasets.extend(other.datasets)
          if weight == 1.:
               self.histogram.Add(other.histogram)
          else:
               self.histogram.Add(other.histogram,weight)

     def reset(self):
          for var in self.variables:
               self.histogram[var].Reset()
     
     def __getattr__(self, attr):
          return getattr(self.histogram, attr)
 
