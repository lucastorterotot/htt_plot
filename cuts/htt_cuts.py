from htt_plot.tools.cut import Cut, CutFlow
import pprint

# Give here for ele/mu/tau variables names as stored in root files
# and the appropriate cut for each channel

t_cuts_tt = {'pt' : '>40',
             'eta' : '<2.1',
             'dz' : '<0.2',
             'decayModeFinding' : '>0.5',
             'q' : '==1.',
             'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017' : '>0.5',
             'againstElectronVLooseMVA6' : '>0.5',
             'againstMuonLoose3' : '>0.5'}
t_cuts_mt = t_cuts_tt
t_cuts_mt['pt'] = '>23'
t_cuts_mt['eta'] = '<=2.3'
t_cuts_et = t_cuts_mt

m_cuts_mt = {'pt' : '>=21',
             'eta' : '<=2.1',
             'dxy' : '<0.045',
             'dz' : '<0.2',
             'iso' : '<0.3'}

e_cuts_et = {'pt' : '>=25',
             'eta' : '<=2.1',
             'dxy' : '<0.045',
             'dz' : '<0.2',
             'iso' : '<0.3'}

# Other cuts not to be processed as cuts listed before

cuts_signal = CutFlow([
    ('mt_tot', 'mt_tot<40'),     
])

cuts_btag_1 = CutFlow([
    ('Btag_1', '(bjet1_csv > 0)'),     
])

cuts_btag_2 = CutFlow([
    ('Btag_2', '(bjet2_csv > 0)'),     
])

###_________________________________________________________________###

# The following is not supposed to be modified once ready

cuts_categories = {
    'kine' : ['pt', 'eta'],
    'id' : {
        'e' : ['id', 'vertex'],
        'm' : ['id', 'vertex'],
        't' : ['charge', 'vertex', 'decaymode', 'against_e', 'against_mu'],
    },
    'iso' :  ['iso'],
}

cuts_lists_per_channel = {
    'tt' : [t_cuts_tt, t_cuts_tt],
    'mt' : [m_cuts_mt, t_cuts_mt],
    'et' : [e_cuts_et, t_cuts_et],
}

channels = cuts_lists_per_channel.keys()

vars_translator = {
    'tt' : {
        't' : {
            'charge' : 'q',
            'decaymode' : 'decayModeFinding',
            'against_e' : 'againstElectronVLooseMVA6',
            'against_mu': 'againstMuonLoose3',
            'iso' : 'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017',
        },
    },
    'mt' : {
        'm' : {},
    },
    'et' : {
        'e' : {},
    },
}

for channel in ['mt', 'et']:
    vars_translator[channel]['t'] = vars_translator['tt']['t']

variables_cut_on_absolute = ['eta', 'dxy', 'dz', 'q']

def get_cut_flow(variables, channel, ptckey):
    result = []
    ptc = ptckey[0]
    for variable in variables:
        if get_cut_str(variable, channel, ptckey) :
            result.append((ptckey+'_'+variable,get_cut_str(variable, channel, ptckey)))
    return result

def get_cut_str(variable, channel, ptckey):
    if channel[0] == channel[1] and len(ptckey)==2:
        leg = channel.index(ptckey[0])+int(ptckey[1])
    else:
        leg = channel.index(ptckey[0])+1
    cuts_list = cuts_lists_per_channel[channel][leg-1]
    if variable == 'vertex':
        result = []
        for dxyz in ['dxy', 'dz']:
            if dxyz in cuts_list.keys():
                result.append(get_cut_str(dxyz, channel, ptc))
        return ' && '.join(result)
    if variable in vars_translator[channel][ptc].keys() and \
       variable not in cuts_list.keys():
        variable = vars_translator[channel][ptc][variable]
    if variable in cuts_list.keys():
        legvar = 'l'+str(leg)+'_'+variable
        if variable in variables_cut_on_absolute:
            legvar = 'abs('+legvar+')'
        return legvar+cuts_list[variable]
    else:
        return None

def get_other_cut_str(variable, dic):
    if variable in dic.keys():
        return variable+dic[variable]
    else:
        return None
    
cuts = {}

for channel in channels:
    cuts[channel] = {}
    cuts[channel]['signal'] = CutFlow([])
    for leg in [1,2]:
        ptc = channel[leg-1]
        ptckey = ptc
        if channel[0] == channel[1]:
            ptckey+=str(leg)
        cuts[channel][ptckey] = {}
        cuts[channel][ptckey]['all'] = CutFlow([])
        for category in cuts_categories.keys():
            variables = cuts_categories[category]
            if isinstance(variables, dict):
                variables = variables[ptc]
            cuts[channel][ptckey][category] = CutFlow(get_cut_flow(variables, channel, ptckey))
            cuts[channel][ptckey]['all'] += cuts[channel][ptckey][category]
        cuts[channel]['signal'] += cuts[channel][ptckey]['all']
        for variable in cuts_signal.keys():
            cuts[channel]['signal'] += cuts_signal
