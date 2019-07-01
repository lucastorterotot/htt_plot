''' General config file for plotting and datacards.
tau-tau channel
'''
from htt_plot.tools.cut import Cut, Cuts

channel = 'tt'

# binning
from htt_plot.channels_configs.htt_common import bins

# variables
from htt_plot.channels_configs.htt_common import variables, datacards_variables

# cuts
from htt_plot.channels_configs.htt_common import cut_mt_tot, cuts_flags, cuts_vetoes, cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine, cut_btag_1, cut_btag_2

cuts_l1 = Cuts(
    l1_pt = 'l1_pt > 40',
    l1_eta = 'abs(l1_eta) < 2.1',
    l1_iso = 'l1_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_charge = 'abs(l1_q) == 1.',
    l1_vertex = 'abs(l1_dz) < 0.2',
    l1_decaymode = 'l1_decayModeFinding > 0.5',
)

cuts_l2 = Cuts(
    l2_pt = 'l2_pt > 40',
    l2_eta = 'abs(l2_eta) < 2.1',
    l2_iso = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_charge = 'abs(l2_q) == 1.',
    l2_vertex = 'abs(l2_dz) < 0.2',
    l2_decaymode = 'l2_decayModeFinding > 0.5',
)

cuts_against_leptons = Cuts(
    l1_against_e = 'l1_againstElectronVLooseMVA6 > 0.5',
    l1_against_mu = 'l1_againstMuonLoose3 > 0.5',
    l2_against_e = 'l2_againstElectronVLooseMVA6 > 0.5',
    l2_against_mu = 'l2_againstMuonLoose3 > 0.5',
)

cut_signal = cuts_l1.all() & cuts_l2.all() & cuts_against_leptons.all() & cut_mt_tot

## triggers
cuts_triggers = Cuts(
    singletau = 'trg_singletau',
    doubletau_35_mediso = 'trg_doubletau_35_mediso',
    doubletau_35_tightiso_tightid = 'trg_doubletau_35_tightiso_tightid',
    doubletau_40_mediso_tightid = 'trg_doubletau_40_mediso_tightid',
    doubletau_40_tightiso = 'trg_doubletau_40_tightiso',
    )
# # tmp hack for old variable names
# cuts_triggers = Cuts(
#     doubletau_lowpt = 'trg_doubletau_lowpt',
#     doubletau_mediso = 'trg_doubletau_mediso',
#     doubletau = 'trg_doubletau',
# )

cut_triggers = cuts_triggers.any()

basic_cuts = cuts_flags.all() & cuts_vetoes.all() & cut_triggers & cut_os & cuts_against_leptons.all()

## iso
cuts_iso = Cuts(
    l1_VTight = 'l1_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_Tight = 'l1_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_VLoose = 'l1_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l1_VVLoose = 'l1_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

## datacards
cuts_datacards = Cuts(
    ZTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    ZL = 'l1_gen_match < 6 && l2_gen_match < 6 && !(l1_gen_match == 5 && l2_gen_match == 5)',
    ZJ = 'l1_gen_match == 6 || l2_gen_match == 6',
    TTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    TTJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    W = '1',
    jetFakes = '1',
)
cuts_datacards['ZLL'] = cuts_datacards['ZL'] | cuts_datacards['ZJ']
cuts_datacards['TT'] = cuts_datacards['TTT'] | cuts_datacards['TTJ']
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']

# weights
from htt_plot.channels_configs.htt_common import weights

# datasets
import htt_plot.datasets.gael_all as datasets

# ### tmp hack
# cut_signal = cuts_iso['l1_Tight'] & cuts_iso['l2_Tight'] & basic_cuts
