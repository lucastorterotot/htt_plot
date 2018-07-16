from dask import delayed
from htt_plot.components.lucas_small import *
from htt_plot.tools.plot import hist, add

var = 'mt_total'
cut = '1'
bins = 50, 0., 500.

mode = 'parallel'
if mode is 'parallel':
    hist = delayed(hist)
    add = delayed(add)

h_data1 = hist('data1', data1, var, cut, *bins)
h_data2 = hist('data2', data2, var, cut, *bins)
h_data3 = hist('data3', data3, var, cut, *bins)
h_data4 = hist('data4', data4, var, cut, *bins)

all_data = [h_data1, h_data2, h_data3, h_data4]

h_data = add('data', all_data)
# h_data.visualize()
if mode is 'parallel':
    print 'running'
    # h_data = h_data.compute(scheduler='single-threaded')
    h_data = h_data.compute()
print h_data.GetEntries()
h_data.Draw()


