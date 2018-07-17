import copy 
from ROOT import TH1F

class Component(object):
     
     def __init__(self, name, *args):
          self.name = name
          self.histogram = TH1F(name, name, *args)
          self.args = args
          self.stack = True
          
     def Clone(self, name):
          return Component(name, *self.args)

     def Add(self, other):
          self.histogram.Add(other.histogram)
     
     def __getattr__(self, attr):
          return getattr(self.histogram, attr)
 
