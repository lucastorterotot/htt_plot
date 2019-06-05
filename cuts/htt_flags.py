from htt_plot.tools.cut import Cut, CutFlow
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
