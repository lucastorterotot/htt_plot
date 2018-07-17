from htt_plot.tools.cut import Cut, CutFlow
import pprint

cuts_mu_kine = CutFlow([
    ('mu_pt', 'l1_pt>23'), 
    ('mu_eta', 'abs(l1_eta)<2.1'), 
])

cuts_mu_id = CutFlow([
    ('mu_id', 'l1_muonid_medium>0.5'), 
    ('mu_vertex', 'abs(l1_dxy)<0.045 && abs(l1_dz)<0.2'), 
])

cuts_mu_iso = CutFlow([
    ('mu_iso', 'l1_reliso05<0.15'),     
])

cuts_mu = cuts_mu_kine + cuts_mu_id + cuts_mu_iso

cuts_tau_kine = CutFlow([
    ('tau_pt', 'l2_pt>30'), 
    ('tau_eta', 'abs(l2_eta)<2.3'),   
])

cuts_tau_id = CutFlow([
    ('tau_vertex', 'abs(l2_dz)<0.2'), 
    ('tau_decaymode', 'l2_decayModeFinding>0.5'),
    ('tau_against_e', 'l2_againstElectronMVA6>0.5'),
    ('tau_against_mu', 'l2_againstMuon3>1.5'),
])

cuts_tau_iso = CutFlow([
    ('tau_iso', 'l2_byTightIsolationMVArun2v1DBoldDMwLT > 0.5'),     
])

cuts_tau = cuts_tau_kine + cuts_tau_id + cuts_tau_iso

cuts_signal = CutFlow([
    ('low_mt', 'mt<40'),     
])

cuts_mt = cuts_mu + cuts_tau + cuts_signal


 
