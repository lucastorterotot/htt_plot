from btag import cuts as btag
from cuts import Cuts

vars = ['mttot', 'pt']

cuts = Cut(
    cut_l1 = 'l1_pt>10 && abs(l1_eta)<1'
    cut_l1_iso = 'l1_tauiso<0.1'
    cut_l2 = 'l1_pt>10 && abs(l1_eta)<1'
    cut_l2_iso = 'l2_tauiso<0.2'
    cut_os = 'l1_q ** l2_q<0'
)

cuts.update(btag.items())

cuts.print_cuts()
print(cuts)
