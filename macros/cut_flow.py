import htt_plot.tools.config as config
from htt_plot.components.lucas_small import *
from htt_plot.tools.efficiencies import Efficiencies
from htt_plot.cuts.generic import cuts_generic
from htt_plot.cuts.mt import cuts_mt

cuts = cuts_generic + cuts_mt

components = [DY, data1]

for comp in components:
    eff = Efficiencies(comp.tree, cuts)
    eff.fill_cut_flow()
    print eff.str_cut_flow()
