from htt_plot.tools.cut import Cuts

cut_l1_fakejet = Cuts(
    l1_fakejet = 'l1_gen_match==6'
)

cut_l2_fakejet = Cuts(
    l2_fakejet = 'l2_gen_match==6'
)

cut_os = Cuts(
    signs = 'l1_q != l2_q'
)

cut_ss = ~cut_os

cut_dy_promptfakeleptons = Cuts(
    dy_promptfakeleptons = 'l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2'
)

cut_TT_nogenuine = Cuts(
    TT_nogenuine = '!(l1_gen_match==5 && l2_gen_match==5)'
)
