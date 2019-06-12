from htt_plot.tools.cut import Cuts
import pprint

t1_cuts_tt = Cuts(
    l1_pt = 'l1_pt > 40',
    l1_eta = 'abs(l1_eta) < 2.1',
    l1_iso = 'l1_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_charge = 'abs(l1_q) == 1.',
    l1_vertex = 'abs(l1_dz) < 0.2',
    l1_decaymode = 'l1_decayModeFinding > 0.5',
    l1_against_e = 'l1_againstElectronVLooseMVA6 > 0.5',
    l1_against_mu = 'l1_againstMuonLoose3 > 0.5',
)

t2_cuts_tt = Cuts(
    l2_pt = 'l2_pt > 40',
    l2_eta = 'abs(l2_eta) < 2.1',
    l2_iso = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_charge = 'abs(l2_q) == 1.',
    l2_vertex = 'abs(l2_dz) < 0.2',
    l2_decaymode = 'l2_decayModeFinding > 0.5',
    l2_against_e = 'l2_againstElectronVLooseMVA6 > 0.5',
    l2_against_mu = 'l2_againstMuonLoose3 > 0.5',
)

m_cuts_mt = Cuts(
    l1_pt = 'l1_pt >= 21',
    l1_eta = 'abs(l1_eta) <= 2.1',
    l1_iso = 'l1_iso < 0.3',
    l1_vertex = 'abs(l1_dxy) < 0.045 && abs(l1_dz) < 0.2',
)

t_cuts_mt = Cuts(
    l2_pt = 'l2_pt >= 23',
    l2_eta = 'abs(l2_eta) <= 2.3',
    l2_iso = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_charge = 'abs(l2_q) == 1.',
    l2_vertex = 'abs(l2_dz) < 0.2',
    l2_decaymode = 'l2_decayModeFinding > 0.5',
    l2_against_e = 'l2_againstElectronVLooseMVA6 > 0.5',
    l2_against_mu = 'l2_againstMuonLoose3 > 0.5',
)

e_cuts_et = Cuts(
    l1_pt = 'l1_pt >= 25',
    l1_eta = 'abs(l1_eta) <= 2.1',
    l1_iso = 'l1_iso < 0.3',
    l1_vertex = 'abs(l1_dxy) < 0.045 && abs(l1_dz) < 0.2',
)

t_cuts_et = t_cuts_mt.clone()

cuts_signal = Cuts(
    mt_tot = 'mt_tot < 40',
)

cuts_btag_1 = Cuts(
    Btag_1 = 'bjet1_csv > 0',
)

cuts_btag_2 = Cuts(
    Btag_2 = 'bjet2_csv > 0',
)

cuts_tt = t1_cuts_tt + t2_cuts_tt + cuts_signal
cuts_mt = m_cuts_mt + t_cuts_mt + cuts_signal
cuts_et = e_cuts_et + t_cuts_et + cuts_signal
