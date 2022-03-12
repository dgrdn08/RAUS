# Ranking Approaches for Unknown Structure (RAUS) Learning

## Summary
This is the RAUS software.

RAUS can readily learn dynamic Bayesian networks (DBNs) and Bayesian networks (BNs) end-to-end as well as be incorporated into existing pipelines as an unknown structure learning engine.

RAUS reduces the complexity of learning unknown structures for greedy search methods from n! to n=3.

RAUS is particularly useful for auto-generating and saving learned feature rankings, network structures, graph visualizations, and model performance metrics, which can significantly reduce project management complexities.

Further, RAUS can be used to learn the intra-structures and inter-structures required for learning a full network (i.e., connecting static and dynamic variables over time).

Note that python files ending in _track1.py and _track2:3.py run three processes in parallel. Therefore, depending on the number of CPU cores available on your local/remote machine, python files ending in _track1.py and _track2:3.py can be run simultaneously.

Further, if you want to run RAUS on multiple datasets, different outcomes, multiple sites, and at multiple prediction windows simultaneously, you can run multiple python files ending in _track1.py and multiple python files ending in _track2:3.py in parallel (again depending on the number of CPU cores available on your local/remote machine).

Note that python files ending in _block1.py, _block2.py, and _block3.py are the three different feature ranking methods (Cramer's V, Chi-squared, and information gain, respectively).

RAUS can handle both train test (TT) split and train validation test (TVT) split input.

RAUS is built on top of the Bayes Net Toolbox (BNT) by [Murphy et al.] (https://github.com/bayesnet/bnt)

## If you use RAUS in your work, please cite the RAUS software.

## The RAUS software is used in paper: "Dynamic Bayesian Networks for Predicting Acute Kidney Injury Before Onset".

# How to use RAUS

To create the conda environment, run:

```shell
$ conda create --name raus python=3.7.3
$ conda activate raus
$ pip install -r requirements.txt

```

Install octave (version 4.2.2) for ubuntu (18.04)

# Example Commands

To run the pipeline and return RAUS track 1 and track2:3 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track1 python AKI_BOS24_track1.py & screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py & screen -S AKI_BOS72_raus_track1 python AKI_BOS72_track1.py & screen -S AKI_BOS24_raus_track2:3 python AKI_BOS24_track2:3.py & screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py & screen -S AKI_BOS72_raus_track2:3 python AKI_BOS72_track2:3.py

```

To run the pipeline and return RAUS track 1 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track1 python AKI_BOS24_track1.py & screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py & screen -S AKI_BOS72_raus_track1 python AKI_BOS72_track1.py

```

To run the pipeline and return RAUS track 2:3 for the AKI dataset, run:

```shell
$ screen -S AKI_BOS24_raus_track2:3 python AKI_BOS24_track2:3.py & screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py & screen -S AKI_BOS72_raus_track2:3 python AKI_BOS72_track2:3.py

```

To run the pipeline and return RAUS track 1 just for the 48-hour BOS prediction window for the AKI dataset, run:

```shell
$ screen -S AKI_BOS48_raus_track1 python AKI_BOS48_track1.py

```

To run the pipeline and return RAUS track 2:3 just for the 48-hour BOS prediction window for the AKI dataset, run:

```shell
$ screen -S AKI_BOS48_raus_track2:3 python AKI_BOS48_track2:3.py

```
