# Data files
<!-- File use description
- primary analysis output used in secondary analysis
- mature datasets released with publication should have accompanying README files and data descriptor files as appropraite.
- Use subfolders for multifile datasets when appropriate and it facilitates documentation
-->

- `challenge_winners.tsv`: table with truth challenge winners based on F1 score for the four technologies and three stratifications. 
- `anonymized_challenge_results_v5.txt`: submission benchmarking results extracted from the combined extended.csv with challenge stratifications and metric geometric mean for HG003 and HG004. Generated using `analysis/mungign/anonymized_results.Rmd`.
- `anonymized_results_by_genome.tsv`: submission benchmarking results extracted from the combined extended.csv files formatted for challenge results reporting. Generated using `analysis/anonymized_results.Rmd`.