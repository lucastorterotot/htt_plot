from htt_plot.tools.cut import Cut

##################
# Define variables values for cuts
##################

pt1=23.
eta1=2.1
iso1=0.15
pt2=30.
eta2=2.3
iso2=1. #1.5

mt_cut_value = 70.

##################
# Define general cuts
##################

cut_flags = Cut('Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_goodVertices && Flag_eeBadScFilter && Flag_globalTightHalo2016Filter && passBadMuonFilter && passBadChargedHadronFilter && badMuonMoriond2017 && badCloneMuonMoriond2017')

cut_vetoes = Cut('!veto_dilepton && !veto_thirdlepton && !veto_otherlepton')

cut_OS = Cut('l1_charge != l2_charge')
cut_SS = ~cut_OS

cut_tau_kinematics = Cut('l2_pt>{pt2} && abs(l2_eta)<{eta2}'.format(pt2=pt2,eta2=eta2))
cut_tau_vertex = Cut('abs(l2_dz)<0.2')
cut_tau_ID = Cut('l2_decayModeFinding>0.5 && l2_againstElectronMVA6>0.5 && l2_againstMuon3>1.5')
cut_tau_iso = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>3.5')

cut_mu_kinematics = Cut('l1_pt>{pt1} && abs(l1_eta)<{eta1}'.format(pt1=pt1,eta1=eta1))
cut_mu_vertex = Cut('abs(l1_dxy)<0.045 && abs(l1_dz)<0.2')
cut_mu_ID = Cut('l1_muonid_medium>0.5')
cut_mu_iso = Cut('l1_reliso05<{iso1}'.format(iso1=iso1))

cut_kinematics = cut_mu_kinematics & cut_tau_kinematics
cut_vertex = cut_mu_vertex & cut_tau_vertex
cut_ID = cut_mu_ID & cut_tau_ID
cut_iso = cut_mu_iso & cut_tau_iso

##################
# Define cuts for DY categories
##################

cut_ztt = Cut('gen_match_2==5')
cut_zl = Cut('gen_match_2<5')
cut_zj = Cut('gen_match_2==6')

##################
# Define cuts for W estimation
##################

cut_high_mt = Cut('mt_total>{mt_cut_value}'.format(mt_cut_value=mt_cut_value))
cut_low_mt = ~cut_high_mt

##################
# Define cuts for QCD estimation
##################

cut_general_QCD = cut_flags & cut_vetoes & cut_kinematics & cut_vertex & cut_ID
cut_iso_QCD_A = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>2.5')
cut_iso_QCD_max = Cut('l2_byIsolationMVArun2v1DBoldDMwLT>0.5')
cut_iso_QCD_C = ~cut_iso_QCD_A & cut_iso_QCD_max
cut_iso_QCD_D = cut_iso_QCD_C

cut_QCD_A = cut_iso_QCD_A & cut_SS & cut_general_QCD
cut_QCD_C = cut_iso_QCD_C & cut_OS & cut_general_QCD
cut_QCD_D = cut_iso_QCD_D & cut_SS & cut_general_QCD

##################
# Define cuts for plotting
##################

cut_plot_mutau = cut_flags & cut_vetoes & cut_kinematics & cut_vertex & cut_ID & cut_iso & cut_OS
