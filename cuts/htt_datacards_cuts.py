from htt_plot.tools.cut import Cuts

cuts_tt = Cuts(
    ZTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    ZL = 'l1_gen_match < 6 && l2_gen_match < 6 && !(l1_gen_match == 5 && l2_gen_match == 5)',
    ZJ = 'l1_gen_match == 6 || l2_gen_match == 6',
    TTT = 'l1_gen_match == 5 && l2_gen_match == 5',
    TTJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    VVT = '(l1_gen_match == 5 && l2_gen_match == 5)',
    VVJ = '!(l1_gen_match == 5 && l2_gen_match == 5)',
    W = '1',
    jetFakes = '1',
)

cuts_mt = Cuts(
    ZTT = 'l2_gen_match == 5',
    ZL = 'l2_gen_match < 5',
    ZJ = 'l2_gen_match == 6',
    TTT = 'l2_gen_match == 5',
    TTJ = 'l2_gen_match != 5',
    VVT = 'l2_gen_match == 5',
    VVJ = 'l2_gen_match != 5',
    W = '1',
    jetFakes = '1',
)

cuts_et = cuts_mt.clone()

# For etau, mutau and tautau channels, ZLL = ZL+ZJ 
# For etau, mutau and tautau channels, TT = TTT+TTJ 
# For etau, mutau and tautau channels, VV = VVT+VVJ 

for cuts in [cuts_tt, cuts_mt, cuts_et]:
    cuts += Cuts(
        ZLL = cuts['ZL'] | cuts['ZJ'],
        TT = cuts['TTT'] | cuts['TTJ'],
        VV = cuts['VVT'] | cuts['VVJ'],
    )
