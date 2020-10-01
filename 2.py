import subprocess
import os, glob
from scipy.io import arff
import pandas as pd
import numpy as np
import pickle as pkl
from fnmatch import fnmatch
#arr = np.zeros((309,988))
arr = np.zeros((309,6552))

def summ_(a, b):
    return (a+b)
arg1="C:/Users/Lyudmila/Downloads/opensmile-2.3.0/bin/Win32/SMILExtract_Release.exe"
#arg2="C:/Users/Lyudmila/Downloads/opensmile-2.3.0/config/emobase.conf"
arg2="C:/Users/Lyudmila/Downloads/opensmile-2.3.0/config/emo_large.conf"
features=[]
y=[]
f_name = []
#arg5="C:/Users/Lyudmila/Desktop/emotion/test/surprised/"
#os.chdir(arg5)


root = "C:/Users/Lyudmila/Desktop/emotion/test"
pattern = "*.wav"
print(os.listdir(root))
for label,d in enumerate(os.listdir(root)):
    print(label,d)
    path=os.path.join(root,d)
    for name in os.listdir(path):
        if fnmatch(name, pattern):
            cmd = arg1+" "+"-C"+" "+arg2+" "+"-I"+" "+os.path.join(path, name)+" "+"-O"+" "+"C:/Users/Lyudmila/Downloads/opensmile-2.3.0/example-audio/out.txt"
            #print(os.path.join(path, name))

            p = subprocess.Popen(cmd)
            p.wait()
            f = open("C:/Users/Lyudmila/Downloads/opensmile-2.3.0/example-audio/out.txt",'r')

            last_line = f.readlines()[-1].split(',')
            result=[float(s) for s in last_line[1:-1]]
            features.append(result)
            #if (subdirs = "angry"):
            y.append(label)
            f_name.append(name)
features=np.array(features)
yy = np.array(y)
f_name1 = np.array(f_name1)
