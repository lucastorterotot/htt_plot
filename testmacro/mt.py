from cuts import Cuts

cuts = Cuts(
    l1 = 'l1_pt>10 && abs(l1_eta)<1',
    l1_iso = 'l1_iso<0.1',
    l2 = 'l1_pt>10 && abs(l1_eta)<1',
    l2_iso = 'l2_tauiso<0.2',
    os = 'l1_q ** l2_q<0',
)

cuts.print_cuts()
print(cuts)
