#!/usr/bin/env python

from htt_plot.tools.cut import Cut, Cuts

import unittest

class TestCuts(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(Cut('weight')),
            'weight')

    def test_and(self):
        self.assertEqual(
            str(Cut('l1_q != l2_q') & Cut('!(l1_q != l2_q)')),
            str(Cut('(l1_q != l2_q) && (!(l1_q != l2_q))')))

    def test_and_not(self):
        self.assertEqual(
            str(Cut('l1_q != l2_q') & ~Cut('l1_q != l2_q')),
            str(Cut('(l1_q != l2_q) && (!(l1_q != l2_q))')))

    def test_or(self):
        self.assertEqual(
            str(Cut('l1_q != l2_q') | Cut('!(l1_q != l2_q)')),
            str(Cut('(l1_q != l2_q) || (!(l1_q != l2_q))')))

    def test_not(self):
        self.assertEqual(
            str(~Cut('l1_q != l2_q')),
            str(Cut('!(l1_q != l2_q)')))

    def test_mul(self):
        self.assertEqual(
            str(Cut('l1_q != l2_q') * Cut('weight')),
            str(Cut('(l1_q != l2_q) * (weight)')))

    def test_imul(self):
        cut_os_itimes_weight = Cut('l1_q != l2_q')
        cut_os_itimes_weight *= Cut('weight')
        self.assertEqual(
            str(cut_os_itimes_weight),
            str(Cut('(l1_q != l2_q) * (weight)')))

    def test_any(self):
        cuts_triggers = Cuts(
            doubletau_lowpt = 'trg_doubletau_lowpt',
            doubletau_mediso = 'trg_doubletau_mediso',
            doubletau = 'trg_doubletau',
        )
        any_triggers_test = Cut(
            '((trg_doubletau_lowpt) || (trg_doubletau) || (trg_doubletau_mediso))'
        )
        self.assertEqual(
            str(cuts_triggers.any()),
            str(any_triggers_test))

    def test_all(self):
        cuts_triggers = Cuts(
            doubletau_lowpt = 'trg_doubletau_lowpt',
            doubletau_mediso = 'trg_doubletau_mediso',
            doubletau = 'trg_doubletau',
        )
        all_triggers_test = Cut(
            '((trg_doubletau) && (trg_doubletau_mediso) && (trg_doubletau_lowpt))'
        )
        self.assertEqual(
            str(cuts_triggers.all()),
            str(all_triggers_test))

    def test_setitem(self):
        cuts_datacards = Cuts(
            VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
            VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
        )
        cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']
        cuts_datacards_VV = Cut(
            '((l1_gen_match == 5 && l2_gen_match == 5)) || (!(l1_gen_match == 5 && l2_gen_match == 5))'
        )
        self.assertEqual(
            str(cuts_datacards['VV']),
            str(cuts_datacards_VV))

if __name__ == '__main__':   
    unittest.main()
