from htt_plot.tools.cut import Cut, CutFlow
import pprint

triggers_list = [
    'trigger_matched_isomu22',
    'trigger_isotkmu22',
    'trigger_isomu22',
    'trigger_matched_isotkmu22',
    'trigger_matched_isomu19tau20',
    'trigger_matched_singlemuon',
    ]

any_trigger_str = '||'.join(triggers_list)

triggers = CutFlow(
    [('triggers', any_trigger_str)]
)
