# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:49:42 2018

@author: D. Kamishima
"""

import numpy as np


def ex_P_calc(pi_e, n_states):
    
    #numpy配列形式のエキスパート軌跡リストから遷移確率を計算
    
    #INPUT
    #pi_e : １行に１軌跡のnumpy配列
    #n_states : 状態数
    
    P = np.zeros((n_states, n_states))
    n_traj, _ = np.shape(pi_e)
    
    for i in range(n_traj):
        
        #軌跡一本ぶんを取り出す
        pi = pi_e[int(i)][:]
        
        #カウントする
        for n in range(len(pi) - 1):
            s = pi[ int(n) ]
            ns = pi[ int(n + 1) ]
            P[int(s)][int(ns)] = P[int(s)][int(ns)] + 1
    
    #最後に確率にする
    for l in range(n_states):
        if int(np.sum(P[int(l)][:])) != 0:
            P[int(l)][:] = P[int(l)][:] / np.sum(P[int(l)][:])
    
    return P


#test code
pi_expert = np.array([[ 0,  1,  2,  3,  4,  9, 14, 19, 24],
                      [ 0,  5, 10, 15, 20, 21, 22, 23, 24],
                      [ 0,  1,  6,  7, 12, 13, 18, 19, 24],
                      [ 0,  5,  6, 11, 12, 17, 18, 23, 24]])




n_states = 25

print( ex_P_calc(pi_expert,25))
