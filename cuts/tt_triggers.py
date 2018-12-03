from htt_plot.tools.cut import Cut, CutFlow
import pprint

triggers_list = [
	      '!trg_doubletau_lowpt',
	      '!trg_doubletau_mediso',
	      '!trg_doubletau'
	      ]


any_trigger_str = '||'.join(triggers_list)

triggers = CutFlow(
    [('triggers', any_trigger_str)]
)
