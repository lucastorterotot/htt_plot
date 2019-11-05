''' General config file for plotting and datacards.
muon-tau channel
'''
from htt_plot.tools.cut import Cut, Cuts

channel = 'mt'

# binning
from htt_plot.channels_configs.htt_common import bins

# variables
from htt_plot.channels_configs.htt_common import variables, datacards_variables, var_name_dict

# cuts
from htt_plot.channels_configs.htt_common import cut_mt_tot, cuts_flags, cuts_vetoes, cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_btag_1, cut_btag_2, cut_btag, cut_nobtag

cut_l1_fakejet = Cut('1')
cut_dy_promptfakeleptons = Cut('l2_gen_match==1 || l2_gen_match==2')

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

cut_signal = cuts_l1.all() & cuts_l2.all() & cuts_against_leptons.all() #& cut_mt_tot

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
    l1_VTight = '1',
    l1_Tight = '1',
    l1_VLoose = '1',
    l1_VVLoose = '1',
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

## cut embedding + no fakes (for MC)

cut_embed = Cut('l2_gen_match == 5')

cut_not_embed = ~cut_embed

cut_fakes = Cut('l2_gen_match==6')

cut_not_fakes = ~cut_fakes

cut_not_fakes_not_embed = cut_not_embed & cut_not_fakes

## datacards
cuts_datacards = Cuts(
    ZTT = 'l2_gen_match == 5',
    ZL = 'l2_gen_match < 6 && !(l2_gen_match == 5)',
    ZJ = 'l2_gen_match == 6',
    TTT = 'l2_gen_match == 5',
    TTJ = '!(l2_gen_match == 5)',
    VVT = '(l2_gen_match == 5)',
    VVJ = '!(l2_gen_match == 5)',
    Diboson_VVT = '(l2_gen_match == 5)',
    Diboson_VVJ = '!(l2_gen_match == 5)',
    singleTop_VVT = '(l2_gen_match == 5)',
    singleTop_VVJ = '!(l2_gen_match == 5)',
    WJ = '1',
    jetFakes = '1',
    data = '1',
    embed = 'l2_gen_match == 5',
)
cuts_datacards['TTL'] = cuts_datacards['ZL']
cuts_datacards['VVL'] = cuts_datacards['ZL']
cuts_datacards['Diboson_VVL'] = cuts_datacards['ZL']
cuts_datacards['singleTop_VVL'] = cuts_datacards['ZL']
cuts_datacards['ZLL'] = cuts_datacards['ZL'] | cuts_datacards['ZJ']
cuts_datacards['TT'] = cuts_datacards['TTT'] | cuts_datacards['TTJ']
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']
for ewk_key in ['VVT', 'VVJ', 'VVL']:
    cuts_datacards['EWK_{}'.format(ewk_key)] = cuts_datacards[ewk_key]
from htt_plot.channels_configs.htt_common import datacard_processes

# weights
from htt_plot.channels_configs.htt_common import weights
weights['MC'] = weights['l2_MC']

emb_weight_simulation_sf = Cut('weight_generator')
emb_weight_scale_factor = Cut('weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * weight_embed_muonID_eff_l2')
emb_weight_lepton_sf = Cut('l1_weight_idiso*(l1_weight_trig_mt*(l1_pt>25)+((0.81*(l1_pt>=21 && l1_pt<22) + 0.82*(l1_pt>=22 && l1_pt<23) + 0.83*(l1_pt>=23))*(l1_pt<25)))')
emb_weight_tau_leg_weight = Cut('(l1_pt>25)+(l1_pt >= 21 && l1_pt<25)*((l2_pt>=20 && l2_pt<25)*0.12714+(l2_pt>=25 && l2_pt<30)*0.46930+0.71983*(l2_pt>=30 && l2_pt<35) + 0.75209*(l2_pt>=35 && l2_pt<40) + 0.78164*(l2_pt>=40 && l2_pt<45) + 0.83241*(l2_pt>=45 && l2_pt<50) + 0.86694*(l2_pt>=50 && l2_pt<60) + 0.89966*(l2_pt>=60 && l2_pt<80) + 0.88534*(l2_pt>=80 && l2_pt<100) + 0.90095*(l2_pt>=100 && l2_pt<150) + 0.84402*(l2_pt>=150 && l2_pt<200) + (l2_pt>=200))')
emb_weight_emb_tau_id = Cut('(l2_gen_match==5)*0.97+(l2_gen_match!=5)*1.0')
emb_weight_emb_veto = Cut('(l1_gen_match==4 && l2_gen_match==5)*1.0')

weights['embed'] = emb_weight_simulation_sf * emb_weight_scale_factor * emb_weight_lepton_sf * emb_weight_tau_leg_weight * emb_weight_emb_tau_id * emb_weight_emb_veto

for w in ['embed_track_1prong_up', 'embed_track_1prong_down', 'embed_track_3prong_up', 'embed_track_3prong_down']:
    weights[w] = weights['embed']

weights['l1_fake'] = Cut('1.0')
weights['l2_fake'] = Cut('l2_fakeweight')

# datasets
import htt_plot.datasets.lucas_mt as datasets

cut_signal = cuts_iso['l2_Tight'] & basic_cuts


# category

basic_cuts_btag = basic_cuts & cut_btag
cut_signal_btag = cuts_iso['l2_Tight'] & basic_cuts_btag

basic_cuts_nobtag = basic_cuts & cut_nobtag
cut_signal_nobtag = cuts_iso['l2_Tight'] & basic_cuts_nobtag

