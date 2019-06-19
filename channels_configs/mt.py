''' General config file for plotting and datacards.
muon-tau channel
'''
from htt_plot.tools.cut import Cut, Cuts

channel = 'mt'

# binning
from htt_plot.channels_configs.htt_common import bins

# variables
from htt_plot.channels_configs.htt_common import variables, datacards_variables

# cuts
from htt_plot.channels_configs.htt_common import cut_mt_tot, cuts_flags, cuts_vetoes, cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine, cut_btag_1, cut_btag_2

cuts_l1 = Cuts(
    l1_pt = 'l1_pt >= 21',
    l1_eta = 'abs(l1_eta) <= 2.1',
    l1_iso = 'l1_iso < 0.3',
    l1_vertex = 'abs(l1_dxy) < 0.045 && abs(l1_dz) < 0.2',
)

cuts_l2 = Cuts(
    l2_pt = 'l2_pt >= 23',
    l2_eta = 'abs(l2_eta) <= 2.3',
    l2_iso = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_charge = 'abs(l2_q) == 1.',
    l2_vertex = 'abs(l2_dz) < 0.2',
    l2_decaymode = 'l2_decayModeFinding > 0.5',
)

cuts_against_leptons = Cuts(
    l2_against_e = 'l2_againstElectronVLooseMVA6 > 0.5',
    l2_against_mu = 'l2_againstMuonLoose3 > 0.5',
)

cut_signal = cuts_l1.all() & cuts_l2.all() & cuts_against_leptons.all() & cut_mt_tot

## triggers
cuts_triggers = Cuts(
    singlemuon_24 = 'trg_singlemuon_24',
    singlemuon_27 = 'trg_singlemuon_27',
    crossmuon_mu24tau20 = 'trg_crossmuon_mu24tau20',
    crossmuon_mu20tau27 = 'trg_crossmuon_mu20tau27',
)

cut_triggers = cuts_triggers.any()

basic_cuts = cuts_flags.all() & cuts_vetoes.all() & cut_triggers & cut_os & cuts_against_leptons.all()

## iso
cuts_iso = Cuts(
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

## datacards
cuts_datacards = Cuts(
    ZTT = 'l2_gen_match == 5',
    ZL = 'l2_gen_match < 5',
    ZJ = 'l2_gen_match == 6',
    TTT = 'l2_gen_match == 5',
    TTJ = 'l2_gen_match != 5',
    VVT = 'l2_gen_match == 5',
    VVJ = 'l2_gen_match != 5',
    W = '1',
    jetFakes = '1',
)
cuts_datacards['ZLL'] = cuts_datacards['ZL'] | cuts_datacards['ZJ']
cuts_datacards['TT'] = cuts_datacards['TTT'] | cuts_datacards['TTJ']
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']

# weights
from htt_plot.channels_configs.htt_common import weights

# datasets
#TODO change
import htt_plot.datasets.gael_all as datasets
