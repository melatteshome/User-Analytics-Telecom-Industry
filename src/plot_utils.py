import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_countplot(df, column, hue=None):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column, hue=hue)
    plt.title(f'Countplot of {column}')
    plt.show()


