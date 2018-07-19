from htt_plot.tools.cut import Cut, CutFlow
import pprint

triggers_list = [
    'trigger_isomu22',
    'trigger_isotkmu22',
    'trigger_isomu19tau20'
    ]

triggers_match_list = [
    'trigger_matched_isomu22',
    'trigger_matched_isotkmu22',
    'trigger_matched_isomu19tau20',
    'trigger_matched_singlemuon',
    ]

trigger_str = ' || '.join(triggers_list)
trigger_match_str = ' || '.join(triggers_match_list)

triggers_with_match_list = []
for k in range(0,min(len(triggers_list),len(triggers_match_list))):
    trigger_with_match = '('+' && '.join([triggers_list[k],triggers_match_list[k]])+')'
    triggers_with_match_list.append(trigger_with_match)

mt_trigger_str = ' || '.join(triggers_with_match_list)

triggers = CutFlow(
    [('triggers', mt_trigger_str)]
)
