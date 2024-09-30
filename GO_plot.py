import argparse
import pandas as pd
import itertools
import seaborn as sns
import matplotlib.pyplot as plt


# Avoid chained_assignment warning when working on slices of dataframes
pd.set_option('mode.chained_assignment', None)


def plot_scat(df):
    sns.set_theme(style="whitegrid")
    f, ax = plt.subplots(figsize=(3 , 8))
    ax = sns.scatterplot(data=df, x='Sets', y=df.columns[1], hue="FDR",
                        palette="flare", size="Fold Enrichment", sizes=(100, 2000)
                          , legend='brief', size_order=[0, 5])
    ax.set_xmargin(0.2)
    ax.legend(shadow=True, borderpad=1.5, labelspacing=1.5, handlelength=3, fontsize='large',
               loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
    return ax


def filter_FRD (df_in, name, top=10, FDR = 0.01):
    df = df_in
    df.rename(columns={df.columns[5]: "Fold Enrichment"}, inplace=True)
    df.rename(columns={df.columns[7]: "FDR"}, inplace=True)
    df.rename(columns={df.columns[4]: "(over/under)"}, inplace=True)
    df.replace({' < 0.01': 0.01, ' > 100': 100}, inplace=True)
    df['Sets'] = name
    df["FDR"] = pd.to_numeric(df["FDR"], downcast="float")
    df["Fold Enrichment"] = pd.to_numeric(df["Fold Enrichment"], downcast="float")
    df = df[(df['FDR'] < FDR)]
    
    #Fold Enrichment for FE < 1  transformation for query
    df_temp = df.copy()
    df_temp['Fold Enrichment'][(df_temp['(over/under)'] == '-')] = 1 / df_temp['Fold Enrichment'][(df_temp['(over/under)'] == '-')]
    df_temp = df_temp.sort_values(by=['Fold Enrichment'], ascending=False)
    filt = df_temp.iloc[0:top, :1].values
    filt = [x[0] for x in filt]
    df = df[(df.iloc[:, 0].isin(filt))]

    return df


def table_join (files, set_names, top, FDR):
    if files == []:
        return "No Input specified"

    dfs = []
    for (file, name) in zip(files, set_names):
        df = pd.read_csv(file, sep='\t', header=0, skiprows=11)
        filtered_df = filter_FRD(df, name, top, FDR)
        dfs.append(filtered_df)
    df = pd.concat(dfs).reset_index()
    return df


def parse_arguments():
    # Handles terminal commands
    """parses all necessary arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="Input_files", action='append', nargs='+',
                        help="Space separated files from GO.")
    parser.add_argument("-names", dest="set_names", action='append', nargs='+',
                        help="Space separated set names.")
    parser.add_argument("-top", dest="top_FE", type=int, default=10,
                        help="Limit the plot to the top N Fold Enrichment changes. Default: 10")
    parser.add_argument("-fdr", dest="fdr", action='store', nargs='?', default=0.01,
                        help="Sets the FDR Treshold to filter data. Default = 0.01")
    parser.add_argument("-o", dest="output_file", nargs='+',
                        help="Output directory, name preffix can be added.")
    return parser.parse_args()


def main():
    print("Loading tables...")
    args = parse_arguments()
    top = args.top_FE
    FDR = args.fdr
    filt_df = table_join(args.Input_files[0],args.set_names[0],top,FDR)
    outdir = args.output_file[0] + "_GO.pdf"
    print("Creating Plot in " + outdir)
    ax = plot_scat(filt_df)
    plt.savefig(outdir, dpi=300, bbox_inches="tight")
    plt.show()

    
if __name__ == "__main__":
    main()
