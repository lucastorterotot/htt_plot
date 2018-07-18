from itertools import count
import fnmatch

from ROOT import TPaveText, TH1

from cpyroot import *
from cpyroot.tools.DataMC.DataMCPlot import DataMCPlot

from styles import set_style, histPref

class Plotter(object):

    _ihist = count(0)
    
    def __init__(self, comps, lumi):
        self.comps = comps
        for comp in self.comps:
            set_style(comp)
        self.lumi = lumi
                
    def _project(self, comp, var, cut, *bins):
        # hist_name = '{}_{}'.format(comp.name, self._ihist.next())
        hist_name = comp.name
        hist = TH1F(hist_name, '', *bins)
        if comp.tree != None:
            comp.tree.Project(hist.GetName(), var, cut)
        print hist_name
        return hist

    def _prepare_plot(self):
        plot = DataMCPlot('CHANGEME', histPref)
        for comp in self.comps:
            hist = comp.histogram
            plot.AddHistogram(comp.name, hist)
        return plot
    
    def draw(self, xtitle, ytitle):
        self.plot = self._prepare_plot()
        self.plot.DrawStack()
        # self.plot.supportHist.GetYaxis().SetTitleOffset(1.35)
        # self.plot.supportHist.GetYaxis().SetNdivisions(5)
        # self.plot.supportHist.GetXaxis().SetNdivisions(5)
        self.plot.supportHist.GetXaxis().SetTitle(xtitle)
        self.plot.supportHist.GetYaxis().SetTitle(ytitle)
        
        minX = self.plot.supportHist.GetXaxis().GetXmin()
        maxX = self.plot.supportHist.GetXaxis().GetXmax()
        NbinsX = self.plot.supportHist.GetXaxis().GetNbins()
        NticksX = 5
        for tick_num in range(1,NticksX):
            bin_to_label = int(tick_num * 1. * NbinsX/NticksX)
            bin_label = int(minX + tick_num * 1. * (maxX-minX)/NticksX)
            self.plot.supportHist.GetXaxis().SetBinLabel(bin_to_label,"{}".format(bin_label))
        self.plot.supportHist.GetXaxis().SetBinLabel(1,"{}".format(int(minX)))
        self.plot.supportHist.GetXaxis().SetBinLabel(NbinsX-1,"{}".format(int(maxX)))
        self.plot.supportHist.GetXaxis().LabelsOption("h")
        
        minY = self.plot.supportHist.GetYaxis().GetXmin()
        maxY = self.plot.supportHist.GetYaxis().GetXmax()
        NbinsY = self.plot.supportHist.GetYaxis().GetNbins()
        NticksY = 5
        for tick_num in range(1,NticksY):
            bin_to_label = int(tick_num * 1. * NbinsY/NticksY)
            bin_label = int(minY + tick_num * 1. * (maxY-minY)/NticksY)
            self.plot.supportHist.GetYaxis().SetBinLabel(bin_to_label,"{}".format(bin_label))
        self.plot.supportHist.GetYaxis().SetBinLabel(1,"{}".format(int(minY)))
        self.plot.supportHist.GetYaxis().SetBinLabel(NbinsY-1,"{}".format(int(maxY)))
        self.plot.supportHist.GetYaxis().LabelsOption("h")
        
        #import pdb; pdb.set_trace()
        gPad.Update()
   
    def write(self, fname):
        the_file = open(fname, 'w')
        the_file.write(str(self.plot))
        the_file.close()    
    
    def print_info(self, detector, xmin=None, ymin=None):
        lumitext = ''
        lumi = self.lumi
        if lumi > 1e18:
            lumi = int(self.lumi / 1e18 *10.)/10.
            lumitext = '{lumi} ab^{{-1}}'.format(lumi=lumi)
        elif lumi > 1e15:
            lumi = int(self.lumi / 1e15 *10.)/10.
            lumitext = '{lumi} fb^{{-1}}'.format(lumi=lumi)  
        elif lumi > 1e12:
            lumi = int(self.lumi / 1e12 *10.)/10.
            lumitext = '{lumi} pb^{{-1}}'.format(lumi=lumi)            
        if not xmin:
            xmin = 0.62
        if not ymin:
            ymin = 0.8
        xmax, ymax = xmin + 0.288, ymin + 0.12
        self.pave = TPaveText(xmin, ymin, xmax, ymax, 'ndc')
        self.pave.AddText(detector)
        self.pave.AddText(lumitext)
        self.pave.SetTextSizePixels(28)
        self.pave.SetTextAlign(11)
        self.pave.SetBorderSize(0)
        self.pave.SetFillColor(0)
        self.pave.SetFillStyle(0)
        self.pave.Draw()
        
