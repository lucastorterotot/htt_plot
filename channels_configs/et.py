''' General config file for plotting and datacards.
ele-tau channel
'''
from htt_plot.tools.cut import Cut, Cuts

channel = 'et'

# binning
from htt_plot.channels_configs.htt_common import bins

# variables
from htt_plot.channels_configs.htt_common import variables, datacards_variables, var_name_dict

# cuts
from htt_plot.channels_configs.htt_common import cut_mt_lepton, cut_mt_lepton_loose, cut_mt_lepton_tight, cuts_flags, cuts_vetoes, cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_btag_1, cut_btag_2, cut_btag, cut_nobtag

cut_dy_promptfakeleptons = Cut('l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2')

cuts_l1 = Cuts(
    l1_pt = 'l1_pt >= 25',
    l1_eta = 'abs(l1_eta) <= 2.1',
    l1_iso = 'l1_iso < 0.15',
    l1_vertex = 'abs(l1_d0) < 0.045 && abs(l1_dz) < 0.2',
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
    l2_against_e = 'l2_againstElectronTightMVA6 > 0.5',
    l2_against_mu = 'l2_againstMuonLoose3 > 0.5',
)

## triggers
cuts_triggers = Cuts(
    singleelectron_27 = 'trg_singleelectron_27 && l1_pt > 28',
    singleelectron_32 = 'trg_singleelectron_32 && l1_pt > 28',
    singleelectron_35 = 'trg_singleelectron_35 && l1_pt > 28',
    crossele_ele24tau30 = 'trg_crossele_ele24tau30 && l1_pt <= 28 && l1_pt > 25',
)

cut_triggers = cuts_triggers.any()

basic_cuts = cuts_flags.all() & cuts_vetoes.all() & cut_triggers & cut_os & cuts_against_leptons.all() & cuts_l1.all() & cuts_l2.all()

## iso
cuts_iso = Cuts(
    l2_VTight = 'l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_Tight = 'l2_byTightIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VLoose = 'l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
    l2_VVLoose = 'l2_byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 > 0.5',
)

## cut embedding + no fakes (for MC)

cut_embed = Cut('l1_gen_match == 3 && l2_gen_match == 5')

cut_not_embed = ~cut_embed

cut_fakes = Cut('l2_gen_match == 6')

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
    WJ = '1',
    jetFakes = '1',
    data = '1',
    embed = 'l1_gen_match == 3 && l2_gen_match == 5',
)
cuts_datacards['ZLL'] = cuts_datacards['ZL'] | cuts_datacards['ZJ']
cuts_datacards['TT'] = cuts_datacards['TTT'] | cuts_datacards['TTJ']
cuts_datacards['VV'] = cuts_datacards['VVT'] | cuts_datacards['VVJ']

cuts_datacards['TTL'] = cuts_datacards['ZL']
cuts_datacards['VVL'] = cuts_datacards['ZL']

for VV_key in ['VVT', 'VVJ', 'VVL']:
    for process_type in ['Diboson', 'singleTop', 'EWK']:
        cuts_datacards['{}_{}'.format(process_type, VV_key)] = cuts_datacards[VV_key]
from htt_plot.channels_configs.htt_common import datacard_processes

# weights
from htt_plot.channels_configs.htt_common import weights
weights['MC'] = weights['l2_MC']
#weights['weight'] = weights['weight'] * Cut("(l2_gen_match==1 || l2_gen_match==3)*(((abs(l1_eta) < 1.46) * 0.88) + ((abs(l1_eta) > 1.5588) * 0.51))+!(l2_gen_match==1 || l2_gen_match==3)") #eletauFakeRateWeightFix

emb_weight_simulation_sf = Cut('weight_generator')
emb_weight_scale_factor = Cut('weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * weight_embed_muonID_eff_l2')

#Weight("(idWeight_1*((l1_pt>28)*(trigger_27_32_35_Weight_1*(abs(l1_eta) < 1.5||l1_pt>=40) + singleTriggerDataEfficiencyWeightKIT_1*(abs(l1_eta)>=1.5)*(l1_pt<40))+(l1_pt<28))*isoWeight_1)<10.0", "lepton_cut"),

