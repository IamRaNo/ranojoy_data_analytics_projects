# plots.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DESIGN SYSTEM SETUP
# ==========================================

def apply_custom_style():
    """
    Applies a modern, cleaner version of the FiveThirtyEight style.
    """
    plt.style.use('fivethirtyeight')
    
    # Custom Palette
    custom_palette = ["#008fd5", "#fc4f30", "#e5ae38", "#6d904f", "#818181"]
    sns.set_palette(custom_palette)
    
    # Overrides for a "Modern" look
    plt.rcParams.update({
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.grid': True,
        'grid.alpha': 0.4,
        'grid.color': '#e6e6e6',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': False,
        'axes.spines.bottom': True,
        'axes.titlelocation': 'left',
        'axes.titleweight': 'bold',
        'axes.titlesize': 18,
        'axes.labelweight': 'bold',
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.frameon': False,
    })
    print("Modern 538 Design System Applied!")

def _add_title_subtitle(ax, title, subtitle):
    """Internal helper to add consistent 538-style headers."""
    # Main Headline
    ax.text(x=0, y=1.12, s=title, fontsize=18, fontweight='bold', 
            transform=ax.transAxes, ha='left')
    # Subtitle
    ax.text(x=0, y=1.05, s=subtitle, fontsize=12, color='#555555', 
            transform=ax.transAxes, ha='left')

# ==========================================
# 2. PLOTTING FUNCTIONS
# ==========================================

# -----------------------------------------------------------------------------
# Pie Chart
# -----------------------------------------------------------------------------
def plot_pie(column, data):
    df = (data[column]
          .value_counts(normalize=True)
          .mul(100)
          .round(2)
          .reset_index(name='percentage')
          )
    
    # Grab the current axis
    ax = plt.gca()
    
    colors = sns.color_palette()
    
    ax.pie(
        x='percentage',
        data=df,
        labels=df[column],
        autopct="%.1f%%",
        colors=colors,
        startangle=90,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1},
        textprops={'fontsize': 9}
    )
    
    _add_title_subtitle(ax, 
                        title=f"Breakdown of {column}", 
                        subtitle=f"Distribution of categories in percentage")

# -----------------------------------------------------------------------------
# Box Plot (Univariate)
# -----------------------------------------------------------------------------
def plot_box(column, data, line_val=0.95):
    ax = plt.gca()
    
    sns.boxplot(x=column, data=data, linewidth=1.5, ax=ax, width=0.5)
    
    # Add quantile line
    quantile_val = data[column].quantile(line_val)
    ax.axvline(quantile_val, color='#fc4f30', linestyle='--', alpha=0.8, linewidth=2)
    ax.text(quantile_val, -0.4, f'{int(line_val*100)}th %tile', color='#fc4f30', fontweight='bold')

    ax.set_xlabel(column.replace('_', ' ').title())
    
    _add_title_subtitle(ax, 
                        title=f"Distribution of {column}", 
                        subtitle=f"Boxplot showing median and outliers")

# -----------------------------------------------------------------------------
# KDE Plot (Univariate)
# -----------------------------------------------------------------------------
def plot_kde(column, data, line_val=0.95):
    ax = plt.gca()
    
    sns.kdeplot(x=column, data=data, fill=True, linewidth=2, ax=ax, alpha=0.3)
    
    quantile_val = data[column].quantile(line_val)
    ax.axvline(quantile_val, color='#fc4f30', linestyle='--', alpha=0.8)
    
    ax.set_ylabel("Density")
    ax.set_yticks([]) 
    ax.set_xlabel(column.replace('_', ' ').title())

    _add_title_subtitle(ax, 
                        title=f"Density Curve of {column}", 
                        subtitle=f"Showing the shape of the data distribution")

# -----------------------------------------------------------------------------
# Bar Plot (Target Analysis)
# -----------------------------------------------------------------------------
def percentage_in_that_class(column, data, target, orient='v'):
    df = (data.groupby(column)[target]
          .value_counts(normalize=True)
          .mul(100)
          .round(2)
          .reset_index(name='pct')
          )
    
    ax = plt.gca()
    
    if orient == 'h':
        sns.barplot(y=column, x='pct', data=df, hue=target, 
                    edgecolor='black', ax=ax,palette='tab20')
        ax.set_xlabel("Percentage (%)")
    else:
        sns.barplot(x=column, y='pct', data=df, hue=target, 
                    edgecolor='black', ax=ax,palette='tab20')
        ax.set_ylabel("Percentage (%)")

    for c in ax.containers:
        ax.bar_label(c, fmt='%.2f%%', padding=3, fontsize=10)

    ax.legend(title=target, bbox_to_anchor=(1, 1))
    
    _add_title_subtitle(ax, 
                        title=f"How {target} varies by {column}", 
                        subtitle=f"Percentage split within each category")

# -----------------------------------------------------------------------------
# KDE Plot (Multivariate)
# -----------------------------------------------------------------------------
def kde_in_all_class(column, data, target):
    ax = plt.gca()
    
    sns.kdeplot(x=column, hue=target, data=data, fill=True, linewidth=2, ax=ax, alpha=0.2)
    
    ax.set_yticks([]) 
    ax.set_xlabel(column.replace('_', ' ').title())
    
    _add_title_subtitle(ax, 
                        title=f"{column} vs. {target}", 
                        subtitle="Compare distribution shapes to find separation")

# -----------------------------------------------------------------------------
# Box Plot (Multivariate)
# -----------------------------------------------------------------------------
def box_in_all_class(column, data, target):
    ax = plt.gca()
    
    sns.boxplot(x=column, y=target, data=data, orient='h', linewidth=1.5, ax=ax)
    
    ax.set_xlabel(column.replace('_', ' ').title())
    
    _add_title_subtitle(ax, 
                        title=f"Comparison: {column} by {target}", 
                        subtitle="Look for differences in medians and spread")

# -----------------------------------------------------------------------------
# Scatter Plot
# -----------------------------------------------------------------------------
def scatter_in_all_class(column, target, data):
    ax = plt.gca()
    
    sns.scatterplot(x=column, y=target, data=data, ax=ax, s=60, alpha=0.6, edgecolor=None)
    
    _add_title_subtitle(ax, 
                        title=f"Relationship: {column} vs {target}", 
                        subtitle="Scatter plot to identify correlation")

# -----------------------------------------------------------------------------
# Heatmap
# -----------------------------------------------------------------------------
def plot_heatmap(ct, annot=True, cmap="Blues"):
    ax = plt.gca()
    
    sns.heatmap(ct, annot=annot, cmap=cmap, fmt=".1f", 
                linewidths=1, linecolor='white', cbar_kws={'shrink': .8}, ax=ax)
    
    _add_title_subtitle(ax, 
                        title="Cross-Tabulation Heatmap", 
                        subtitle="Intensity of values across categories")