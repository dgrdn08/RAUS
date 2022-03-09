"""
    Paper: "Dynamic Bayesian Networks for Predicting Acute Kidney Injury Before Onset"
    Authors: David Gordon, Panayiotis Petousis, Anders O. Garlid, Susanne B. Nicholas, Keith Norris, Katherine Tuttle,
    and Alex A.T. Bui, on behalf of CURE-CKD
    Journal: TBD YYYY

    Contact: d.gordon@ucla.edu

    This directory contains implementations of RAUS for unknown structure learning algorithms using an AKI dataset.

    To run the pipeline and return the RAUS track1, run:

```shell
$ screen -S raus_aki_bos72_track1 python AKI_BOS72_track1.py

"""

import os
from multiprocessing import Pool


track1 = ("track1_block1.py --file_name_train '/home/ssm-user/data/aki_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/aki_data_ucla_test.csv' --max_iter 10 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '' --outcome_name 'AKI_BOS72' --select_best_k 1 --cv_top_features 8 --max_fan_in 10 --clipback '_24hourperiod_0' --clipfront '_4days' --cols_start '24hourperiod_0' --cols_end '_4days' --COLS ser_albumin_24hourperiod_0 gfr_24hourperiod_0 ser_calcium_24hourperiod_0 ser_wbc_24hourperiod_0 serhemo_24hourperiod_0 serbun_24hourperiod_0 ser_sodium_24hourperiod_0 ser_potassium_24hourperiod_0 --TARGET aki_progression_4days", "track1_block2.py --file_name_train '/home/ssm-user/data/aki_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/aki_data_ucla_test.csv' --max_iter 10 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '' --outcome_name 'AKI_BOS72' --select_best_k 1 --chi2_top_features 8 --max_fan_in 10 --clipback '_24hourperiod_0' --clipfront '_4days' --cols_start '24hourperiod_0' --cols_end '_4days' --COLS ser_albumin_24hourperiod_0 gfr_24hourperiod_0 ser_calcium_24hourperiod_0 ser_wbc_24hourperiod_0 serhemo_24hourperiod_0 serbun_24hourperiod_0 ser_sodium_24hourperiod_0 ser_potassium_24hourperiod_0 --TARGET aki_progression_4days", "track1_block3.py --file_name_train '/home/ssm-user/data/aki_data_ucla_train.csv' --file_name_valid '/home/ssm-user/data/aki_data_ucla_test.csv' --max_iter 10 --sequence_length_dbn 4 --track 'Track1' --site 'UCLA' --adjusted '' --outcome_name 'AKI_BOS72' --select_best_k 1 --ig_top_features 8 --max_fan_in 10 --clipback '_24hourperiod_0' --clipfront '_4days' --cols_start '24hourperiod_0' --cols_end '_4days' --COLS ser_albumin_24hourperiod_0 gfr_24hourperiod_0 ser_calcium_24hourperiod_0 ser_wbc_24hourperiod_0 serhemo_24hourperiod_0 serbun_24hourperiod_0 ser_sodium_24hourperiod_0 ser_potassium_24hourperiod_0 --TARGET aki_progression_4days")


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, track1)