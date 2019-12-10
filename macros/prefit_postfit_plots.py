import copy

from ROOT import TFile, TPaveText, Double, TH1F
from htt_plot.tools.plotting.plotter import Plotter
from htt_plot.tools.component import Hist_Component
from cpyroot.tools.DataMC.Stack import Stack
from array import array


cat_dict = { 'tt_btag':'htt_tt_9_13TeV'}#'tt_nobtag':'htt_tt_8_13TeV',
#{'tt_inclusive':'htt_tt_7_13TeV'}


limits = {600:0.0341033935546875,
          800:0.037841796875,
          900:0.0146484375
}

def plot(prefit=True,bonly=True, mass=None):
    data_file = TFile('htt_tt.inputs_datacards_mt_tot.root')
    if mass:
        shapes_file = TFile('fitDiagnosticstest_output_{}.root'.format(mass))
    else:
        shapes_file = TFile('fitDiagnosticstest_output.root')
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

        data_hist_tmp = data_shape_dir.Get('data_obs')
        if cat == 'tt_btag':
            data_hist = TH1F('data_obs','data_obs', 29, array('d',[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,225,250,275,300,325,350,400,500,4000]))
        elif cat == 'tt_nobtag':
            data_hist = TH1F('data_hist','data_hist', 29, array('d',[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,225,250,275,300,325,350,400,500,700,900,4000]))
        data_hist.SetTitle('')
        data_histcomp = copy.copy(data_hist)
        data_graph = shapes_dir.Get('data')
        for b in range(data_hist.GetNbinsX()):
            x = Double(0)
            y = Double(0)
            data_graph.GetPoint(b,x,y)
            data_histcomp.SetBinContent(b+1,y/(data_hist.GetBinLowEdge(b+2)-data_hist.GetBinLowEdge(b+1)))
            if y==0.:
                data_histcomp.SetBinError(b+1,1)
            else:
                data_histcomp.SetBinError(b+1,data_graph.GetErrorY(b)*data_histcomp.GetBinContent(b+1)/y)
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

        if mass:
            unvar_sig_bb = shapes_dir.Get('bbH')
            sig_hist = copy.copy(data_hist)
            sig_hist.SetName('signal_bbH{}'.format(mass))
            for b in range(sig_hist.GetNbinsX()):
                sig_hist.SetBinContent(b+1,(unvar_sig_bb.GetBinContent(b+1))/(data_hist.GetBinLowEdge(b+2)-data_hist.GetBinLowEdge(b+1)))
                sig_hist.SetBinError(b+1,0)
            # sig_hist.Scale(limits[mass])
            sig_hist.SetTitle('')
            comp_sig = Hist_Component(sig_hist)
            comp_sig.var = 'mt_tot'
            comps.append(comp_sig)
        
            # unvar_sig_gg = data_shape_dir.Get('ggH{}'.format(mass))
            # sig_hist = copy.copy(data_hist)
            # sig_hist.SetName('signal_ggH{}'.format(mass))
            # for b in range(sig_hist.GetNbinsX()):
            #     sig_hist.SetBinContent(b+1,(unvar_sig_gg.GetBinContent(b+1))/(data_hist.GetBinLowEdge(b+2)-data_hist.GetBinLowEdge(b+1)))
            #     sig_hist.SetBinError(b+1,0)
            # sig_hist.SetTitle('')
            # comp_sig = Hist_Component(sig_hist)
            # comp_sig.var = 'mt_tot'
            # comps.append(comp_sig)
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
        cat_name = "#tau_{h}#tau_{h} " + cat[3:]
        plotter.draw('m_{T}^{tot}','dN/dm_{T}^{tot} (1/GeV)', sys_error_hist=uncertainties, category=cat_name)
        if prefit:
            outfilename = 'prefit_plots_{}'
        else:
            if bonly:
                outfilename = 'postfit_b_plots_{}'
            else:
                outfilename = 'postfit_s_plots_{}'
        if mass:
            # plotter.write((outfilename+str(mass)+'.root').format(cat))
            plotter.write((outfilename+str(mass)+'.pdf').format(cat))
            plotter.write((outfilename+str(mass)+'.png').format(cat))
        else:
            # plotter.write((outfilename+'.root').format(cat))
            plotter.write((outfilename+'.pdf').format(cat))
            plotter.write((outfilename+'.png').format(cat))

# plot(prefit=False,bonly=False)
# plot(prefit=False,bonly=True)
for mass in [400,450,600,800,900,1400,1800,2000]:
    plot(prefit=False,bonly=False,mass=mass)
