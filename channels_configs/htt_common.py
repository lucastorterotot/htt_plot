''' General config file for plotting and datacards.
HTT common config
'''
from array import array
from htt_plot.tools.cut import Cut, Cuts

# binning
from array import array

var_name_dict = {'sqrt((l1_pt+l2_pt)**2-(l1_pt*cos(l1_phi)+l2_pt*cos(l2_phi))**2-(l1_pt*sin(l1_phi)+l2_pt*sin(l2_phi))**2)':'l1_l2_mt',
                 'sqrt(2*l1_pt*l2_pt*(1-cos(l1_phi-l2_phi)))':'l1_l2_mt_bis'}

bins = {
    'l1_eta' : (50, -2.5, 2.5),
    'l1_phi' : (40, -4, 4),
    'l1_pt'  : (40, 0., 600),
    'l2_eta' : (50, -2.5, 2.5),
    'l2_phi' : (40, -4, 4),
    'l2_pt'  : (40, 0., 600),
    'j1_pt'  : (60, 0., 600.),
    'j2_pt'  : (60, 0., 600.),
    'j2_eta' : (50, -2.5, 2.5),
    'j1_eta' : (50, -2.5, 2.5),
    'n_jets_pt20' : (20, 0, 20),
    'b1_pt'  : (30, 0., 600.),
    'b2_pt'  : (30, 0., 600.),
    'b1_eta' : (20, -2.5, 2.5),
    'b2_eta' : (20, -2.5, 2.5),
    'met'  : (60, 0., 600),
    'metphi'  : (30,-4,4),
    'mt_tot' : (31, array('d',[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,225,250,275,300,325,350,400,500,700,900,4000])),#,700,900
    #'mt_tot' : (35, 0, 700),
    'm_vis'   : (80,0,800),
    'l1_mt'   : (60,0,600),
    'l2_mt'   : (60,0,600),
    'pt_tt'   : (60,0,600),
    'l1_gen_match' : (8,0,8),
    'l2_gen_match' : (8,0,8),
    'sqrt((l1_pt+l2_pt)**2-(l1_pt*cos(l1_phi)+l2_pt*cos(l2_phi))**2-(l1_pt*sin(l1_phi)+l2_pt*sin(l2_phi))**2)'   : (60,0,600),
    'sqrt(2*l1_pt*l2_pt*(1-cos(l1_phi-l2_phi)))'   : (60,0,1000)
}

# variables
variables = bins.keys()
datacards_variables = ['mt_tot']
# variables = datacards_variables # just for testing

# processes
datacard_processes = ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','VVT','VVJ','VV','W','jetFakes','data_obs','embedded']

# common cuts
cuts_flags = Cuts(
    goodVertices = 'Flag_goodVertices',
    TightHalo = 'Flag_globalTightHalo2016Filter',
    # SuperTightHalo = 'Flag_globalSuperTightHalo2016Filter',
    Noise = 'Flag_HBHENoiseFilter',
    NoiseIso = 'Flag_HBHENoiseIsoFilter',
    EcalDeadCell = 'Flag_EcalDeadCellTriggerPrimitiveFilter',
    BadPFMuon = 'Flag_BadPFMuonFilter',
    BadChargedCandidate = 'Flag_BadChargedCandidateFilter',
    # eeBadSc = 'Flag_eeBadScFilter',
    ecalBadCalib = 'Flag_ecalBadCalibFilter'
)

cuts_vetoes = Cuts(
    dileptonveto = '!veto_dilepton', 
    thirdleptonveto = '!veto_extra_elec', 
    otherleptonveto = '!veto_extra_muon', 
)



cut_l1_fakejet = Cut('l1_gen_match==6')
cut_l2_fakejet = Cut('l2_gen_match==6')


cut_os = Cut('l1_q != l2_q')
cut_ss = ~cut_os

cut_nobtag = Cut('b1_pt == -99')
cut_btag = ~cut_nobtag



cut_mt_tot = Cut('mt_tot < 40')

cut_btag_1 = Cut('bjet1_csv > 0')

cut_btag_2 = Cut('bjet2_csv > 0')

# weights
weights = Cuts(
    weight = 'weight',
    l1_MC = 'l1_weight_mutotaufake_loose * l1_weight_etotaufake_vloose * l1_weight_tauid_tight',
    l2_MC = 'l2_weight_mutotaufake_loose * l2_weight_etotaufake_vloose * l2_weight_tauid_tight',
    DY = 'weight_dy * weight_generator',# * '+dy_stitching_weight
    DY_pTrweigh_up = '(1+(weight_dy-1)*1.1)/(weight_dy)',
    DY_pTrweigh_down = '(1+(weight_dy-1)*0.9)/(weight_dy)',
    TT = 'weight_top',
    TT_pTrweigh_up = '(1+(weight_top-1)*2)/(weight_top)',
    TT_pTrweigh_down = '(1+(weight_top-1)*0)/(weight_top)',
    l1_fake = 'l1_fakeweight*0.5',
    l2_fake = 'l2_fakeweight*0.5'
    )


