import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
BMI = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (BMI > 25).astype(int)

# 3
df[['cholesterol', 'gluc']] = df[['cholesterol', 'gluc']].replace([1, 2, 3], [0, 1, 1])

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))

    # 8
    fig = sns.catplot(x='variable', y='total', data=df_cat, hue='value', col='cardio', kind='bar')

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(14, 14))

    # 15
    ax = sns.heatmap(corr, lw=1, annot=True, fmt='.1f', square = True)

    # 16
    fig.savefig('heatmap.png')
    return fig
