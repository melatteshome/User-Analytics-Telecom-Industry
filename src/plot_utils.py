import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_count(df, col, title, xlabel, ylabel, figsize=(10, 6)):
    plt.figure(figsize=figsize)
    sns.countplot(data=df, x=col)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_hist(df, col, title, xlabel, ylabel, bins=10, figsize=(10, 6)):
    plt.figure(figsize=figsize)
    plt.hist(df[col], bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

