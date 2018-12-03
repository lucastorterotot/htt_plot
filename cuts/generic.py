from htt_plot.tools.cut import Cut, CutFlow
from htt_plot.cuts.tt_triggers import triggers
import pprint

flags = [
    'Flag_goodVertices',
    'Flag_globalTightHalo2016Filter',
    'Flag_globalSuperTightHalo2016Filter',
    'Flag_HBHENoiseFilter',
    'Flag_HBHENoiseIsoFilter',
    'Flag_EcalDeadCellTriggerPrimitiveFilter',
    'Flag_BadPFMuonFilter',
    'Flag_BadChargedCandidateFilter',
    'Flag_eeBadScFilter',
    'Flag_ecalBadCalibFilter'
]

cuts_flags = CutFlow(
    [(flag, flag) for flag in flags]
)

print '\ncut_flow: flags: '
print cuts_flags

cuts_vetoes = CutFlow([
    ('dileptonveto', '!veto_dilepton'), 
    ('thirdleptonveto', '!veto_extra_elec'), 
    ('otherleptonveto', '!veto_extra_muon'), 
])

print '\ncut_flow: vetoes:'
print cuts_vetoes

cuts_generic = cuts_flags #+ cuts_vetoes

print '\ncut_flow: generic'

print cuts_generic

cuts_VTight_isolation = CutFlow([
    ('l1_VTight_isolation','l1_byVTightIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_VTight_isolation','l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017>0.5')
])

cuts_l1_VLoose_notVTight_isolation = CutFlow([
    ('l2_VLoose_isolation','l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_notVTight_isolation','l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017<0.5')    
])

cuts_l2_VLoose_notVTight_isolation = CutFlow([
    ('l2_VLoose_isolation','l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_notVTight_isolation','l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017<0.5')    
])

cuts_against_leptons = CutFlow([
    ('l1_againstleptons','l1_againstElectronVLooseMVA6 > 0.5 && l1_againstMuonLoose3 > 0.5'),
    ('l2_againstleptons','l2_againstElectronVLooseMVA6 > 0.5 && l2_againstMuonLoose3 > 0.5')
])

cut_l1_fakejet = Cut('l1_fakejet','l1_gen_match==6')
cut_l2_fakejet = Cut('l2_fakejet','l2_gen_match==6')

cut_os = Cut('opposite_sign', 'l1_q != l2_q')
cut_ss = Cut('same_sign',  'l1_q == l2_q')

cut_dy_ztt = Cut('dy_ztt', 'l2_gen_match==5')
cut_dy_zl = Cut('dy_zl', 'l2_gen_match<5')
cut_dy_zj = Cut('dy_zj', 'l2_gen_match==6')

l1_FakeFactorApplication_Region = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l1_VLoose_notVTight_isolation + cuts_VTight_isolation['l2_VTight_isolation']
l2_FakeFactorApplication_Region = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l2_VLoose_notVTight_isolation + cuts_VTight_isolation['l1_VTight_isolation']

signal_region = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_VTight_isolation

signal_region_MC = signal_region

signal_region_MC_nofakes = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet

pprint.pprint(Cut.available_cuts())
