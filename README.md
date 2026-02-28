# Happiness According to Mechanical Turks: Quantitative + Qualitative Exploration of the Hedonometer (labMT1.0) Dataset

This project provides an **example project structure** (and an instructor/demo script) for the Seminars 3 & 4 group project using the **labMT 1.0** dataset (Data Set S1 from the Hedonometer paper). 

It includes:
- the labMT 1.0 dataset file (`data/raw/Data_Set_S1.txt`)
- a runnable demo analysis script (`src/hedonometer_labmt_demo.py`) that produces a *typical* set of outputs aligned to the assignment
- course documents in `docs/` (original paper + paper companion + assignment + project quickstart), provided as **.pdf**

## Folder layout (course convention)

- `src/` — Python scripts you run
- `data/raw/` — input data (treat as read-only)
- `figures/` — PNG plots (embed these in your GitHub README)
- `tables/` — CSV tables/summaries (optional to embed, but useful for analysis)
- `docs/` — assignment + paper companion + quickstart handout

## Setup + run (from the project root)

### 1) Create a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

### 2) Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 3) Run the demo analysis
```bash
python3 src/run_analysis.py
```

1. Load, clean, and describe the dataset

1.1 Load the file

Code tasks

• Read the tab-delimited file into a pandas DataFrame.
• Skip or handle the comment lines at the top (the dataset begins after metadata
lines).
• Convert numeric columns to numeric types (floats/ints).
• Replace -- with missing values (NaN).
• Confirm the number of rows and columns.


• Explain how you loaded the file (1–3 sentences).

  We loaded the LabMT 1.0 dataset (Data_Set_S1.txt) as a file with a delimited tab, using pandas.read_csv(). The file begins with three lines of metadata so in order to skip those rows, we used skiprows=3. We converted all the numeric columns into numeric types using pd.to_numeric() and replacing "--" values with NaN to show the missing ranks.

• State the shape of the dataset (rows × columns).
  After loading and clearing the dataset, it contains [10222] rows x [8] columns.

• Give one sentence explaining what a missing rank (--) means in this dataset.
  A missing rank (--) means that the word does not appear in the corpus's top 5000 most frequest words used in constructing the dataset, and not that the word does not appear at all in that corpus. 
  
1.2 Create a data dictionary

Code tasks

• List each column name and its data type.
• Count missing values per column.

