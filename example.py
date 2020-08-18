import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/mike/Documents/Utilities/Python/idl_colorbars/')
from idl_colorbars import getcmap

mycmap=getcmap(109)

arr=np.indices((30,30))
arr=arr[0]+arr[1]
plt.imshow(arr,cmap=mycmap)
plt.show()
