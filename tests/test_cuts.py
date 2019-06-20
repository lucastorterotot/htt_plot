#!/usr/bin/env python

from htt_plot.tools.cut import Cut, Cuts

cuts_triggers = Cuts(
    doubletau_lowpt = 'trg_doubletau_lowpt',
    doubletau_mediso = 'trg_doubletau_mediso',
    doubletau = 'trg_doubletau',
)

any_triggers = cuts_triggers.any()
all_triggers = cuts_triggers.all()

any_triggers_test = Cut(
    '((trg_doubletau) || (trg_doubletau_mediso) || (trg_doubletau_lowpt))'
    )
all_triggers_test = Cut(
    '((trg_doubletau) && (trg_doubletau_mediso) && (trg_doubletau_lowpt))'
    )

cuts_datacards = Cuts(
    VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
)
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']
cuts_datacards_VV = Cut(
    '((l1_gen_match == 5 && l2_gen_match == 5)) || (!(l1_gen_match == 5 && l2_gen_match == 5))'
    )

cut_os = Cut('l1_q != l2_q')
cut_ss = ~cut_os
not_cut_os = Cut('!(l1_q != l2_q)')
cut_os_and_cut_ss = Cut('(l1_q != l2_q) && (!(l1_q != l2_q))')
cut_os_or_cut_ss = Cut('(l1_q != l2_q) || (!(l1_q != l2_q))')

weight = Cut('weight')

cut_os_times_weight = Cut('(l1_q != l2_q) * (weight)')
cut_os_itimes_weight = Cut('l1_q != l2_q')
cut_os_itimes_weight *= weight

import unittest

class TestCuts(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(weight),
            'weight',
            "Cut str fails")

    def test_and(self):
        self.assertEqual(
            str(cut_os & cut_ss),
            str(cut_os_and_cut_ss),
            "Cut and fails")

    def test_and_not(self):
        self.assertEqual(
            str(cut_os & ~cut_os),
            str(cut_os_and_cut_ss),
            "Cut and not fails")

    def test_or(self):
        self.assertEqual(
            str(cut_os | cut_ss),
            str(cut_os_or_cut_ss),
            "Cut or fails")

    def test_not(self):
        self.assertEqual(
            str(cut_ss),
            str(not_cut_os),
            "Cut not fails")

    def test_mul(self):
        self.assertEqual(
            str(cut_os*weight),
            str(cut_os_times_weight),
            "Cut mul fails")

    def test_imul(self):
        self.assertEqual(
            str(cut_os_times_weight),
            str(cut_os_times_weight),
            "Cut imul fails")

    def test_any(self):
        self.assertEqual(
            str(any_triggers),
            str(any_triggers_test),
            "Cuts any fails")

    def test_all(self):
        self.assertEqual(
            str(all_triggers),
            str(all_triggers_test),
            "Cuts all fails")

    def test_setitem(self):
        self.assertEqual(
            str(cuts_datacards['VV']),
            str(cuts_datacards_VV),
            "Cuts setitem fails")

if __name__ == '__main__':   
    unittest.main()
