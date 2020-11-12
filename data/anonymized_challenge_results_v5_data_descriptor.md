# Data Descriptor
Data values description for https://nist-giab.s3.amazonaws.com/anonymized_challenge_results_v5.txt

For the following metric descriptions, "TRUTH" refers to the GIAB benchmark set and "QUERY" the submission vcf. 
Metric definitions from Krusche et al. 2019 https://doi.org/10.1038/s41587-019-0054-x.

- Participant(s): Participant name or team name, random 5 character alpha numeric code used for anonomyous submissions.  
- Technology: 	Sequencing technology or technologies used for the submission. Either ILLUMINA, PACBIO, ONT, or MULTI.  
- Multi_Details: For submissions using multiple technologies, concatenated name of input technologies.  
- Submission_Name: Brief descriptive submission name, random 5 character alpha numeric code used for anonomyous submissions.	
- challenge_cat: Genome stratification used for winner assignments, either "All Benchmark Regions", "Difficult-to-Map Regions", or "MHC".  
    - All Benchmark Regions: V4.2 benchmark regions
    - Difficult-to-Map Regions: Union of segmental duplications and “low mappability” regions where 100 bp read pairs have <=2 mismatches and <=1 indel difference from another region of the genome.  
    - MHC: Major histocompatibility complex  
- FP.al: The number of query variant calls which could not be matched by genotype or by alleles, but which have a truth variant call within a specified distance	
- FP.gt: This is the number of query variants with an incorrect genotype, but the correct allele (e.g., when the query GT is 1/1 and truth GT is 0/1)
- METRIC.F1_Score: The harmonic mean between recall and precision. 2 * METRIC.Recall* METRIC.Precision / (METRIC.Recall + METRIC.Precision)	
- METRIC.Precision: Fraction of querycalls that are consistent with a truth allele and genotype call within the confident regions. QUERY.TP/(QUERY.TP + QUERY.FP)  	
- METRIC.Recall: Fraction of truth calls that are consistent with a query allele and genotype call within the confident regions. TRUTH.TP/(TRUTH.TP + TRUTH.FN)  
- QUERY.FP: Number of query calls for which there is no truth call that is consistent with the query call and its genotype.   
- QUERY.TP: Number of query calls for which there is a truth call that is consistent with the query call and its genotype. This can differ from TRUTH.TP if complex changes are represented as a single change in TRUTH.TP and as multiple primitive SNVs and indels in QUERY.TP, or vice versa.	
- TRUTH.FN: Number of truth calls for which there is no query call that is consistent with the query call and its genotype. 
- TRUTH.TP: Number of truth calls for which there is a query call that is consistent with the truth call and its genotype