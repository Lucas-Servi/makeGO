makeGO
==========

Plot **Fold Enrichment (FE)** from the PantherDB (http://go.pantherdb.org) GO (Gene Ontology) output into a **Bubble Plot**.


# Installation Guide:

### Install from Github
```
git clone https://github.com/Lucas-Servi/makeGO.git
cd makeGO
```
- `sudo`, if required

# System Requirements
## Hardware requirements
`makeGO` package requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
The package has been tested on the following systems:
+ Linux: Ubuntu 18.04+

### Python Dependencies
`makeGO` depends on:

```
matplotlib
numpy
pandas
seaborn
```

# How to use

This script runs on terminal with the following parameters:
```
python3 GO_plot.py -i <input-file.txt> <input-file.txt> <input-file.txt> -names name1 name2 name3 -o <output-file.pdf>
```

- **-i**  | **--input-file**:  files(**.txt**) from PantherDB, each file correspond to a set or cluster. Same GO analysis (Biological processes, Cellular Components, etc.) are recomemended. **Full directory must be used** (e.g.: /home/.../file1.txt)
- **-o**  | **--output-file**: a **.pdf** format file containing the dot plot where y-axis show GO groups and x-axis are the differente sets/clusters from the input-files.
- **-names** | **-set-names**: list of names corresponding to the x-label of the plot.
- **-top** | **-top-FE-results** (optional - default=10): only plot the top n FE-change results.
- **-fdr** | **-fdr-treshold** (optional - default=0.01): sets the FDR treshold of the GO groups.


# AUTHOR/SUPPORT

Lucas Servi, lucasservi@gmail.com </br>



