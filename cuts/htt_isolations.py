from htt_plot.tools.cut import Cuts

cuts_iso_tt = Cuts(
    l1_VTight = 'l1_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_Tight = 'l1_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_VLoose = 'l1_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_VVLoose = 'l1_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

cuts_iso_mt = Cuts(
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

cuts_iso_et = cuts_iso_mt.clone()
