makeGO
==========

Plot Fold Enrichment (FE) from the PantherDB GO output.

## How to use the script

This script runs on terminal with the following parameters:
```
python3 GO_plot.py -i <input-file.txt> <input-file.txt> <input-file.txt> -names name1 name2 name3 -o <output-file.pdf>
```

- **-i**  | **--input-file**:  files(**.txt**) from PantherDB, each file correspond to a set or cluster. Same GO analysis (Biological processes, Cellular Components, etc.) are recomemended.
- **-o**  | **--output-file**: a **.pdf** format file containing the dot plot where y-axis show GO gruops and x-axis are the differente sets/clusters from the input-files.
- **-names** | **-set-names**: list of names corresponding to the x-label of the plot
- **-top** | **-top-FE-results** (optional - default=10):
- **-fdr** | **-fdr-treshold** (optional - default=0.01):


### AUTHOR/SUPPORT

Lucas Servi, lucasservi@gmail.com </br>



