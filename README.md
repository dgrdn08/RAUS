#  Code repository for paper: "Dynamic Bayesian Networks for Predicting Acute Kidney Injury Before Onset"

## Authors: David Gordon, Panayiotis Petousis, Anders O. Garlid, Susanne B. Nicholas, Keith Norris, Katherine Tuttle, and Alex A.T. Bui, on behalf of CURE-CKD

### Journal: TBD YYYY

#### Contact: d.gordon@ucla.edu

## This directory contains implementations of RAUS for unknown structure learning using an AKI dataset. RAUS reduces the complexity of learning unknown structures for greedy search methods from n! to n=3.
#### This directory is particularly useful for auto-generating and storing learned rankings, structures, graph visualizations, and model performance metrics, which can significantly reduce project management complexities.

## Note that both track1.py and track2:3.py run three processes in parallel. Depending on the number of CPU cores available on your local/remote machine, both tracks can be run simultaneously.

## Also you can run multiple track1.py and track2:3.py files in parallel if want to run on multiple datasets, different outcomes, multiple sites, and at multiple prediction windows (again depending on the number of CPU cores available on your local/remote machine)
### To do this update the flags in the track1.py and track2:3.py files and their related parsers in the track1_block1.py, track1_block2.py, track1_block3.py, track2_block1.py, track2_block2.py, track2_block3.py, and track3.py files to reflect your settings.
#### Note that block1, block2, and block3 are the three different ranking approach methods (Cramer's V, Chi-squared, and information gain, respectively).

## Note that the framework can handle both train test (TT) split (e.g., AKI dataset) and train validation test (TVT) split input.


### To create the conda environment, run:

```shell
$ conda create --name raus python=3.7.3
$ conda activate raus
$ pip install -r requirements.txt

```

### Install octave (version 4.2.2) for ubuntu (18.04)

###  To run the pipeline and return RAUS track 1 and track2:3 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track1 python AKI_BOS24_track1.py & screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py & screen -S AKI_BOS72_raus_track1 python AKI_BOS72_track1.py & screen -S AKI_BOS24_raus_track2:3 python AKI_BOS24_track2:3.py & screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py & screen -S AKI_BOS72_raus_track2:3 python AKI_BOS72_track2:3.py

```

###  To run the pipeline and return RAUS track 1 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track1 python AKI_BOS24_track1.py & screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py & screen -S AKI_BOS72_raus_track1 python AKI_BOS72_track1.py

```

###  To run the pipeline and return RAUS track 2:3 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track2:3 python AKI_BOS24_track2:3.py & screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py & screen -S AKI_BOS72_raus_track2:3 python AKI_BOS72_track2:3.py

```

###  To run the pipeline and return RAUS track 1 just for the 48-hour BOS prediction window for the AKI dataset, run:

```shell
$ screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py

```

###  To run the pipeline and return RAUS track 2:3 just for the 48-hour BOS prediction window for the AKI dataset, run:

```shell
$ screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py

```
