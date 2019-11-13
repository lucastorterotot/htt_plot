import copy

from ROOT import TFile, TPaveText
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.component import Hist_Component
from cpyroot.tools.DataMC.Stack import Stack

cat_dict = {'tt_nobtag':'htt_tt_8_13TeV',
            'tt_btag':'htt_tt_9_13TeV'}
#{'tt_inclusive':'htt_tt_7_13TeV'}

data_file = TFile('htt_tt.inputs_datacards_mt_tot.root')
shapes_file = TFile('fitDiagnosticstest_output.root')

def plot(prefit=True,bonly=True):
    if prefit:
        shapedir = 'shapes_prefit'
    else:
        if bonly:
            shapedir = 'shapes_fit_b'
        else:
            shapedir = 'shapes_fit_s'
    
    for cat in cat_dict:
        ### subdir retrieval
        data_shape_dir = data_file.Get(cat)
        shapes_dir = shapes_file.Get(shapedir).Get(cat_dict[cat])
        unc_hist = shapes_dir.Get('total_background')

        
        comp_names = ['TTL','VVL','ZL','Embedded','jetFakes']
        comps = []

        data_hist = data_shape_dir.Get('data_obs')
        data_hist.SetTitle('')
        data_histcomp = copy.copy(data_hist)
        for b in range(data_hist.GetNbinsX()):
                data_histcomp.SetBinContent(b+1,data_hist.GetBinContent(b+1)/(data_hist.GetBinLowEdge(b+2)-data_hist.GetBinLowEdge(b+1)))
                if data_hist.GetBinContent(b+1)==0.:
                    data_histcomp.SetBinError(b+1,1)
                else:
                    data_histcomp.SetBinError(b+1,data_hist.GetBinError(b+1)*data_histcomp.GetBinContent(b+1)/data_hist.GetBinContent(b+1))
        comp = Hist_Component(data_histcomp)
        comp.var = 'mt_tot'
        comps.append(comp)
    
        for comp_name in comp_names:
            unvar_h = shapes_dir.Get(comp_name)
            h = copy.copy(data_hist)
            h.SetName(comp_name)
            for b in range(h.GetNbinsX()):
                h.SetBinContent(b+1,unvar_h.GetBinContent(b+1)/(h.GetBinLowEdge(b+2)-h.GetBinLowEdge(b+1)))
                h.SetBinError(b+1,0)
            h.SetTitle('')
            comp = Hist_Component(h)
            comp.var = 'mt_tot'
            comps.append(comp)

        # if prefit:
        #     unvar_sig_gg = data_shape_dir.Get('ggH600')
        #     unvar_sig_bb = data_shape_dir.Get('bbH600')
        # else:
        #     unvar_sig_gg = shapes_dir.Get('ggH')
        #     unvar_sig_bb = shapes_dir.Get('bbH')
        # sig_hist = copy.copy(data_hist)
        # sig_hist.SetName('signal_H600')
        # for b in range(sig_hist.GetNbinsX()):
        #     sig_hist.SetBinContent(b+1,unvar_sig_gg.GetBinContent(b+1)+unvar_sig_bb.GetBinContent(b+1))
        #     sig_hist.SetBinError(b+1,0)
        # sig_hist.SetTitle('')
        # comp_sig = Hist_Component(sig_hist)
        # comp_sig.var = 'mt_tot'
        # comps.append(comp_sig)
        
        ### prep unc hist
        uncertainties = copy.copy(data_hist)
        uncertainties.SetName('total_background')
        uncertainties_rel = copy.copy(uncertainties)
        for b in range(uncertainties.GetNbinsX()):
            uncertainties.SetBinContent(b+1,unc_hist.GetBinContent(b+1)/(data_hist.GetBinLowEdge(b+2)-data_hist.GetBinLowEdge(b+1)))
            uncertainties.SetBinError(b+1,unc_hist.GetBinError(b+1)*uncertainties.GetBinContent(b+1)/unc_hist.GetBinContent(b+1))
            uncertainties_rel.SetBinContent(b+1,1)
            uncertainties_rel.SetBinError(b+1,uncertainties.GetBinError(b+1)/uncertainties.GetBinContent(b+1))
        
        plotter = Plotter(comps,41.5)

        plotter.draw('m_{T}^{tot}','dN/dm_{T}^{tot} (1/GeV)', sys_error_hist=uncertainties, category="#tau_{h}#tau_{h} inclusive")
        if prefit:
            outfilename = 'prefit_plots_{}'
        else:
            if bonly:
                outfilename = 'postfit_b_plots_{}'
            else:
                outfilename = 'postfit_s_plots_{}'
        # plotter.write((outfilename+'.root').format(cat))
        plotter.write((outfilename+'.pdf').format(cat))
        plotter.write((outfilename+'.png').format(cat))

plot(prefit=False,bonly=True)
# plot(prefit=False,bonly=True)
