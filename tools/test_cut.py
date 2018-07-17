import unittest
import pprint 
from cut import *

class TestCut(unittest.TestCase):
    
    def test_1_cut(self):
        cut = Cut('a', 'p>1')
        self.assertEqual(str(cut), 'p>1')
        neg = ~cut
        self.assertEqual(str(neg), '!(p>1)')
        cut2 = Cut('b', 'e<0')
        cut_and_cut2 = cut & cut2
        self.assertEqual(str(cut_and_cut2), '(p>1) && (e<0)')
        neg = ~cut_and_cut2
        self.assertEqual(str(neg), '!((p>1) && (e<0))')
        
    def test_2_cutflow(self):
        cuts = CutFlow([
            ('pcut', 'p>1'),
            ('ecut', 'e<0')
        ])
        
    def test_3_cutflow_and_cut(self):
        cuts = CutFlow([
            ('pcut', 'p>1'),
            ('ecut', 'e<0')
        ])
        cut =  Cut('a', 'p==3')
        cuts2 = cuts + cut
        cuts += cut
        
    
if __name__ == '__main__':
    unittest.main()
