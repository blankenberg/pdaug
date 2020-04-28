import glob, os

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt;plt.interactive(True)
import matplotlib



def HTML_Gen(html):

    out_html = open(html,'w')             
    part_1 =  """

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Bootstrap Example</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <body>
    <style>
    div.container_1 {
      width:600px;
      margin: auto;
     padding-right: 10; 
    }
    div.table {
      width:600px;
      margin: auto;
     padding-right: 10; 
    }
    </style>
    </head>
    <div class="jumbotron text-center">
      <h1> Machine Learning Algorithm Assessment Report </h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-sm-4">
          <img src="Out.png" alt="Smiley face" height="500" width="400">
        </div>

      </div>
    </div>
    </body>
    </html>
    """ 
    out_html.write(part_1)
    out_html.close()

def BoxPlot(InFile, Method, Feature, Label, RotationX, RotationY, FigHight, FigWidth,  Workdirpath, htmlOutDir, htmlFname, Index, ClassLabel):

    Workdirpath = os.path.join(os.getcwd(),'report_dir')

    if not os.path.exists(htmlOutDir):
        os.makedirs(htmlOutDir)

    df  = pd.read_csv(InFile, sep="\t")

    if Method == 'Feature':

        f = Feature.split(',')

        plt.figure(figsize=(int(FigHight),int(FigWidth)))
        sns.boxplot(data=df[f])
        plt.xticks(rotation=int(RotationX))
        plt.yticks(rotation=int(RotationY))
        plt.savefig(os.path.join(Workdirpath, htmlOutDir, "Out.png"), dpi=600)

    else:

        f = Feature.split(',')
        sns.boxplot(x=Label, y=df[f[0]], width=0.3, data=df, linewidth=0.4, fliersize=0.5)
        plt.xticks(rotation=RotationX)
        plt.yticks(rotation=RotationY)
        plt.savefig(os.path.join(Workdirpath, htmlOutDir, "Out.png"), dpi=600)

    HTML_Gen(os.path.join(Workdirpath, htmlOutDir, htmlFname))

if __name__=="__main__":

    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-I", "--InFile", required=True, default=None, help="Input file")
    parser.add_argument("-M", "--Method", required=True, default=None, help="Plotting method")
    parser.add_argument("-Rx", "--RotationX", required=False, default=0, help="Roatate xticks")
    parser.add_argument("-Ry", "--RotationY", required=False, default=0, help="Roatate yticks")
    parser.add_argument("-H", "--FigHight", required=False,  default=6,  help="Figure Hight")
    parser.add_argument("-W", "--FigWidth", required=False, default=4, help="Figure Width")
    parser.add_argument("-Ix", "--Index", required=False, default=True, help="Index")
    parser.add_argument("-C", "--ClassLabel", required=False, default="class_label", help="Class Label")
    parser.add_argument("-F", "--Features", required=True, default=None, help="Feature list to plot")
    parser.add_argument("-O","--htmlOutDir", required=False, default=os.path.join(os.getcwd(),'report_dir'),  help="HTML Out Dir")
    parser.add_argument("-Hf","--htmlFname", required=False, help="HTML out file", default="jai.html")
    parser.add_argument("-Wp","--Workdirpath", required=False, default=os.getcwd(), help="Working Directory Path")
    parser.add_argument("-L","--Label", required=False, default=False, help="X axis label")
    args = parser.parse_args()

BoxPlot(args.InFile, args.Method, args.Features, args.Label, args.RotationX, args.RotationY, args.FigHight, args.FigWidth,  args.Workdirpath,  args.htmlOutDir, args.htmlFname, args.Index, args.ClassLabel)






