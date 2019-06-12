from htt_plot.tools.cut import Cuts

channel = 'tt'

from htt_plot.cuts.htt_cuts import cuts_tt as cut_signal

from htt_plot.cuts.htt_triggers_ot import cuts_tt as triggers
triggers = triggers.any()
triggers = Cuts(triggers = triggers)

from htt_plot.cuts.htt_isolations import cuts_iso_tt as cuts_iso

from htt_plot.cuts.htt_flags import cuts_flags
from htt_plot.cuts.htt_vetoes import cuts_vetoes
from htt_plot.cuts.htt_generic import cut_l1_fakejet, cut_l2_fakejet, cut_os, cut_ss, cut_dy_promptfakeleptons, cut_TT_nogenuine

basic_cuts = cuts_flags + cuts_vetoes + triggers + cut_os

from htt_plot.cuts.htt_datacards_cuts import cuts_tt as cuts_datacards

from htt_plot.cuts.htt_weights import weights
