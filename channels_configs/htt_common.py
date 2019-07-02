''' General config file for plotting and datacards.
HTT common config
'''
from htt_plot.tools.cut import Cut, Cuts

# binning
from array import array
bins = {
    'l1_eta' : (50, -2.5, 2.5),
    'l1_pt'  : (32, 0., 160.),
    'l2_eta' : (50, -2.5, 2.5),
    'l2_pt'  : (32, 0., 160.),
    'met'  : (32, 0., 160.),
    'mt_tot' : (30, 0., 300.),
    'm_vis'   : (32, 0., 200.)
}

# variables
variables = bins.keys()
datacards_variables = ['mt_tot']
variables = datacards_variables+[variables[0]] # just for testing

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

cut_dy_promptfakeleptons = Cut(
    'l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2')

cut_TT_nogenuine = Cut('!(l1_gen_match==5 && l2_gen_match==5)')



cut_mt_tot = Cut('mt_tot < 40')

cut_btag_1 = Cut('bjet1_csv > 0')

cut_btag_2 = Cut('bjet2_csv > 0')

# weights
weights = Cuts(
    weight = 'weight',
    MC = 'l1_weight_mutotaufake_loose * l1_weight_etotaufake_vloose * l1_weight_tauid_vtight * l2_weight_mutotaufake_loose * l2_weight_etotaufake_vloose * l2_weight_tauid_vtight',
    DY = 'weight_dy * weight_generator',# * '+dy_stitching_weight
    embed = 'weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * weight_embed_muonID_eff_l2 * weight_embed_DoubleTauHLT_eff_l1 * weight_embed_DoubleTauHLT_eff_l2 * weight_embed_track_l1 * weight_embed_track_l2',
    l1_fake = 'l1_fakeweight*0.5',
    l2_fake = 'l2_fakeweight*0.5'
    )

# systematics

sys_dict = {
    
    'top_pT_reweighting_up':{'processes':['TTT','TTJ','TT'],
                             'change':'dataset'},
    
    'top_pT_reweighting_down': {'processes': ['TTT','TTJ','TT'],
                                'change':'dataset'},
    
    'DY_pT_reweighting_up': {'processes': ['ZTT','ZL','ZJ','ZLL','DY'],
                             'change':'dataset'},
    
    'DY_pT_reweighting_down': {'processes': ['ZTT','ZL','ZJ','ZLL','DY'],
                               'change':'dataset'},
    
    'METrecoil_response_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                              'change':'dataset'},
    
    'METrecoil_response_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                'change':'dataset'},
    
    'METrecoil_resolution_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                'change':'dataset'},
    
    'METrecoil_resolution_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                  'change':'dataset'},
    
    'METunclustered_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                          'change':'dataset'},
    
    'METunclustered_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                            'change':'dataset'},
    
    'TES_HadronicTau_1prong0pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'TES_HadronicTau_1prong0pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                        'change':'dataset'},
    
    'TES_HadronicTau_1prong1pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'TES_HadronicTau_1prong1pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                        'change':'dataset'},
    
    'TES_HadronicTau_3prong0pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'TES_HadronicTau_3prong0pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                        'change':'dataset'},
    
    'TES_HadronicTau_3prong1pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'TES_HadronicTau_3prong1pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                        'change':'dataset'},
    
    'TES_promptMuon_1prong0pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                     'change':'dataset'},
    
    'TES_promptMuon_1prong0pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                       'change':'dataset'},
    
    'TES_promptEle_1prong0pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                    'change':'dataset'},
    
    'TES_promptEle_1prong0pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'TES_promptEle_1prong1pi0_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                    'change':'dataset'},
    
    'TES_promptEle_1prong1pi0_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','Embedded','DY','std_bkg'],
                                      'change':'dataset'},
    
    'CMS_scale_j_eta0to5_13Tev_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                     'change':'dataset'},
    
    'CMS_scale_j_eta0to5_13Tev_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                       'change':'dataset'},
    
    'CMS_scale_j_eta0to3_13Tev_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                     'change':'dataset'},
    
    'CMS_scale_j_eta0to3_13Tev_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                       'change':'dataset'},
    
    'CMS_scale_j_eta3to5_13Tev_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                     'change':'dataset'},
    
    'CMS_scale_j_eta3to5_13Tev_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                       'change':'dataset'},
    
    'CMS_scale_j_RelativeBal_13TeV_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                         'change':'dataset'},
    
    'CMS_scale_j_RelativeBal_13TeV_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                           'change':'dataset'},
    
    'CMS_scale_j_RelativeSample_13TeV_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                            'change':'dataset'},
    
    'CMS_scale_j_RelativeSample_13TeV_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                                              'change':'dataset'},
    
    'Btagging_up': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                    'change':'dataset'},
    
    'Btagging_down': {'processes': ['ZTT','ZL','ZJ','ZLL','TTT','TTJ','TT','W','VV','VVJ','VVT','Diboson_VVT','Diboson_VVJ','singleTop_VVT','singleTop_VVJ','DY','std_bkg'],
                      'change':'dataset'}
}

