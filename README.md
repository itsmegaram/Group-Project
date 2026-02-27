# Group-Project# 
## Dataset: LabMT 1.0 (word happiness lexicon)

Raw file: `data/raw/Data_Set_S1.txt`  
Parsing notes:
- The first 3 lines are metadata (we skip them); the table starts on line 4.
- The file is whitespace-delimited.
- Missing values are encoded as `--` in the raw file and loaded as `NaN`.

### Columns (data dictionary)
- `word` (string): the word/token.
- `happiness_rank` (int): rank by average happiness score (1 = happiest in this list).
- `happiness_average` (float): mean happiness rating for the word.
- `happiness_standard_deviation` (float): standard deviation of happiness ratings.
- `twitter_rank` (float, nullable): frequency rank in Twitter (missing for many words).
- `google_rank` (float, nullable): frequency rank in Google Books (missing for many words).
- `nyt_rank` (float, nullable): frequency rank in New York Times (missing for many words).
- `lyrics_rank` (float, nullable): frequency rank in song lyrics (missing for many words).

### Data types (from `src/01_data_wrangling.py`)
- `word`: string
- `happiness_rank`: int64
- `happiness_average`: float64
- `happiness_standard_deviation`: float64
- `twitter_rank`, `google_rank`, `nyt_rank`, `lyrics_rank`: float64 (nullable due to missing values)

### Missingness overview
Missing values per column:
- `twitter_rank`: 5222 missing
- `google_rank`: 5222 missing
- `nyt_rank`: 5222 missing
- `lyrics_rank`: 5222 missing
All happiness-related columns and `word` have 0 missing values.

Sanity check:
- Duplicate words: 0