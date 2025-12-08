# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Defining all the necessary plots

# For Pie Chart of Single Column
def plot_pie(column,data):
    df = (data[column].
          value_counts(normalize= True).
          mul(100).
          round(2).
          reset_index(name = 'percentage')
          )
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

# For KDE Plot os Single  Column
def plot_kde(column,data):
    sns.kdeplot(x = column,
                data =data,
                linewidth = 2)
    plt.title(f"Distribution of {column}",weight = 'bold')

# For Bar Plot of Categorical Type Column and Target Column
def percentage_in_that_class(column, data, target, orient):

    df = (
        data.groupby(column)[target]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index(name='percentage_of_that_class')
    )
    # horizontal
    if orient == 'h':
        ax = sns.barplot(
            y=column,
            x='percentage_of_that_class',
            data=df,
            hue=target,
            edgecolor='black',
            palette='tab20'
        )
    # vertical
    else:  # orient == 'v'
        ax = sns.barplot(
            x=column,
            y='percentage_of_that_class',
            data=df,
            hue=target,
            edgecolor='black',
            palette='tab20'
        )
    for c in ax.containers:
        ax.bar_label(c)

    plt.title(f'Percentage of {column} from each {target} class', weight='bold')

# For KDE Plot in Different Target Classes
def kde_in_all_class(column,data,target):
    sns.kdeplot(x = column,
                hue = target,
                data=data
                )
    plt.title(f"Distribution of {column} by {target}")

# For Box Plot in Different Target Classes
def box_in_all_class(column,data,target):
    sns.boxplot(x = column,
                hue = target,
                data=data
                )
    plt.title(f"Distribution of {column} by {target}")

# For Scatterplot in Different Target Classes
def scatter_in_all_class(column,target,data):
    plt.scatterplot(x = column,
                    y=target,
                    data=data,
                    color = 'teal')
    plt.title(f"Scatter plot of {column} in all {target}")

# For Heatmap for Large Categorical Classes
def plot_heatmap(ct, annot=True, cmap="Blues"):
    sns.heatmap(ct, 
                annot=annot, 
                cmap=cmap, 
                mt=".1f", 
                linewidths=.5)
    plt.title("Crosstab Heatmap")
    plt.xlabel(ct.columns.name if ct.columns.name else "Columns")
    plt.ylabel(ct.index.name if ct.index.name else "Index")