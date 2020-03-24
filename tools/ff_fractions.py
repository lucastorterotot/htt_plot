from ROOT import TFile, TH1F, TDirectoryFile

channels_names = {
    'tt' : 'tt',
    'mt' : 'mt',
    'et' : 'et'
    }

def make_fractions(output_dir, channel, components_dict):
    for variable in components_dict.keys():
        for category in components_dict[variable].keys():
            for sys in components_dict[variable][category].keys():
                make_fractions_single(output_dir, channel, variable, components_dict[variable][category][sys], category=category, systematic=sys)
            print('FF frac file for category {} and variable {} made with {} systematics.'.format(category, variable, len(components_dict[variable][category].keys())))

def make_fractions_single(output_dir, channel, variable, components_dict, category='inclusive', systematic='nominal'):
    '''This funciton aims at producing a root file containing all
    histograms needed for datacards. To do so, provide a dict of components
    (class Component) that have the ROOT histograms to be used.
    Gives also the output directory and the variable name, so that you can
    make datacards for different variables.'''
    rootfilename = '_'.join(['htt', channel, 'for_FF_fractions'])
    rootfile = TFile('{}/{}.root'.format(output_dir, rootfilename), 'UPDATE')
    rootdirname = '_'.join([channels_names[channel], variable, category])
    rootdir = rootfile.GetDirectory(rootdirname)
    if not rootdir:
        rootdir = TDirectoryFile(rootdirname, rootdirname)
    rootdir.cd()
    for key, component in components_dict.iteritems():
        histname = '_'.join([key,systematic])
        if systematic == 'nominal':
            histname = key
        else:
            histname = histname.replace('up','Up')
            histname = histname.replace('down','Down')
        if rootdir.Get(histname):
            continue
        hist = component.histogram.Clone(histname)
        if histname[:len("fakes_")] == "fakes_":
            hist.Scale(-1)
        hist.SetTitle(key)
        hist.Write()
    rootfile.Close()
