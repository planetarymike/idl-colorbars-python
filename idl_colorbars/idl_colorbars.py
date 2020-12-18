# idl_colorbars.py
__all__ = ['getcmap', 'showcmaps']

import os as _os
import glob as _glob
import numpy as _np
import matplotlib.pyplot as _plt
import matplotlib.image as _mpimg
from matplotlib.colors \
    import LinearSegmentedColormap as _LinearSegmentedColormap


def getcmap(num,
            reverse=False,
            vmin=0, vmax=1):
    """
    Load a matplotlib colormap corresponding to the IDL colomap of the
    same number.

    Parameters
    ----------
    num : int
        Number of the colormap to load.
    reverse : bool
        Whether to reverse the colormap. Defaults to False.
    vmin : float
        Load the colormap starting at fractional value vmin, ignoring
        colors that occur earlier in the colormap. Applied before
        reversal, if any.
    vmax : float
        Load the colormap ending at fractional value vmin, ignoring
        colors that occur later in the colormap. Applied before
        reversal, if any.

    Returns
    -------
    sm : matplotlib.colors.LinearSegmentedColormap
        colormap object that can be fed to any matplotlib function
        that needs a colormap

    Notes
    -----
    Available colormaps can be viewed with the showcmaps() function

    Examples
    --------
    >>> mycmap=getcmap(109)
    >>> arr=np.indices((30,30))
    >>> arr=arr[0]+arr[1]
    >>> import matplotlib.pyplot as plt
    >>> plt.imshow(arr,cmap=mycmap)
    >>> plt.show()
    """

    # Identify the file associated with this colormap number
    fnames = _glob.glob(_os.path.join(_os.path.dirname(__file__),
                                      'IDL_rgb_values',
                                      str(num).zfill(3)+'*'))
    # Load the data from file
    data = _np.loadtxt(fnames[0], delimiter=',')

    # Reverse if requested
    if reverse:
        data = _np.flip(data, axis=0)

    # Truncate if requested
    datalength = len(data)
    dmin = int(datalength*vmin)
    dmax = int(datalength*vmax)
    if dmax == datalength:
        dmax = datalength-1
    if dmin == datalength:
        dmin = datalength-1
    data = data[dmin:dmax+1]

    # construct the matplotlib object and return
    cm = _LinearSegmentedColormap.from_list('my_cmap', data)

    return cm


def showcmaps():
    """
    Show matplotlib image of available colormaps

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    example_fname = _os.path.join(_os.path.dirname(__file__),
                                  'all_idl_tables.png')

    img = _mpimg.imread(example_fname)
    _plt.imshow(img)
    _plt.axis("off")
    _plt.show()