emb_weight_lepton_trg = Cut('(l1_pt>=28)+(l1_pt<28)*((abs(l1_eta)>=1.5)*l1_weight_trig_et+(abs(l1_eta)<1.5)*l1_weight_trig_et*(1/((l1_pt<28)*(abs(l1_eta)<1.5)+(l1_pt>=28)+(abs(l1_eta)>=1.5))))') # < 10 ?

emb_weight_low_crossele_nonclosure = Cut("(l1_pt<28)*((abs(l1_eta)<=1.5)*0.852469262576+(abs(l1_eta)>1.5)*0.689309270861)+(l1_pt>=28)")

emb_weight_singleelectron_nonclosure = Cut("(l1_pt>=28)*(l1_pt<40)*((abs(l1_eta)<=1.5)*0.950127109065+(abs(l1_eta)>1.5)*0.870372483259)+(l1_pt<28)+(l1_pt>=40)")

emb_weight_lepton_sf = Cut('l1_weight_idiso*((l1_pt>28)*(l1_weight_trig_e*(abs(l1_eta) < 1.5 || l1_pt >= 40) + 1.0*(abs(l1_eta)>=1.5 && l1_pt < 40))+(l1_pt<28))')

emb_weight_tau_leg_weight = Cut('(l2_pt<=20)*1.0+(l2_pt>20&&l2_pt<=25)*1.08+(l2_pt>25&&l2_pt<=30)*1.05+(l2_pt>30&&l2_pt<=35)*1.11+(l2_pt>35&&l2_pt<=40)*1.09+(l2_pt>40)*1.10')
emb_weight_emb_tau_id = Cut('(l2_gen_match==5)*0.97+(l2_gen_match!=5)*1.0')
emb_weight_emb_veto = Cut('(l1_gen_match==3 && l2_gen_match==5)*1.0')

weights['embed'] = emb_weight_simulation_sf * emb_weight_scale_factor * emb_weight_lepton_sf * emb_weight_tau_leg_weight * emb_weight_emb_tau_id * emb_weight_emb_veto

#emb_weight_lepton_trg = Cut('1.0')
#emb_weight_lepton_sf = Cut('1.0')
emb_weight_tau_leg_weight = Cut('1.0')
weights['embed'] = emb_weight_simulation_sf * emb_weight_scale_factor * emb_weight_lepton_trg * emb_weight_low_crossele_nonclosure * emb_weight_singleelectron_nonclosure * emb_weight_lepton_sf * emb_weight_tau_leg_weight * emb_weight_emb_tau_id * emb_weight_emb_veto

for w in ['embed_track_1prong_up', 'embed_track_1prong_down', 'embed_track_3prong_up', 'embed_track_3prong_down']:
    weights[w] = weights['embed']

weights['l1_fake'] = Cut('1.0')
weights['l2_fake'] = Cut('l2_fakeweight')

# datasets
import htt_plot.datasets.lucas_et as datasets

cut_signal = cuts_iso['l2_Tight'] & basic_cuts

# categories

categories = {
    'nobtag_tight' : cut_nobtag & cut_mt_lepton_tight,
    'btag_tight' : cut_btag & cut_mt_lepton_tight,
    'nobtag_loosemt' : cut_nobtag & cut_mt_lepton_loose,
    'btag_loosemt' : cut_btag & cut_mt_lepton_loose,
    'nobtag_Vloosemt' : cut_nobtag & ~cut_mt_lepton,
    'btag_Vloosemt' : cut_btag & ~cut_mt_lepton,
    }

merging_categories = {
    'nobtag' : ['nobtag_tight', 'nobtag_loosemt'],
    'btag' : ['btag_tight', 'btag_loosemt'],
    'tight' : ['nobtag_tight', 'btag_tight'],
    'loosemt' : ['nobtag_loosemt', 'btag_loosemt'],
    'Vloosemt' : ['nobtag_Vloosemt', 'btag_Vloosemt'],
    }
merging_categories['inclusive'] = merging_categories['btag']+merging_categories['nobtag']
merging_categories['allmt'] = merging_categories['inclusive']+merging_categories['Vloosemt']

basic_cuts_btag = basic_cuts & cut_btag
cut_signal_btag = cuts_iso['l2_Tight'] & basic_cuts_btag

basic_cuts_nobtag = basic_cuts & cut_nobtag
cut_signal_nobtag = cuts_iso['l2_Tight'] & basic_cuts_nobtag
