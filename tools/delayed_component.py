import copy 
from dask import delayed, compute
from ROOT import TH1F
     
class Component(object):
     def __init__(self, component_cfg):
          self.histogram = {}
          self.cfg = component_cfg
          self.name = self.cfg.name
          for var in self.cfg.variables:
               import locale; locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
               self.histogram[var] = TH1F(self.name+var, self.name+var, *self.cfg.bins[var])
               self.histogram[var].Draw()

     def project(self, verbose=False):
          for dataset in self.cfg.datasets:
               for var in self.cfg.variables:
                    histo = TH1F(self.cfg.name+dataset.name+var, self.cfg.name+dataset.name, *self.cfg.bins[var])
                    if not hasattr(dataset.tree,'Project'):
                         import pdb;pdb.set_trace()
                    dataset.tree.Project(self.cfg.name+dataset.name+var, var, self.cfg.cut)
                    if histo.Integral() == 0 and 'fake' in self.name:
                         print '\n', 'component :',self.cfg.name, 'dataset :',dataset.name
                         print dataset
                         print dataset.tree
                    if verbose:
                         print '\n', 'component :',self.cfg.name, 'dataset :',dataset.name
                         if not dataset.is_data:
                              print 'lumi prescale:', dataset.nevts/dataset.xsection
                              print 'lumiweight:', dataset.weight
                         print 'integral prescale:', histo.Integral()
                    histo.Scale(dataset.weight)
                    histo.Scale(self.cfg.scale)
                    if verbose:
                         print 'integral postscale:', histo.Integral()
                    self.histogram[var].Add(histo)
                    
     def Clone(self, name):
          new = Component(self.cfg)
          for var in self.cfg.variables:
               new.histogram[var] = self.histogram[var].Clone(name)
          return new

     def merge(self, others):
          for var in self.cfg.variables:
               for other in others:
                    self.histogram[var].Add(other.histogram[var])
          

     def Add(self, other, weight=1.):
          self.cfg.datasets.extend(other.datasets)
          if weight == 1.:
               self.histogram.Add(other.histogram)
          else:
               self.histogram.Add(other.histogram,weight)

     def reset(self):
          for var in self.cfg.variables:
               self.histogram[var].Reset()     
               
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
