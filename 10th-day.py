#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:04:07 2020

@author: kudevara
"""

# 6th(thr) : numpy 
# 7th(fri): strings / files
# 8th(sat): oops
# 9th(sun): NLP
# 10th and 11th(Mon/Tue): ML/DL
# 12th 13th (wed/Thr): Bigdata
# 14th / 15th / 16th (Fri/Sat/Sun): DS/Algo
# ************
# 17th to 31st Docker & Kubernetes

from matplotlib import animation
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import sys

def update(f_name, rolls, faces, freq):
    for i in range(rolls):
        freq[random.randrange(1,7)-1] += 1
    plt.cla()    
    axes = sns.barplot(x=value, y=freq, palette='bright')
    plt.show()
num_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')
fig = plt.figure('play rolls')
value = list(range(1,7))
freq = [0] * 6

dice_animation = animation.FuncAnimation(
                            fig, 
                            update, 
                            frames=num_of_frames, 
                            repeat=False,
                            interval=33,
                            fargs=(rolls_per_frame, value, freq))
plt.show()

# no. of frames 
# no. of dices

# python script.py 10000 100
# static viz... ippo panna poratrhu dynamic viz
# FuncAnimation
# frame by frame
# 33 ms between frames
# 1000 / 33 => 30 FPS




