import numpy as np
import pandas as pd
from scipy.stats import binom, beta
from scipy.optimize import minimize
from numpy.random import default_rng
import matplotlib.pyplot as plt

def plotBeta(a,b):
    fig, ax = plt.subplots(1, 1)
    (mean, var) = beta.stats(a,b)
    mode = (a-1)/(a+b -2)
    print(f"mean:{mean}, var:{var}, mode:{mode}")
    x = np.linspace(0, 1, 100)
    ax.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')


def beta_stats(a, b):
    (mean, var) = beta.stats(a,b)
    mode = (a-1)/(a+b -2)
    return (float(mean), mode,float(var), np.sqrt(var))

def summarize_beta_bin(alpha, beta, y, n):
   (prior_mean, prior_mode, prior_var, prior_std) = beta_stats(alpha, beta)
   (post_mean, post_mode, post_var, post_std) = beta_stats(alpha+y, beta+(n-y))
   return pd.DataFrame({'alpha': [alpha, alpha+y], 'beta': [beta, beta+(n-y)], \
                        'mean': [prior_mean, post_mean], 'mode': [prior_mode, post_mode],\
                       'var': [prior_var, post_var], 'std': [prior_std, post_std]})


def plotBetaBinomial(a,b,y,n):
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(0, 1, 100)
    ax.set(xlabel='pi', ylabel='density', title='BetaBinomial')
    ax.grid()
    ax.fill_between(x, 0, beta.pdf(x, a, b), alpha=0.6, label = 'prior')
    ax.fill_between(x, 0, beta.pdf(x, y+1, n-y+1), alpha=0.6, label='likelyhood')
    ax.fill_between(x, 0, beta.pdf(x, y+a, n-y+b), alpha=0.6, label = 'posterior')
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    