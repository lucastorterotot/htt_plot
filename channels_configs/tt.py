''' General config file for plotting and datacards.
tau-tau channel
'''
from htt_plot.tools.cut import Cut, Cuts

channel = 'tt'

# binning
from htt_plot.channels_configs.htt_common import bins

# variables
from htt_plot.channels_configs.htt_common import variables, datacards_variables, var_name_dict

# cuts
from htt_plot.channels_configs.htt_common import cut_mt_tot, cuts_flags, cuts_vetoes, cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_btag_1, cut_btag_2, cut_btag, cut_nobtag

cut_dy_promptfakeleptons = Cut(
    'l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2')

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

cut_signal = cuts_l1.all() & cuts_l2.all() & cuts_against_leptons.all() #& cut_mt_tot

#singletau = 'trg_singletau',
## triggers
cuts_triggers = Cuts(
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

basic_cuts = cuts_flags.all() & cuts_vetoes.all() & cut_triggers & cut_os & cuts_against_leptons.all()# test cuts_os

### CAREFUL HERE ONLY CHANGE TO TEST

# basic_cuts = basic_cuts & Cut('j1_pt > 30 && j2_pt > 30')

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

## cut embedding + no fakes (for MC)

cut_embed = Cut('(l1_gen_match == 5) && (l2_gen_match == 5)')

cut_not_embed = ~cut_embed

cut_fakes = Cut('l1_gen_match==6 || l2_gen_match==6')

cut_not_fakes = ~cut_fakes

cut_not_fakes_not_embed = cut_not_embed & cut_not_fakes

## datacards
cuts_datacards = Cuts(
    ZTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    ZL = 'l1_gen_match < 6 && l2_gen_match < 6 && !(l1_gen_match == 5 && l2_gen_match == 5)',
    ZJ = 'l1_gen_match == 6 || l2_gen_match == 6',
    TTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    TTJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    Diboson_VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    Diboson_VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    singleTop_VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    singleTop_VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    EWK_VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    EWK_VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    WJ = '1',
    jetFakes = '1',
    data = '1',
    embed = 'l1_gen_match == 5 && l2_gen_match == 5',
)
cuts_datacards['TTL'] = cuts_datacards['ZL']
cuts_datacards['Diboson_VVL'] = cuts_datacards['ZL']
cuts_datacards['singleTop_VVL'] = cuts_datacards['ZL']
cuts_datacards['EWK_VVL'] = cuts_datacards['ZL']
cuts_datacards['ZLL'] = cuts_datacards['ZL'] | cuts_datacards['ZJ']
cuts_datacards['TT'] = cuts_datacards['TTT'] | cuts_datacards['TTJ']
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']
from htt_plot.channels_configs.htt_common import datacard_processes

# ## specific cuts


# 'ZTT': signal_region_MC_nofakes_DY & cfg.cuts_datacards['ZTT']


# weights
from htt_plot.channels_configs.htt_common import weights
weights['MC'] = weights['l1_MC']*weights['l2_MC']

weights['embed'] = Cut('weight_generator * weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * weight_embed_track_l1 * (0.18321*(l1_pt>=30 && l1_pt<35) + 0.53906*(l1_pt>=35 && l1_pt<40) + 0.63658*(l1_pt>=40 && l1_pt<45) + 0.73152*(l1_pt>=45 && l1_pt<50) + 0.79002*(l1_pt>=50 && l1_pt<60) + 0.84666*(l1_pt>=60 && l1_pt<80) + 0.84919*(l1_pt>=80 && l1_pt<100) + 0.86819*(l1_pt>=100 && l1_pt<150) + 0.88206*(l1_pt>=150 && l1_pt<200) + (l1_pt>=200)) * weight_embed_muonID_eff_l2 * weight_embed_track_l2 * (0.18321*(l2_pt>=30 && l2_pt<35) + 0.53906*(l2_pt>=35 && l2_pt<40) + 0.63658*(l2_pt>=40 && l2_pt<45) + 0.73152*(l2_pt>=45 && l2_pt<50) + 0.79002*(l2_pt>=50 && l2_pt<60) + 0.84666*(l2_pt>=60 && l2_pt<80) + 0.84919*(l2_pt>=80 && l2_pt<100) + 0.86819*(l2_pt>=100 && l2_pt<150) + 0.88206*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')
weights['embed_track_1prong_up'] = Cut('weight_generator * weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * ((l1_decay_mode==0)*0.983+(l1_decay_mode==1)*0.983*1.065+(l1_decay_mode==10)*0.975*0.975*0.975) * (0.18321*(l1_pt>=30 && l1_pt<35) + 0.53906*(l1_pt>=35 && l1_pt<40) + 0.63658*(l1_pt>=40 && l1_pt<45) + 0.73152*(l1_pt>=45 && l1_pt<50) + 0.79002*(l1_pt>=50 && l1_pt<60) + 0.84666*(l1_pt>=60 && l1_pt<80) + 0.84919*(l1_pt>=80 && l1_pt<100) + 0.86819*(l1_pt>=100 && l1_pt<150) + 0.88206*(l1_pt>=150 && l1_pt<200) + (l1_pt>=200)) * weight_embed_muonID_eff_l2 * ((l2_decay_mode==0)*0.983+(l2_decay_mode==1)*0.983*1.065+(l2_decay_mode==10)*0.975*0.975*0.975) * (0.18321*(l2_pt>=30 && l2_pt<35) + 0.53906*(l2_pt>=35 && l2_pt<40) + 0.63658*(l2_pt>=40 && l2_pt<45) + 0.73152*(l2_pt>=45 && l2_pt<50) + 0.79002*(l2_pt>=50 && l2_pt<60) + 0.84666*(l2_pt>=60 && l2_pt<80) + 0.84919*(l2_pt>=80 && l2_pt<100) + 0.86819*(l2_pt>=100 && l2_pt<150) + 0.88206*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')
weights['embed_track_1prong_down'] = Cut('weight_generator * weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * ((l1_decay_mode==0)*0.967+(l1_decay_mode==1)*0.967*1.038+(l1_decay_mode==10)*0.975*0.975*0.975) * (0.18321*(l1_pt>=30 && l1_pt<35) + 0.53906*(l1_pt>=35 && l1_pt<40) + 0.63658*(l1_pt>=40 && l1_pt<45) + 0.73152*(l1_pt>=45 && l1_pt<50) + 0.79002*(l1_pt>=50 && l1_pt<60) + 0.84666*(l1_pt>=60 && l1_pt<80) + 0.84919*(l1_pt>=80 && l1_pt<100) + 0.86819*(l1_pt>=100 && l1_pt<150) + 0.88206*(l1_pt>=150 && l1_pt<200) + (l1_pt>=200)) * weight_embed_muonID_eff_l2 * ((l2_decay_mode==0)*0.967+(l2_decay_mode==1)*0.967*1.038+(l2_decay_mode==10)*0.975*0.975*0.975) * (0.18321*(l2_pt>=30 && l2_pt<35) + 0.53906*(l2_pt>=35 && l2_pt<40) + 0.63658*(l2_pt>=40 && l2_pt<45) + 0.73152*(l2_pt>=45 && l2_pt<50) + 0.79002*(l2_pt>=50 && l2_pt<60) + 0.84666*(l2_pt>=60 && l2_pt<80) + 0.84919*(l2_pt>=80 && l2_pt<100) + 0.86819*(l2_pt>=100 && l2_pt<150) + 0.88206*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')
weights['embed_track_3prong_up'] = Cut('weight_generator * weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * ((l1_decay_mode==0)*0.975+(l1_decay_mode==1)*0.975*1.051+(l1_decay_mode==10)*0.983*0.983*0.983) * (0.18321*(l1_pt>=30 && l1_pt<35) + 0.53906*(l1_pt>=35 && l1_pt<40) + 0.63658*(l1_pt>=40 && l1_pt<45) + 0.73152*(l1_pt>=45 && l1_pt<50) + 0.79002*(l1_pt>=50 && l1_pt<60) + 0.84666*(l1_pt>=60 && l1_pt<80) + 0.84919*(l1_pt>=80 && l1_pt<100) + 0.86819*(l1_pt>=100 && l1_pt<150) + 0.88206*(l1_pt>=150 && l1_pt<200) + (l1_pt>=200)) * weight_embed_muonID_eff_l2 * ((l2_decay_mode==0)*0.975+(l2_decay_mode==1)*0.975*1.051+(l2_decay_mode==10)*0.983*0.983*0.983) * (0.18321*(l2_pt>=30 && l2_pt<35) + 0.53906*(l2_pt>=35 && l2_pt<40) + 0.63658*(l2_pt>=40 && l2_pt<45) + 0.73152*(l2_pt>=45 && l2_pt<50) + 0.79002*(l2_pt>=50 && l2_pt<60) + 0.84666*(l2_pt>=60 && l2_pt<80) + 0.84919*(l2_pt>=80 && l2_pt<100) + 0.86819*(l2_pt>=100 && l2_pt<150) + 0.88206*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')
weights['embed_track_3prong_down'] = Cut('weight_generator * weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * ((l1_decay_mode==0)*0.975+(l1_decay_mode==1)*0.975*1.051+(l1_decay_mode==10)*0.967*0.967*0.967) * (0.18321*(l1_pt>=30 && l1_pt<35) + 0.53906*(l1_pt>=35 && l1_pt<40) + 0.63658*(l1_pt>=40 && l1_pt<45) + 0.73152*(l1_pt>=45 && l1_pt<50) + 0.79002*(l1_pt>=50 && l1_pt<60) + 0.84666*(l1_pt>=60 && l1_pt<80) + 0.84919*(l1_pt>=80 && l1_pt<100) + 0.86819*(l1_pt>=100 && l1_pt<150) + 0.88206*(l1_pt>=150 && l1_pt<200) + (l1_pt>=200)) * weight_embed_muonID_eff_l2 * ((l2_decay_mode==0)*0.975+(l2_decay_mode==1)*0.975*1.051+(l2_decay_mode==10)*0.967*0.967*0.967) * (0.18321*(l2_pt>=30 && l2_pt<35) + 0.53906*(l2_pt>=35 && l2_pt<40) + 0.63658*(l2_pt>=40 && l2_pt<45) + 0.73152*(l2_pt>=45 && l2_pt<50) + 0.79002*(l2_pt>=50 && l2_pt<60) + 0.84666*(l2_pt>=60 && l2_pt<80) + 0.84919*(l2_pt>=80 && l2_pt<100) + 0.86819*(l2_pt>=100 && l2_pt<150) + 0.88206*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')

# datasets
import htt_plot.datasets.gael_all as datasets

cut_signal = cuts_iso['l1_Tight'] & cuts_iso['l2_Tight'] & basic_cuts


# category

basic_cuts_btag = basic_cuts & cut_btag
cut_signal_btag = cuts_iso['l1_Tight'] & cuts_iso['l2_Tight'] & basic_cuts_btag

basic_cuts_nobtag = basic_cuts & cut_nobtag
cut_signal_nobtag = cuts_iso['l1_Tight'] & cuts_iso['l2_Tight'] & basic_cuts_nobtag
