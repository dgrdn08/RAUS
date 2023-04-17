###### Global Variables ######

# VM dataset paths
UCLA_Train = "/home/ssm-user/data/aki_data_ucla_train.csv"
UCLA_Test = "/home/ssm-user/data/aki_data_ucla_test.csv"

# variables
COLS = (
    "ser_albumin_24hourperiod_0"
    + " gfr_24hourperiod_0"
    + " ser_calcium_24hourperiod_0"
    + " ser_wbc_24hourperiod_0"
    + " serhemo_24hourperiod_0"
    + " serbun_24hourperiod_0"
    + " ser_sodium_24hourperiod_0"
    + " ser_potassium_24hourperiod_0"
)

# structure identifiers
#STRUCTURE = "structure"

# structure targets
TARGET_BOS24 = "aki_progression_2days"
TARGET_BOS48 = "aki_progression_3days"
TARGET_BOS72 = "aki_progression_4days"

# what the temporal cols start with
COLS_Start = "24hourperiod_0"

# what the temporal outcome col ends with
COLS_End_BOS24 = "_2days"
COLS_End_BOS48 = "_3days"
COLS_End_BOS72 = "_4days"

# outcome identifier (if 'TVT' loads train, valid, and test (TVT) sets and appends outcome identifier to output files else loads train, test (TT) sets and appends outcome identifier to output files)
Outcome_BOS24 = "AKI_BOS24"
Outcome_BOS48 = "AKI_BOS48"
Outcome_BOS72 = "AKI_BOS72"

# site identifiers
UCLA = "UCLA"

# clipfront/clipback identifiers
Clipfront_BOS24 = "_2days"
Clipfront_BOS48 = "_3days"
Clipfront_BOS72 = "_4days"
Clipback = "_24hourperiod_0"

# sequence lengths
seq_len_bn = "1"
seq_len_dbn_bos24 = "6"
seq_len_dbn_bos48 = "5"
seq_len_dbn_bos72 = "4"

# iterations
max_iterations = "10"

# maximum in-degree edges per node
max_fan_in = "10"

# best k
select_best_k = "1"

# number of top features to select
cv_top_features = "8"
chi2_top_features = "8"
ig_top_features = "8"

# track
Track1 = "Track1"
Track2 = "Track2:3"
