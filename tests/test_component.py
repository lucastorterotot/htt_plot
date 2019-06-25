#!/usr/bin/env python

from htt_plot.tools.component import Component, Component_cfg
from htt_plot.tools.cut import Cut

import unittest
from htt_plot.tools.dataset import Dataset

class TestBuilder(unittest.TestCase):

    def test_cfg(self):
        import os 
        basepath = os.path.expandvars(
            '/data2/gtouquet/MSSM_Samples_310119/{}/tree_fakes.root')
        treename = 'events'
        variable = 'mt_tot'
        bins = (100, 0., 3000.)
        cut = ''
        
        n_ev_dy_incl = 48675378. + 49125561.
        DYJetsToLL_M50 = Dataset(
            'DYJetsToLL_M50',
            basepath.format('DYJetsToLL_M50'),
            n_ev_dy_incl, 5765.4,
            treename = treename
        )
        
        cfg1_cut = Cut('l1_pt > 30 || l2_pt > 30')
        cfg1 = Component_cfg(
            name = '_'.join([DYJetsToLL_M50.name, '1']),
            variable = variable,
            dataset = DYJetsToLL_M50,
            cut = cfg1_cut)

        cfg2 = Component_cfg(
            name = '_'.join([DYJetsToLL_M50.name, '2']),
            variable = variable,
            dataset = DYJetsToLL_M50)

        self.assertEqual(
            str(cfg1['cut']),
            str(cfg1_cut))

        self.assertEqual(
            cfg2['cut'],
            Component_cfg.defaults['cut'])

        return cfg1, cfg2

    def test_comp(self):
        cfg1, cfg2 = self.test_cfg()
        comp1 = Component(cfg1)
        comp2 = Component(cfg2)
        comp3 = comp1.Clone('clone')

        self.assertEqual(
            comp1.id + 1,
            comp2.id)

        self.assertEqual(
            comp1.name,
            cfg1['name'])

        self.assertEqual(
            comp1.var,
            cfg1['variable'])

        self.assertEqual(
            comp1.histogram.GetName(),
            '_'.join([comp1.name, comp1.var, str(comp1.id)]))

        self.assertEqual(
            comp1.id + 2,
            comp3.id)

        self.assertEqual(
            comp3.name,
            'clone')

        self.assertEqual(
            comp3.var,
            cfg1['variable'])

        self.assertEqual(
            comp3.histogram.GetName(),
            '_'.join(['clone', comp1.var, str(comp3.id)]))

        self.assertEqual(
            comp3.histogram.Integral(),
            comp1.histogram.Integral())

if __name__ == '__main__':   
    unittest.main()
