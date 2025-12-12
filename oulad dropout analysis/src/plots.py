# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Defining all the necessary plots

#______________________________________________________________________________
# For Pie Chart of Single Column
def plot_pie(column,data):
    df = (data[column].
          value_counts(normalize= True).
          mul(100).
          round(2).
          reset_index(name = 'percentage')
          )
    plt.pie(x = 'percentage',
            data= df,
            labels=df[column],
            autopct="%.2f%%",
            colors=plt.cm.tab20.colors,
            shadow=True,
            startangle= 200,
            textprops={'size': 'smaller'},
            wedgeprops={'edgecolor':'white'})
    plt.title(f"Distribution of {column}",weight = 'bold')

#______________________________________________________________________________
# For Box Plot os Single  Column
def plot_box(column,data,line_val = .95):
    mini = data[column].min()
    maxi = data[column].max()
    sns.boxplot(x = column,
                data =data,
                linewidth = 2)
    plt.axvline(data[column].quantile(line_val),color = 'red')
    plt.xticks(np.linspace(mini,maxi,20).astype('int'))
    plt.title(f"Distribution of {column}",weight = 'bold')

#______________________________________________________________________________
# For KDE Plot os Single  Column
def plot_kde(column,data,line_val = .95):
    mini = data[column].min()
    maxi = data[column].max()
    sns.kdeplot(x = column,
                data =data,
                linewidth = 2)
    plt.axvline(data[column].quantile(line_val),color = 'red')
    plt.xticks(np.linspace(mini,maxi,20).astype('int'))
    plt.title(f"Distribution of {column}",weight = 'bold')

#______________________________________________________________________________
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

#______________________________________________________________________________
# For KDE Plot in Different Target Classes
def kde_in_all_class(column,data,target):
    mini = data[column].min()
    maxi = data[column].max()
    sns.kdeplot(x = column,
                hue = target,
                data=data
                )
    plt.xticks(np.linspace(mini,maxi,20).astype('int'))
    plt.title(f"Distribution of {column} by {target}")

#______________________________________________________________________________
# For Box Plot in Different Target Classes
def box_in_all_class(column,data,target):
    mini = data[column].min()
    maxi = data[column].max()
    sns.boxplot(x = column,
                hue = target,
                data=data
                )
    plt.xticks(np.linspace(mini,maxi,20).astype('int'))
    plt.title(f"Distribution of {column} by {target}")

#______________________________________________________________________________
# For Scatterplot in Different Target Classes
def scatter_in_all_class(column,target,data):
    plt.scatter(x = column,
                    y=target,
                    data=data,
                    color = 'teal')
    plt.title(f"Scatter plot of {column} in all {target}")

#______________________________________________________________________________
# For Heatmap for Large Categorical Classes
def plot_heatmap(ct, annot=True, cmap="Blues"):
    sns.heatmap(ct, 
                annot=annot, 
                cmap=cmap, 
                fmt=".1f", 
                linewidths=.5)
    plt.title("Crosstab Heatmap")
    plt.xlabel(ct.columns.name if ct.columns.name else "Columns")
    plt.ylabel(ct.index.name if ct.index.name else "Index")