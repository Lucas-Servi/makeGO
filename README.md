makeGO
==========

Plot **Fold Enrichment (FE)** from the PantherDB (http://go.pantherdb.org) GO (Gene Ontology) output into a **Bubble Plot** (saved as a high dpi .pdf file).


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
Any of this libraries can be installed by using  ``` pip install <library name> ```


# How to use

This script runs on terminal with the following parameters:
```
python3 GO_plot.py -i <input-file.txt> <input-file.txt> <input-file.txt> -names <name1> <name2> <name3> -o <output-file.pdf>
```

- **-i**  | **--input-file**:  files(**.txt**) from PantherDB, each file correspond to a set or cluster. Same GO analysis (Biological processes, Cellular Components, etc.) are recomemended. **Full directory must be used** (e.g.: /home/.../file1.txt)
- **-o**  | **--output-file**: a **.pdf** format file containing the dot plot where y-axis show GO groups and x-axis are the differente sets/clusters from the input-files.
- **-names** | **-set-names**: list of names corresponding to the x-label of the plot.
- **-top** | **-top-FE-results** (optional - default=10): only plot the top n FE-change results.
- **-fdr** | **-fdr-treshold** (optional - default=0.01): sets the FDR treshold of the GO groups.


## Example


*Files used in this example are saved in the* ```demo``` *folder of this repository* 


Go to PantherDB-GO for plants (https://www.arabidopsis.org/tools/go_term_enrichment.jsp), paste the **demo_gene_list.txt**, Choose Organism **Arabidopsis thaliana** and Choose desired GO Aspect.

<p align="center">
<img width="50%" height="50%" alt="Gene list Submission" src="https://github.com/Lucas-Servi/makeGO/blob/main/demo/example_gene_list.png"></p>


Once the information is submitted, export the PantherDB data as **Table**:

<p align="center">
<img width="60%" height="60%" alt="Export as table" src="https://github.com/Lucas-Servi/makeGO/blob/main/demo/example_panther.png"></p>


The expected output running the following code 


``` python3 GO_plot.py -i /home/[user]/.../panther_exported_table.txt -names cluster1 -o ./plot ```


should look like this(saved as a high dpi .pdf file):


<p align="center">
<img width="60%" height="60%" alt="Plot Example" src="https://github.com/Lucas-Servi/makeGO/blob/main/demo/demo.jpg"></p>


# AUTHOR/SUPPORT

Lucas Servi, lucasservi@gmail.com </br>



