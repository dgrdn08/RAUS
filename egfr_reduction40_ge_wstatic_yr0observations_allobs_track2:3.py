"""
    Paper:
    Authors:

    Journal: TBD YYYY

    Contact: 

    This directory contains implementations of RAUS for unknown structure learning algorithms using an AKI dataset.

    To run the pipeline and return the RAUS track2:3, run:

```shell
$ screen -S egfr_reduction40_ge_wstatic_raus_track2:3 python egfr_reduction40_ge_wstatic_yr0observations_track2:3.py

"""

import os
from multiprocessing import Pool


track2 = ("track2_block1.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'wstatic_yr0observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year0' --cols_end '_ge' --COLS year0_mean year0_scr_count year0_hba1c_count year0_hba1c_mean year0_uacr_count year0_uacr_mean year0_upcr_count year0_upcr_mean year0_bp_count year0_sbp_mean year0_dbp_mean year0_pp_mean year0_map_mean year0_av_count year0_ipv_count year0_aceiarb_coverage year0_sglt2_coverage year0_glp1_coverage year0_nsaid_coverage year0_ppi_coverage year0_mra_coverage demo_sex demo_race_ethnicity_cat ruca_4_class ruca_7_class study_entry_period_egfrckd_flag study_entry_period_dxckd_flag study_entry_period_albprockd_flag study_entry_DM_flag study_entry_PDM_flag study_entry_HTN_flag study_entry_aceiarb_flag study_entry_sglt2_flag study_entry_glp1_flag study_entry_nsaid_flag study_entry_ppi_flag study_entry_mra_flag study_entry_age --TARGET year1_reduction_40_ge", "track2_block2.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'wstatic_yr0observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year0' --cols_end '_ge' --COLS year0_mean year0_scr_count year0_hba1c_count year0_hba1c_mean year0_uacr_count year0_uacr_mean year0_upcr_count year0_upcr_mean year0_bp_count year0_sbp_mean year0_dbp_mean year0_pp_mean year0_map_mean year0_av_count year0_ipv_count year0_aceiarb_coverage year0_sglt2_coverage year0_glp1_coverage year0_nsaid_coverage year0_ppi_coverage year0_mra_coverage demo_sex demo_race_ethnicity_cat ruca_4_class ruca_7_class study_entry_period_egfrckd_flag study_entry_period_dxckd_flag study_entry_period_albprockd_flag study_entry_DM_flag study_entry_PDM_flag study_entry_HTN_flag study_entry_aceiarb_flag study_entry_sglt2_flag study_entry_glp1_flag study_entry_nsaid_flag study_entry_ppi_flag study_entry_mra_flag study_entry_age --TARGET year1_reduction_40_ge","track2_block3.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'wstatic_yr0observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year0' --cols_end '_ge' --COLS year0_mean year0_scr_count year0_hba1c_count year0_hba1c_mean year0_uacr_count year0_uacr_mean year0_upcr_count year0_upcr_mean year0_bp_count year0_sbp_mean year0_dbp_mean year0_pp_mean year0_map_mean year0_av_count year0_ipv_count year0_aceiarb_coverage year0_sglt2_coverage year0_glp1_coverage year0_nsaid_coverage year0_ppi_coverage year0_mra_coverage demo_sex demo_race_ethnicity_cat ruca_4_class ruca_7_class study_entry_period_egfrckd_flag study_entry_period_dxckd_flag study_entry_period_albprockd_flag study_entry_DM_flag study_entry_PDM_flag study_entry_HTN_flag study_entry_aceiarb_flag study_entry_sglt2_flag study_entry_glp1_flag study_entry_nsaid_flag study_entry_ppi_flag study_entry_mra_flag study_entry_age --TARGET year1_reduction_40_ge")



def run_process(process):
    os.system('python {}'.format(process))
    return process


pool = Pool(processes=3)
pool.map(run_process, track2)
