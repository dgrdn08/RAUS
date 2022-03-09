"""
    Paper:
    Authors:

    Journal: TBD YYYY

    Contact: 

    This directory contains implementations of RAUS for unknown structure learning algorithms using an AKI dataset.

    To run the pipeline and return the RAUS track2:3, run:

```shell
$ screen -S egfr_reduction40_ge_wyr1_raus_track2:3 python egfr_reduction40_ge_wstatic_yr1observations_track2:3.py

"""

import os
from multiprocessing import Pool


track2 = ("track2_block1.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'w_yr1observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge", "track2_block2.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'w_yr1observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge","track2_block3.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --sequence_length_bn 1 --max_iter 50 --track 'Track2:3' --site 'UCLA' --adjusted 'w_yr1observations_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge")



def run_process(process):
    os.system('python {}'.format(process))
    return process


pool = Pool(processes=3)
pool.map(run_process, track2)
