from htt_plot.tools.cut import Cut, CutFlow

cut_defs_per_channel = {
    'tt' : [
        Cut('ZTT', 'l1_gen_match==5 && l2_gen_match==5'),
        Cut('ZL', 'l1_gen_match<6 && l2_gen_match<6 && !(l1_gen_match==5 && l2_gen_match==5)'),
        Cut('ZJ', 'l1_gen_match==6 || l2_gen_match==6'),
        Cut('TTT', 'l1_gen_match==5 && l2_gen_match==5'),
        Cut('TTJ', '!(l1_gen_match==5 && l2_gen_match==5)'),
        Cut('VVT', '(l1_gen_match==5 && l2_gen_match==5)'),
        Cut('VVJ', '!(l1_gen_match==5 && l2_gen_match==5)'),
    ],
    'mt' : [
        Cut('ZTT', 'l2_gen_match==5'),
        Cut('ZL', 'l2_gen_match<5'),
        Cut('ZJ', 'l2_gen_match==6'),
        Cut('TTT', 'l2_gen_match==5'),
        Cut('TTJ', 'l2_gen_match!=5'),
        Cut('VVT', 'l2_gen_match==5'),
        Cut('VVJ', 'l2_gen_match!=5'),
    ],
    'all' : [
        Cut('W', '1'),
        Cut('jetFakes', '1'),
    ],
}

# For etau, mutau and tautau channels, ZLL = ZL+ZJ defined later in this file
# For etau, mutau and tautau channels, TT = TTT+TTJ defined later in this file
# For etau, mutau and tautau channels, VV = VVT+VVJ defined later in this file

# Not using CutFlow to get only Cuts in final dicts
def get_cut_add(key, channel, cut_keys):
    cutstr = '(' + ') || ('.join(
        [cuts_datacards[channel][cut].cutstr for cut in cut_keys]
    ) + ')'
    return Cut(key, cutstr)

cut_defs_per_channel['et'] = cut_defs_per_channel['mt']

cuts_datacards = {}

from htt_plot.cuts.htt_cuts import channels
for channel in channels:
    cuts_datacards[channel] = {}
    for cut in cut_defs_per_channel[channel] + cut_defs_per_channel['all']:
        cuts_datacards[channel][cut.name] = cut
    cuts_datacards[channel]['ZLL']= get_cut_add('ZLL',channel, ['ZL',  'ZJ' ])
    cuts_datacards[channel]['TT'] = get_cut_add('TT', channel, ['TTT', 'TTJ'])
    cuts_datacards[channel]['VV'] = get_cut_add('VV', channel, ['VVT', 'VVJ'])
