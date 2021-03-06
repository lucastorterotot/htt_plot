from ROOT import TFile, TH1F, TDirectoryFile

channels_names = {
    'tt' : 'tt',
    'mt' : 'mt',
    'et' : 'et'
    }

syst_rename_dir = {
    }

# some systematics are 50% correlated between backgrounds => copy and rename datacards with adapted names that will be taken into account with a 0.5 factor

syst_split_list = {
    'TES_HadronicTau_1prong0pi0_up',
    'TES_HadronicTau_1prong0pi0_down',
    'TES_HadronicTau_1prong1pi0_up',
    'TES_HadronicTau_1prong1pi0_down',
    'TES_HadronicTau_3prong0pi0_up',
    'TES_HadronicTau_3prong0pi0_down',
    'TES_HadronicTau_3prong1pi0_up',
    'TES_HadronicTau_3prong1pi0_down',
    'TES_promptMuon_1prong0pi0_up',
    'TES_promptMuon_1prong0pi0_down',
    'TES_promptEle_1prong0pi0_up',
    'TES_promptEle_1prong0pi0_down',
    'TES_promptEle_1prong1pi0_up',
    'TES_promptEle_1prong1pi0_down'
    }

types_dir = {
    'Embedded' : ['emb_'],
    'TTL' : ['mc_'],
    'VVL' : ['mc_'],
    'ZL' : ['mc_'],
    'jetFakes' : ['emb_','mc_'],
    'ZTT' : ['mc_'],
    'ZJ' : ['mc_'],
    'TTT' : ['mc_'],
    'TTJ' : ['mc_'],
    'VVT' : ['mc_'],
    'VVJ' : ['mc_'],
    'W' : ['mc_']
    }

for _H125 in ['HiggsVBF125', 'HiggsGGH125', 'HiggsGGH125_ext', 'HiggsTTH125', 'HiggsWplusH125', 'HiggsWminusH125', 'HiggsZH125']:
    types_dir[_H125] = ['mc_']

for mass in [80,100,110,120,130,140,180,200,250,90,350,1600,1800,2000,300,400,450,600,700,800,900,1200,1400,1500,2300,2600,2900,3200]:
    types_dir['ggH{}'.format(mass)] = ['mc_']
    types_dir['bbH{}'.format(mass)] = ['mc_']

#jetFakes-related systematics shift histograms must be re-normalized to the nominal integral (see https://gitlab.cern.ch/cms-htt/Jet2TauFakesFiles/tree/2017/SM2017#step-3-application-of-uncertainties) for now hardcoding the value of the integral of nominal jetFakes contributionto re-scale
jetFakes_integral = {'nobtag': 28226.1,
                     'btag': 679.867}
    
def make_datacards(output_dir, channel, variable, components_dict_with_categories, systematics=['nominal']):
    for category in components_dict_with_categories.keys():
        make_datacards_singlecat(output_dir, channel, variable, components_dict_with_categories[category], category=category, systematics=systematics)

def make_datacards_singlecat(output_dir, channel, variable, components_dict, category='inclusive', systematics=['nominal']):
    '''This funciton aims at producing a root file containing all
    histograms needed for datacards. To do so, provide a dict of components
    (class Component) that have the ROOT histograms to be used.
    Gives also the output directory and the variable name, so that you can
    make datacards for different variables.'''
    rootfilename = '_'.join(['htt', channel+'.inputs', 'datacards', variable])
    rootfile = TFile('{}/{}.root'.format(output_dir, rootfilename), 'UPDATE')
    rootdirname = '_'.join([channels_names[channel], category])
    rootdir = rootfile.GetDirectory(rootdirname)
    if not rootdir:
        rootdir = TDirectoryFile(rootdirname, rootdirname)
    rootdir.cd()
    for systematic in systematics:
        for key, component in components_dict[systematic].iteritems():
            histname = '_'.join([key,systematic])
            if systematic == 'nominal':
                histname = key
            elif histname in syst_rename_dir:
                histname = syst_rename_dir[histname]
            else:
                histname = histname.replace('up','Up')
                histname = histname.replace('down','Down')
            if rootdir.Get(histname):
                continue
            hist = component.histogram.Clone(histname)
            if 'jetFakes' in histname and 'ff_' in systematic :
                hist.Scale(components_dict['nominal']['jetFakes'].histogram.Integral(0,hist.GetNbinsX()+1)/hist.Integral(0,hist.GetNbinsX()+1))
            hist.SetMinimum(0.0)
            hist.SetBinContent(0,0)
            hist.SetBinContent(hist.GetNbinsX()+1,0)
            hist.SetTitle(key)
            #if not ((systematic!='nominal') and ('jetFakes' in histname)):
            hist.Write()
            if systematic in syst_split_list:
                hist_list = []
                for sys_type in types_dir[key]:
                    if 'Down' in histname:
                        new_histname = histname.replace('Down',sys_type+'Down')
                    elif 'Up' in histname:
                        new_histname = histname.replace('Up',sys_type+'Up')
                    hist_list.append(component.histogram.Clone(new_histname))
                    hist_list[-1].SetMinimum(0.0)
                    hist_list[-1].SetBinContent(0,0)
                    hist_list[-1].SetBinContent(hist.GetNbinsX()+1,0)
                    hist_list[-1].SetTitle(key)
                    hist_list[-1].Write()
    rootfile.Close()
    print('Datacards for category {} and variable {} made.'.format(category, variable))
