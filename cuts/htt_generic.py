from htt_plot.tools.cut import Cut, CutFlow
import pprint

cut_l1_fakejet = Cut('l1_fakejet','l1_gen_match==6')
cut_l2_fakejet = Cut('l2_fakejet','l2_gen_match==6')

cut_os = Cut('opposite_sign', 'l1_q != l2_q')
cut_ss = Cut('same_sign',  'l1_q == l2_q')

cut_dy_promptfakeleptons = Cut('cut_dy_promptfakeleptons', 'l1_gen_match==1 || l1_gen_match==2 || l2_gen_match==1 || l2_gen_match==2')
# cut_dy_signal = Cut('dy_signal',)

cut_TT_nogenuine = Cut('cut_TT_nogenuine', '!(l1_gen_match==5 && l2_gen_match==5)')
