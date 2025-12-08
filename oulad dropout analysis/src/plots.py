
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_pie(column,data):
    df = data[column].value_counts(normalize= True).mul(100).round(2).reset_index(name = 'percentage')
    explode = [0.1 if p == df['percentage'].max() else 0 for p in df['percentage']]
    plt.pie(x = 'percentage',
            data= df,
            labels=df[column],
            autopct="%.2f%%",
            colors=plt.cm.tab20.colors,
            shadow=True,
            startangle= 60,
            explode=explode,
            textprops={'size': 'smaller'},
            wedgeprops={'edgecolor':'white'})
    plt.title(f"Distribution of {column}",weight = 'bold')

def plot_kde(column,data):
    sns.kdeplot(x = column,data =data)
    plt.title(f"Distribution of {column}",weight = 'bold')

def percentage_in_that_class(column,data,target,orient):
    df =data.groupby(column)[target].value_counts(normalize=True).mul(100).round(2).reset_index(name ='percentage_of_that_class')
    ax = sns.barplot(x = column,y = 'percentage_of_that_class',data = df,hue= target,orient=orient,edgecolor = 'black',palette = 'tab20')
    for container in ax.containers:
        ax.bar_label(container)
    plt.title(f'Percentage of {column} from each {target} class',weight = 'bold')


def kde_in_both_class(column,data,target):
    sns.kdeplot(x = column,hue = target,data=data)
    plt.title(f"Distribution of {column} by {target}")

def plot_heatmap(ct, annot=True, cmap="Blues"):
    sns.heatmap(ct, annot=annot, cmap=cmap, fmt=".1f", linewidths=.5)
    plt.title("Crosstab Heatmap")
    plt.xlabel(ct.columns.name if ct.columns.name else "Columns")
    plt.ylabel(ct.index.name if ct.index.name else "Index")