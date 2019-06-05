from htt_plot.tools.cut import Cut, CutFlow
import pprint

isolation_strings = {
    'VTight' : 'byVTightIsolationMVArun2017v2DBoldDMwLT2017',
    'Tight' : 'byTightIsolationMVArun2017v2DBoldDMwLT2017',
    'VLoose' : 'byVLooseIsolationMVArun2017v2DBoldDMwLT2017',
    'VVLoose' : 'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017'
}

cuts_iso = {}

from htt_plot.cuts.htt_cuts import channels
for channel in channels:
    cuts_iso[channel] = {}
    for wp in isolation_strings.keys():
        cuts_iso[channel][wp] = {}
        for leg in [1,2]:
            ptc = channel[leg-1]
            if channel[0] == channel[1]:
                ptc+=str(leg)
            if 't' in ptc :
                cutstr = 'l'+str(leg)+'_'+isolation_strings[wp]+'>0.5'
            else:
                cutstr = '1'
            cuts_iso[channel][wp][ptc] = Cut(
                'l'+str(leg)+'_'+wp+'_isolation',
                cutstr
            )
