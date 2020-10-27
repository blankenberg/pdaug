import modlamp
from modlamp.datasets import load_AMPvsTM
from modlamp.datasets import load_AMPvsUniProt
from modlamp.datasets import load_ACPvsTM
from modlamp.datasets import load_ACPvsRandom
from modlamp.database import query_apd
from modlamp.database import query_camp
import os
import pandas as pd

def DataGen(DataBaseType, OutFile, IDs):

    if DataBaseType == 'AMPvsTM':
        data = load_AMPvsTM()

    elif DataBaseType == 'AMPvsUniProt':
        data = load_AMPvsUniProt()

    elif DataBaseType == 'ACPvsTM':
        data = load_ACPvsTM()

    elif DataBaseType == 'ACPvsRandom':
        data = load_ACPvsRandom()

    elif DataBaseType == 'query_apd':

        data = query_apd([int(i) for i in IDs.split(',')])
        df = pd.DataFrame(data, columns=['Peptides'])
        df.to_csv(OutFile, index=False, sep='\t')
        exit()

    elif DataBaseType == 'query_camp':
        data = query_camp([int(i) for i in IDs.split(',')])
        df = pd.DataFrame(data, columns=['Peptides'])
        df.to_csv(OutFile, index=False, sep='\t')
        exit()

    else:
        print ("Enter Correct Values")
        exit()

    Target = data.target.tolist()
    Target_list = set(Target)
    df = data.sequences


    Target = pd.DataFrame(Target, columns=['Target'])
    df = pd.DataFrame(df, columns=['Peptide'])
    
    df = pd.DataFrame(df)
    df = pd.concat([df, Target], axis=1)

    df.to_csv(OutFile, index=False, sep='\t')


if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--DataBaseType",
                        required=True,
                        default=None,
                        help="Name of the dataset ")
                        
    parser.add_argument("-o", "--OutFile",
                        required=False,
                        default='Out.tsv',
                        help="Out put file name for str descriptors")   

    parser.add_argument("-L", "--List",
    					required=False,
    					default=None,
    					help="List of integer as ID")

    args = parser.parse_args()
    DataGen(args.DataBaseType, args.OutFile, args.List)
