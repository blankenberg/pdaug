import pandas as pd 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-I", "--InFile", required=True, default=None, help="Input data file")
parser.add_argument("-C", "--ClassLabel", required=False, default=0, help="Class Label 0 or 1")
parser.add_argument("-t", "--ClassLabelTitle", required=False, default='Class_label', help="Title to use for class label column (Class_label)")
parser.add_argument("-O", "--OutFile", required=False, default='OutFile.tsv', help="Output file name")

args = parser.parse_args()

df1 = pd.read_csv(args.InFile, sep="\t")
df2 = pd.DataFrame([args.ClassLabel]*df1.shape[0], columns=[args.ClassLabelTitle])

df = pd.concat([df1, df2], axis=1)
df.to_csv(args.OutFile, sep="\t", index=False)