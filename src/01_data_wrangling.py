"""
Data wrangling for LabMT 1.0 word list.

- Raw file: data/raw/Data_Set_S1.txt
- The first 3 lines are metadata, so we skip them (table starts on line 4).
- The table is whitespace-delimited.
- Missing values are encoded as "--" in the raw file, loaded as NaN.
"""


import pandas as pd

# Path to the raw dataset (tab-delimited).
DATA_PATH = "data/raw/Data_Set_S1.txt"

# Load the dataset:
# - sep="\t": tab-delimited
# - comment="#": skip metadata/comment lines starting with '#', if any
# - na_values=["--"]: treat "--" as missing values (NaN)
df = pd.read_csv(
    DATA_PATH,
    sep=r"\s+",
    skiprows=3,           # first 3 lines are metadata, table starts on line 4
    na_values=["--"],
    engine="python",      # more forgiving with whitespace-delimited text
)

print("=== SHAPE (rows, cols) ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(list(df.columns))

print("\n=== DTYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES PER COLUMN (descending) ===")
print(df.isna().sum().sort_values(ascending=False))

print("\n=== HEAD (first 10 rows) ===")
print(df.head(10))

# Simple sanity check: are there duplicate words?
if "word" in df.columns:
    dup_n = int(df["word"].duplicated().sum())
    print("\n=== SANITY CHECK: duplicated words ===")
    print("duplicated word count:", dup_n)