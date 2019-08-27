from ROOT import TFile, TH1F, TDirectoryFile

channels_names = {
    'tt' : 'tt',
    'mt' : 'tt',
    'et' : 'tt'
    }

def make_datacards(output_dir, channel, variable, components_dict, category='inclusive', systematics=['nominal']):
    '''This funciton aims at producing a root file containing all
    histograms needed for datacards. To do so, provide a dict of components
    (class Component) that have the ROOT histograms to be used.
    Gives also the output directory and the variable name, so that you can
    make datacards for different variables.'''
    rootfilename = '_'.join(['htt', channel+'.inputs', 'datacards', variable])
    rootfile = TFile('{}/{}.root'.format(output_dir, rootfilename), 'UPDATE')
    rootdirname = '_'.join([channels_names[channel], category])
    rootdir = TDirectoryFile(rootdirname, rootdirname)
    rootdir.cd()
    for systematic in systematics:
        for key, component in components_dict[systematic].iteritems():
            if systematic == 'nominal':
                histname = key
            else:
                histname = '_'.join([key,systematic])
                histname = histname.replace('up','Up')
                histname = histname.replace('down','Down')
            hist = component.histogram.Clone(histname)
            hist.SetTitle(key)
            hist.Write()
    rootfile.Close()
    print('Datacards for category {} and variable {} made.'.format(category, variable))
