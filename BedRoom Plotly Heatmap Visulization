import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
df = pd.read_csv('/content/combined_data_CSIsumed.csv')

# Create the 3D heatmap
fig = go.Figure(data=go.Scatter3d(
    x=df['x_loc'],
    y=df['y_loc'],
    z=df['z_loc'],
    mode='markers',
    marker=dict(
        size=3,
        color=df['csi_phase_rad'],
        colorscale='Viridis',
        opacity=0.8
    )
))

# Set axis labels
fig.update_layout(scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
))

# Set the layout and display the figure
fig.show()
