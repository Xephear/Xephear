import pandas as pd
from graphviz import Digraph
import sys

# Create a dataframe from the CSV data
data = {
    'From': [
        'Chapter 1 - Choice 1A', 'Chapter 1 - Choice 1A', 'Chapter 1 - Choice 1B', 'Chapter 1 - Choice 1B',
        'Chapter 1 - Outcome 1A-1A', 'Chapter 1 - Outcome 1A-1B', 'Chapter 1 - Outcome 1B-1A', 'Chapter 1 - Outcome 1B-1B',
        'Chapter 2 - Choice 2A', 'Chapter 2 - Choice 2A', 'Chapter 2 - Choice 2B', 'Chapter 2 - Choice 2B',
        'Chapter 2 - Choice 2C', 'Chapter 2 - Choice 2C', 'Chapter 2 - Outcome 2A-1A', 'Chapter 2 - Outcome 2A-1D',
        'Chapter 2 - Outcome 2B-1A', 'Chapter 2 - Outcome 2B-1B', 'Chapter 2 - Outcome 2C-1A', 'Chapter 2 - Outcome 2C-1B',
        'Chapter 3 - Choice 3A', 'Chapter 3 - Choice 3A', 'Chapter 3 - Choice 3B', 'Chapter 3 - Choice 3B',
        'Chapter 3 - Choice 3C', 'Chapter 3 - Choice 3C', 'Chapter 3 - Choice 3D', 'Chapter 3 - Choice 3D',
        'Chapter 3 - Outcome 3A-1A', 'Chapter 3 - Outcome 3A-1B', 'Chapter 3 - Outcome 3B-1A', 'Chapter 3 - Outcome 3B-1B',
        'Chapter 3 - Outcome 3C-2A', 'Chapter 3 - Outcome 3C-2B', 'Chapter 3 - Outcome 3D-3A', 'Chapter 3 - Outcome 3D-3B',
        'Chapter 4 - Choice 4A', 'Chapter 4 - Choice 4A', 'Chapter 4 - Choice 4B', 'Chapter 4 - Choice 4B',
        'Chapter 4 - Choice 4C', 'Chapter 4 - Choice 4C'
    ],
    'To': [
        'Chapter 1 - Outcome 1A-1A', 'Chapter 1 - Outcome 1A-1B', 'Chapter 1 - Outcome 1B-1A', 'Chapter 1 - Outcome 1B-1B',
        'Chapter 2 (from Outcome 1A-1A)', 'Chapter 2 (from Outcome 1A-1B)', 'Chapter 2 (from Outcome 1B-1A)', 'Chapter 2 (from Outcome 1B-1B)',
        'Chapter 2 - Outcome 2A-1A', 'Chapter 2 - Outcome 2A-1D', 'Chapter 2 - Outcome 2B-1A', 'Chapter 2 - Outcome 2B-1B',
        'Chapter 2 - Outcome 2C-1A', 'Chapter 2 - Outcome 2C-1B', 'Chapter 3 (from Outcome 2A-1A)', 'Chapter 3 (from Outcome 2A-1D)',
        'Chapter 3 (from Outcome 2B-1A)', 'Chapter 3 (from Outcome 2B-1B)', 'Chapter 3 (from Outcome 2C-1A)', 'Chapter 3 (from Outcome 2C-1B)',
        'Chapter 3 - Outcome 3A-1A', 'Chapter 3 - Outcome 3A-1B', 'Chapter 3 - Outcome 3B-1A', 'Chapter 3 - Outcome 3B-1B',
        'Chapter 3 - Outcome 3C-2A', 'Chapter 3 - Outcome 3C-2B', 'Chapter 3 - Outcome 3D-3A', 'Chapter 3 - Outcome 3D-3B',
        'Chapter 4 (from Outcome 3A-1A)', 'Chapter 4 (from Outcome 3A-1B)', 'Chapter 4 (from Outcome 3B-1A)', 'Chapter 4 (from Outcome 3B-1B)',
        'Chapter 4 (from Outcome 3C-2A)', 'Chapter 4 (from Outcome 3C-2B)', 'Chapter 4 (from Outcome 3D-3A)', 'Chapter 4 (from Outcome 3D-3B)',
        'Chapter 4 - Outcome 4A-1A', 'Chapter 4 - Outcome 4A-1B', 'Chapter 4 - Outcome 4B-2A', 'Chapter 4 - Outcome 4B-2B',
        'Chapter 4 - Outcome 4C-3A', 'Chapter 4 - Outcome 4C-3B'
    ]
}
df = pd.DataFrame(data)

# Create a directed graph
dot = Digraph()

# Add nodes and edges
for index, row in df.iterrows():
    dot.node(row['From'], row['From'])
    dot.node(row['To'], row['To'])
    dot.edge(row['From'], row['To'])

# Save and render the graph
dot.render('flowchart', format='png')

# Display the graph
from IPython.display import Image
Image('flowchart.png')
