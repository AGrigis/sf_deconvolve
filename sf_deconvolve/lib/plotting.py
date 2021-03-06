# -*- coding: utf-8 -*-

"""PLOTTING ROUTINES

This module contains methods for making plots.

:Author: Samuel Farrens <samuel.farrens@gmail.com>

:Version: 1.1

:Date: 05/01/2017

"""

import os
import numpy as np
import matplotlib.pyplot as plt


def plotCost(cost_list, output=None):
    """Plot cost function

    Plot the final cost function

    Parameters
    ----------
    cost_list : list
        List of cost function values
    output : str, optional
        Output file name

    """

    if isinstance(output, type(None)):
        file_name = 'cost_function.png'
    else:
        file_name = os.path.join(output, '_cost_function.png')

    plt.figure()
    plt.plot(np.log10(cost_list), 'r-')
    plt.title('Cost Function')
    plt.xlabel('Iteration')
    plt.ylabel('$\log_{10}$ Cost')
    plt.savefig(file_name)
    plt.close()

    print ' - Saving cost function data to:', file_name
