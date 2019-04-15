from htt_plot.tools.cut import Cut, CutFlow
from htt_plot.cuts.tt_triggers import triggers
import pprint

flags = [
    'Flag_goodVertices',
    'Flag_globalTightHalo2016Filter',
    # 'Flag_globalSuperTightHalo2016Filter',
    'Flag_HBHENoiseFilter',
    'Flag_HBHENoiseIsoFilter',
    'Flag_EcalDeadCellTriggerPrimitiveFilter',
    'Flag_BadPFMuonFilter',
    'Flag_BadChargedCandidateFilter',
    # 'Flag_eeBadScFilter',
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

cuts_generic = cuts_flags + cuts_vetoes

print '\ncut_flow: generic'

print cuts_generic

cut_pt_tt = Cut('cut_pt_tt', 'sqrt( ( l1_pt*cos(l1_phi)+l2_pt*cos(l2_phi)+met*cos(metphi))*(l1_pt*cos(l1_phi)+l2_pt*cos(l2_phi)+met*cos(metphi) ) + ( l1_pt*sin(l1_phi)+l2_pt*sin(l2_phi)+met*sin(metphi) )*( l1_pt*sin(l1_phi)+l2_pt*sin(l2_phi)+met*sin(metphi) ) ) > 50.')

cuts_VTight_isolation = CutFlow([
    ('l1_VTight_isolation','l1_byVTightIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_VTight_isolation','l2_byVTightIsolationMVArun2017v2DBoldDMwLT2017>0.5')
])

cuts_Tight_isolation = CutFlow([
    ('l1_Tight_isolation','l1_byTightIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_Tight_isolation','l2_byTightIsolationMVArun2017v2DBoldDMwLT2017>0.5')
])

cuts_l1_VLoose_notTight_isolation = CutFlow([
    ('l1_VLoose_isolation','l1_byVLooseIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l1_notTight_isolation','l1_byTightIsolationMVArun2017v2DBoldDMwLT2017<0.5')    
])

cuts_l2_VLoose_notTight_isolation = CutFlow([
    ('l2_VLoose_isolation','l2_byVLooseIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l2_notTight_isolation','l2_byTightIsolationMVArun2017v2DBoldDMwLT2017<0.5')    
])


cuts_l1_VLoose_notVTight_isolation = CutFlow([
    ('l1_VLoose_isolation','l1_byVLooseIsolationMVArun2017v2DBoldDMwLT2017>0.5'),
    ('l1_notVTight_isolation','l1_byVTightIsolationMVArun2017v2DBoldDMwLT2017<0.5')    
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
cut_dy_promptfakeleptons = Cut('cut_dy_promptfakeleptons', 'l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2')
# cut_dy_signal = Cut('dy_signal',)

cut_TT_nogenuine = Cut('cut_TT_nogenuine', '!(l1_gen_match==5 && l2_gen_match==5)')

l1_FakeFactorApplication_Region = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l1_VLoose_notTight_isolation + cuts_Tight_isolation['l2_Tight_isolation'] #+ cut_pt_tt
l1_FakeFactorApplication_Region_genuinetauMC = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l1_VLoose_notTight_isolation + cuts_Tight_isolation['l2_Tight_isolation'] + ~cut_l1_fakejet #+ cut_pt_tt
l2_FakeFactorApplication_Region = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l2_VLoose_notTight_isolation + cuts_Tight_isolation['l1_Tight_isolation'] #+ cut_pt_tt
l2_FakeFactorApplication_Region_genuinetauMC = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_l2_VLoose_notTight_isolation + cuts_Tight_isolation['l1_Tight_isolation'] + ~cut_l2_fakejet #+ cut_pt_tt

signal_region_cut = cuts_generic + triggers + cut_os + cuts_against_leptons + cuts_Tight_isolation #+ cut_pt_tt

signal_region_MC = signal_region_cut

signal_region_MC_nofakes = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet

signal_region_MC_nofakes_DY = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet + cut_dy_promptfakeleptons

signal_region_MC_nofakes_TT = signal_region_MC + ~cut_l1_fakejet + ~cut_l2_fakejet + cut_TT_nogenuine

pprint.pprint(Cut.available_cuts())




#### weights

weight='weight'
weight_MC = 'weight*l1_weight_mutotaufake_loose*l1_weight_etotaufake_vloose*l1_weight_tauid_vtight*l2_weight_mutotaufake_loose*l2_weight_etotaufake_vloose*l2_weight_tauid_vtight'
weight_MC_DY = 'weight*l1_weight_mutotaufake_loose*l1_weight_etotaufake_vloose*l1_weight_tauid_vtight*l2_weight_mutotaufake_loose*l2_weight_etotaufake_vloose*l2_weight_tauid_vtight*weight_dy*weight_generator'#*'+dy_stitching_weight

#### cuts+weights


signal_region = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight=weight)
signal_region_Embedded = '({cut})*({weight})'.format(cut=str(signal_region_cut),weight='weight*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
signal_region_MC = '({cut})*({weight})'.format(cut=str(signal_region_MC),weight=weight_MC)
signal_region_MC_nofakes_DY = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_DY),weight=weight_MC_DY)
signal_region_MC_nofakes_TT = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes_TT),weight=weight_MC)
signal_region_MC_nofakes = '({cut})*({weight})'.format(cut=str(signal_region_MC_nofakes),weight=weight_MC)
l1_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region),weight='l1_fakeweight*0.5')
print 'l1 ASR:',l1_FakeFactorApplication_Region
l2_FakeFactorApplication_Region = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region),weight='l2_fakeweight*0.5')
print 'l2 ASR:',l2_FakeFactorApplication_Region
l1_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l2_FakeFactorApplication_Region_genuinetauMC_Embedded = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5*weight_embed_DoubleMuonHLT_eff*weight_embed_muonID_eff_l1*weight_embed_muonID_eff_l2*weight_embed_DoubleTauHLT_eff_l1*weight_embed_DoubleTauHLT_eff_l2*weight_embed_track_l1*weight_embed_track_l2')
l1_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l1_FakeFactorApplication_Region_genuinetauMC),weight='weight*l1_fakeweight*0.5')
l2_FakeFactorApplication_Region_genuinetauMC = '({cut})*({weight})'.format(cut=str(l2_FakeFactorApplication_Region_genuinetauMC),weight='weight*l2_fakeweight*0.5')
