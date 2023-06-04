# -*- coding: utf-8 -*-
from __future__ import print_function, division
from os.path import expanduser
from pylab import rcParams
import seaborn as sns
sns.set(style="white")

def _mm_to_inches(*mms):
    return [mm / 25.4 for mm in mms]

FONTSIZE = 8
params = {'figure.figsize': _mm_to_inches(180, 80), # 180 or 88mm wide for Scientific Data
          'axes.labelsize': FONTSIZE, # FONTSIZE for x and y labels (was FONTSIZE)
          'axes.titlesize': FONTSIZE,
          'font.size': FONTSIZE, # was FONTSIZE
          'legend.fontsize': FONTSIZE, # was FONTSIZE
          'xtick.labelsize': FONTSIZE,
          'ytick.labelsize': FONTSIZE,
          'font.family': 'Bitstream Vera Sans'
}

rcParams.update(params)

def format_axes(ax, tick_size=4):
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color='k', size=tick_size)    

    return ax


#FIG_DIR = expanduser("~/Dropbox/MyWork/imperial/PhD/writing/papers/scientific-data-2014/figures")

BLUE = (0.2980392156862745, 0.4470588235294118, 0.6901960784313725)
GREEN = (0.3333333333333333, 0.6588235294117647, 0.40784313725490196)

new_names = {
    'Light': 'Dimmable LED kitchen ceiling lights',
    'Computer monitor': '24\" LCD computer monitor',
    'Television': '34\" CRT television'
}

###Updates Carlos
#fontsize line
#removed FIR_DIR line for automatic figure saving