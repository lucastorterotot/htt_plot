
import htt_plot.tools.config as config
config.parallel = False

from htt_plot.components.lucas_small import *
from htt_plot.tools.plot import hist, add

from htt_plot.cuts.generic import cuts_generic
from htt_plot.cuts.mt import cuts_mt

cuts = cuts_generic + cuts_mt
var = 'mt_total'
cut = str(cuts)
bins = 50, 0., 500.

h_data1 = hist('data1', data1, var, cut, *bins)
h_data2 = hist('data2', data2, var, cut, *bins)
h_data3 = hist('data3', data3, var, cut, *bins)
h_data4 = hist('data4', data4, var, cut, *bins)

all_data = [h_data1, h_data2, h_data3, h_data4]

h_data = add('data', all_data)
# h_data.visualize()
if config.parallel:
    print 'running'
    # h_data = h_data.compute(scheduler='single-threaded')
    h_data = h_data.compute()
print h_data.GetEntries()
h_data.Draw()


