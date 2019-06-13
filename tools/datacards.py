from ROOT import TFile, TH1F

def make_datacards(output_dir, variable, components_dict):
    rootfile = TFile(output_dir+'/datacards_'+variable+'.root', 'recreate')
    for key, component in components_dict.items():
        hist = component.histogram.Clone(key)
        hist.SetTitle(key)
        hist.Write()
    rootfile.Close()
    print('Datacards for var '+variable+' made.')
