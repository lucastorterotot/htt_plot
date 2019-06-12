from htt_plot.tools.cut import Cuts

weights = Cuts(
    weight = 'weight',
    MC = 'l1_weight_mutotaufake_loose * l1_weight_etotaufake_vloose * l1_weight_tauid_vtight * l2_weight_mutotaufake_loose * l2_weight_etotaufake_vloose * l2_weight_tauid_vtight',
    DY = 'weight_dy * weight_generator',# * '+dy_stitching_weight
    embed = 'weight_embed_DoubleMuonHLT_eff * weight_embed_muonID_eff_l1 * weight_embed_muonID_eff_l2 * weight_embed_DoubleTauHLT_eff_l1 * weight_embed_DoubleTauHLT_eff_l2 * weight_embed_track_l1 * weight_embed_track_l2',
    l1_fake = 'l1_fakeweight*0.5',
    l2_fake = 'l2_fakeweight*0.5'
    )
