import pandas as pd
import numpy as np

### Shorten the name of the adjacency matrices (as dataframes) post-processing before loading into Windows/Ubuntu systems.

## paths to adjacency matrics (as dataframes) with row (the index) and column names
#track2
path_1 = './intraStructures/matrix_form/chisquarerank_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr0-1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_2 = './intraStructures/matrix_form/cramersv_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr0-1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_3 = './intraStructures/matrix_form/ig_mi_ranking_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr0-1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_4 = './intraStructures/matrix_form/chisquarerank_intra_structure_w_column_names_egfr_reduction40_wr_UCLAwstatic_yr0observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_5 = './intraStructures/matrix_form/cramersv_intra_structure_w_column_names_egfr_reduction40_wr_UCLAwstatic_yr0observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_6 = './intraStructures/matrix_form/ig_mi_ranking_intra_structure_w_column_names_egfr_reduction40_wr_UCLAwstatic_yr0observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_7 = './intraStructures/matrix_form/chisquarerank_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_8 = './intraStructures/matrix_form/cramersv_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'
path_9 = './intraStructures/matrix_form/ig_mi_ranking_intra_structure_w_column_names_egfr_reduction40_wr_UCLAw_yr1observations_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track2:3.csv'

#track1
path_10 = './interStructures/matrix_form/chisquarerank_inter_structure_w_column_names_egfr_reduction40_wr_UCLA_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track1.csv'
path_11 = './interStructures/matrix_form/cramersv_inter_structure_w_column_names_egfr_reduction40_wr_UCLA_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track1.csv'
path_12 = './interStructures/matrix_form/ig_mi_ranking_inter_structure_w_column_names_egfr_reduction40_wr_UCLA_w_Race_Adjusted_Variables_Not_UACR_or_UPCR_Track1.csv'

## Track2 ##
# year0 and year1 observations (intra-structure)
chi2_UCLA_intra_struct_yr0_1 = pd.read_csv(path_1,index_col='Unnamed: 0')
cv_UCLA_intra_struct_yr0_1 = pd.read_csv(path_2,index_col='Unnamed: 0')
ig_UCLA_intra_struct_yr0_1 = pd.read_csv(path_3,index_col='Unnamed: 0')

# map back to folder
chi2_UCLA_intra_struct_yr0_1.to_csv('./intraStructures/matrix_form/chi2_UCLA_intra_struct_yr0_1.csv')
cv_UCLA_intra_struct_yr0_1.to_csv('./intraStructures/matrix_form/cv_UCLA_intra_struct_yr0_1.csv')
ig_UCLA_intra_struct_yr0_1.to_csv('./intraStructures/matrix_form/ig_UCLA_intra_struct_yr0_1.csv')

# year0 and static observations (intra-structure)
chi2_UCLA_intra_struct_yr0_s = pd.read_csv(path_4,index_col='Unnamed: 0')
cv_UCLA_intra_struct_yr0_s = pd.read_csv(path_5,index_col='Unnamed: 0')
ig_UCLA_intra_struct_yr0_s = pd.read_csv(path_6,index_col='Unnamed: 0')

# map back to folder
chi2_UCLA_intra_struct_yr0_s.to_csv('./intraStructures/matrix_form/chi2_UCLA_intra_struct_yr0_s.csv')
cv_UCLA_intra_struct_yr0_s.to_csv('./intraStructures/matrix_form/cv_UCLA_intra_struct_yr0_s.csv')
ig_UCLA_intra_struct_yr0_s.to_csv('./intraStructures/matrix_form/ig_UCLA_intra_struct_yr0_s.csv')

# year1 observations (intra-structure)
chi2_UCLA_intra_struct_yr1 = pd.read_csv(path_7,index_col='Unnamed: 0')
cv_UCLA_intra_struct_yr1 = pd.read_csv(path_8,index_col='Unnamed: 0')
ig_UCLA_intra_struct_yr1 = pd.read_csv(path_9,index_col='Unnamed: 0')

# map back to folder
chi2_UCLA_intra_struct_yr1.to_csv('./intraStructures/matrix_form/chi2_UCLA_intra_struct_yr1.csv')
cv_UCLA_intra_struct_yr1.to_csv('./intraStructures/matrix_form/cv_UCLA_intra_struct_yr1.csv')
ig_UCLA_intra_struct_yr1.to_csv('./intraStructures/matrix_form/ig_UCLA_intra_struct_yr1.csv')

## Track 1 ##
# year1-4 observations (inter-structure)
chi2_UCLA_inter_struct_yr1_4 = pd.read_csv(path_10,index_col='Unnamed: 0')
cv_UCLA_inter_struct_yr1_4 = pd.read_csv(path_11,index_col='Unnamed: 0')
ig_UCLA_inter_struct_yr1_4 = pd.read_csv(path_12,index_col='Unnamed: 0')

# map back to folder
chi2_UCLA_inter_struct_yr1_4.to_csv('./interStructures/matrix_form/chi2_UCLA_inter_struct_yr1_4.csv')
cv_UCLA_inter_struct_yr1_4.to_csv('./interStructures/matrix_form/cv_UCLA_inter_struct_yr1_4.csv')
ig_UCLA_inter_struct_yr1_4.to_csv('./interStructures/matrix_form/ig_UCLA_inter_struct_yr1_4.csv')
