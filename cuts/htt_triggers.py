from htt_plot.tools.cut import Cuts

cuts_tt = Cuts(
    singletau = 'trg_singletau',
    doubletau_35_mediso = 'trg_doubletau_35_mediso',
    doubletau_35_tightiso_tightid = 'trg_doubletau_35_tightiso_tightid',
    doubletau_40_mediso_tightid = 'trg_doubletau_40_mediso_tightid',
    doubletau_40_tightiso = 'trg_doubletau_40_tightiso',
    )

cuts_mt = Cuts(
    singlemuon_24 = 'trg_singlemuon_24',
    singlemuon_27 = 'trg_singlemuon_27',
    crossmuon_mu24tau20 = 'trg_crossmuon_mu24tau20',
    crossmuon_mu20tau27 = 'trg_crossmuon_mu20tau27',
)

cuts_et = Cuts(
    singleelectron_27 = 'trg_singleelectron_27',
    singleelectron_32 = 'trg_singleelectron_32',
    singleelectron_35 = 'trg_singleelectron_35',
    crossele_ele24tau30 = 'trg_crossele_ele24tau30',
)
