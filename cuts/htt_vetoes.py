from htt_plot.tools.cut import Cuts

cuts_vetoes = Cuts(
    dileptonveto = '!veto_dilepton', 
    thirdleptonveto = '!veto_extra_elec', 
    otherleptonveto = '!veto_extra_muon', 
)
