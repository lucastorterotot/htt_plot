''' General config file for plotting and datacards.
tau-tau channel
'''

from htt_plot.tools.cut import Cuts

channel = 'tt'

# binning
from htt_plot.binning import bins

# variables
variables = bins.keys()
variables = ['mt_tot'] # just for testing

# cuts
from htt_plot.cuts.htt_cuts import cuts_tt as cut_signal
from htt_plot.cuts.htt_cuts import cuts_against_leptons_tt as cuts_against_leptons

from htt_plot.cuts.htt_triggers_ot import cuts_tt as triggers
triggers = Cuts(triggers = triggers.any())

from htt_plot.cuts.htt_isolations import cuts_iso_tt as cuts_iso

from htt_plot.cuts.htt_flags import cuts_flags
from htt_plot.cuts.htt_vetoes import cuts_vetoes
from htt_plot.cuts.htt_generic import cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine

basic_cuts = cuts_flags + cuts_vetoes + triggers + cut_os + cuts_against_leptons

from htt_plot.cuts.htt_datacards_cuts import cuts_tt as cuts_datacards

# weights
from htt_plot.cuts.htt_weights import weights

# datasets
import htt_plot.datasets.gael_all as datasets

### tmp hack
cut_signal = Cuts()
###

for leg in ['l1', 'l2']:
    cut_signal += cuts_iso[leg+'_Tight']

cut_signal += basic_cuts
