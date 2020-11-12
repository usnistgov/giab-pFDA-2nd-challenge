## Data Raw
<!-- File use description
- Raw input data files (read-only)
- datasets released with publication should have accompanying README files and data descriptor files as appropraite.
- Use subfolders for multifile datasets when appropriate and it facilitates documentation
-->

- `v1_challenge_results.xlsx`: V1 benchmarking results scraped manually from https://precision.fda.gov/challenges/truth/results. 
- `TruthV1_extendedcsv`: V1 challenge winners benchmarked against the V4.2 benchmarkset used to evaluate the second challenge. 
- `anonymized_metadata_table.tsv`: generated manually and programatically with `analysis/munging/anonymized_results.Rmd` from metadta files in `data-raw/intermediate_metadata`.
- `TruthChallegeV2`: non-anonymized benchmarking extended.csvs, not included in git repo.

## Intermediate Metadata
- `submission_metadata.csv`: manually reformatted `Truth_metadata.xlsx` table from `data-raw` to remove merged cells. Manually updated GENeTres submission names to match AnonMap table. 
- `anonymized_challenge_results.tsv`: initial results file, final results file modified based on TODO..... 