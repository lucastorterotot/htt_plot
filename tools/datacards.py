from ROOT import TFile, TH1F

def make_datacards(output_dir, variable, components_dict):
    rootfile = TFile(output_dir+'/datacards_'+variable+'.root', 'recreate')
    for key, component in components_dict.items():
        hist = TH1F(key, 'Datacard '+key+' for var '+variable, *component.cfg.bins)
        hist.Add(component.histogram)
        hist.Write()
    rootfile.Close()
