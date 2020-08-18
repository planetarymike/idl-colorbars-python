import glob
import numpy as np
import os
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

def getcmap(no,reverse=False,vmin=0,vmax=1):
    fnames = glob.glob(os.path.join(os.path.dirname(__file__),'IDL_rgb_values',str(no).zfill(3)+'*'))
    data = np.loadtxt(fnames[0],delimiter=',')
    if reverse:
        data=np.flip(data,axis=0)
    datalength=len(data)
    dmin=int(datalength*vmin)
    dmax=int(datalength*vmax)
    if dmax==datalength:
        dmax=datalength-1
    if dmin==datalength:
        dmin=datalength-1
    data=data[dmin:dmax+1]
    
    cm = LinearSegmentedColormap.from_list('my_cmap',data)
    return cm
