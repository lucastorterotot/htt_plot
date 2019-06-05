from htt_plot.tools.cut import Cut, CutFlow
import pprint

cuts_vetoes = CutFlow([
    ('dileptonveto', '!veto_dilepton'), 
    ('thirdleptonveto', '!veto_extra_elec'), 
    ('otherleptonveto', '!veto_extra_muon'), 
])
