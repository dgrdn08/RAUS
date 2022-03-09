import pandas as pd

### UCLA Site

# load current registry data files
df_train_ucla_v2 = pd.read_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_train.csv',low_memory=False)
df_valid_ucla_v2 = pd.read_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_valid.csv',low_memory=False)
df_test_ucla_v2 = pd.read_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_test.csv',low_memory=False)

#start RUCA codes at 1 (for octave)
df_train_ucla_v2['ruca_7_class'] = df_train_ucla_v2.ruca_7_class.replace([2,3,4,5,6,7,8],[1,2,3,4,5,6,7])
df_train_ucla_v2['ruca_4_class'] = df_train_ucla_v2.ruca_4_class.replace([2,3,4,5],[1,2,3,4])

df_valid_ucla_v2['ruca_7_class'] = df_valid_ucla_v2.ruca_7_class.replace([2,3,4,5,6,7,8],[1,2,3,4,5,6,7])
df_valid_ucla_v2['ruca_4_class'] = df_valid_ucla_v2.ruca_4_class.replace([2,3,4,5],[1,2,3,4])

df_test_ucla_v2['ruca_7_class'] = df_test_ucla_v2.ruca_7_class.replace([2,3,4,5,6,7,8],[1,2,3,4,5,6,7])
df_test_ucla_v2['ruca_4_class'] = df_test_ucla_v2.ruca_4_class.replace([2,3,4,5],[1,2,3,4])

