# -*- coding: utf-8 -*-
"""
ALBA dictionary builder

Created on Thu Sep 27 16:49:42 2018

@author: D. Kamishima
"""
# Referenced https://qiita.com/Salinger/items/529a77f2ceeb39998665


import numpy as np
from numba import jit
import pickle

@jit
def DicBuilder(filename):
    
    print("Building Dictionary...")
    
    dictionary = {}
    
    opname = filename + ".txt"
    
    f = open(opname)
    
    line = f.readline()
    
    max_traj_len = 0
    
    
    while line:
        line = f.readline()
        words = line.split(" ")
        
        w_len = len(words)
        
        if w_len > max_traj_len:
            max_traj_len = w_len
        
        word_list = list(set(words))
        
        for i in range(len(word_list)):
            #If Not in dictionary, add this word.
            if (word_list[i] in dictionary.keys()) == False:
                dictionary[word_list[i]] = int(len(dictionary) + 1)
    
    f.close()
    
    # Save this Dictionary
    
    svname = filename + ".dump"
    
    with open(svname, "w") as f:
        pickle.dump(dictionary, f)
    
    print("Completed dict: in {}.".format(svname))
    
    
    return max_traj_len
