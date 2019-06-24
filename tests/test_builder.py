#!/usr/bin/env python

from htt_plot.tools.builder import build_cfg, build_cfgs, create_component, merge_cfgs, merge_components, project

import unittest
from htt_plot.tools.dataset import Dataset

class TestBuilder(unittest.TestCase):

    def test_build_cfgs(self):
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
        DYJetsToLL_M50_ext = Dataset(
            'DYJetsToLL_M50_ext',
            basepath.format('DYJetsToLL_M50_ext'),
            n_ev_dy_incl, 5765.4,
            treename = treename
        )
        
        DY_datasets = [DYJetsToLL_M50,DYJetsToLL_M50_ext]
        ZTT_cfgs = build_cfgs(
            [dataset.name+'_ZTT' for dataset in DY_datasets], 
            DY_datasets, variable,
            cut, bins)
        
        self.assertEqual(
            len(ZTT_cfgs),
            2)
        
        self.assertEqual(
            ZTT_cfgs[0]['name'],
            '_'.join([DY_datasets[0].name, 'ZTT']))
        
        self.assertEqual(
            ZTT_cfgs[0]['dataset'],
            DY_datasets[0])
        
        self.assertEqual(
            ZTT_cfgs[0]['variable'],
            variable)
        
        self.assertEqual(
            ZTT_cfgs[0]['cut'],
            cut)
        
        self.assertEqual(
            ZTT_cfgs[0]['bins'],
            bins)

        return ZTT_cfgs

    def test_create_delayed_comps(self):
        ZTT_cfgs = self.test_build_cfgs()
        for cfg in ZTT_cfgs :
            cfg['dataset'].weight = .5
            cfg['dataset'].scale = 1
        delayed_comps = [create_component(cfg) for cfg in ZTT_cfgs]
        from dask import compute
        comps = compute(*delayed_comps)

        self.assertEqual(
            ZTT_cfgs[0]['dataset'].tree.GetEntries(),
            comps[0].histogram.GetEntries())
        
        self.assertEqual(
            ZTT_cfgs[0]['dataset'].tree.GetEntries()*ZTT_cfgs[0]['dataset'].weight*ZTT_cfgs[0]['dataset'].scale,
            comps[0].histogram.Integral())
        
        self.assertEqual(
            len(ZTT_cfgs),
            len(comps))

        return ZTT_cfgs, delayed_comps

    def test_merge_comps(self):
        ZTT_cfgs, delayed_comps = self.test_create_delayed_comps()
        by_cfg = merge_cfgs('cfg', ZTT_cfgs)
        by_comp = merge_components('comp', delayed_comps)

        from dask import compute
        by_cfg = compute(by_cfg)[0]
        by_comp = compute(by_comp)[0]

        self.assertEqual(
            by_cfg.histogram.Integral(),
            by_comp.histogram.Integral())
        
        self.assertEqual(
            ZTT_cfgs[0]['dataset'].tree.GetEntries()*ZTT_cfgs[0]['dataset'].weight*ZTT_cfgs[0]['dataset'].scale \
            + ZTT_cfgs[1]['dataset'].tree.GetEntries()*ZTT_cfgs[1]['dataset'].weight*ZTT_cfgs[1]['dataset'].scale,
            by_comp.histogram.Integral())

if __name__ == '__main__':   
    unittest.main()
