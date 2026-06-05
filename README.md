# substitutions

This collection of scripts allows the user to detect amino acid substitutions from mass spectrometry data. It relies on MaxQuant to perform the initial analysis, and applies a series of filters to separate amino acid substitutions from other PTMs detected by MaxQuant's dependent peptides algorithm.

The module requires python >=3.6

# Important note

This workflow was [originally developed by Ernest Mordret](https://github.com/ernestmordret/substitutions) and published in [Mordret et al. (2019)](https://doi.org/10.1016/j.molcel.2019.06.041). The present workflow is a simplified version of [Manuel Koesters's adaptation to python 3](https://github.com/MKoesters/substitutions) downloaded on September 13, 2021. It includes only the detection of amino acid substitutions, while the quantification and plotting scripts were omitted. 
Beyond the work of Ernest Mordret and Manuel Koesters, the present workflow allows for the analysis of additional organisms by adding a variable for [NCBI codon tables](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi) as well as labels for mispairing and "danger mods" to allow for subsequent filtering (rather than removal). For subsequent quantification in Skyline, identifications are filtered and re-structured using my [Skyline pipeline](https://github.com/nfreyer/skyline_pipeline).

To run the detection, create a params file and run:

```
python run.py -d path\to\params.py
```