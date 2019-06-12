from htt_plot.tools.cut import Cuts

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
