"""
    Paper:
    Authors:

    Journal: TBD YYYY

    Contact:

    This directory contains implementations of RAUS for unknown structure learning algorithms using an AKI dataset.

    To run the pipeline and return the RAUS track1, run:

```shell
$ screen -S egfr_reduction40_ge_raus_track1 python egfr_reduction40_ge_yr1-4observations_track1.py & screen -S egfr_reduction40_ge_raus_yr0-1_track2:3 python egfr_reduction40_ge_yr0-1observations_allobs_track2:3.py & screen -S egfr_reduction40_ge_raus_wstatic_yr0_track2:3 python egfr_reduction40_ge_wstatic_yr0observations_allobs_track2:3.py & screen -S egfr_reduction40_ge_raus_yr1_track2:3 python egfr_reduction40_ge_yr1observations_allobs_track2:3.py

"""

import os
from multiprocessing import Pool


track1 = ("track1_block1.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --max_iter 50 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --rank_filter 1 --cv_rank_filter2 year1_uacr_mean year1_upcr_mean year1_dbp_mean year1_sbp_mean year1_pp_mean year1_map_mean --select_percentile 1 --percentile 80 --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge", "track1_block2.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --max_iter 50 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --select_percentile 1 --percentile 80 --rank_filter 1 --chi2_rank_filter2 year1_dbp_mean year1_uacr_mean year1_pp_mean --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge", "track1_block3.py --file_name_train '/home/ssm-user/data/egfr_reduction_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/egfr_reduction_data_ucla_valid.csv' --file_name_test '/home/ssm-user/data/egfr_reduction_data_ucla_test.csv' --max_iter 50 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '_w_Race_Adjusted_Variables' --outcome_name 'egfr_reduction40_ge' --rank_filter 1 --ig_rank_filter2 year1_upcr_mean year1_uacr_mean year1_pp_mean year1_dbp_mean year1_sbp_mean year1_map_mean --select_percentile 1 --percentile 80 --max_fan_in 2 --clipback '' --clipfront '' --cols_start 'year1' --cols_end '_ge' --COLS year1_mean year1_scr_count year1_hba1c_count year1_hba1c_mean year1_uacr_count year1_uacr_mean year1_upcr_count year1_upcr_mean year1_bp_count year1_sbp_mean year1_dbp_mean year1_pp_mean year1_map_mean year1_av_count year1_ipv_count year1_aceiarb_coverage year1_sglt2_coverage year1_glp1_coverage year1_nsaid_coverage year1_ppi_coverage year1_mra_coverage --TARGET year2_reduction_40_ge")


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, track1)
