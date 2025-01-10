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

def plot_boxplot(data, title, x_label, color='lightcoral'):
    """
    Plot a boxplot.

    Parameters:
    - data: Series or array-like
        Data to be plotted.
    - title: str
        Plot title.
    - x_label: str
        Label for the x-axis.
    - color: str, optional
        Color for the plot.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data, color=color)
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()