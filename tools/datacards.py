from ROOT import TFile, TH1F

def make_datacards(output_dir, variable, components_dict):
    '''This funciton aims at producing a root file containing all
    histograms needed for datacards. To do so, provide a dict of components
    (class Component) that have the ROOT histograms to be used.
    Gives also the output directory and the variable name, so that you can
    make datacards for different variables.'''
    
    rootfile = TFile(output_dir+'/datacards_'+variable+'.root', 'recreate')
    for key, component in components_dict.items():
        hist = component.histogram.Clone(key)
        hist.SetTitle(key)
        hist.Write()
    rootfile.Close()
    print('Datacards for var '+variable+' made.')
