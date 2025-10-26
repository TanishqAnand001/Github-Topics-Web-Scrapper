import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the style once for all plots
sns.set_style("whitegrid")


def convert_stars_to_numeric(stars_str):
    stars_str = stars_str.strip()
    if 'k' in stars_str.lower():
        return int(float(stars_str.lower().replace('k', '')) * 1000)
    return int(stars_str.replace(',', ''))


def plot_top_repos(df):
    # Prepare data
    df_copy = df.copy()
    df_copy['Stars_numeric'] = df_copy['Stars'].apply(convert_stars_to_numeric)
    top_10_repos = df_copy.sort_values(by='Stars_numeric', ascending=False).head(10)

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='Stars_numeric', y='Repository Name', data=top_10_repos, palette='viridis', hue='Repository Name',
                legend=False, ax=ax)
    ax.set_title('Top 10 Most Starred Repositories', fontsize=16)
    ax.set_xlabel('Number of Stars', fontsize=12)
    ax.set_ylabel('Repository Name', fontsize=12)

    # Return the figure object
    return fig


def plot_top_topics(df):
    # Prepare data
    df_copy = df.copy()
    if 'Stars_numeric' not in df_copy.columns:
        df_copy['Stars_numeric'] = df_copy['Stars'].apply(convert_stars_to_numeric)
    top_topics = df_copy.groupby('Topic Title')['Stars_numeric'].sum().sort_values(ascending=False).head(10)

    # Create plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x=top_topics.values, y=top_topics.index, palette='plasma', hue=top_topics.index, legend=False, ax=ax)
    ax.set_title('Top 10 Topics by Total Stars', fontsize=16)
    ax.set_xlabel('Total Number of Stars', fontsize=12)
    ax.set_ylabel('Topic', fontsize=12)

    # Return the figure object
    return fig