# PrecisionFDA Truth Challenge v2 Workflow

This Snakemake workflow implements a standard variant calling pipeline consisting of read preprocessing, alignment to a reference genome (GRCh38),
variant calling using a conventional non-machine-learning variant caller, and filtering of results using variant databases (dbSNP, gnomAD, SweGen,
and the Danish population reference).

The workflow was submitted to the [precisionFDA Truth Challenge v2](https://precision.fda.gov/challenges/10).

## Usage

`snakemake --use-conda --conda-frontend mamba -p -j 48`
