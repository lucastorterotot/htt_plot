sys_dict_samples = {'top_pT_reweighting_up':{'processes':['TT']},
    
    'top_pT_reweighting_down': {'processes': ['TT']},
    
    # 'DY_pT_reweighting_up': {'processes': ['DY']},
    
    # 'DY_pT_reweighting_down': {'processes': ['DY']},
    
    # 'METrecoil_response_up': {'processes': ['all_MC']},
    
    # 'METrecoil_response_down': {'processes': ['all_MC']},
    
    # 'METrecoil_resolution_up': {'processes': ['all_MC']},
    
    # 'METrecoil_resolution_down': {'processes': ['all_MC']},
    
    # 'METunclustered_up': {'processes': ['all_MC']},
    
    # 'METunclustered_down': {'processes': ['all_MC']},
    
    # 'TES_HadronicTau_1prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_1prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_1prong1pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_1prong1pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_3prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_3prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_3prong1pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_HadronicTau_3prong1pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptMuon_1prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptMuon_1prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptEle_1prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptEle_1prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptEle_1prong1pi0_up': {'processes': ['all_MC','Embedded']},
    
    # 'TES_promptEle_1prong1pi0_down': {'processes': ['all_MC','Embedded']},
    
    # 'CMS_scale_j_eta0to5_13Tev_up': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_eta0to5_13Tev_down': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_eta0to3_13Tev_up': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_eta0to3_13Tev_down': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_eta3to5_13Tev_up': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_eta3to5_13Tev_down': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_RelativeBal_13TeV_up': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_RelativeBal_13TeV_down': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_RelativeSample_13TeV_up': {'processes': ['all_MC']},
    
    # 'CMS_scale_j_RelativeSample_13TeV_down': {'processes': ['all_MC']},
    
    # 'Btagging_up': {'processes': ['all_MC']},
    
    # 'Btagging_down': {'processes': ['all_MC']}
}

for key, item in sys_dict_samples.iteritems():
    if 'all_MC' in item['processes']:
        item['processes'].extend(['DY','TT','Diboson','singleTop','W'])
