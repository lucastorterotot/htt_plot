from ROOT import TFile, TH1F

def make_datacards(output_dir, variable, **kwargs):
    ''' kwargs are components which names are the future TH1 names '''
    rootfile = TFile(output_dir+'/datacards_'+variable+'.root', 'recreate')
    for key in kwargs.keys():
        component = kwargs[key]
        hist = TH1F(key, 'Datacard '+key+' for var '+variable, *component.cfg.bins[variable])
        hist.Add(component.histogram[variable])
        hist.Write()
    rootfile.Close()
