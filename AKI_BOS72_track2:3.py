"""
    This directory contains implementations of RAUS for unknown structure learning algorithms using an AKI dataset.

    To run the pipeline and return the RAUS track2:3, run:

```shell
$ screen -S raus_aki_bos72_track2:3 python AKI_BOS72_track2:3.py

"""

import os
from multiprocessing import Pool
from RAUS_CONSTANTS import *


track2 = (
    "track2_block1.py --file_name_train "
    + UCLA_Train
    + " --file_name_valid "
    + UCLA_Test
    + " --max_iter "
    + max_iterations
    + " --sequence_length_bn "
    + seq_len_bn
    + " --track "
    + Track2
    + " --site "
    + UCLA
    + " --adjusted ''"
    + " --outcome_name "
    + Outcome_BOS72
    + " --select_best_k "
    + select_best_k
    + " --cv_top_features "
    + cv_top_features
    + " --max_fan_in "
    + max_fan_in
    + "--clipback "
    + Clipback
    + " --clipfront "
    + Clipfront_BOS72
    + " --cols_start "
    + COLS_Start
    + " --cols_end"
    + COLS_End_BOS72
    + " --COLS "
    + COLS
    + " --TARGET "
    + TARGET_BOS72
    + " ",
    "track2_block2.py --file_name_train "
    + UCLA_Train
    + " --file_name_valid "
    + UCLA_Test
    + " --max_iter "
    + max_iterations
    + " --sequence_length_bn "
    + seq_len_bn
    + " --track "
    + Track2
    + " --site "
    + UCLA
    + " --adjusted ''"
    + " --outcome_name "
    + Outcome_BOS72
    + " --select_best_k "
    + select_best_k
    + " --chi2_top_features "
    + chi2_top_features
    + " --max_fan_in"
    + max_fan_in
    + "--clipback "
    + Clipback
    + " --clipfront "
    + Clipfront_BOS72
    + " --cols_start "
    + COLS_Start
    + " --cols_end "
    + COLS_End_BOS72
    + " --COLS "
    + COLS
    + "--TARGET "
    + TARGET_BOS72
    + " ",
    "track2_block3.py --file_name_train "
    + UCLA_Train
    + " --file_name_valid "
    + UCLA_Test
    + " --max_iter "
    + max_iterations
    + " --sequence_length_bn "
    + seq_len_bn
    + " --track "
    + Track2
    + " --site "
    + UCLA
    + " --adjusted ''"
    + " --outcome_name "
    + Outcome_BOS72
    + " --select_best_k "
    + select_best_k
    + " --ig_top_features "
    + ig_top_features
    + "--max_fan_in "
    + max_fan_in
    + " --clipback "
    + Clipback
    + " --clipfront "
    + Clipfront_BOS72
    + " --cols_start "
    + COLS_Start
    + " --cols_end "
    + COLS_End_BOS72
    + " --COLS "
    + COLS
    + "--TARGET"
    + TARGET_BOS72
    + " ",
)

track3 = (
    "track3.py --max_iter "
    + max_iterations
    + " --sequence_length_dbn "
    + seq_len_dbn_bos72
    + " --track "
    + Track2
    + " --site "
    + UCLA
    + " --adjusted ''"
    + " --outcome_name "
    + Outcome_BOS72
    + " --cols_start "
    + COLS_Start
    + " --cols_end "
    + COLS_End_BOS72
    + " --max_fan_in "
    + max_fan_in
    + " --clipback "
    + Clipback
    + " --clipfront "
    + Clipfront_BOS72
    + " --COLS "
    + COLS
    + " --TARGET "
    + TARGET_BOS72
    + " ",
)


def run_process(process):
    os.system('python {}'.format(process))
    return process


pool = Pool(processes=4)
pool.map(run_process, track2)
pool.map(run_process, track3)
