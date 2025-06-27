import pyvista as pv
from stl import mesh
import numpy as np

# Load the STL file
stl_file = 'StallCentered.stl'
try:
    your_mesh = mesh.Mesh.from_file(stl_file)
except FileNotFoundError:
    print(f"Error: The file {stl_file} was not found.")
    exit()

# Reshape the vertices array
vertices = your_mesh.vectors.reshape(-1, 3)

# Create the face array
# The number of faces is the number of vectors
num_faces = len(your_mesh.vectors)
# Create a list of faces, where each face is [3, i, i+1, i+2] for each triangle
faces = np.hstack((np.full((num_faces, 1), 3), np.arange(num_faces * 3).reshape(-1, 3)))

# Create a PyVista mesh
mesh_pv = pv.PolyData(vertices, faces)

# Create a plotter object
plotter = pv.Plotter(window_size=[800, 600])

# Add the mesh to the plotter
plotter.add_mesh(mesh_pv, color='lightblue', show_edges=False)

# Enable trackball-style interaction
plotter.enable_trackball_actor_style()

# Set camera position to focus on the object
plotter.camera_position = 'iso'

# Add a title
plotter.add_text("Interactive STL Viewer", position='upper_edge', font_size=18)

# Show the plot
print("Showing interactive plot. Close the window to exit.")
plotter.show()