| Column | Description | Data Type | Missing Values |
|--------|-------------|-----------|----------------|
| word | This represents the lexical item that is evaluated for emotional valence| string | 0 |
| happiness_rank | Rank when ordered by average happiness (1 = highest) | int64 | 0 |
| happiness_average | this represents the mean happiness score assigned to the word on a 1-9 scale | float64 | 0 |
| happiness_standard_deviation | this represents the standard deviation of happiness ratings for the word | float64 | 0 |
| twitter_rank | this represents the frequency rank of the word in Twitter's top 5000 most frequent words | float64 | 5222 (missing values indicate the word does not appear in Twitter's top-5000 list used for this dataset) | 
| google_rank | this represents the frequency rank of the word in the Google Books corpus (top 5000 only) | float64 | 5222 (missing values indicate the word does not appear in Google Books' top-5000 list) |
| nyt_rank | this represents the frequency rank of the word in the New York Times corpus (top 5000 only) | float64 | 5222 (missing values indicate the word does not appear in the NYT top-5000 list) |
| lyrics_rank | this represents the frequency rank of the word in a song lyrics corpus (top 5000 only) | float64 | 5222 (missing values indicate the word does not appear in the lyrics top-5000 list) |



1.3 Sanity checks

Code tasks

• Check for duplicated words (are any words repeated?).
• Inspect a random sample of 15 rows.
• Identify the 10 most positive and 10 most negative words by average happiness.
Write-up tasks (README)
• Choose 2–3 sanity checks and explain what they tell you about data quality.
• Briefly comment on whether the most positive/negative words “make sense” to
you—and what “make sense” even means here.

  We checked for ducplicated words and there are [0] duplicated words in the dataset.
  
  We inspected a random sample of 15 rows and the sample shows:

  | Sample | Range | Interpretation |
  |--------|-------|----------------|
  | Happiness scores | 3.24 - 7.96 | fall within 1-9 scale |
  | Standard deviations | 1.05 - 1.62 | plausible and within a reasonable range | 

  This shows the data falls within expected ranges 

  We identified the 10 most positive and 10 most negative words by sorting happiness_average.
  The most positive words tend to reflect positive emotional or social concepts, while the most negative words are related to harm or suffering. These results "make sense" in relation to the broad cultural understanding of these concepts, rather than the objective truth. 

2. Quantitative exploration: distributions and relationships
   
Your goal is to describe what the dataset “looks like” statistically, and to notice patterns that
invite interpretation.

2.1 Distribution of happiness scores

Code tasks

• Plot a histogram of happiness_average.
• Compute summary statistics:
– mean, median
– standard deviation
– 5th and 95th percentiles (or similar)

• Interpret the histogram in words. Is the distribution centered? skewed? clustered?
• Identify 1 pattern you did not expect.

  The distribution in the histogram is slightly left-skewed and most words cluster around 5-6 which means the average happiness is moderately high. 
  The distribution is centered near the median of 5.44, so most of the words are neutral or barely above it, and there is a peak around 5.5, so a large number of words have happiness values in that moderate-high range.
  

2.2 Disagreement: which words are “contested”?

The dataset includes happiness_standard_deviation. That means you can ask: which
words did people disagree about?

Code tasks

• Plot happiness_average (x-axis) vs happiness_standard_deviation (y-axis) as a scatterplot.
• Identify the 15 words with the highest standard deviation.

  We have identified the 15 words with the highest standard deviation: fucking, fuckin, fucked, pussy, whiskey, slut, cigarettes, fuck, mortality, cigarette, motherfuckers, churches, motherfucking, capitalism, and porn. 

• Pick 5 of the “most disagreed-about” words and discuss why they might be contested:
– ambiguity / multiple meanings
– cultural references
– slang and time period
– irony, profanity, or taboo
• Connect your qualitative interpretation to the quantitative pattern.

  5 of the "most disagreed-about" words are fucking / fuckin / fucked / motherfuckers / motherfucking. 
  The reason why these words might be contested is because of profanity, intensity, and dependency on context when it comes to the meaning. Some people might see it as negative or even offensive, while others see it in a humurous light, casual or even positive in certain informal circumstances.  

2.3 Corpus comparison: what counts as “common language” depends on where you look

The dataset includes a rank column for each corpus. This lets you study overlap and
difference.

Code tasks

• For each corpus (Twitter / Google Books / NYT / Lyrics):
– count how many labMT words appear in its top 5000 (i.e., rank is not
missing)

  All four corpuses have 5,000 LabMT words with ranks, which represents roughly 49% share of the lexicon.

• Compute a simple overlap table:
– e.g., how many words appear in both Twitter and NYT? in all four?

  There are 1816 words that appear in all four corpuses, which highlights that "common language" is dependent on the source as well. 

• Make at least one plot about corpus differences (your choice):
– bar chart of “how many words are present”
– heatmap-like table (even simple) of overlaps
– scatterplot of Twitter rank vs NYT rank for words present in both (optional)


• Interpret what your plot suggests about the four corpora.
• Give one concrete example of a word that is “common” in one corpus but missing in
another, and interpret why that might be.


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

## 4.0 Critical reflection: how was this dataset generated, and why does it matter?
## 4.1 Reconstructing the pipeline
How our dataset emerged.
1. From a LabMT lexicon words were selected.
2. These selected words were rated on a happiness scale.
3. We calculated the score of happiness for each word.
4. After scoring the happiness scale, disagreement was measured by standard deviation.
5. Word frequency rankins are collected from various platforms, Twitter, Google Books, NYT and Lyrics.
6. These datasets were merged into one table linking, which includes
   - word
   - happiness_average
   - happiness_standard_deviation
   - corpus rank columns
7. Words that did not appear on the corpus, received a "missing" value.
8. The final gathered dataset was turned into a CSV file for analysis. 

## 4.2 Consequences and limitations

1. Choice: English-only lexicon, only English words were included.
  Consequence: This can have an impact on linguistic bias, and not be as globally representative. 
Example: Twitter slang terms differ from formal writing in NYT.

2. Choice: Specific corpora was selected (Twitter, NYT, Lyrics, GOOGLE Books)
  Consequence: This dataset compares specific genres and platforms.
This showcases a different social group. This explains why some words appear in one corpus but not in the other one. 
Example: Twitter contains slang, Google Books does not, different words appear.

3. Choice: Survey-based happiness ratings
   Consequence: The received happiness score come from human rates  using a scale from 1-9. These ratings revel beyond universal truths, because time, cultural norms and raters as individuals are not taken into account. 
   
4. Choice: Words are being used without clear context
  Consequence: Meaning can change depending on context, exemplifying how the happiness score might not reflect real usage.
Example: "Fucking" had a high standard deviation. This word can be used in various contexts and ways, humorous, offensive or positive. Therefore it needs to be critically seen.

5. Choice: using only Top-5000 frequency constraint per corpus
   Consequence: By including only 5000 most frequent words in each corpus, the rare and emerging words may be left out. Therefore, the "missing value" is misleading, since it does have a value if given context outside of the top 5000 list. 

# 4.3 If you were to use this dataset as an instrument today...
To be able to use this dataset as a measurement instrument, it would be used to given a direction, not as a precise emotional detector. To get a more comprehensive understanding and analysis, it would need a more nuanced interpretation. This dataset works well for a large-scale analysis. 

We would use this dataset for:
  1. Comparing emotional tone across genres and platforms: By analyzing a few different corpora (Twitter, Google Books, NYT) we can identify and point out on shifts across multiple forms of media. 
  2. To help identify contested vocabulary: Our dataset reveals which words tend to be controversial to the feeling linked to them. 

This dataset is not recommended for:
  1. Making claims about individuals intent with words: this dataset lacks to showcase the complexity and usage of words in various contexts. 
  2. Measuring complex emotions, such as sarcasm and irony: the scope of the dataset is limited, which hides certain feelings, that would require deeper emotional analysis.
  3. Analyzing multilangual populations: the dataset does not go beyond the English language, whish leaves out emotional expression in other cultural contexts. 
     
To improve this dataset we would include contextual embeddings and leave isolated words out of the analysis and expand beyond English language. This dataset would be ideal for macrolevel trends, where interpretation is slightly more limited. 