### create yr0 observations from time_zero observations
#train set
df_train_ucla_v2['year0_hba1c_count'] = df_train_ucla_v2.time_zero_hba1c_count
df_train_ucla_v2['year0_hba1c_mean'] = df_train_ucla_v2.time_zero_hba1c_mean
df_train_ucla_v2['year0_uacr_count'] = df_train_ucla_v2.time_zero_uacr_count
df_train_ucla_v2['year0_upcr_count'] = df_train_ucla_v2.time_zero_upcr_count
df_train_ucla_v2['year0_bp_count'] = df_train_ucla_v2.time_zero_bp_count
df_train_ucla_v2['year0_av_count'] = df_train_ucla_v2.time_zero_av_count
df_train_ucla_v2['year0_ipv_count'] = df_train_ucla_v2.time_zero_ipv_count
df_train_ucla_v2['year0_aceiarb_coverage'] = df_train_ucla_v2.time_zero_aceiarb_coverage
df_train_ucla_v2['year0_sglt2_coverage'] = df_train_ucla_v2.time_zero_sglt2_coverage
df_train_ucla_v2['year0_glp1_coverage'] = df_train_ucla_v2.time_zero_glp1_coverage
df_train_ucla_v2['year0_nsaid_coverage'] = df_train_ucla_v2.time_zero_nsaid_coverage
df_train_ucla_v2['year0_ppi_coverage'] = df_train_ucla_v2.time_zero_ppi_coverage
df_train_ucla_v2['year0_mra_coverage'] = df_train_ucla_v2.time_zero_mra_coverage
df_train_ucla_v2['year0_scr_count'] = df_train_ucla_v2.time_zero_scr_count
df_train_ucla_v2['year0_mean'] = df_train_ucla_v2.time_zero_mean
df_train_ucla_v2['year0_uacr_mean'] = df_train_ucla_v2.time_zero_uacr_mean
df_train_ucla_v2['year0_upcr_mean'] = df_train_ucla_v2.time_zero_upcr_mean
df_train_ucla_v2['year0_sbp_mean'] = df_train_ucla_v2.time_zero_sbp_mean
df_train_ucla_v2['year0_dbp_mean'] = df_train_ucla_v2.time_zero_dbp_mean
df_train_ucla_v2['year0_pp_mean'] = df_train_ucla_v2.time_zero_pp_mean
df_train_ucla_v2['year0_map_mean'] = df_train_ucla_v2.time_zero_map_mean
#valid set
df_valid_ucla_v2['year0_hba1c_count'] = df_valid_ucla_v2.time_zero_hba1c_count
df_valid_ucla_v2['year0_hba1c_mean'] = df_valid_ucla_v2.time_zero_hba1c_mean
df_valid_ucla_v2['year0_uacr_count'] = df_valid_ucla_v2.time_zero_uacr_count
df_valid_ucla_v2['year0_upcr_count'] = df_valid_ucla_v2.time_zero_upcr_count
df_valid_ucla_v2['year0_bp_count'] = df_valid_ucla_v2.time_zero_bp_count
df_valid_ucla_v2['year0_av_count'] = df_valid_ucla_v2.time_zero_av_count
df_valid_ucla_v2['year0_ipv_count'] = df_valid_ucla_v2.time_zero_ipv_count
df_valid_ucla_v2['year0_aceiarb_coverage'] = df_valid_ucla_v2.time_zero_aceiarb_coverage
df_valid_ucla_v2['year0_sglt2_coverage'] = df_valid_ucla_v2.time_zero_sglt2_coverage
df_valid_ucla_v2['year0_glp1_coverage'] = df_valid_ucla_v2.time_zero_glp1_coverage
df_valid_ucla_v2['year0_nsaid_coverage'] = df_valid_ucla_v2.time_zero_nsaid_coverage
df_valid_ucla_v2['year0_ppi_coverage'] = df_valid_ucla_v2.time_zero_ppi_coverage
df_valid_ucla_v2['year0_mra_coverage'] = df_valid_ucla_v2.time_zero_mra_coverage
df_valid_ucla_v2['year0_scr_count'] = df_valid_ucla_v2.time_zero_scr_count
df_valid_ucla_v2['year0_mean'] = df_valid_ucla_v2.time_zero_mean
df_valid_ucla_v2['year0_uacr_mean'] = df_valid_ucla_v2.time_zero_uacr_mean
df_valid_ucla_v2['year0_upcr_mean'] = df_valid_ucla_v2.time_zero_upcr_mean
df_valid_ucla_v2['year0_sbp_mean'] = df_valid_ucla_v2.time_zero_sbp_mean
df_valid_ucla_v2['year0_dbp_mean'] = df_valid_ucla_v2.time_zero_dbp_mean
df_valid_ucla_v2['year0_pp_mean'] = df_valid_ucla_v2.time_zero_pp_mean
df_valid_ucla_v2['year0_map_mean'] = df_valid_ucla_v2.time_zero_map_mean
#test set
df_test_ucla_v2['year0_hba1c_count'] = df_test_ucla_v2.time_zero_hba1c_count
df_test_ucla_v2['year0_hba1c_mean'] = df_test_ucla_v2.time_zero_hba1c_mean
df_test_ucla_v2['year0_uacr_count'] = df_test_ucla_v2.time_zero_uacr_count
df_test_ucla_v2['year0_upcr_count'] = df_test_ucla_v2.time_zero_upcr_count
df_test_ucla_v2['year0_bp_count'] = df_test_ucla_v2.time_zero_bp_count
df_test_ucla_v2['year0_av_count'] = df_test_ucla_v2.time_zero_av_count
df_test_ucla_v2['year0_ipv_count'] = df_test_ucla_v2.time_zero_ipv_count
df_test_ucla_v2['year0_aceiarb_coverage'] = df_test_ucla_v2.time_zero_aceiarb_coverage
df_test_ucla_v2['year0_sglt2_coverage'] = df_test_ucla_v2.time_zero_sglt2_coverage
df_test_ucla_v2['year0_glp1_coverage'] = df_test_ucla_v2.time_zero_glp1_coverage
df_test_ucla_v2['year0_nsaid_coverage'] = df_test_ucla_v2.time_zero_nsaid_coverage
df_test_ucla_v2['year0_ppi_coverage'] = df_test_ucla_v2.time_zero_ppi_coverage
df_test_ucla_v2['year0_mra_coverage'] = df_test_ucla_v2.time_zero_mra_coverage
df_test_ucla_v2['year0_scr_count'] = df_test_ucla_v2.time_zero_scr_count
df_test_ucla_v2['year0_mean'] = df_test_ucla_v2.time_zero_mean
df_test_ucla_v2['year0_uacr_mean'] = df_test_ucla_v2.time_zero_uacr_mean
df_test_ucla_v2['year0_upcr_mean'] = df_test_ucla_v2.time_zero_upcr_mean
df_test_ucla_v2['year0_sbp_mean'] = df_test_ucla_v2.time_zero_sbp_mean
df_test_ucla_v2['year0_dbp_mean'] = df_test_ucla_v2.time_zero_dbp_mean
df_test_ucla_v2['year0_pp_mean'] = df_test_ucla_v2.time_zero_pp_mean
df_test_ucla_v2['year0_map_mean'] = df_test_ucla_v2.time_zero_map_mean

