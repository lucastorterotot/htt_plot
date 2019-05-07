from htt_plot.tools.cut import Cut, CutFlow
import pprint

# Triggers base name for each channels
triggers_base_per_channel = {
    'et':[
        'singleelectron_27',
        'singleelectron_32',
        'singleelectron_35',
        'crossele_ele24tau30',
        ],
    'mt':[
        'singlemuon_24',
        'singlemuon_27',
        'crossmuon_mu24tau20',
        'crossmuon_mu20tau27',
        ],
    'tt':[
        'singletau',
        'doubletau_35_mediso',
        'doubletau_35_tightiso_tightid',
        'doubletau_40_mediso_tightid',
        'doubletau_40_tightiso',
        ],
}

# Triggers prefix and suffixes=status
triggers_prefix = 'trg_'
triggers_status = ['', 'matched', 'fired']

###_________________________________________________________________###

# The following is not supposed to be modified once ready

triggers_lists={}
any_trigger_strs={}
triggers_CutFlows={}

for channel in triggers_base_per_channel.keys():
    triggers_lists[channel]={}
    any_trigger_strs[channel]={}
    triggers_CutFlows[channel]={}
    for status in triggers_status:
        if status == '':
            suffix = ''
        else:
            suffix = '_'+status
        triggers_list = [triggers_prefix+trgstr+suffix for trgstr in triggers_base_per_channel[channel]]
        triggers_lists[channel][status] = triggers_list
        any_trigger_str = ' ( '+' || '.join(triggers_list)+' ) '
        any_trigger_strs[channel][status] = any_trigger_str
        triggers_CutFlows[channel][status] = CutFlow(
            [('triggers_'+channel+suffix, any_trigger_str)]
        )
