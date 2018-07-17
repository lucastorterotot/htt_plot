import unittest

from efficiencies import Efficiencies

# getting a test tree
import os
from ROOT import TFile
test_fname = os.path.dirname(__file__) + '../test/data/WJetsToLNu_LO_ext.root'
test_file = TFile(test_fname)
tree = test_file.Get('tree')

# getting cuts
from htt_plot.cuts.generic import cuts_generic
from htt_plot.cuts.mt import cuts_mt
cuts = cuts_generic + cuts_mt
print cuts

class TestEfficiencies(unittest.TestCase):
        
    def test_1(self):
        eff = Efficiencies(tree, cuts)
        eff.marginal()
        
    def test_2(self):
        eff = Efficiencies(tree, cuts)
        eff.fill_cut_flow()
        print eff.str_cut_flow()

if __name__ == '__main__':
    unittest.main()
