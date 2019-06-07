from ROOT import TFile

def make_datacards(output_dir, variable, **kwargs):
    ''' kwargs are components which names are the future TH1 names '''
    rootfile = TFile(output_dir+'/datacards_'+variable+'.root', 'recreate')
    for key in kwargs.keys():
        component = kwargs[key]
        hist = component.histogram[variable]
        hist.SetName(key)
        hist.Write()
    rootfile.Close()
