import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from matsankey.sankey import sankey


df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'toy_data.csv'))

leftlableorder = ['A', 'B', 'C']

allisos = list(pd.concat([df['left'], df['right']]).unique())
vbarhues = sns.color_palette("Spectral", len(allisos))
colorDict = {}
for i in range(len(allisos)):
    colorDict[allisos[i]] = vbarhues[i]

fig, ax = plt.subplots(figsize=(8, 6))

sankey(
    left=df['left'],
    right=df['right'],
    leftWeight=df['weight'],
    leftLabels=leftlableorder,
    colorDict=colorDict,
    ax=ax,
    stripAlpha=0.6,
    fontsize=13,
    grayStrips=True,
)

out_path = os.path.join(os.path.dirname(__file__), 'toy_sankey.png')
plt.savefig(out_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {out_path}")
