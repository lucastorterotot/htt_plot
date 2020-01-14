sys_dict_samples = {'top_pT_reweighting_up':{'processes':['TT']},
    
    'top_pT_reweighting_down': {'processes': ['TT']},
    
    'DY_pT_reweighting_up': {'processes': ['DY']},
    
    'DY_pT_reweighting_down': {'processes': ['DY']},
    
    'METrecoil_response_up': {'processes': ['DY','signal','W']},
    
    'METrecoil_response_down': {'processes': ['DY','signal','W']},
    
    'METrecoil_resolution_up': {'processes': ['DY','signal','W']},
    
    'METrecoil_resolution_down': {'processes': ['DY','signal','W']},
    
    'METunclustered_up': {'processes': ['all_MC']},
    
    'METunclustered_down': {'processes': ['all_MC']},
    
    'TES_HadronicTau_1prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_1prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_1prong1pi0_up': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_1prong1pi0_down': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_3prong0pi0_up': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_3prong0pi0_down': {'processes': ['all_MC','Embedded']},
    
    'TES_HadronicTau_3prong1pi0_up': {'processes': ['all_MC']},
    
    'TES_HadronicTau_3prong1pi0_down': {'processes': ['all_MC']},
    
    'TES_promptMuon_1prong0pi0_up': {'processes': ['all_MC']},
    
    'TES_promptMuon_1prong0pi0_down': {'processes': ['all_MC']},
    
    'TES_promptEle_1prong0pi0_up': {'processes': ['all_MC']},
    
    'TES_promptEle_1prong0pi0_down': {'processes': ['all_MC']},
    
    'TES_promptEle_1prong1pi0_up': {'processes': ['all_MC']},
    
    'TES_promptEle_1prong1pi0_down': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta0to5_13Tev_up': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta0to5_13Tev_down': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta0to3_13TeV_up': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta0to3_13TeV_down': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta3to5_13TeV_up': {'processes': ['all_MC']},
    
    'CMS_scale_j_eta3to5_13TeV_down': {'processes': ['all_MC']},
    
    'CMS_scale_j_RelativeBal_13TeV_up': {'processes': ['all_MC']},
    
    'CMS_scale_j_RelativeBal_13TeV_down': {'processes': ['all_MC']},
    
    'CMS_scale_j_RelativeSample_13TeV_up': {'processes': ['all_MC']},
    
    'CMS_scale_j_RelativeSample_13TeV_down': {'processes': ['all_MC']},
    
    'Btagging_up': {'processes': ['all_MC']},
    
    'Btagging_down': {'processes': ['all_MC']},

    'Embedding_tracking_1prong_up': {'processes': ['Embedded']},
                    
    'Embedding_tracking_1prong_down': {'processes': ['Embedded']},

    'Embedding_tracking_3prong_up': {'processes': ['Embedded']},
                    
    'Embedding_tracking_3prong_down': {'processes': ['Embedded']},
}

for key, item in sys_dict_samples.iteritems():
    if 'all_MC' in item['processes']:
        item['processes'].extend(['DY','TT','Diboson','singleTop','W','signal','EWK'])
    if 'DY' in item['processes']:
        item['processes'].extend(['ZJ','ZLL','ZTT','ZL'])
    if 'TT' in item['processes']:
        item['processes'].extend(['TTT','TTL','TTJ'])
    if 'Diboson' in item['processes'] and 'singleTop' in item['processes']:
        item['processes'].extend(['VV','VVL','VVT','VVJ'])