### create with recurrence (_wr) label from _ge label
#train set
df_train_ucla_v2['year1_reduction_40_wr'] = df_train_ucla_v2.year1_reduction_40_ge
df_train_ucla_v2['year2_reduction_40_wr'] = df_train_ucla_v2.year2_reduction_40_ge
df_train_ucla_v2['year3_reduction_40_wr'] = df_train_ucla_v2.year3_reduction_40_ge
df_train_ucla_v2['year4_reduction_40_wr'] = df_train_ucla_v2.year4_reduction_40_ge
df_train_ucla_v2['year5_reduction_40_wr'] = df_train_ucla_v2.year5_reduction_40_ge

df_train_ucla_v2.year1_reduction_40_wr.value_counts()
df_train_ucla_v2.year2_reduction_40_wr.value_counts()
df_train_ucla_v2.year3_reduction_40_wr.value_counts()
df_train_ucla_v2.year4_reduction_40_wr.value_counts()
df_train_ucla_v2.year5_reduction_40_wr.value_counts()


df_train_ucla_v2.to_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_train_wr_5max.csv')

#valid set
df_valid_ucla_v2['year1_reduction_40_wr'] = df_valid_ucla_v2.year1_reduction_40_ge
df_valid_ucla_v2['year2_reduction_40_wr'] = df_valid_ucla_v2.year2_reduction_40_ge
df_valid_ucla_v2['year3_reduction_40_wr'] = df_valid_ucla_v2.year3_reduction_40_ge
df_valid_ucla_v2['year4_reduction_40_wr'] = df_valid_ucla_v2.year4_reduction_40_ge
df_valid_ucla_v2['year5_reduction_40_wr'] = df_valid_ucla_v2.year5_reduction_40_ge

df_valid_ucla_v2.year1_reduction_40_wr.value_counts()
df_valid_ucla_v2.year2_reduction_40_wr.value_counts()
df_valid_ucla_v2.year3_reduction_40_wr.value_counts()
df_valid_ucla_v2.year4_reduction_40_wr.value_counts()
df_valid_ucla_v2.year5_reduction_40_wr.value_counts()

df_valid_ucla_v2.to_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_valid_wr_5max.csv')

# test set
df_test_ucla_v2['year1_reduction_40_wr'] = df_test_ucla_v2.year1_reduction_40_ge
df_test_ucla_v2['year2_reduction_40_wr'] = df_test_ucla_v2.year2_reduction_40_ge
df_test_ucla_v2['year3_reduction_40_wr'] = df_test_ucla_v2.year3_reduction_40_ge
df_test_ucla_v2['year4_reduction_40_wr'] = df_test_ucla_v2.year4_reduction_40_ge
df_test_ucla_v2['year5_reduction_40_wr'] = df_test_ucla_v2.year5_reduction_40_ge

df_test_ucla_v2.year1_reduction_40_wr.value_counts()
df_test_ucla_v2.year2_reduction_40_wr.value_counts()
df_test_ucla_v2.year3_reduction_40_wr.value_counts()
df_test_ucla_v2.year4_reduction_40_wr.value_counts()
df_test_ucla_v2.year5_reduction_40_wr.value_counts()

df_test_ucla_v2.to_csv('/home/davidgordon/Desktop/DBN PAPER DATA/split_label_encoded_datasets/cure_ckd_egfr_registry_preprocessed_project_preproc_data_discretized_label_enc_UCLA_test_wr_5max.csv')
