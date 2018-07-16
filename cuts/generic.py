from htt_plot.tools.cut import Cut, CutFlow
import pprint

flags = [
    'Flag_HBHENoiseFilter',
    'Flag_HBHENoiseIsoFilter',
    'Flag_EcalDeadCellTriggerPrimitiveFilter',
    'Flag_goodVertices', 
    'Flag_eeBadScFilter', 
    'Flag_globalTightHalo2016Filter', 
    'passBadMuonFilter', 
    'passBadChargedHadronFilter', 
    'badMuonMoriond2017', 
    'badCloneMuonMoriond2017', 
]

cuts_flags = CutFlow(
    [(flag, flag) for flag in flags]
)

print '\ncut_flow: flags: '
print cuts_flags

cuts_vetoes = CutFlow([
    ('dileptonveto', '!veto_dilepton'), 
    ('thirdleptonveto', '!veto_thirdlepton'), 
    ('otherleptonveto', '!veto_otherlepton'), 
])

print '\ncut_flow: vetoes:'
print cuts_vetoes

cuts_generic = cuts_flags + cuts_vetoes

print '\ncut_flow: generic'

print cuts_generic

cut_os = Cut('opposite_sign', 'l1_charge != l2_charge')
cut_ss = Cut('same_sign',  'l1_charge == l2_charge')

cut_dy_ztt = Cut('dy_ztt', 'gen_match_2==5')
cut_dy_zl = Cut('dy_zl', 'gen_match_2<5')
cut_dy_zj = Cut('dy_zj', 'gen_match_2==6')

pprint.pprint(Cut.available_cuts())
