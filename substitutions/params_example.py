output_dir = path/to/output
#
#PARAMETERS FOR DETECT
#specify a path to the fasta file (DNA sequence of protein coding sequences)
path_to_fasta = path/to/cdna.all.fa
#specify NCBI codon table to use during SeqIO translations
# Table 1 = Standard
# Table 2 = Vertebrate Mitochondrial (HUMAN)
# Table 5 = Invertebrate Mitochondrial (DROSOPHILA)
# Table 11 = Bacterial, Archaeal, Plant Plastid (E. COLI)
codon_table = 11
#path to MaxQuant's table, allPeptides.txt
path_to_allPeptides = path/to/allPeptides.txt
#m/z tolerance, used to filter DP–BP couples that resemble substitutions
#and exclude couples that resemble known PTM
tol = 0.005
#these parameters control the filtering of n-term and c-term modifications
n_term_prob_cutoff = 0.05
c_term_prob_cutoff = 0.05
#defines the minimal threshold on MaxQuant's localisation probability. Only
#DP–BP peptides for which the localisation of the modification has be been
#determined with higher confidence will be retained. 
positional_probability_cutoff = 0.95
#FDR for the final target-decoy FDR procedure
fdr = 0.01
#OPTIONAL PARAMETER : provide a regex to extract the gene name from the
#description of the fasta records.
#ex: regex = 'gene_symbol\:(.*)$'
#if the regex parameter is not defined, the program will use the fasta
#id in place of the gene name.
regex = gene_symbol\:(.*)(\s|$)