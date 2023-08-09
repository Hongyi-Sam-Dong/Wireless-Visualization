import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
df = pd.read_csv('/content/Received Power.csv')

# Create separate figures for each Tx
for num in range(1, 5):
    # Filter the DataFrame for the current Tx
    df_tx = df[df['rx_grid_number'] == num]

    # Create the 3D scatter plot
    fig = go.Figure(data=go.Scatter3d(
        x=df_tx['x_loc'],
        y=df_tx['y_loc'],
        z=df_tx['z_loc'],
        mode='markers',
        marker=dict(
            size=3,
            color=df_tx['csi_phase_rad'],
            colorscale='hot',
            opacity=0.8
        )
    ))

    # Set axis labels
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))

    # Set the title for the current Tx
    fig.update_layout(title=f'3D Scatter Plot for Tx {num}')

    # Display the figure for the current Tx
    fig.show()
