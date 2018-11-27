from htt_plot.tools.cut import Cut, CutFlow
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

cuts_generic = cuts_flags + cuts_vetoes

print '\ncut_flow: generic'

print cuts_generic

cut_os = Cut('opposite_sign', 'l1_q != l2_q')
cut_ss = Cut('same_sign',  'l1_q == l2_q')

cut_dy_ztt = Cut('dy_ztt', 'l2_gen_match==5')
cut_dy_zl = Cut('dy_zl', 'l2_gen_match<5')
cut_dy_zj = Cut('dy_zj', 'l2_gen_match==6')

pprint.pprint(Cut.available_cuts())
